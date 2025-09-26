"""
RCFD-PCG: Ridge-Corrected Frequent-Directions Preconditioned Conjugate Gradient

This package provides a deterministic, single-pass sketch-based preconditioner
for overdetermined least-squares problems and a preconditioned CG solver.

Public API:
- build_rcfd_sketch
- rcfd_pcg_solve
- SyntheticProblem (helper for quick experiments)
"""

from .rcfd import (
    build_rcfd_sketch,
    rcfd_pcg_solve,
    build_rcfd_preconditioner,
    SyntheticProblem,
    save_preconditioner,
    load_preconditioner,
)

__all__ = [
    "build_rcfd_sketch",
    "rcfd_pcg_solve",
    "build_rcfd_preconditioner",
    "SyntheticProblem",
    "save_preconditioner",
    "load_preconditioner",
]


