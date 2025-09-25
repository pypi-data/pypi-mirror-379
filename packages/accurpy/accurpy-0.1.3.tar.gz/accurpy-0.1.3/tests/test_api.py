import numpy as np
from accurpy import syncF

def test_scalar_roundtrip():
    y = syncF(10.0, skip_exp=False, mode="strict")
    z = syncF(10.0, skip_exp=False, mode="opt")
    assert np.isfinite(y) and np.isfinite(z)

def test_vectorized_shape():
    x = np.linspace(1e-12, 100.0, 1000)
    y = syncF(x, skip_exp=True, mode="opt")
    assert isinstance(y, np.ndarray)
    assert y.shape == x.shape
    assert y.dtype == np.float64
