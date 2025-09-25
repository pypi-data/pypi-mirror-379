import numpy as np
import pytest
from accurpy import approx_FM_new

def ulp_distance(a, b):
    av = a.view(np.uint64)
    bv = b.view(np.uint64)
    return np.abs(av.astype(np.int64) - bv.astype(np.int64)).astype(np.uint64)

@pytest.mark.slow
def test_opt_vs_strict_ulp_10k():
    x = np.concatenate([
        np.geomspace(1e-18, 1e-6, 3000),
        np.geomspace(1e-6, 1.0,  3000),
        np.linspace(1.0, 300.0, 4000),
    ]).astype(np.float64)

    for skip in (False, True):
        ys = approx_FM_new(x, skip_exp=skip, mode="strict")
        yo = approx_FM_new(x, skip_exp=skip, mode="opt")
        ulp = ulp_distance(ys, yo)
        assert ulp.max() <= 1, f"OPT exceeded 1 ULP at {ulp.max()}"
