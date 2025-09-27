"""Embedding helpers: batched HTTP client for local embedding service and dataframe helpers."""
from typing import Iterable, List, Dict, Sequence, Optional
import time
import requests
from math import ceil
import numpy as np
import pandas as pd
from tqdm import tqdm
from .cache import SQLiteCache


DEFAULT_EMBEDDING_URL = "http://localhost:1234/v1/embeddings"
DEFAULT_MODEL = "text-embedding-embeddinggemma-300m"


def get_embedding(text: str, model: str = DEFAULT_MODEL, url: str = DEFAULT_EMBEDDING_URL, timeout: float = 30.0) -> List[float]:
    """Fetch a single embedding from the local embedding service.

    This wraps a single POST and returns the first embedding vector found.
    """
    payload = {"model": model, "input": text}
    resp = requests.post(url, json=payload, headers={"Content-Type": "application/json"}, timeout=timeout)
    resp.raise_for_status()
    body = resp.json()
    data = body.get("data") or body.get("embeddings") or []
    if not data:
        return []
    item = data[0]
    if isinstance(item, dict) and "embedding" in item:
        return item["embedding"]
    if isinstance(item, list):
        return item
    return []


def embed_texts(texts: Sequence[str], url: str = DEFAULT_EMBEDDING_URL, model: str = DEFAULT_MODEL, batch_size: int = 100, retries: int = 2, backoff: float = 0.5, timeout: float = 30.0, show_progress: bool = False, cache: Optional[SQLiteCache] = None) -> List[List[float]]:
    """Embed a sequence of texts by batching requests to a local embedding endpoint.

    This function deduplicates and batches requests, with simple retry/backoff logic.
    Returns a list of embedding vectors in the same order as `texts`.
    """
    texts_list = ["" if t is None else str(t) for t in texts]
    results: List[List[float]] = []
    # if cache provided, prefill results for cached items
    cached_map: Dict[str, object] = {}
    if cache is not None:
        cached_map = cache.get_multi(texts_list)
    n_batches = ceil(len(texts_list) / batch_size) if batch_size > 0 else 1
    iterator = range(n_batches)
    if show_progress:
        iterator = tqdm(iterator, desc="Embedding batches")
    # We'll collect new embeddings to write back to cache at the end
    new_cache_entries: Dict[str, object] = {}
    for i in iterator:
        batch = texts_list[i * batch_size: (i + 1) * batch_size]
        # for items already cached, consume from cache and skip network call
        missing = [t for t in batch if t not in cached_map]
        # fill cached results in order
        batch_results: List[List[float]] = []
        if missing:
            payload = {"model": model, "input": missing}
            attempt = 0
            while True:
                try:
                    resp = requests.post(url, json=payload, headers={"Content-Type": "application/json"}, timeout=timeout)
                    resp.raise_for_status()
                    body = resp.json()
                    data = body.get("data") or body.get("embeddings") or []
                    batch_embeddings: List[List[float]] = []
                    for item in data:
                        if isinstance(item, dict) and "embedding" in item:
                            batch_embeddings.append(item["embedding"])
                        elif isinstance(item, list):
                            batch_embeddings.append(item)
                        else:
                            batch_embeddings.append([])
                    # pad if necessary
                    if len(batch_embeddings) < len(missing):
                        batch_embeddings.extend([[] for _ in range(len(missing) - len(batch_embeddings))])
                    # update cached_map and new_cache_entries
                    for t, emb in zip(missing, batch_embeddings):
                        cached_map[t] = emb
                        new_cache_entries[t] = emb
                    break
                except Exception:
                    attempt += 1
                    if attempt > retries:
                        for t in missing:
                            cached_map[t] = []
                            new_cache_entries[t] = []
                        break
                    time.sleep(backoff * attempt)
        # now produce batch_results in original batch order from cached_map
        for t in batch:
            batch_results.append(cached_map.get(t, []))
        results.extend(batch_results)
    # write back to cache if provided
    if cache is not None and new_cache_entries:
        cache.set_many(new_cache_entries)
    return results


def embed_unique_texts(df: pd.DataFrame, text_cols: Sequence[str], url: str = DEFAULT_EMBEDDING_URL, model: str = DEFAULT_MODEL, batch_size: int = 100, show_progress: bool = False) -> pd.DataFrame:
    """Return a DataFrame mapping unique text -> embedding (columns: 'text', 'embedding').

    This collects unique strings across `text_cols`, fetches embeddings for them (batched),
    and returns a two-column DataFrame indexed by text.
    """
    # collect unique texts
    unique_texts = pd.unique(df[list(text_cols)].astype(str).values.ravel())
    unique_texts = [t for t in unique_texts if t is not None]
    if len(unique_texts) == 0:
        return pd.DataFrame(columns=["text", "embedding"]).set_index("text")
    embeddings = embed_texts(unique_texts, url=url, model=model, batch_size=batch_size, show_progress=show_progress)
    embedding_df = pd.DataFrame({"text": list(unique_texts), "embedding": list(embeddings)})
    embedding_df = embedding_df.set_index("text")
    return embedding_df


def embed_dataframe(df: pd.DataFrame, text_cols: Sequence[str], url: str = DEFAULT_EMBEDDING_URL, model: str = DEFAULT_MODEL, batch_size: int = 100, show_progress: bool = False) -> pd.DataFrame:
    """Backward-compatible wrapper: return a copy of df with new columns <col>_embedding for each text column.

    Uses `create_embedding_dataframe` internally.
    """
    return create_embedding_dataframe(df, text_cols=text_cols, url=url, model=model, batch_size=batch_size, show_progress=show_progress)


def create_embedding_dataframe(df: pd.DataFrame, text_cols: Sequence[str], url: str = DEFAULT_EMBEDDING_URL, model: str = DEFAULT_MODEL, batch_size: int = 100, show_progress: bool = False) -> pd.DataFrame:
    """Create a copy of `df` with new columns <col>_embedding for each text column.

    Uses `embed_dataframe` internally to avoid duplicate requests.
    """
    # build mapping of unique text -> embedding using the dedicated function
    embedding_df = embed_unique_texts(df, text_cols=text_cols, url=url, model=model, batch_size=batch_size, show_progress=show_progress)
    df_out = df.copy()
    for col in text_cols:
        # map returns a Series of embedding lists (or NaN). keep as-is.
        df_out[f"{col}_embedding"] = df_out[col].astype(str).map(lambda t: embedding_df["embedding"].get(t) if t in embedding_df.index else embedding_df["embedding"].get(t, []))
    return df_out
