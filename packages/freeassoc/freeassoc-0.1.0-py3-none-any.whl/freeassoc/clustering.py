"""Grouping and clustering helpers."""
from typing import Optional, Sequence
import numpy as np
import pandas as pd


def compare_vectors(X: np.ndarray, metric: str = "arccos") -> np.ndarray:
    """Compute pairwise similarity matrix for X.

    Supported metrics: 'cosine' (dot-product normalized), 'arccos' (cosine -> arccos similarity),
    'euclidean' (distance), 'pearson', 'spearman' (not implemented here, falls back to cosine).
    """
    if X.ndim != 2:
        raise ValueError("X must be 2D array")
    n = X.shape[0]
    if metric in {"cosine", "arccos"}:
        # normalize rows
        norms = np.linalg.norm(X, axis=1, keepdims=True)
        norms[norms == 0] = 1.0
        Xn = X / norms
        sim = Xn @ Xn.T
        sim = np.clip(sim, -1.0, 1.0)
        if metric == "arccos":
            # convert to similarity in [0,1]
            sim = 1.0 - np.arccos(sim) / np.pi
        return sim
    elif metric == "euclidean":
        D = np.sqrt(((X[:, None, :] - X[None, :, :]) ** 2).sum(axis=2))
        return D
    else:
        # fallback: cosine
        return compare_vectors(X, metric="cosine")


def group_vectors(df: pd.DataFrame, embedding_col: str = "embedding", linkage: Optional[str] = None, threshold: float = 0.95) -> pd.DataFrame:
    """Simple grouping: create groups by hierarchical clustering on cosine similarity.

    df must have an `embedding` column that holds vectors (numpy arrays or lists).
    Returns a DataFrame with one row per group: columns 'group_id','group_size','group_texts','embedding'.
    """
    X = np.vstack(df[embedding_col].values)
    sim = compare_vectors(X, metric="arccos")
    from scipy.cluster.hierarchy import linkage as _linkage, fcluster
    from scipy.spatial.distance import squareform
    D = 1.0 - sim
    condensed = squareform(D, checks=False)
    Z = _linkage(condensed, method="complete" if linkage is None else linkage)
    # choose k by threshold
    from scipy.cluster.hierarchy import fcluster
    k = max(1, int(len(X) * (1 - threshold)))
    labels = fcluster(Z, t=k, criterion="maxclust")
    cliques = {}
    for i, lab in enumerate(labels):
        cliques.setdefault(lab, []).append(i)
    rows = []
    for gid, idxs in cliques.items():
        vectors = X[idxs]
        mean_vec = vectors.mean(axis=0)
        rows.append({
            "group_id": gid,
            "group_size": len(idxs),
            "group_texts": [df.index[i] for i in idxs],
            "embedding": mean_vec
        })
    out = pd.DataFrame(rows).set_index("group_id")
    return out


def cluster_vectors(embedding: pd.DataFrame | np.ndarray, method: str = "hclust", k: Optional[int] = None, eps: Optional[float] = None, metric: str = "euclidean") -> pd.DataFrame:
    """Cluster 2D points (or vectors). Returns DataFrame with 'cluster' labels per row.

    embedding: DataFrame with numeric columns or an ndarray (n x d)
    """
    if isinstance(embedding, pd.DataFrame):
        X = embedding.values
    else:
        X = np.asarray(embedding)
    if X.ndim == 1:
        X = X.reshape(-1, 1)
    n = X.shape[0]
    if method == "hclust":
        from scipy.cluster.hierarchy import linkage as _linkage, fcluster
        from scipy.spatial.distance import pdist
        D = pdist(X, metric=metric)
        Z = _linkage(D, method="complete" if k is None else "average")
        if k is None:
            # try to infer clusters by inconsistency
            labels = fcluster(Z, t=1.0, criterion="distance")
        else:
            labels = fcluster(Z, t=k, criterion="maxclust")
        return pd.DataFrame({"cluster": labels}, index=getattr(embedding, "index", None))
    elif method == "dbscan":
        from sklearn.cluster import DBSCAN
        if eps is None:
            eps = 0.5
        labels = DBSCAN(eps=eps, metric=metric).fit_predict(X)
        return pd.DataFrame({"cluster": labels}, index=getattr(embedding, "index", None))
    else:
        raise ValueError("Unsupported method")
