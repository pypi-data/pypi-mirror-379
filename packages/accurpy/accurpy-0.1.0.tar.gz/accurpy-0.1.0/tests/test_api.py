import numpy as np
from accurpy import approx_FM_new

def test_scalar_roundtrip():
    y = approx_FM_new(10.0, skip_exp=False, mode="strict")
    z = approx_FM_new(10.0, skip_exp=False, mode="opt")
    assert np.isfinite(y) and np.isfinite(z)

def test_vectorized_shape():
    x = np.linspace(1e-12, 100.0, 1000)
    y = approx_FM_new(x, skip_exp=True, mode="opt")
    assert isinstance(y, np.ndarray)
    assert y.shape == x.shape
    assert y.dtype == np.float64
