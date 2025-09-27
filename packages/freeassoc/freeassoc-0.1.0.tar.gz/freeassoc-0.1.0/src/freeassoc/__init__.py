"""freeassoc package - lightweight utilities for free association processing."""

__version__ = "0.1.0"

from .core import clean_words, average_embeddings
from .clustering import group_vectors, cluster_vectors
from .projection import project_vectors
from .analysis import build_label_frequency
from .embeddings import embed_texts, embed_dataframe
from .chat import infer_labels, infer_labels_batched

__all__ = [
    "__version__",
    "clean_words",
    "average_embeddings",
    "group_vectors",
    "cluster_vectors",
    "project_vectors",
    "build_label_frequency",
    "embed_texts",
    "embed_dataframe",
    "infer_labels",
    "infer_labels_batched",
]
