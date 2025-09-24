import numpy as np
from linalg_fromscratch import cosine_similarity, cosine_similarity_matrix

def test_cosine_basic_cases():
    assert np.isclose(cosine_similarity([1,2,3], [2,4,6]), 1.0)
    assert np.isclose(cosine_similarity([1,0,0], [0,1,0]), 0.0)
    assert np.isclose(cosine_similarity([1,-1], [-1,1]), -1.0, atol=1e-12)

def test_cosine_matrix_symmetry_and_diagonal():
    X = np.array([[1,0,0],[1,1,0],[0,1,1]], dtype=float)
    S = cosine_similarity_matrix(X)
    assert np.allclose(S, S.T, atol=1e-12)
    assert np.allclose(np.diag(S), 1.0)

def test_cosine_zero_vector_raises():
    with np.testing.assert_raises(ValueError):
        cosine_similarity([0,0,0], [1,2,3])