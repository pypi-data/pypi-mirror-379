
# freeassoc

Lightweight utilities for processing free-association responses.

Features
- Clean short text responses
- Average and manage embeddings
- Grouping / hierarchical clustering
- Projections (classical MDS, UMAP, PaCMAP)
- Label-frequency matrices and a small cross-validated OLS report

Quick start
1. Create and activate a virtual environment.

2. Install requirements:

```bash
pip install freeassoc
```

Development & tests
- The project uses a `src/` layout. When running tests from the repo root, make the package importable with PYTHONPATH:

```bash
PYTHONPATH=src python -m pytest -q
```

Examples
- See `examples/simple_df_example.py` for a quick runnable demonstration of embedding, caching, and label inference.
 
Status
- Work in progress. Use at your own risk;

Compatibility
- Tested with Python 3.10.

Attribution
- This repository is a Python adaptation of the R project `associatoR` (https://github.com/samuelae/associatoR) originally created by Dirk Wulff.

Author
- Ali Alhosseini

