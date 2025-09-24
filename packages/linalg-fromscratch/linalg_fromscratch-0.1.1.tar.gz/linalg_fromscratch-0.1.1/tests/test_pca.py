import numpy as np
from linalg_fromscratch import PCA_FromScratch, PCA_SVD

def _make_lowrank_data(n=400, d=5, k=2, noise=0.1, seed=0):
    rng = np.random.default_rng(seed)
    A = rng.normal(size=(n, k))
    B = rng.normal(size=(k, d))
    X = A @ B + noise * rng.normal(size=(n, d))
    return X

def _align_signs(W, V):
    C = W.T @ V
    signs = np.sign(np.diag(C))
    signs[signs == 0] = 1
    return W * signs

def test_pca_components_orthonormal():
    X = _make_lowrank_data()
    p = PCA_FromScratch(n_components=3).fit(X)
    I = p.components_.T @ p.components_
    assert np.allclose(I, np.eye(I.shape[0]), atol=1e-8)

def test_variance_equals_eigenvalue_on_projection():
    X = _make_lowrank_data()
    p = PCA_FromScratch(n_components=3).fit(X)
    Z = p.transform(X)
    var = np.var(Z, axis=0, ddof=1)
    assert np.allclose(var, p.explained_variance_, rtol=1e-5, atol=1e-7)

def test_reconstruction_error_monotonic():
    X = _make_lowrank_data()
    errs = []
    for k in range(1, 5):
        p = PCA_FromScratch(n_components=k).fit(X)
        Z = p.transform(X)
        Xr = p.inverse_transform(Z)
        mse = np.mean((X - Xr)**2)
        errs.append(mse)
    assert all(errs[i] >= errs[i+1] - 1e-10 for i in range(len(errs)-1))

def test_pca_covariance_vs_svd_equivalence():
    X = _make_lowrank_data(n=500, d=6, k=3, noise=0.2, seed=123)
    cov = PCA_FromScratch(n_components=6).fit(X)
    svd = PCA_SVD(n_components=6).fit(X)
    aligned = _align_signs(svd.components_, cov.components_)
    assert np.linalg.norm(cov.components_ - aligned) < 1e-6
    assert np.allclose(cov.explained_variance_, svd.explained_variance_, rtol=1e-7, atol=1e-9)
    assert np.allclose(cov.explained_variance_ratio_, svd.explained_variance_ratio_, rtol=1e-7, atol=1e-9)