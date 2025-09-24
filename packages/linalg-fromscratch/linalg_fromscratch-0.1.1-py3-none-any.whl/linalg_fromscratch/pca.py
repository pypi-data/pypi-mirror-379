import numpy as np

class PCA_FromScratch:
    def __init__(self, n_components: int = None):
        self.n_components = n_components
        self.mean_ = None
        self.components_ = None
        self.explained_variance_ = None
        self.explained_variance_ratio_ = None

    def fit(self, X: np.ndarray):
        X = np.asarray(X, dtype=float)
        n, d = X.shape
        if self.n_components is None:
            self.n_components = d
        self.mean_ = X.mean(axis=0)
        Xc = X - self.mean_
        C = (Xc.T @ Xc) / (n - 1)
        eigvals, eigvecs = np.linalg.eigh(C)
        order = np.argsort(eigvals)[::-1]
        eigvals = eigvals[order]
        eigvecs = eigvecs[:, order]
        k = min(self.n_components, d)
        self.components_ = eigvecs[:, :k]
        self.explained_variance_ = eigvals[:k]
        total = eigvals.sum() if eigvals.sum() > 0 else 1e-12
        self.explained_variance_ratio_ = self.explained_variance_ / total
        return self

    def transform(self, X: np.ndarray) -> np.ndarray:
        if self.mean_ is None or self.components_ is None:
            raise RuntimeError("Call fit before transform.")
        X = np.asarray(X, dtype=float)
        Xc = X - self.mean_
        return Xc @ self.components_

    def fit_transform(self, X: np.ndarray) -> np.ndarray:
        return self.fit(X).transform(X)

    def inverse_transform(self, Z: np.ndarray) -> np.ndarray:
        return Z @ self.components_.T + self.mean_

class PCA_SVD:
    def __init__(self, n_components: int = None):
        self.n_components = n_components
        self.mean_ = None
        self.components_ = None
        self.explained_variance_ = None
        self.explained_variance_ratio_ = None

    def fit(self, X: np.ndarray):
        X = np.asarray(X, dtype=float)
        n, d = X.shape
        if self.n_components is None:
            self.n_components = d
        self.mean_ = X.mean(axis=0)
        Xc = X - self.mean_
        U, S, Vt = np.linalg.svd(Xc, full_matrices=False)
        eigvals = (S ** 2) / (n - 1)
        order = np.argsort(eigvals)[::-1]
        eigvals = eigvals[order]
        Vt = Vt[order, :]
        k = min(self.n_components, d)
        self.components_ = Vt[:k, :].T
        self.explained_variance_ = eigvals[:k]
        total = eigvals.sum() if eigvals.sum() > 0 else 1e-12
        self.explained_variance_ratio_ = self.explained_variance_ / total
        return self

    def transform(self, X: np.ndarray) -> np.ndarray:
        if self.mean_ is None or self.components_ is None:
            raise RuntimeError("Call fit before transform.")
        X = np.asarray(X, dtype=float)
        Xc = X - self.mean_
        return Xc @ self.components_

    def fit_transform(self, X: np.ndarray) -> np.ndarray:
        return self.fit(X).transform(X)

    def inverse_transform(self, Z: np.ndarray) -> np.ndarray:
        return Z @ self.components_.T + self.mean_