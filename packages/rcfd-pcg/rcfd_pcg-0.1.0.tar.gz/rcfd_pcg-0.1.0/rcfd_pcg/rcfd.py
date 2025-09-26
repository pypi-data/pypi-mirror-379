from __future__ import annotations

import math
from dataclasses import dataclass
import os
from typing import Callable, Iterable, Optional, Tuple, Dict, Any
import time

import numpy as np
from .util import choose_compression_params, choose_shrink_multiple, limit_blas_threads, estimate_spectral_spread_indicator
from concurrent.futures import ThreadPoolExecutor

try:
    import scipy.sparse as sp
    from scipy.linalg import cho_factor, cho_solve
    from scipy.sparse.linalg import lsqr
except Exception:  # pragma: no cover - optional at import time for type checkers
    sp = None  # type: ignore
    cho_factor = None  # type: ignore
    cho_solve = None  # type: ignore
    lsqr = None  # type: ignore

# Optional PyTorch support (convert to NumPy on ingress). Allow skipping import via env var to speed up CLI runs.
_RCFD_SKIP_TORCH_IMPORT = bool(os.environ.get("RCFD_SKIP_TORCH_IMPORT", ""))
if not _RCFD_SKIP_TORCH_IMPORT:
    try:  # pragma: no cover - optional dependency
        import torch  # type: ignore
    except Exception:  # pragma: no cover
        torch = None  # type: ignore
else:  # pragma: no cover
    torch = None  # type: ignore

# Optional CuPy for GPU sketch auto-detection
try:  # pragma: no cover - optional dependency
    import cupy as _cp  # type: ignore
    _RCFD_HAS_CUPY = True
    try:
        _RCFD_NUM_GPU = _cp.cuda.runtime.getDeviceCount()
    except Exception:
        _RCFD_NUM_GPU = 0
except Exception:  # pragma: no cover
    _RCFD_HAS_CUPY = False
    _RCFD_NUM_GPU = 0


def _is_sparse_matrix(A: np.ndarray) -> bool:
    return sp is not None and sp.issparse(A)


def _as_dense_row_block(A_block: np.ndarray) -> np.ndarray:
    if sp is not None and sp.issparse(A_block):
        return A_block.toarray()
    return np.asarray(A_block)


def rcfd_shrink(sketch_matrix: np.ndarray, ridge_lambda: float) -> np.ndarray:
    """
    Perform a ridge-aware Frequent-Directions shrink on the sketch matrix.

    Parameters
    ----------
    sketch_matrix: np.ndarray
        Current sketch matrix B with shape (ell, d).
    ridge_lambda: float
        Ridge parameter used to protect the weakest singular direction.

    Returns
    -------
    np.ndarray
        The updated sketch matrix of the same shape as the input.
    """
    U, s, Vt = np.linalg.svd(sketch_matrix, full_matrices=False)
    s2 = s ** 2
    weakest_energy = float(s2[-1]) if s2.size > 0 else 0.0
    shift = max(weakest_energy - ridge_lambda, 0.0)
    s_new = np.sqrt(np.maximum(s2 - shift, 0.0))
    return (U * s_new) @ Vt


def _compress_buffer_to_top_rows(buffer_matrix: np.ndarray, ell: int, ridge_lambda: float) -> np.ndarray:
    """
    Compress an overfull buffer (rows_filled x d) to at most ell rows using
    eigen-decomposition of the d x d Gram matrix.

    Returns a matrix of shape (ell, d) whose first r rows are s_new_i * v_i^T
    for the top r right singular vectors v_i, where r = min(ell, d).
    """
    d = buffer_matrix.shape[1]
    # Work on d x d Gram for speed when ell >> d
    gram_d = buffer_matrix.T @ buffer_matrix
    s2, V = np.linalg.eigh(gram_d)
    # eigh returns ascending eigenvalues; reverse to descending
    s2 = s2[::-1]
    V = V[:, ::-1]
    r = min(ell, d, s2.size)
    # Ridge-aware threshold based on the ell-th singular value if available
    thr_index = min(s2.size - 1, max(0, ell - 1))
    threshold = float(s2[thr_index])
    shift = max(threshold - ridge_lambda, 0.0)
    s_new = np.sqrt(np.maximum(s2[:r] - shift, 0.0))
    # Build compressed sketch: rows are s_new_i * v_i^T
    B_comp = np.zeros((ell, d), dtype=buffer_matrix.dtype)
    if r > 0:
        B_comp[:r, :] = (V[:, :r] * s_new).T
    return B_comp


def _randomized_compress_buffer(
    buffer_matrix: np.ndarray,
    ell: int,
    ridge_lambda: float,
    oversampling: int = 8,
    power_iters: int = 0,
    rng: Optional[np.random.Generator] = None,
    parallel_blocks: int = 1,
) -> np.ndarray:
    """
    Randomized low-rank compression of buffer to top ell rows using a sketch of the Gram matrix.

    Uses a range-finder on A (buffer) via Gaussian test matrix to approximate top right singular vectors.
    This reduces cost relative to exact eigendecomposition for large buffers.
    """
    A = buffer_matrix
    n_rows, d = A.shape
    r = min(ell, d)
    target = min(d, r + oversampling)
    if target <= 0:
        return np.zeros((ell, d), dtype=A.dtype)

    # Gaussian test matrix
    if rng is None:
        rng = np.random.default_rng()
    Omega = rng.standard_normal((d, target))
    # Optionally compute Y in parallel across row chunks
    if int(parallel_blocks) > 1:
        Y = np.empty((n_rows, target), dtype=A.dtype)
        num_workers = min(int(parallel_blocks), max(1, n_rows))
        chunk = max(1, (n_rows + num_workers - 1) // num_workers)
        def mul_chunk(s: int, t: int) -> None:
            Y[s:t] = A[s:t, :] @ Omega
        # Avoid BLAS oversubscription while Python threads are active
        with limit_blas_threads(1):
            with ThreadPoolExecutor(max_workers=num_workers) as ex:
                futures = [ex.submit(mul_chunk, s, min(s + chunk, n_rows)) for s in range(0, n_rows, chunk)]
                for f in futures:
                    f.result()
    else:
        Y = A @ Omega  # (n_rows x target)
    # Power iterations (optional)
    for _ in range(max(0, int(power_iters))):
        Z = A.T @ Y
        if int(parallel_blocks) > 1:
            Y2 = np.empty_like(Y)
            num_workers = min(int(parallel_blocks), max(1, n_rows))
            chunk = max(1, (n_rows + num_workers - 1) // num_workers)
            def mul_chunk2(s: int, t: int) -> None:
                Y2[s:t] = A[s:t, :] @ Z
            # Avoid BLAS oversubscription while Python threads are active
            with limit_blas_threads(1):
                with ThreadPoolExecutor(max_workers=num_workers) as ex:
                    futures = [ex.submit(mul_chunk2, s, min(s + chunk, n_rows)) for s in range(0, n_rows, chunk)]
                    for f in futures:
                        f.result()
            Y = Y2
        else:
            Y = A @ Z
    # Orthonormal basis of range(A)
    Q, _ = np.linalg.qr(Y, mode="reduced")  # (n_rows x q)
    # Projected small matrix
    Bsmall = Q.T @ A  # (q x d)
    # Eigh on Gram of small
    gram_small = Bsmall.T @ Bsmall
    s2, V = np.linalg.eigh(gram_small)
    s2 = s2[::-1]
    V = V[:, ::-1]
    take = min(r, V.shape[1])
    # Ridge-aware shrink
    thr_index = min(s2.size - 1, max(0, ell - 1))
    threshold = float(s2[thr_index])
    shift = max(threshold - ridge_lambda, 0.0)
    s_new = np.sqrt(np.maximum(s2[:take] - shift, 0.0))
    B_comp = np.zeros((ell, d), dtype=A.dtype)
    if take > 0:
        B_comp[:take, :] = (V[:, :take] * s_new).T
    return B_comp


def build_rcfd_sketch(
    A: np.ndarray,
    ridge_lambda: float,
    epsilon: float = 0.25,
    batch_size: int = 1024,
    shrink_multiple: int = 2,
    compression: str = "auto",  # "auto", "eigh" or "rand"
    oversampling: int = 8,
    power_iters: int = 0,
    sketch_dtype: str = "float32",
    random_state: Optional[int] = None,
    num_passes: int = 1,
    parallel_blocks: int = 1,
    spill_dir: Optional[str] = None,
) -> np.ndarray:
    """
    Build a ridge-corrected Frequent-Directions sketch B for A.

    This function makes a single logical pass over the rows of A and maintains
    a compact sketch B of shape (ell, d), where ell = ceil(d / epsilon).

    Parameters
    ----------
    A: np.ndarray or scipy.sparse matrix
        Data matrix of shape (n, d). Sparse matrices are supported (CSR/CSC/COO).
    ridge_lambda: float
        Ridge parameter lambda >= 0.
    epsilon: float
        Target relative distortion parameter in (0, 1). Typical 0.15–0.35.
    batch_size: int
        Number of rows to pull at a time (for sparse matrices, improves speed).

    Parameters
    ----------
    shrink_multiple: int
        Maintain a buffer of size shrink_multiple * ell and shrink only when
        the buffer is full. Use 2 for standard amortization (≈ one SVD per ell rows).

    Returns
    -------
    np.ndarray
        Sketch matrix B with shape (ell, d).
    """
    if epsilon <= 0 or epsilon >= 1:
        raise ValueError("epsilon must be in (0, 1)")

    if ridge_lambda < 0:
        raise ValueError("ridge_lambda must be >= 0")

    # Convert PyTorch tensors to NumPy if needed
    if torch is not None and hasattr(A, "detach") and hasattr(A, "cpu"):
        try:
            A = A.detach().cpu().numpy()
        except Exception:
            pass

    n, d = A.shape
    ell = int(math.ceil(d / float(epsilon)))
    # Auto-tune shrink_multiple if negative or zero
    if int(shrink_multiple) < 1:
        shrink_multiple = choose_shrink_multiple(d)
    else:
        shrink_multiple = int(shrink_multiple)
    capacity = max(ell * shrink_multiple, ell)

    rng = np.random.default_rng(random_state)

    # Resolve compression strategy
    if compression not in ("auto", "eigh", "rand", "eigh_inc"):
        raise ValueError("compression must be one of {'auto','eigh','eigh_inc','rand'}")
    effective_compression = compression
    eff_oversampling = oversampling
    eff_power_iters = power_iters

    if compression == "auto":
        # Estimate density if sparse
        est_density = None
        if _is_sparse_matrix(A):
            try:
                est_density = float(A.nnz) / float(A.shape[0] * A.shape[1])
            except Exception:
                est_density = None
        eff_method, eff_oversampling, eff_power_iters = choose_compression_params(d, est_density)
        effective_compression = eff_method
        # Probe-based spread estimator (dense and sparse) to refine parameters
        if effective_compression == "rand" and eff_power_iters <= 1:
            try:
                indicator = estimate_spectral_spread_indicator(A, max_rows=2048, power_iters=3)
                # Thresholds chosen from ablation guidance
                if indicator > 100.0:
                    eff_power_iters = max(eff_power_iters, 1)
                    if 128 <= d <= 4096:
                        eff_oversampling = max(eff_oversampling, 12)
                elif indicator > 30.0:
                    eff_power_iters = max(eff_power_iters, 1)
            except Exception:
                pass

    # Cache for incremental eig updates
    eig_cache: Dict[str, np.ndarray] = {}

    def _incremental_eig_compress_buffer(buffer_matrix: np.ndarray) -> np.ndarray:
        dloc = buffer_matrix.shape[1]
        gram_d = buffer_matrix.T @ buffer_matrix
        # Use previous eigenvectors as a subspace guess when available
        V_prev = eig_cache.get("V")
        rloc = min(ell, dloc)
        if V_prev is not None and V_prev.shape[0] == dloc and V_prev.shape[1] >= 1:
            q = min(rloc, V_prev.shape[1])
            V0 = V_prev[:, :q]
            Y = gram_d @ V0
            Q, _ = np.linalg.qr(Y, mode="reduced")
            T = Q.T @ gram_d @ Q
            evals, Z = np.linalg.eigh(T)
            evals = evals[::-1]
            Z = Z[:, ::-1]
            take = min(rloc, Z.shape[1])
            V_approx = Q @ Z[:, :take]
            eig_cache["V"] = V_approx
            # Ridge-aware shrink
            thr_index = min(evals.size - 1, max(0, ell - 1))
            threshold = float(evals[thr_index])
            shift = max(threshold - ridge_lambda, 0.0)
            s_new = np.sqrt(np.maximum(evals[:take] - shift, 0.0))
            B_comp = np.zeros((ell, dloc), dtype=buffer_matrix.dtype)
            if take > 0:
                B_comp[:take, :] = (V_approx * s_new).T
            return B_comp
        else:
            # Fallback to exact path and seed the cache
            s2, V = np.linalg.eigh(gram_d)
            s2 = s2[::-1]
            V = V[:, ::-1]
            take = min(rloc, V.shape[1])
            eig_cache["V"] = V[:, :take]
            thr_index = min(s2.size - 1, max(0, ell - 1))
            threshold = float(s2[thr_index])
            shift = max(threshold - ridge_lambda, 0.0)
            s_new = np.sqrt(np.maximum(s2[:take] - shift, 0.0))
            B_comp = np.zeros((ell, dloc), dtype=buffer_matrix.dtype)
            if take > 0:
                B_comp[:take, :] = (V[:, :take] * s_new).T
            return B_comp

    def _single_pass() -> np.ndarray:
        spill_path: Optional[str] = None
        B: np.ndarray
        if spill_dir:
            try:
                import os, tempfile
                fd, tmp_path = tempfile.mkstemp(prefix="rcfd_sketch_", suffix=".dat", dir=spill_dir)
                os.close(fd)
                spill_path = tmp_path
                B = np.memmap(tmp_path, dtype=sketch_dtype, mode="w+", shape=(capacity, d))  # type: ignore
            except Exception:
                B = np.zeros((capacity, d), dtype=sketch_dtype)
                spill_path = None
        else:
            B = np.zeros((capacity, d), dtype=sketch_dtype)
        rows_filled = 0

        # Stream in blocks (supports sparse and dense) with vectorized copies
        def compress_current():
            nonlocal rows_filled
            if rows_filled == 0:
                return
            if effective_compression == "rand":
                compressed_local = _randomized_compress_buffer(
                    B[:rows_filled], ell, ridge_lambda, oversampling=eff_oversampling, power_iters=eff_power_iters, rng=rng, parallel_blocks=parallel_blocks
                )
            elif effective_compression == "eigh_inc":
                compressed_local = _incremental_eig_compress_buffer(B[:rows_filled])
            else:
                compressed_local = _compress_buffer_to_top_rows(B[:rows_filled], ell, ridge_lambda)
            B[:ell] = compressed_local
            rows_filled = ell

        for start in range(0, n, batch_size):
            stop = min(start + batch_size, n)
            block = _as_dense_row_block(A[start:stop, :]) if _is_sparse_matrix(A) else np.asarray(A[start:stop, :])
            m = block.shape[0]
            blk_idx = 0
            while blk_idx < m:
                space = capacity - rows_filled
                if space == 0:
                    compress_current()
                    space = capacity - rows_filled
                take = min(space, m - blk_idx)
                if take > 0:
                    B[rows_filled:rows_filled + take] = block[blk_idx:blk_idx + take]
                    rows_filled += take
                    blk_idx += take

        if rows_filled == 0:
            result = np.array(B[:1], copy=True)
            # Cleanup memmap file if used
            try:
                del B
            except Exception:
                pass
            if spill_path is not None:
                try:
                    import os as _os
                    _os.remove(spill_path)
                except Exception:
                    pass
            return result
        # Final compression if buffer larger than ell
        if rows_filled > ell:
            if effective_compression == "rand":
                compressed = _randomized_compress_buffer(
                    B[:rows_filled], ell, ridge_lambda, oversampling=eff_oversampling, power_iters=eff_power_iters, rng=rng, parallel_blocks=parallel_blocks
                )
            elif effective_compression == "eigh_inc":
                compressed = _incremental_eig_compress_buffer(B[:rows_filled])
            else:
                compressed = _compress_buffer_to_top_rows(B[:rows_filled], ell, ridge_lambda)
            B[:ell] = compressed
            rows_filled = ell
        result = np.array(B[: max(rows_filled, 1)], copy=True)
        # Cleanup memmap file if used
        try:
            del B
        except Exception:
            pass
        if spill_path is not None:
            try:
                import os as _os
                _os.remove(spill_path)
            except Exception:
                pass
        return result

    # Auto-disable 2nd pass unless adversarial spectrum is suspected
    # Heuristic: if epsilon is not extremely small and d is moderate, 2-pass rarely helps
    effective_passes = int(num_passes)
    if effective_passes > 1 and (epsilon >= 0.15 and d <= 2048):
        effective_passes = 1

    # Support 1-pass or simple 2-pass refinement
    if effective_passes <= 1:
        return _single_pass()
    # First pass
    _ = _single_pass()
    # Second pass from original A (simple refinement)
    return _single_pass()


def _gram_cholesky_from_sketch(sketch_matrix: np.ndarray, ridge_lambda: float) -> Tuple[np.ndarray, Tuple[np.ndarray, bool]]:
    d = sketch_matrix.shape[1]
    # Build Gram in float64 for numerical robustness regardless of sketch dtype
    gram = (sketch_matrix.T @ sketch_matrix).astype(np.float64, copy=False)
    # Add ridge and a tiny diagonal floor based on energy scale
    trace_val0 = float(np.trace(gram))
    diag_floor = max(1e-15, 1e-12 * trace_val0 / (d + 1e-30))
    gram += (float(ridge_lambda) + diag_floor) * np.eye(d, dtype=gram.dtype)

    # Always symmetrize before factorization
    gram = 0.5 * (gram + gram.T)

    # Robustify: add progressively larger diagonal jitter and retry
    trace_val = float(np.trace(gram))
    base = max(1e-12, 1e-14 * trace_val / (d + 1e-30))
    last_err: Exception | None = None
    for attempt in range(6):
        try:
            jitter = (10.0 ** attempt) * base
            c_factor = cho_factor(gram + jitter * np.eye(d, dtype=gram.dtype), lower=False, check_finite=False)
            return gram, c_factor
        except Exception as e:
            last_err = e
            continue

    # Fallback: eigenvalue floor to ensure SPD
    evals, V = np.linalg.eigh(gram)
    floor = max(base, 1e-12)
    evals_floor = np.maximum(evals, floor)
    gram_spd = (V * evals_floor) @ V.T
    c_factor = cho_factor(gram_spd, lower=False, check_finite=False)
    return gram_spd, c_factor


class _SpmvCounter:
    def __init__(self, A: np.ndarray):
        self.A = A
        self.num_Ax = 0
        self.num_ATx = 0

    def Ax(self, v: np.ndarray) -> np.ndarray:
        self.num_Ax += 1
        return self.A @ v

    def ATx(self, v: np.ndarray) -> np.ndarray:
        self.num_ATx += 1
        return self.A.T @ v


def _apply_normal_eq_matvec(A: np.ndarray, v: np.ndarray, ridge_lambda: float, counter: Optional[_SpmvCounter] = None) -> np.ndarray:
    if counter is None:
        Av = A @ v
        At_A_v = A.T @ Av
    else:
        Av = counter.Ax(v)
        At_A_v = counter.ATx(Av)
    return At_A_v + ridge_lambda * v


def _apply_normal_eq_matvec_parallel(
    A: np.ndarray,
    v: np.ndarray,
    ridge_lambda: float,
    threads: int,
    chunk_size: Optional[int] = None,
    counter: Optional[_SpmvCounter] = None,
) -> np.ndarray:
    """Shared-memory parallel matvec for (A^T A + lam I) v.

    Falls back to single-thread path when threads<=1 or A is sparse.
    """
    if threads <= 1 or _is_sparse_matrix(A):
        return _apply_normal_eq_matvec(A, v, ridge_lambda, counter)

    n, d = A.shape
    num_workers = min(int(threads), max(1, n))
    # First compute Av in row chunks
    Av = np.empty(n, dtype=float)
    chunk = int(chunk_size) if (chunk_size is not None and int(chunk_size) > 0) else max(1, (n + num_workers - 1) // num_workers)

    def mul_Ax_rowblock(start: int, stop: int) -> None:
        Av[start:stop] = A[start:stop, :] @ v

    # Avoid BLAS oversubscription while Python threads are active
    with limit_blas_threads(1):
        with ThreadPoolExecutor(max_workers=num_workers) as ex:
            futures = [ex.submit(mul_Ax_rowblock, s, min(s + chunk, n)) for s in range(0, n, chunk)]
            for f in futures:
                f.result()

    # Optionally count one Ax and one ATx per global operation
    if counter is not None:
        counter.num_Ax += 1
        counter.num_ATx += 1

    # Compute A^T Av via reduction across row chunks
    partials: list[np.ndarray] = []

    def mul_ATx_rowblock(start: int, stop: int) -> np.ndarray:
        return A[start:stop, :].T @ Av[start:stop]

    with limit_blas_threads(1):
        with ThreadPoolExecutor(max_workers=num_workers) as ex:
            futures2 = [ex.submit(mul_ATx_rowblock, s, min(s + chunk, n)) for s in range(0, n, chunk)]
            for f in futures2:
                partials.append(f.result())
    At_A_v = np.sum(partials, axis=0)
    return At_A_v + ridge_lambda * v


def rcfd_pcg_solve(
    A: np.ndarray,
    b: np.ndarray,
    ridge_lambda: float,
    epsilon: float = 0.25,
    tol: float = 1e-6,
    max_iter: int = 200,
    batch_size: Optional[int] = None,
    shrink_multiple: int = 2,
    count_spmv: bool = False,
    compression: str = "auto",
    oversampling: int = 8,
    power_iters: int = 0,
    preconditioner: Optional[Tuple[np.ndarray, bool]] = None,
    record_history: bool = False,
    random_state: Optional[int] = None,
    precond_min_ridge: float = 1e-7,
    sketch_dtype: str = "float32",
    return_diagnostics: bool = False,
    num_passes: int = 1,
    parallel_blocks: int = 1,
    return_torch: bool = False,
    dense_chunk_size: Optional[int] = None,
    precond_type: str = "chol",
    num_col_blocks: int = 1,
    auto_bail_out: bool = True,
    bail_out_threshold: float = 5.0,
    precond_warmup_solves: int = 0,
    spill_dir: Optional[str] = None,
    force_gpu_sketch: bool = False,
) -> Tuple[np.ndarray, Optional[dict]]:
    """
    Solve min_x 0.5*||Ax-b||^2 + 0.5*lambda*||x||^2 using RCFD preconditioned CG on normal equations.

    Parameters
    ----------
    A: np.ndarray or scipy.sparse matrix
        Matrix of shape (n, d).
    b: np.ndarray
        Right-hand side vector of shape (n,).
    ridge_lambda: float
        Ridge parameter lambda >= 0.
    epsilon: float
        Sketch distortion parameter in (0, 1).
    tol: float
        Relative tolerance on residual in the normal equations.
    max_iter: int
        Maximum number of PCG iterations.
    return_diagnostics: bool
        If True, also returns a diagnostics dictionary.

    Returns
    -------
    x: np.ndarray
        Solution vector of shape (d,).
    diagnostics: dict or None
        If requested, includes iteration count and final residual norm.
    """
    n, d = A.shape
    b = np.asarray(b).reshape(-1)
    if b.shape[0] != n:
        raise ValueError("b must have shape (n,)")

    t_start = time.perf_counter()
    # Optional bail-out (skip preconditioner) for well-conditioned problems
    bail_out_triggered = False
    bail_out_info: Optional[Dict[str, Any]] = None
    bail_out_threshold = float(bail_out_threshold)
    bail_out_max_dim = 4096
    if auto_bail_out and preconditioner is None:
        try:
            sample_rows = int(min(4096, A.shape[0]))
            indicator = float(estimate_spectral_spread_indicator(A, max_rows=sample_rows, power_iters=2))
            bail_out_info = {
                "indicator": indicator,
                "threshold": bail_out_threshold,
                "dimension": int(A.shape[1]),
                "max_dimension": bail_out_max_dim,
                "sample_rows": sample_rows,
                "triggered": False,
                "reason": "threshold_not_met",
            }
            if indicator <= bail_out_threshold and A.shape[1] <= bail_out_max_dim:
                bail_out_triggered = True
                bail_out_info["triggered"] = True
                bail_out_info["reason"] = "spectral_spread"
        except Exception as exc:
            bail_out_info = {
                "triggered": False,
                "threshold": bail_out_threshold,
                "dimension": int(A.shape[1]),
                "error": repr(exc),
            }

    # Build deterministic sketch and preconditioner if not provided
    if preconditioner is None and not bail_out_triggered:
        t0 = time.perf_counter()
        # Conservative GPU auto-chooser: only when requested or clearly available and beneficial (d>=1024)
        use_gpu = False
        if force_gpu_sketch:
            use_gpu = _RCFD_HAS_CUPY and _RCFD_NUM_GPU >= 1
        elif (_RCFD_HAS_CUPY and _RCFD_NUM_GPU >= 1 and A.shape[1] >= 1024):
            use_gpu = True
        if use_gpu:
            try:
                from .gpu import build_rcfd_sketch_gpu_rand  # type: ignore
                B = build_rcfd_sketch_gpu_rand(A, ridge_lambda=ridge_lambda, epsilon=epsilon, oversampling=oversampling, power_iters=power_iters)
                # Bring back to CPU numpy array
                try:
                    B = _cp.asnumpy(B)  # type: ignore[name-defined]
                except Exception:
                    pass
            except Exception:
                # Fallback to CPU sketch
                B = build_rcfd_sketch(
                    A,
                    ridge_lambda=ridge_lambda,
                    epsilon=epsilon,
                    batch_size=batch_size if batch_size is not None else 1024,
                    shrink_multiple=shrink_multiple,
                    compression=compression,
                    oversampling=oversampling,
                    power_iters=power_iters,
                    sketch_dtype=sketch_dtype,
                    random_state=random_state,
                    num_passes=num_passes,
                    parallel_blocks=parallel_blocks,
                    spill_dir=spill_dir,
                )
        else:
            B = build_rcfd_sketch(
                A,
                ridge_lambda=ridge_lambda,
                epsilon=epsilon,
                batch_size=batch_size if batch_size is not None else 1024,
                shrink_multiple=shrink_multiple,
                compression=compression,
                oversampling=oversampling,
                power_iters=power_iters,
                sketch_dtype=sketch_dtype,
                random_state=random_state,
                num_passes=num_passes,
                parallel_blocks=parallel_blocks,
                spill_dir=spill_dir,
            )
        t1 = time.perf_counter()
        # Use a slightly larger ridge for the preconditioner to ensure SPD
        if str(precond_type) == "blockdiag" and int(num_col_blocks) > 1:
            dcols = A.shape[1]
            k = max(1, int(num_col_blocks))
            splits = [int(i * dcols / k) for i in range(k)] + [dcols]
            chol_list: list[tuple[Tuple[np.ndarray, bool], slice]] = []
            for i in range(k):
                s, e = splits[i], splits[i + 1]
                if e <= s:
                    continue
                A_block = A[:, s:e]
                B_block = build_rcfd_sketch(
                    A_block,
                    ridge_lambda=ridge_lambda,
                    epsilon=epsilon,
                    batch_size=batch_size if batch_size is not None else 1024,
                    shrink_multiple=shrink_multiple,
                    compression=compression,
                    oversampling=oversampling,
                    power_iters=power_iters,
                    sketch_dtype=sketch_dtype,
                    random_state=random_state,
                    num_passes=num_passes,
                    parallel_blocks=parallel_blocks,
                    spill_dir=spill_dir,
                )
                _, chol_i = _gram_cholesky_from_sketch(B_block, ridge_lambda=max(ridge_lambda, precond_min_ridge))
                chol_list.append((chol_i, slice(s, e)))
            chol = chol_list  # type: ignore[assignment]
        else:
            _, chol = _gram_cholesky_from_sketch(B, ridge_lambda=max(ridge_lambda, precond_min_ridge))
        # Optional warm-up solves to prime caches/NUMA
        if int(precond_warmup_solves) > 0:
            try:
                k = int(precond_warmup_solves)
                for _ in range(k):
                    v = np.random.standard_normal(d)
                    _ = cho_solve(chol, v, check_finite=False)
            except Exception:
                pass
        t2 = time.perf_counter()
        sketch_rows = B.shape[0]
    else:
        if bail_out_triggered:
            chol = None
            sketch_rows = int(np.ceil(A.shape[1] / max(1e-9, epsilon)))
            t0 = t1 = t2 = None
        else:
            chol = preconditioner
            sketch_rows = int(np.ceil(A.shape[1] / max(1e-9, epsilon)))
            t0 = t1 = t2 = None  # not measured when provided

    def M_inv(vec: np.ndarray) -> np.ndarray:
        if bail_out_triggered or chol is None:
            return vec
        # Support tuple chol or block-diagonal list of (chol, slice)
        if isinstance(chol, tuple) and len(chol) == 2 and hasattr(chol[0], "shape"):
            return cho_solve(chol, vec, check_finite=False)  # type: ignore[arg-type]
        if isinstance(chol, list):
            out = np.zeros_like(vec)
            for (c_tuple, slc) in chol:  # type: ignore[assignment]
                out[slc] = cho_solve(c_tuple, vec[slc], check_finite=False)
            return out
        return vec

    # Normal equations: (A^T A + lambda I) x = A^T b
    # Convert b if torch tensor
    if torch is not None and hasattr(b, "detach") and hasattr(b, "cpu"):
        try:
            b = b.detach().cpu().numpy()
        except Exception:
            b = np.asarray(b)
    rhs = A.T @ b
    x = np.zeros(d, dtype=float)

    counter: Optional[_SpmvCounter] = _SpmvCounter(A) if count_spmv else None

    def normal_matvec(v: np.ndarray) -> np.ndarray:
        return _apply_normal_eq_matvec_parallel(A, v, ridge_lambda, threads=parallel_blocks, chunk_size=dense_chunk_size, counter=counter)

    t_pcg0 = time.perf_counter()
    r = rhs - normal_matvec(x)
    z = M_inv(r)
    p = z.copy()
    rz_old = float(r @ z)
    rhs_norm = float(np.linalg.norm(rhs))

    iters = 0
    residual_history = [] if record_history else None
    for k in range(max_iter):
        Ap = normal_matvec(p)
        denom = float(p @ Ap)
        if denom == 0.0:
            break
        alpha = rz_old / denom
        x = x + alpha * p
        r = r - alpha * Ap
        res_norm = float(np.linalg.norm(r))
        if record_history:
            residual_history.append(res_norm)
        if res_norm <= tol * (rhs_norm + 1e-30):
            iters = k + 1
            break
        z = M_inv(r)
        rz_new = float(r @ z)
        beta = rz_new / (rz_old + 1e-30)
        p = z + beta * p
        rz_old = rz_new
        iters = k + 1

    t_end = time.perf_counter()

    if return_diagnostics:
        diagnostics = {
            "iterations": iters,
            "residual_norm": float(np.linalg.norm(r)),
            "rhs_norm": rhs_norm,
            "sketch_rows": sketch_rows,
            "dimension": d,
        }
        if counter is not None:
            diagnostics.update({
                "num_spmv_Ax": int(counter.num_Ax),
                "num_spmv_ATx": int(counter.num_ATx),
            })
        # Timing diagnostics (seconds) with None guards (bail-out path sets t0/t1/t2=None)
        t_sketch = 0.0
        t_chol = 0.0
        if preconditioner is None and (t0 is not None) and (t1 is not None):
            t_sketch = (t1 - t0)
        if preconditioner is None and (t1 is not None) and (t2 is not None):
            t_chol = (t2 - t1)
        diagnostics.update({
            "time_total": (t_end - t_start),
            "time_sketch": t_sketch,
            "time_cholesky": t_chol,
            "time_pcg": (t_end - t_pcg0),
        })
        diagnostics["bail_out"] = bool(bail_out_triggered)
        if bail_out_info is not None:
            diagnostics["bail_out_details"] = bail_out_info
        if record_history and residual_history is not None:
            diagnostics["residual_history"] = residual_history
        if return_torch and torch is not None and (hasattr(A, "is_tensor") or hasattr(b, "is_tensor")):
            # Best-effort conversion back to torch on CPU; user can move to GPU if desired
            try:
                x_tensor = torch.from_numpy(x)
                return x_tensor, diagnostics
            except Exception:
                return x, diagnostics
        return x, diagnostics
    if return_torch and torch is not None and (hasattr(A, "is_tensor") or hasattr(b, "is_tensor")):
        try:
            x_tensor = torch.from_numpy(x)
            return x_tensor, None
        except Exception:
            return x, None
    return x, None


def build_rcfd_preconditioner(
    A: np.ndarray,
    ridge_lambda: float,
    epsilon: float = 0.25,
    batch_size: int = 1024,
    shrink_multiple: int = 2,
    compression: str = "auto",
    oversampling: int = 8,
    power_iters: int = 0,
    precond_min_ridge: float = 1e-7,
    sketch_dtype: str = "float32",
    num_passes: int = 1,
    parallel_blocks: int = 1,
    precond_warmup_solves: int = 0,
    spill_dir: Optional[str] = None,
) -> Tuple[Tuple[np.ndarray, bool], Dict[str, Any]]:
    """
    Build and return a Cholesky-based preconditioner (cho_factor) for reuse.
    Returns ((c, lower), meta) where meta includes lambda, epsilon, sketch_rows, d.
    """
    B = build_rcfd_sketch(
        A,
        ridge_lambda=ridge_lambda,
        epsilon=epsilon,
        batch_size=batch_size,
        shrink_multiple=shrink_multiple,
        compression=compression,
        oversampling=oversampling,
        power_iters=power_iters,
        sketch_dtype=sketch_dtype,
        num_passes=num_passes,
        parallel_blocks=parallel_blocks,
        spill_dir=spill_dir,
    )
    gram, chol = _gram_cholesky_from_sketch(B, ridge_lambda=max(ridge_lambda, precond_min_ridge))
    # Optional warm-up solves to prime caches/NUMA
    if int(precond_warmup_solves) > 0:
        try:
            k = int(precond_warmup_solves)
            d = B.shape[1]
            for _ in range(k):
                v = np.random.standard_normal(d)
                _ = cho_solve(chol, v, check_finite=False)
        except Exception:
            pass
    meta = {
        "ridge_lambda": float(ridge_lambda),
        "epsilon": float(epsilon),
        "sketch_rows": int(B.shape[0]),
        "dimension": int(B.shape[1]),
        "dtype": str(gram.dtype),
    }
    return chol, meta


def save_preconditioner(path: str, chol: Tuple[np.ndarray, bool], meta: Dict[str, Any]) -> None:
    import hashlib
    c, lower = chol
    # Compute checksum for integrity
    checksum = hashlib.sha256(c.tobytes()).hexdigest()
    enriched = dict(meta)
    enriched.setdefault("precond_version", 1)
    enriched.setdefault("checksum", checksum)
    np.savez(path, c=c, lower=np.array([int(lower)], dtype=np.int8), **enriched)


def load_preconditioner(path: str) -> Tuple[Tuple[np.ndarray, bool], Dict[str, Any]]:
    import hashlib
    data = np.load(path, allow_pickle=False)
    c = data["c"]
    lower = bool(int(data["lower"][0]))
    # Parse known numeric fields
    meta: Dict[str, Any] = {}
    for k in data.files:
        if k in ("c", "lower"):
            continue
        if k in ("ridge_lambda", "epsilon"):
            try:
                meta[k] = float(data[k])
                continue
            except Exception:
                pass
        if k in ("sketch_rows", "dimension", "precond_version"):
            try:
                meta[k] = int(data[k])
                continue
            except Exception:
                pass
        try:
            meta[k] = str(data[k])
        except Exception:
            # Fallback best-effort
            meta[k] = data[k]

    # Verify checksum if present
    try:
        stored = str(meta.get("checksum", ""))
        actual = hashlib.sha256(c.tobytes()).hexdigest()
        meta["checksum_ok"] = (stored == "" or stored == actual)
        meta["checksum_actual"] = actual
    except Exception:
        meta["checksum_ok"] = False
    return (c, lower), meta


@dataclass
class SyntheticProblem:
    """
    Helper to generate synthetic tall-skinny least-squares problems with a 
    controlled spectrum and optional noise.
    """

    num_rows: int
    num_cols: int
    spectrum_decay: str = "power"  # "power" or "exp"
    power_exponent: float = 1.0
    exp_rate: float = 0.01
    density: float = 0.05  # 5% density for sparse if using sparse
    noise_std: float = 0.0
    random_seed: int = 0
    make_sparse: bool = True

    def make(self) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
        rng = np.random.default_rng(self.random_seed)
        d = self.num_cols

        # Right singular vectors
        V, _ = np.linalg.qr(rng.standard_normal((d, d)))

        # Singular values
        if self.spectrum_decay == "power":
            s = np.array([(i + 1) ** (-self.power_exponent) for i in range(d)], dtype=float)
        elif self.spectrum_decay == "exp":
            s = np.exp(-self.exp_rate * np.arange(d))
        else:
            raise ValueError("spectrum_decay must be 'power' or 'exp'")

        # Construct A = U Sigma V^T approximately via random sparse U
        n = self.num_rows
        if self.make_sparse and sp is not None:
            # Random sparse U with given density
            U_data = rng.standard_normal(int(n * d * self.density))
            U_rows = rng.integers(0, n, size=U_data.size)
            U_cols = rng.integers(0, d, size=U_data.size)
            U = sp.coo_matrix((U_data, (U_rows, U_cols)), shape=(n, d)).tocsr()
            A = U @ (V * s)
        else:
            U = rng.standard_normal((n, d))
            A = U @ (V * s)

        x_true = rng.standard_normal(d)
        b = A @ x_true
        if self.noise_std > 0:
            if self.make_sparse and sp is not None and sp.issparse(A):
                noise = rng.standard_normal(A.shape[0]) * self.noise_std
            else:
                noise = rng.standard_normal(n) * self.noise_std
            b = b + noise

        return A, b, x_true


