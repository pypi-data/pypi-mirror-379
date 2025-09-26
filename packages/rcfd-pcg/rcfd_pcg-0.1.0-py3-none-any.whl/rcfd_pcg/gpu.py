from __future__ import annotations

from typing import Optional, Tuple, Dict, Any


def _require_cupy():
    try:
        import cupy as cp  # type: ignore
    except Exception as e:  # pragma: no cover
        raise RuntimeError("CuPy is required for GPU prototype: pip install cupy-cuda11x (or appropriate build)") from e
    return cp


def build_rcfd_sketch_gpu(
    A,
    ridge_lambda: float,
    epsilon: float = 0.25,
    device: Optional[int] = None,
):
    """GPU prototype: build sketch via full Gram eigendecomposition on GPU.

    This is an O(d^3) path intended as a prototype. For large d, prefer CPU randomized compression.
    Returns a CuPy array B with shape (ell, d).
    """
    cp = _require_cupy()
    with cp.cuda.Device(device) if device is not None else cp.cuda.Device():
        A_gpu = cp.asarray(A)
        n, d = A_gpu.shape
        ell = int((d + float(epsilon) - 1) // float(epsilon)) if epsilon > 0 else d
        ell = max(1, min(ell, d))
        gram = A_gpu.T @ A_gpu
        s2, V = cp.linalg.eigh(gram)
        s2 = s2[::-1]
        V = V[:, ::-1]
        r = int(min(ell, d, s2.size))
        thr_index = int(min(s2.size - 1, max(0, ell - 1)))
        threshold = float(s2[thr_index].get())
        shift = max(threshold - ridge_lambda, 0.0)
        s_new = cp.sqrt(cp.maximum(s2[:r] - shift, 0.0))
        B = cp.zeros((ell, d), dtype=A_gpu.dtype)
        if r > 0:
            B[:r, :] = (V[:, :r] * s_new).T
        return B


def build_rcfd_sketch_gpu_rand(
    A,
    ridge_lambda: float,
    epsilon: float = 0.25,
    oversampling: int = 8,
    power_iters: int = 0,
    device: Optional[int] = None,
):
    """GPU randomized compression prototype for building RCFD sketch.

    Uses a range-finder on the Gram to approximate top right singular vectors on GPU.
    Returns a CuPy array B with shape (ell, d).
    """
    cp = _require_cupy()
    with cp.cuda.Device(device) if device is not None else cp.cuda.Device():
        A_gpu = cp.asarray(A)
        n, d = A_gpu.shape
        ell = int((d + float(epsilon) - 1) // float(epsilon)) if epsilon > 0 else d
        ell = max(1, min(ell, d))

        r = min(ell, d)
        target = int(min(d, r + int(max(0, oversampling))))
        if target <= 0:
            return cp.zeros((ell, d), dtype=A_gpu.dtype)

        Omega = cp.random.standard_normal((d, target), dtype=A_gpu.dtype)
        Y = A_gpu @ Omega  # (n x target)
        for _ in range(max(0, int(power_iters))):
            Z = A_gpu.T @ Y  # (d x target)
            Y = A_gpu @ Z    # (n x target)

        Q, _ = cp.linalg.qr(Y, mode="reduced")  # (n x target)
        Bsmall = Q.T @ A_gpu  # (target x d)

        gram = Bsmall.T @ Bsmall
        s2, V = cp.linalg.eigh(gram)
        s2 = s2[::-1]
        V = V[:, ::-1]
        take = int(min(ell, d, s2.size))
        thr_index = int(min(s2.size - 1, max(0, ell - 1)))
        threshold = float(cp.asnumpy(s2[thr_index]))
        shift = max(threshold - ridge_lambda, 0.0)
        s_new = cp.sqrt(cp.maximum(s2[:take] - shift, 0.0))
        B = cp.zeros((ell, d), dtype=A_gpu.dtype)
        if take > 0:
            B[:take, :] = (V[:, :take] * s_new).T
        return B

def rcfd_pcg_solve_gpu(
    A,
    b,
    ridge_lambda: float,
    epsilon: float = 0.25,
    tol: float = 1e-6,
    max_iter: int = 200,
    record_history: bool = False,
    preconditioner_mode: str = "none",
    device: Optional[int] = None,
) -> Tuple["object", Dict[str, Any]]:
    """GPU prototype: CG on normal equations using CuPy ops.

    Preconditioner: none or diagonal (prototype). Returns (x_gpu, diagnostics).
    """
    cp = _require_cupy()
    with cp.cuda.Device(device) if device is not None else cp.cuda.Device():
        A_gpu = cp.asarray(A)
        b_gpu = cp.asarray(b).reshape(-1)
        n, d = A_gpu.shape
        x = cp.zeros(d, dtype=A_gpu.dtype)

        def normal_matvec(v):
            Av = A_gpu @ v
            AtAv = A_gpu.T @ Av
            return AtAv + ridge_lambda * v

        rhs = A_gpu.T @ b_gpu
        r = rhs - normal_matvec(x)
        if str(preconditioner_mode).lower() == "diag":
            diag_entries = cp.sum(A_gpu * A_gpu, axis=0) + ridge_lambda
            diag_entries = cp.maximum(diag_entries, 1e-30)

            def M_inv(vec):
                return vec / diag_entries
        else:
            def M_inv(vec):
                return vec

        z = M_inv(r)
        p = z.copy()
        rz_old = float(cp.dot(r, z).get())
        rhs_norm = float(cp.linalg.norm(rhs).get())

        iters = 0
        hist = [] if record_history else None
        for k in range(int(max_iter)):
            Ap = normal_matvec(p)
            denom = float(cp.dot(p, Ap).get())
            if denom == 0.0:
                break
            alpha = rz_old / denom
            x = x + alpha * p
            r = r - alpha * Ap
            res_norm = float(cp.linalg.norm(r).get())
            if record_history:
                hist.append(res_norm)
            if res_norm <= tol * (rhs_norm + 1e-30):
                iters = k + 1
                break
            z = M_inv(r)
            rz_new = float(cp.dot(r, z).get())
            beta = rz_new / (rz_old + 1e-30)
            p = z + beta * p
            rz_old = rz_new
            iters = k + 1

        diagnostics: Dict[str, Any] = {
            "iterations": int(iters),
            "residual_norm": float(res_norm),
            "rhs_norm": float(rhs_norm),
        }
        if record_history and hist is not None:
            diagnostics["residual_history"] = hist
        return x, diagnostics


