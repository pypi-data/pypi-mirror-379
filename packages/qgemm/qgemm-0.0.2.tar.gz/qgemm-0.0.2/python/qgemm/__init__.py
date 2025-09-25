"""
qgemm Python package
 - Importing this package attempts to load the compiled CUDA/C++ extension
   which registers torch.ops.qgemm.* operators.

Build the extension first (see README) or install the package with
QGEMM_BUILD_EXT=1 so the module qgemm._C is available.
"""

from __future__ import annotations

import importlib
from typing import Any

_loaded: bool = False
_err: Exception | None = None


def _try_import_extension() -> bool:
    global _loaded, _err
    if _loaded:
        return True
    try:
        importlib.import_module("qgemm._C")
        _loaded = True
        return True
    except Exception as e:  # pragma: no cover - best-effort auto-load
        _err = e
        return False


# Auto-load at import time (best effort). Users can ignore if only using CPU utils.
_try_import_extension()

__all__ = [
    "_try_import_extension",
]

