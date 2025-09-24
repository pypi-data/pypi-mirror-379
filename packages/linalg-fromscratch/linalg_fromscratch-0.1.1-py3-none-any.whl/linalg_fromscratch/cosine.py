import numpy as np

def cosine_similarity(x: np.ndarray, y: np.ndarray) -> float:
    x = np.asarray(x, dtype=float).ravel()
    y = np.asarray(y, dtype=float).ravel()
    denom = np.linalg.norm(x) * np.linalg.norm(y)
    if denom == 0:
        raise ValueError("Cosine similarity is undefined for zero vectors.")
    return float(np.dot(x, y) / denom)

def cosine_similarity_matrix(X: np.ndarray) -> np.ndarray:
    X = np.asarray(X, dtype=float)
    norms = np.linalg.norm(X, axis=1, keepdims=True)
    norms = np.where(norms == 0, 1e-12, norms)
    X_unit = X / norms
    return X_unit @ X_unit.T