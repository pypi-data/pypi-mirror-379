from __future__ import annotations

from typing import Optional, Tuple, Any

import numpy as np

try:
    import scipy.sparse.linalg as spla
except Exception:  # pragma: no cover
    spla = None  # type: ignore

from .rcfd import build_rcfd_preconditioner


def make_normal_operator(A: np.ndarray, ridge_lambda: float):
    if spla is None:
        raise RuntimeError("SciPy is required for LinearOperator support")
    n, d = A.shape

    def mv(v: np.ndarray) -> np.ndarray:
        return A.T @ (A @ v) + ridge_lambda * v

    def rmv(v: np.ndarray) -> np.ndarray:
        return A.T @ (A @ v) + ridge_lambda * v

    return spla.LinearOperator(shape=(d, d), matvec=mv, rmatvec=rmv, dtype=float)


def make_cholesky_preconditioner_operator(chol: Tuple[np.ndarray, bool]):
    if spla is None:
        raise RuntimeError("SciPy is required for LinearOperator support")
    from scipy.linalg import cho_solve

    c, lower = chol
    d = c.shape[0]

    def mv(v: np.ndarray) -> np.ndarray:
        return cho_solve((c, lower), v, check_finite=False)

    return spla.LinearOperator(shape=(d, d), matvec=mv, rmatvec=mv, dtype=float)


def cg_solve_normal_eq(
    A: np.ndarray,
    b: np.ndarray,
    ridge_lambda: float,
    tol: float = 1e-6,
    max_iter: int = 200,
    use_rcfd_preconditioner: bool = True,
    rcfd_eps: float = 0.25,
) -> Tuple[np.ndarray, dict]:
    """
    Solve (A^T A + lam I) x = A^T b using SciPy CG with optional RCFD preconditioner.
    Returns (x, diagnostics).
    """
    if spla is None:
        raise RuntimeError("SciPy is required for CG solve")
    n, d = A.shape
    rhs = A.T @ b
    H = make_normal_operator(A, ridge_lambda)

    M = None
    if use_rcfd_preconditioner:
        chol, _ = build_rcfd_preconditioner(A, ridge_lambda=ridge_lambda, epsilon=rcfd_eps)
        M = make_cholesky_preconditioner_operator(chol)

    x0 = np.zeros(d)
    # SciPy changed CG signature (tol -> rtol, added atol). Try new API first, fallback to old.
    try:
        x, info = spla.cg(H, rhs, x0=x0, rtol=tol, atol=0, maxiter=max_iter, M=M)  # SciPy >= 1.11
    except TypeError:
        x, info = spla.cg(H, rhs, x0=x0, tol=tol, maxiter=max_iter, M=M)  # SciPy <= 1.10
    diagnostics = {"cg_info": info}
    return x, diagnostics


