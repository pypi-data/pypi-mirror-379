import unittest
from freeassoc.cache import SQLiteCache
from freeassoc.embeddings import embed_texts
from unittest.mock import patch, MagicMock


class CacheTests(unittest.TestCase):
    def test_cache_get_set(self):
        c = SQLiteCache(path=":memory:")
        c.set_many({"a": [1, 2], "b": [3, 4]})
        got = c.get_multi(["a", "x"]) 
        self.assertIn("a", got)
        self.assertNotIn("x", got)
        c.close()

    @patch("freeassoc.embeddings.requests.post")
    def test_embed_texts_uses_cache(self, mock_post):
        # Setup cache with one item
        c = SQLiteCache(path=":memory:")
        c.set_many({"cached": [9, 9]})
        # Mock response for missing items
        mock_resp = MagicMock()
        mock_resp.raise_for_status.return_value = None
        mock_resp.json.return_value = {"data": [{"embedding": [1, 1]}]}
        mock_post.return_value = mock_resp
        texts = ["cached", "new"]
        embs = embed_texts(texts, batch_size=10, cache=c)
        # ensure requests.post was called only once (for the missing "new")
        self.assertEqual(mock_post.call_count, 1)
        self.assertEqual(embs[0], [9, 9])
        self.assertEqual(embs[1], [1, 1])
        c.close()


if __name__ == "__main__":
    unittest.main()
