"""Chat-based label inference helpers that call a local chat completions endpoint.

Functions:
- infer_labels(examples_list, model_name, base_url): call chat endpoint per examples group and extract label wrapped in @...@
- infer_labels_batched(df, text_column, batch_size, base_url): apply infer_labels in batches and attach 'labels' column
"""
from typing import List, Sequence, Optional
import requests
import re
import time
import pandas as pd
from .cache import SQLiteCache

DEFAULT_CHAT_URL = "http://localhost:1234/v1/chat/completions"
DEFAULT_CHAT_MODEL = "qwen/qwen3-4b"

LABEL_RE = re.compile(r"@([^@]{1,100})@?")


def _extract_label_from_text(text: str) -> str:
    if not isinstance(text, str):
        return ""
    t = text.replace("'@'", "@").replace('"@"', "@")
    m = LABEL_RE.search(t)
    if m:
        return m.group(1).strip()
    # fallback: return first up to 4 word-like tokens
    words = re.findall(r"\w+", t)
    return " ".join(words[:4]).strip()


def infer_labels(examples_list: Sequence[Sequence[str]], model_name: str = DEFAULT_CHAT_MODEL, base_url: str = DEFAULT_CHAT_URL, timeout: float = 30.0, retries: int = 1, cache: Optional[SQLiteCache] = None) -> List[str]:
    """For each list of examples (strings), ask the chat API to suggest a short label.

    expected response should contain '@label@' or a short label; function will extract the label.
    Returns list of labels corresponding to each examples list.
    """
    results: List[str] = []
    for examples in examples_list:
        prompt = (
            "Generate a specific and accurate one or two word category label that summarizes the following examples: "
            f"{examples}. The best label can be among the examples. Place '@' before and after the label."
        )
        payload = {
            "model": model_name,
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 32,
        }
        # compute a cache key from the examples (simple join)
        cache_key = "|||".join([str(x) for x in examples])
        if cache is not None:
            existing = cache.get_multi([cache_key], table="labels")
            if cache_key in existing:
                results.append(existing[cache_key])
                continue
        attempt = 0
        resp_json = None
        while True:
            try:
                resp = requests.post(base_url, json=payload, timeout=timeout, headers={"Content-Type": "application/json"})
                resp.raise_for_status()
                resp_json = resp.json()
                break
            except Exception:
                attempt += 1
                if attempt > retries:
                    resp_json = None
                    break
                time.sleep(0.5 * attempt)
        if resp_json is None:
            results.append("")
            continue
        # chat response shape may vary; try common keys
        content = ""
        if isinstance(resp_json, dict):
            # OpenAI-like: choices[0].message.content
            choices = resp_json.get("choices") or resp_json.get("result") or []
            if choices:
                first = choices[0]
                if isinstance(first, dict):
                    # try nested message content
                    if "message" in first and isinstance(first["message"], dict):
                        content = first["message"].get("content", "")
                    else:
                        content = first.get("text") or first.get("message") or ""
                elif isinstance(first, str):
                    content = first
        elif isinstance(resp_json, list):
            # older formats
            content = resp_json[0]
        label = _extract_label_from_text(content)
        results.append(label)
        # store in cache
        if cache is not None:
            cache.set_many({cache_key: label}, table="labels")
    return results


def infer_labels_batched(df: pd.DataFrame, text_column: str, batch_size: int = 50, base_url: str = DEFAULT_CHAT_URL, model_name: str = DEFAULT_CHAT_MODEL) -> pd.DataFrame:
    """Apply infer_labels in batches over a DataFrame column and store results in a new 'labels' column."""
    results = []
    for i in range(0, len(df), batch_size):
        batch_texts = df[text_column].iloc[i : i + batch_size].tolist()
        # each item is a list of examples; ensure structure is correct
        # if items are lists already, wrap accordingly
        examples_list = []
        for t in batch_texts:
            if isinstance(t, (list, tuple)):
                examples_list.append(list(t))
            else:
                # assume comma-separated or single string; split by semicolon or comma
                if isinstance(t, str) and (";" in t or "," in t):
                    parts = re.split(r"[;,]\\s*", t)
                    examples_list.append([p for p in parts if p])
                else:
                    examples_list.append([t])
        labels = infer_labels(examples_list, model_name=model_name, base_url=base_url)
        results.extend(labels)
    out = df.copy()
    out["labels"] = results
    return out
