import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
from freeassoc.embeddings import create_embedding_dataframe


class EmbeddingMoreTests(unittest.TestCase):
    @patch("freeassoc.embeddings.requests.post")
    def test_create_embedding_dataframe(self, mock_post):
        mock_resp = MagicMock()
        mock_resp.raise_for_status.return_value = None
        # return two embeddings for two unique texts
        mock_resp.json.return_value = {"data": [{"embedding": [1, 0]}, {"embedding": [0, 1]}]}
        mock_post.return_value = mock_resp
        df = pd.DataFrame({"word_1": ["a", "b"], "word_2": ["b", "a"]})
        out = create_embedding_dataframe(df, ["word_1", "word_2"], batch_size=2)
        self.assertIn("word_1_embedding", out.columns)
        self.assertEqual(out["word_1_embedding"][0], [1, 0])


if __name__ == "__main__":
    unittest.main()
