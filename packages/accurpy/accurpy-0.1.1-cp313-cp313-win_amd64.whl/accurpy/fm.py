\
from __future__ import annotations
import numpy as np

try:
    from . import _fm as _cext
    _HAVE_CEXT = True
except Exception:
    _cext = None
    _HAVE_CEXT = False

# Python DD fallback (bit-for-bit STRICT)
from ._dd_fallback import syncF as _syncF_py

def syncF(x, *, skip_exp: bool = False, mode: str = "strict", out=None):
    """
    Ultra-accurate double-double approximation for the "new FM" function.
    
    This implements the new FM function with ≤1 ULP accuracy using double-double
    precision arithmetic. The function computes:
    
    FM_new(x, skip_exp=False) = (P/Q)/s * x * exp(-x)  [with exponential]
    FM_new(x, skip_exp=True)  = (P/Q)/s * x            [without exponential]
    
    where P/Q is a validated (14,14) rational approximation and s = t²√(1+x)
    with t = cbrt(x/(1+x)).

    Parameters
    ----------
    x : float or array-like of float
        Input values (non-negative)
    skip_exp : bool, optional
        If False: returns (P/Q)/s * x * exp(-x) (new FM with exponential)
        If True:  returns (P/Q)/s * x (new FM without exponential)
        Default is False
    mode : {"strict","opt"}, optional
        "strict": ≤ 1 ULP accuracy; exact double-double operation ordering
        "opt":    faster FMA-based double-double; validated ≤ 1 ULP vs STRICT
        Default is "strict"
    out : numpy.ndarray, optional
        Optional output array (must be float64 and match input shape)

    Returns
    -------
    float or np.ndarray of float64
        Approximated FM_new values with ≤1 ULP accuracy
        
    Notes
    -----
    All computations are performed in double-double precision (≈106 bits)
    with a single rounding to IEEE-754 double at the end. The exponential
    exp(-x) is computed entirely in double-double when skip_exp=False.
    """
    mode = mode.lower()
    if np.isscalar(x):
        if _HAVE_CEXT:
            if mode == "strict":
                return _cext.fm_skipexp_strict(x) if skip_exp else _cext.fm_with_exp_strict(x)
            elif mode == "opt":
                return _cext.fm_skipexp_opt(x) if skip_exp else _cext.fm_with_exp_opt(x)
        # fallback
        return _syncF_py(float(x), skip_exp=skip_exp)

    a = np.asarray(x, dtype=np.float64, order="C")
    if out is not None:
        if out.dtype != np.float64 or out.shape != a.shape:
            raise ValueError("out must be float64 and match input shape")

    if _HAVE_CEXT:
        # Use buffer API (zero-copy) and return frombuffer -> copy to 'out' or new array
        buf = memoryview(a).cast("B")  # raw bytes
        if mode == "strict":
            bb = _cext.fm_skipexp_strict_buf(buf) if skip_exp else _cext.fm_with_exp_strict_buf(buf)
        elif mode == "opt":
            bb = _cext.fm_skipexp_opt_buf(buf) if skip_exp else _cext.fm_with_exp_opt_buf(buf)
        else:
            raise ValueError("mode must be 'strict' or 'opt'")

        y = np.frombuffer(bb, dtype=np.float64).reshape(a.shape)
        if out is None:
            return y.copy()  # own the result
        out[...] = y
        return out

    # Fallback: Python DD loop (slower)
    if out is None:
        out = np.empty_like(a, dtype=np.float64)
    it = np.nditer([a, out], flags=["refs_ok", "multi_index"], op_flags=[["readonly"], ["writeonly"]])
    for xi, yi in it:
        yi[...] = _syncF_py(float(xi), skip_exp=skip_exp)
    return out
