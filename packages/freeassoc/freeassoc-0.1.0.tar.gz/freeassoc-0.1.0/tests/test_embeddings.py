import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
from freeassoc.embeddings import embed_texts, embed_dataframe


class EmbeddingTests(unittest.TestCase):
    @patch("freeassoc.embeddings.requests.post")
    def test_embed_texts_batch(self, mock_post):
        # mock a response object
        mock_resp = MagicMock()
        mock_resp.raise_for_status.return_value = None
        mock_resp.json.return_value = {"data": [{"embedding": [1, 2]}, {"embedding": [3, 4]}]}
        mock_post.return_value = mock_resp
        texts = ["a", "b"]
        embs = embed_texts(texts, batch_size=2)
        self.assertEqual(len(embs), 2)
        self.assertEqual(embs[0], [1, 2])

    @patch("freeassoc.embeddings.requests.post")
    def test_embed_dataframe(self, mock_post):
        mock_resp = MagicMock()
        mock_resp.raise_for_status.return_value = None
        mock_resp.json.return_value = {"data": [{"embedding": [1, 1]}, {"embedding": [2, 2]}]}
        mock_post.return_value = mock_resp
        df = pd.DataFrame({"word_1": ["a", "b"], "word_2": ["b", "a"]})
        out = embed_dataframe(df, ["word_1", "word_2"], batch_size=2)
        self.assertIn("word_1_embedding", out.columns)
        self.assertEqual(out["word_1_embedding"][0], [1, 1])


if __name__ == "__main__":
    unittest.main()
