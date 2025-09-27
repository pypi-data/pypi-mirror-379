import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
from freeassoc.chat import infer_labels, infer_labels_batched
from freeassoc.cache import SQLiteCache


class ChatTests(unittest.TestCase):
    @patch("freeassoc.chat.requests.post")
    def test_infer_labels_simple(self, mock_post):
        mock_resp = MagicMock()
        mock_resp.raise_for_status.return_value = None
        # Simulate an OpenAI-like response with choices[0].message.content
        mock_resp.json.return_value = {"choices": [{"message": {"content": "@friendship@"}}]}
        mock_post.return_value = mock_resp
        examples = [["friend", "love", "companionship"], ["dog", "pet"]]
        labels = infer_labels(examples)
        self.assertEqual(labels[0], "friendship")

    @patch("freeassoc.chat.requests.post")
    def test_infer_labels_batched(self, mock_post):
        mock_resp = MagicMock()
        mock_resp.raise_for_status.return_value = None
        mock_resp.json.return_value = {"choices": [{"message": {"content": "@joy@"}}]}
        mock_post.return_value = mock_resp
        df = pd.DataFrame({"group_texts": ["happy, joyful", "sad, blue"]})
        out = infer_labels_batched(df, "group_texts", batch_size=1)
        self.assertIn("labels", out.columns)
        self.assertEqual(out["labels"][0], "joy")

    @patch("freeassoc.chat.requests.post")
    def test_infer_labels_uses_cache(self, mock_post):
        # seed cache with a precomputed label
        cache = SQLiteCache(path=":memory:")
        key = "apple|||banana"
        cache.set_many({key: "cached-fruit"}, table="labels")

        # ensure requests.post would fail if called
        mock_post.side_effect = AssertionError("requests.post should not be called for cached inputs")

        labels = infer_labels([["apple", "banana"]], base_url="http://example.com", model_name="m", cache=cache)
        assert labels == ["cached-fruit"]


if __name__ == "__main__":
    unittest.main()
