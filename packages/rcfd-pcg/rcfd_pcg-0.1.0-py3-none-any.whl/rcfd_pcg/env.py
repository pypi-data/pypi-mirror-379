from __future__ import annotations

import os
import platform
from typing import Dict, Any


def collect_environment() -> Dict[str, Any]:
    try:
        import numpy as np  # type: ignore
    except Exception:
        np = None  # type: ignore
    try:
        import scipy  # type: ignore
    except Exception:
        scipy = None  # type: ignore

    env = {
        "python": platform.python_version(),
        "platform": platform.platform(),
        "system": platform.system(),
        "machine": platform.machine(),
        "processor": platform.processor(),
        "cpu_count": os.cpu_count(),
        "numpy": getattr(np, "__version__", None),
        "scipy": getattr(scipy, "__version__", None),
        "OMP_NUM_THREADS": os.environ.get("OMP_NUM_THREADS"),
        "OPENBLAS_NUM_THREADS": os.environ.get("OPENBLAS_NUM_THREADS"),
        "MKL_NUM_THREADS": os.environ.get("MKL_NUM_THREADS"),
        "NUMEXPR_NUM_THREADS": os.environ.get("NUMEXPR_NUM_THREADS"),
    }
    return env


