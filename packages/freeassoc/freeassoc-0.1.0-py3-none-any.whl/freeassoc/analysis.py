"""Small analysis helpers.

This module provides two helpers that mirror the original utility behavior used
by the tests:

- build_label_frequency(df, n_labels=5, top_k=41, drop_labels=None) -> (df_out, top_labels)
- ols_cv_report(df, targets=..., num_cols=..., bin_cols=..., cat_cols=..., k=5) -> pd.DataFrame
"""
from typing import Iterable, Mapping, Optional, Sequence, Union
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import KFold, cross_val_score


def build_label_frequency(df: pd.DataFrame, n_labels: int = 5, top_k: int = 41, drop_labels: Optional[Sequence[str]] = None):
    """Build frequency counts of the most common labels across word/label columns.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame containing label columns (e.g. label_1 ... label_n)
    n_labels : int
        Number of label columns to consider (default 5)
    top_k : int
        Number of top labels to keep (default 41)
    drop_labels : optional list
        Labels to exclude from the top list

    Returns
    -------
    freq_df : pd.DataFrame
        Original DataFrame augmented with count_<label> columns
    top_labels : list
        List of labels used as columns
    """
    # Collect label column names
    label_cols = [f"label_{i}" for i in range(1, n_labels + 1)]

    # Melt into one column of labels
    all_labels = df[label_cols].melt(value_name="label")["label"]

    # Frequency counts
    label_counts = all_labels.value_counts()

    # Top labels
    top_labels = label_counts.reset_index().head(top_k)["label"].to_list()

    if drop_labels:
        top_labels = [lbl for lbl in top_labels if lbl not in drop_labels]

    # Initialize frequency matrix and fill
    label_freq = np.zeros((len(df), len(top_labels)))
    for i, r in df.iterrows():
        for j in range(1, n_labels + 1):
            label = r.get(f"label_{j}")
            if label in top_labels:
                label_idx = top_labels.index(label)
                label_freq[i, label_idx] += 1

    col_names = [f"count_{label}" for label in top_labels]
    freq_df = pd.DataFrame(label_freq, columns=col_names, index=df.index)
    df_out = pd.concat([df.copy(), freq_df], axis=1)
    return df_out, top_labels


def ols_cv_report(
    df: pd.DataFrame,
    targets: Sequence[str],
    num_cols: Optional[Union[Sequence[str], str]] = None,
    bin_cols: Optional[Union[Sequence[str], str]] = None,
    cat_cols: Optional[Union[Sequence[str], str]] = None,
    *,
    k: int = 5,
    random_state: int = 42,
) -> pd.DataFrame:
    """Quick cross-validated OLS-style report.

    This is a simplified version sufficient for the test-suite: for each target
    it computes cross-validated R^2 (mean/std) and an in-sample R^2 from a
    linear regression fit.
    """
    def _norm(x):
        if x is None:
            return []
        if isinstance(x, str):
            return [x]
        return list(x)

    num_cols = _norm(num_cols)
    bin_cols = _norm(bin_cols)
    cat_cols = _norm(cat_cols)

    parts = []
    if num_cols:
        parts.append(df[num_cols])
    if bin_cols:
        parts.append(df[bin_cols])
    if cat_cols:
        X_cat = pd.get_dummies(df[cat_cols], drop_first=True, dtype=float)
        parts.append(X_cat)

    if parts:
        X = pd.concat(parts, axis=1)
    else:
        X = pd.DataFrame(index=df.index)

    results = []
    kf = KFold(n_splits=max(2, k), shuffle=True, random_state=random_state)

    for y in targets:
        y_vec = df[y]
        # when X has no columns, cross_val_score will fail; fall back to constant model
        if X.shape[1] == 0:
            r2_mean = 0.0
            r2_std = 0.0
            in_sample = 0.0
        else:
            lr = LinearRegression()
            try:
                scores = cross_val_score(lr, X, y_vec, cv=kf, scoring="r2")
                r2_mean = float(scores.mean())
                r2_std = float(scores.std(ddof=1)) if scores.size > 1 else 0.0
            except Exception:
                r2_mean = 0.0
                r2_std = 0.0
            # in-sample
            try:
                lr.fit(X, y_vec)
                in_sample = float(lr.score(X, y_vec))
            except Exception:
                in_sample = 0.0

        results.append({"target": y, "r2_mean": r2_mean, "r2_std": r2_std, "in_sample_r2": in_sample})

    return pd.DataFrame(results)
