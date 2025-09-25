# accurpy

Ultra-accurate and fast **double-double** (≈106-bit) approximation for the “new FM” function, with:

- **STRICT** mode (≤ 1 ULP across a broad domain), mirroring a validated Python DD algorithm
- **OPT** mode (FMA + 1-step `cbrt`), validated ≤ 1 ULP against STRICT on a dense 120k grid

## Install
```bash
pip install accurpy
```

## Usage
```python
import numpy as np
from accurpy import syncF

y_strict = syncF(10.0, skip_exp=False, mode="strict")
y_opt    = syncF(10.0, skip_exp=False, mode="opt")

x = np.geomspace(1e-12, 300.0, 1_000_000)
y = syncF(x, skip_exp=True, mode="opt")
```

## Parameters
- `skip_exp=False` — returns (P/Q)/s * x * exp(-x) (new FM with exponential)
- `skip_exp=True`  — returns (P/Q)/s * x (new FM without exponential)

## Modes
- `mode="strict"` — full double-double path with exact operation order (≤ 1 ULP).
- `mode="opt"` — faster path (FMA-based DD; 1-step `cbrt`), validated ≤ 1 ULP vs STRICT.

If the extension is unavailable, `accurpy` falls back to Python DD (slow but ≥ STRICT accuracy).

## License
MIT
