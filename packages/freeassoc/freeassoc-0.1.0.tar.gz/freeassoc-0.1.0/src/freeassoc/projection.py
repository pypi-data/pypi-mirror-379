"""Projection helpers: MDS, UMAP (if available), PacMAP stub."""
from typing import Union, Optional
import numpy as np
import pandas as pd


def classical_mds(D: np.ndarray, k: int = 2) -> np.ndarray:
    n = D.shape[0]
    if D.shape[0] != D.shape[1]:
        raise ValueError("D must be square distance matrix")
    J = np.eye(n) - np.ones((n, n)) / n
    B = -0.5 * J @ (D ** 2) @ J
    evals, evecs = np.linalg.eigh(B)
    idx = np.argsort(evals)[::-1]
    evals = evals[idx]
    evecs = evecs[:, idx]
    pos = evals > 0
    m = min(k, pos.sum())
    L = np.diag(np.sqrt(evals[:m]))
    V = evecs[:, :m]
    X = V @ L
    if m < k:
        X = np.hstack([X, np.zeros((n, k - m))])
    return X


def project_vectors(embedding: pd.DataFrame, method: str = "mds", k: int = 2, verbose: bool = False) -> pd.DataFrame:
    if method not in {"mds", "umap", "pacmap"}:
        raise ValueError("unsupported method")
    if isinstance(embedding, pd.DataFrame):
        X = embedding.values
        index = embedding.index
    else:
        X = embedding
        index = None
    if method == "mds":
        # compute pairwise euclidean distances
        from scipy.spatial.distance import pdist, squareform
        D = squareform(pdist(X, metric="euclidean"))
        Y = classical_mds(D, k=k)
    else:
        # try optional packages
        if method == "umap":
            try:
                from umap import UMAP
            except Exception:
                raise RuntimeError("umap not installed")
            reducer = UMAP(n_components=k, random_state=42)
            Y = reducer.fit_transform(X)
        elif method == "pacmap":
            try:
                from pacmap import PaCMAP
            except Exception:
                raise RuntimeError("pacmap not installed")
            reducer = PaCMAP(n_components=k, random_state=42)
            Y = reducer.fit_transform(X)
    df = pd.DataFrame(Y, index=index, columns=[f"dim_{j}" for j in range(k)])
    return df
