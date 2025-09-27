"""Core utilities: cleaning, simple embedding stubs, averaging embeddings."""
from typing import List, Sequence
import re
import numpy as np
import pandas as pd

WORD_RE = re.compile(r"[\w\u4e00-\u9fff]+", flags=re.UNICODE)


def clean_words(words: Sequence[str]) -> List[str]:
    """Clean a sequence of words/short phrases.

    - normalize whitespace
    - remove non-word characters except CJK
    - lowercase ASCII
    - collapse empty to empty string
    """
    out = []
    for w in words:
        if w is None:
            out.append("")
            continue
        s = str(w).strip()
        # replace smart quotes
        s = s.replace("\u2019", "'").replace("\u201c", '"').replace("\u201d", '"')
        # extract word-like tokens (allow CJK ranges)
        tokens = WORD_RE.findall(s)
        if not tokens:
            out.append("")
        else:
            # if contains ascii letters, lowercase
            joined = " ".join(tokens)
            if any(("a" <= ch.lower() <= "z") for ch in joined):
                joined = joined.lower()
            out.append(joined)
    return out


def average_embeddings(df: pd.DataFrame, text_cols: Sequence[str], embedding_col_name: str = "avg_embedding") -> pd.DataFrame:
    """Given a DataFrame where each text column has a corresponding <col>_embedding (list/np.array),
    compute the average embedding per row and store in `embedding_col_name`.

    If a column has missing embedding, it is skipped in the mean. If all are missing, a zero vector is used.
    """
    df = df.copy()
    embeddings = []
    first_vec = None
    for i, row in df.iterrows():
        vecs = []
        for col in text_cols:
            key = f"{col}_embedding"
            v = row.get(key, None)
            if v is None or (isinstance(v, float) and np.isnan(v)):
                continue
            arr = np.asarray(v, dtype=float)
            if arr.size == 0:
                continue
            vecs.append(arr)
            if first_vec is None:
                first_vec = arr
        if not vecs:
            if first_vec is None:
                embeddings.append(np.zeros(1, dtype=float))
            else:
                embeddings.append(np.zeros_like(first_vec))
        else:
            embeddings.append(np.mean(np.vstack(vecs), axis=0))
    df[embedding_col_name] = embeddings
    return df
