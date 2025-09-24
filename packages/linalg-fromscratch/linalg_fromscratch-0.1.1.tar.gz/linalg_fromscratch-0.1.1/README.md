## Run in Google Colab

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](
https://colab.research.google.com/github/Izewdevlabs/Cosine_PCA/blob/main/notebooks/Cosine_PCA_FromScratch.ipynb
)


## Notebooks

Interactive demos are in the [`notebooks/`](./notebooks) folder.

- [Cosine_PCA_FromScratch.ipynb](./notebooks/Cosine_PCA_FromScratch.ipynb)  
  Demonstrates cosine similarity, PCA (covariance + SVD), explained variance plots, and reconstruction.

## Run in Binder

[![Binder](https://mybinder.org/badge_logo.svg)](
https://mybinder.org/v2/gh/Izewdevlabs/Cosine_PCA/HEAD?labpath=notebooks%2FCosine_PCA_FromScratch.ipynb
)


# Cosine_PCA

![Python tests](https://github.com/Izewdevlabs/Cosine_PCA/actions/workflows/python-tests.yml/badge.svg)


# linalg_fromscratch (NumPy) — Cosine + PCA with Tests

A tiny, dependency-light set of linear algebra utilities implemented from scratch in NumPy,
with a pytest suite you can drop into any repo.

## Structure
```
linalg_fromscratch/
├── src/
│   └── linalg_fromscratch/
│       ├── __init__.py
│       ├── cosine.py
│       └── pca.py
├── tests/
│   ├── test_cosine.py
│   └── test_pca.py
├── pytest.ini
├── requirements.txt
└── README.md
```

## Run tests
```bash
pip install -r requirements.txt
pytest
```

## Notes
- Cosine similarity guards against zero vectors.
- `PCA_FromScratch`: covariance eigendecomposition.
- `PCA_SVD`: SVD-based PCA. Tests confirm equivalence up to sign flips.
- Tests include:
  - Cosine edge cases
  - Orthonormality of components
  - Variance-along-PCs equals eigenvalues
  - Reconstruction error decreases with more components
  - Covariance-PCA vs SVD-PCA numerical equivalence
