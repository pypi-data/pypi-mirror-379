"""Simple SQLite-backed cache for embeddings and chat responses."""
from typing import Dict, Iterable, Optional
import sqlite3
import json
import threading
import unicodedata
import re


class SQLiteCache:
    """A tiny SQLite-backed cache mapping text -> value (JSON stored).
    
    Usage:
        cache = SQLiteCache(path="./.cache.db")
        existing = cache.get_multi(["a","b"])  # returns dict of cached entries
        cache.set_many({"a": [1,2], "b": [3,4]})
    """

    def __init__(self, path: str = ":memory:"):
        self.path = path
        self._lock = threading.RLock()
        self._conn: Optional[sqlite3.Connection] = None
        self._ensure()

    def _ensure(self):
        with self._lock:
            if self._conn is None:
                self._conn = sqlite3.connect(self.path, check_same_thread=False)
                cur = self._conn.cursor()
                cur.execute(
                    """CREATE TABLE IF NOT EXISTS embeddings (
                        text TEXT PRIMARY KEY,
                        value TEXT
                    )"""
                )
                self._conn.commit()

    def _ensure_table(self, table: str):
        """Ensure a custom table exists."""
        with self._lock:
            self._ensure()
            cur = self._conn.cursor()
            cur.execute(
                f"CREATE TABLE IF NOT EXISTS {table} (text TEXT PRIMARY KEY, value TEXT)"
            )
            self._conn.commit()

    def _normalize(self, text: str) -> str:
        """Return a canonical form for cache keys.

        Operations:
        - Normalize unicode (NFKC)
        - Casefold (Unicode-aware lowercase)
        - Replace runs of whitespace with single space and strip
        - Remove simple punctuation characters
        """
        if text is None:
            return ""
        t = str(text)
        # Unicode normalization
        t = unicodedata.normalize("NFKC", t)
        # casefold for case-insensitive matching
        t = t.casefold()
        # Remove common ASCII punctuation/symbols conservatively.
        # Avoid using `\p{...}` Unicode properties to remain stdlib-only.
        t = re.sub(r"[!\"#$%&'()*+,\-./:;<=>?@\[\\\]\^_`{|}~]", " ", t)
        # collapse whitespace
        t = re.sub(r"\s+", " ", t).strip()
        return t

    def get_multi(self, texts: Iterable[str], table: str = "embeddings") -> Dict[str, object]:
        """Return a dict of text -> parsed value for texts found in cache."""
        self._ensure()
        if table != "embeddings":
            self._ensure_table(table)
        texts = [str(t) for t in texts]
        if not texts:
            return {}
        placeholders = ",".join("?" for _ in texts)
        q = f"SELECT text, value FROM {table} WHERE text IN ({placeholders})"
        cur = self._conn.cursor()
        cur.execute(q, texts)
        rows = cur.fetchall()
        out = {}
        for t, v in rows:
            try:
                out[t] = json.loads(v)
            except Exception:
                out[t] = None
        return out

    def set_many(self, mapping: Dict[str, object], table: str = "embeddings"):
        """Store multiple text -> value in cache (value serialized as JSON)."""
        if not mapping:
            return
        self._ensure()
        if table != "embeddings":
            self._ensure_table(table)
        cur = self._conn.cursor()
        items = [(k, json.dumps(v)) for k, v in mapping.items()]
        cur.executemany(f"REPLACE INTO {table}(text, value) VALUES(?,?)", items)
        self._conn.commit()

    def close(self):
        if self._conn:
            self._conn.close()
            self._conn = None
