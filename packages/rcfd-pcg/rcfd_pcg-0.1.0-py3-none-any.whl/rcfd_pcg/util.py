from __future__ import annotations

from contextlib import contextmanager
from typing import Iterator, Optional


def choose_epsilon_auto(d: int) -> float:
    """Heuristic epsilon chooser.

    Tuned toward smaller eps around moderate d based on recent ablations.
    """
    if d < 256:
        # Favor smaller epsilon for moderate d based on ablations
        return 0.15
    if d < 2048:
        return 0.25
    return 0.35

def choose_compression_params(d: int, density: float | None = None) -> tuple[str, int, int]:
    """Return (compression, oversampling, power_iters) based on dimension d and optional density.

    density: fraction of nonzeros in A (0..1). If None, only d is used.
    """
    if d < 256:
        # For small d, prefer randomized when matrix is sufficiently sparse; otherwise exact
        if density is not None and density <= 0.05:
            # Prefer a bit more oversampling around d≈200 sparse
            return ("rand", 12 if d >= 128 else 8, 1)
        return ("eigh", 6, 0)
    # Sparse matrices typically benefit from lower power iters
    if density is not None and density < 0.01:
        if d < 1024:
            return ("rand", 6, 0)
        return ("rand", 8, 0)
    if d < 1024:
        # Prefer a bit more oversampling around moderate d for stability
        return ("rand", 12 if 128 <= d <= 512 else 8, 1)
    return ("rand", 12, 1)

def choose_shrink_multiple(d: int) -> int:
    if d < 256:
        return 2
    if d < 1024:
        return 3
    return 4


def estimate_spectral_spread_indicator(A: object, max_rows: int = 2048, power_iters: int = 3) -> float:
    """Estimate an indicator of spectral spread of A^T A.

    Uses a small-row sample and a brief power iteration on A^T A to approximate
    the top eigenvalue, compared against the median diagonal entry (column variance).

    Returns a positive float; larger implies stronger spread/ill-conditioning.
    Best-effort and cheap; falls back to 1.0 on failure.
    """
    try:
        import numpy as _np  # local import to avoid forcing numpy at import time for some tools
        n, d = A.shape
        srows = min(int(max_rows), n)
        if srows < 8:
            return 1.0
        As = A[:srows, :]
        # Center columns for variance estimate
        col_means = _np.mean(As, axis=0)
        centered = As - col_means
        col_vars = _np.mean(centered * centered, axis=0) + 1e-30
        median_diag = float(_np.median(col_vars))
        # Power iteration on A^T A via repeated matvecs
        v = _np.random.standard_normal(d)
        v = v / (_np.linalg.norm(v) + 1e-30)
        for _ in range(max(1, int(power_iters))):
            w = As.T @ (As @ v)
            norm_w = _np.linalg.norm(w)
            if norm_w == 0.0:
                break
            v = w / norm_w
        # Rayleigh quotient approximation of top eigenvalue
        AtAv = As.T @ (As @ v)
        lambda_max = float(v @ AtAv)
        indicator = lambda_max / (median_diag + 1e-30)
        if not _np.isfinite(indicator) or indicator <= 0:
            return 1.0
        return indicator
    except Exception:
        return 1.0

def recommend_rcfd_params(d: int, density: float | None = None, sparse: bool = False) -> dict:
    """Recommend epsilon, compression method, oversampling, power, and threads given d and density.

    Returns a dict with keys: epsilon, compression, oversampling, power_iters, threads, sketch_dtype.
    """
    eps = choose_epsilon_auto(d)
    compression, overs, power = choose_compression_params(d, density)
    # Thread heuristic: sparse and moderate d benefits from 2 threads for randomized block matmuls
    threads = 2 if (sparse and 128 <= d <= 512) else 1
    return {
        "epsilon": eps,
        "compression": compression,
        "oversampling": overs,
        "power_iters": power,
        "threads": threads,
        "sketch_dtype": "float32",
    }


def set_cpu_affinity_prefer_cores(core_ids: list[int] | None) -> bool:
    """Attempt to pin the current process/threads to the given CPU cores.

    Returns True on best-effort success, False otherwise. No-ops if unsupported.
    """
    try:
        import os
        if core_ids and hasattr(os, "sched_setaffinity"):
            os.sched_setaffinity(0, set(int(c) for c in core_ids))
            return True
        # Windows fallback via psutil if available
        if core_ids:
            try:
                import psutil  # type: ignore
                p = psutil.Process()
                p.cpu_affinity([int(c) for c in core_ids])
                return True
            except Exception:
                return False
    except Exception:
        return False
    return False


@contextmanager
def limit_blas_threads(desired_threads: Optional[int]) -> Iterator[bool]:
    """Best-effort context manager to set BLAS threadpool limits during the block.

    Uses threadpoolctl when available. Returns an iterator that yields True if
    limits were applied, otherwise False. If desired_threads is None, yields False.
    """
    if desired_threads is None:
        yield False
        return
    try:  # pragma: no cover - optional dependency
        from threadpoolctl import threadpool_limits  # type: ignore

        with threadpool_limits(limits=int(desired_threads)):
            yield True
        return
    except Exception:
        # Fallback: do nothing; users can pin via environment per docs
        yield False


