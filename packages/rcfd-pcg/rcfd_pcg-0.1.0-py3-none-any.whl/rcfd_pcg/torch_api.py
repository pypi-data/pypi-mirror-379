from __future__ import annotations

from typing import Optional, Tuple, Dict, Any


def cg_solve_normal_eq_torch(
    A,
    b,
    ridge_lambda: float = 0.0,
    tol: float = 1e-6,
    max_iter: int = 200,
    record_history: bool = False,
    preconditioner_mode: str = "none",  # "none" or "diag"
) -> Tuple["object", Dict[str, Any]]:
    """
    Autograd-safe CG on normal equations using PyTorch ops only.

    Solves (A^T A + lam I) x = A^T b. This path is differentiable wrt A and b.
    No preconditioner is used to preserve autograd friendliness.
    """
    try:
        import torch  # type: ignore
    except Exception as e:  # pragma: no cover
        raise RuntimeError("PyTorch is required for cg_solve_normal_eq_torch")

    if not torch.is_tensor(A) or not torch.is_tensor(b):
        raise TypeError("A and b must be torch.Tensors")

    n, d = A.shape
    b = b.reshape(n)
    x = torch.zeros(d, dtype=A.dtype, device=A.device)

    def normal_matvec(v):
        Av = A @ v
        AtAv = A.T @ Av
        return AtAv + ridge_lambda * v

    rhs = A.T @ b
    r = rhs - normal_matvec(x)

    # Optional simple diagonal preconditioner (autograd-safe prototype)
    if str(preconditioner_mode).lower() == "diag":
        diag_entries = torch.sum(A * A, dim=0) + ridge_lambda
        # Avoid division by zero
        diag_entries = torch.clamp(diag_entries, min=1e-30)
        def M_inv(vec):
            return vec / diag_entries
    else:
        def M_inv(vec):
            return vec

    z = M_inv(r)
    p = z.clone()
    rz_old = torch.dot(r, z)
    rhs_norm = torch.linalg.norm(rhs)

    iters = 0
    hist = [] if record_history else None
    for k in range(max_iter):
        Ap = normal_matvec(p)
        denom = torch.dot(p, Ap)
        if denom.abs() == 0:
            break
        alpha = rz_old / denom
        x = x + alpha * p
        r = r - alpha * Ap
        res_norm = torch.linalg.norm(r)
        if record_history:
            hist.append(res_norm.detach().cpu().item())
        if res_norm <= tol * (rhs_norm + 1e-30):
            iters = k + 1
            break
        z = M_inv(r)
        rz_new = torch.dot(r, z)
        beta = rz_new / (rz_old + 1e-30)
        p = z + beta * p
        rz_old = rz_new
        iters = k + 1

    diag: Dict[str, Any] = {
        "iterations": int(iters),
        "residual_norm": float(res_norm.detach().cpu().item()),
        "rhs_norm": float(rhs_norm.detach().cpu().item()),
    }
    if record_history and hist is not None:
        diag["residual_history"] = hist
    return x, diag


