import unittest
import numpy as np
import pandas as pd
from freeassoc.core import clean_words, average_embeddings
from freeassoc.clustering import compare_vectors, group_vectors, cluster_vectors
from freeassoc.projection import project_vectors
from freeassoc.analysis import build_label_frequency, ols_cv_report


class BasicTests(unittest.TestCase):
    def test_clean_words(self):
        inp = ["  Hello!", "Café", "测试", None, "don't"]
        out = clean_words(inp)
        self.assertEqual(out[0], "hello")
        self.assertIn("测试", out[2])
        self.assertEqual(out[3], "")

    def test_average_embeddings(self):
        df = pd.DataFrame({
            "word_1_embedding": [np.array([1.0, 0.0]), np.array([0.0, 0.0])],
            "word_2_embedding": [np.array([0.0, 1.0]), None]
        })
        df_out = average_embeddings(df, ["word_1", "word_2"], embedding_col_name="avg_embedding")
        self.assertEqual(len(df_out["avg_embedding"][0]), 2)
        self.assertTrue(np.allclose(df_out["avg_embedding"][1], np.array([0.0, 0.0])))

    def test_compare_vectors(self):
        X = np.array([[1, 0], [0, 1]])
        sim = compare_vectors(X, metric="arccos")
        self.assertTrue(sim.shape == (2, 2))
        self.assertAlmostEqual(sim[0, 1], sim[1, 0])

    def test_group_and_cluster(self):
        df = pd.DataFrame({"embedding": [np.array([1.0, 0.0]), np.array([0.9, 0.1]), np.array([0.0, 1.0])]})
        g = group_vectors(df, embedding_col="embedding", threshold=0.5)
        self.assertTrue("group_size" in g.columns)
        # projection
        proj = project_vectors(pd.DataFrame([ [1,0],[0,1] ]), method="mds")
        self.assertEqual(proj.shape[1], 2)
        # clustering
        c = cluster_vectors(proj, method="hclust", k=2)
        self.assertIn("cluster", c.columns)

    def test_analysis(self):
        df = pd.DataFrame({
            "label_1": ["a","b"],
            "label_2": ["b","c"],
            "age": [20,30],
            "gender": [0,1],
            "education": ["x","y"],
            "income": ["l","m"],
            "y1": [1.0, 2.0]
        })
        out, top = build_label_frequency(df, n_labels=2, top_k=3)
        self.assertTrue(all(c.startswith("count_") for c in out.columns if c.startswith("count_")))
        report = ols_cv_report(df, targets=["y1"], num_cols=["age"], bin_cols=["gender"], cat_cols=["education","income"], k=2)
        self.assertIn("r2_mean", report.columns)


if __name__ == "__main__":
    unittest.main()
