from __future__ import annotations

import argparse
import json
import time
from typing import Dict, Any

import numpy as np

from .rcfd import rcfd_pcg_solve, SyntheticProblem, build_rcfd_preconditioner
from .env import collect_environment

try:
    from scipy.sparse.linalg import lsqr as scipy_lsqr
    from scipy.sparse.linalg import lsmr as scipy_lsmr
    from scipy.sparse.linalg import LinearOperator as ScipyLinearOperator
    from scipy.sparse.linalg import cg as scipy_cg
    from scipy.linalg import cho_factor, cho_solve, lstsq
except Exception:  # pragma: no cover
    scipy_lsqr = None
    scipy_lsmr = None
    ScipyLinearOperator = None
    scipy_cg = None
    cho_factor = None  # type: ignore
    cho_solve = None  # type: ignore
    lstsq = None  # type: ignore


def _parse_args(argv):
    p = argparse.ArgumentParser(description="Benchmark RCFD-PCG vs LSQR on synthetic problems")
    p.add_argument("--n", type=int, default=20000)
    p.add_argument("--d", type=int, default=200)
    p.add_argument("--lam", type=float, default=0.0)
    p.add_argument("--eps", type=float, default=0.25)
    p.add_argument("--tol", type=float, default=1e-6)
    p.add_argument("--repeats", type=int, default=3)
    p.add_argument("--sparse", action="store_true")
    p.add_argument("--density", type=float, default=0.05, help="Density in (0,1] for sparse synthetic A")
    p.add_argument("--noise", type=float, default=0.0)
    p.add_argument("--seed", type=int, default=0)
    p.add_argument("--json", action="store_true")
    p.add_argument("--out-json", type=str, default="", help="Optional path to save JSON output")
    p.add_argument("--sketch-dtype", choices=["float32","float64"], default="float32", help="Sketch dtype for RCFD runs")
    p.add_argument("--num-passes", type=int, default=1, help="Number of passes for RCFD sketch (1 or 2)")
    p.add_argument("--threads", type=int, default=1, help="Parallel blocks for randomized compression (>=1)")
    p.add_argument("--threads-compare", type=str, default="", help="Comma list of thread counts to compare for RCFD (e.g., '1,2')")
    p.add_argument("--reuse-precond", action="store_true", help="Build preconditioner once and reuse across repeats")
    p.add_argument("--ascii", action="store_true", help="Force ASCII-only symbols in human-readable output")
    p.add_argument("--ascii-default", action="store_true", help="Force ASCII-only symbols when console is not UTF-8 (Windows-friendly)")
    p.add_argument("--spectrum", type=str, choices=["power","exp"], default="power", help="Synthetic spectrum shape: power or exp")
    p.add_argument("--power-exp", type=float, default=1.0, help="Power-law exponent for singular values when --spectrum=power")
    p.add_argument("--exp-rate", type=float, default=0.01, help="Exponential rate for singular values when --spectrum=exp")
    p.add_argument("--dense-baselines", type=str, choices=["auto","on","off"], default="auto", help="Control printing dense baselines regardless of sparsity")
    p.add_argument("--precond-type", type=str, choices=["chol","blockdiag"], default="chol", help="Preconditioner type: Cholesky or block-diagonal by column partitions")
    p.add_argument("--num-col-blocks", type=int, default=1, help="Column blocks for block-diagonal preconditioner (>=1)")
    return p.parse_args(argv)


def _run_rcfd(A, b, lam, eps, tol, repeats, reuse_precond: bool = False, sketch_dtype: str = "float32", num_passes: int = 1, threads: int = 1, precond_type: str = "chol", num_col_blocks: int = 1) -> Dict[str, Any]:
    times = []
    iters: list[float | None] = []
    bail_flags: list[bool] = []
    bail_details: list[Dict[str, Any]] = []
    chol = None
    if repeats > 1 and hasattr(A, "shape") and reuse_precond:
        # Build once
        chol, _ = build_rcfd_preconditioner(A, lam, eps, sketch_dtype=sketch_dtype, num_passes=num_passes, parallel_blocks=threads)

    for _ in range(repeats):
        t0 = time.perf_counter()
        _, diag = rcfd_pcg_solve(
            A,
            b,
            ridge_lambda=lam,
            epsilon=eps,
            tol=tol,
            count_spmv=True,
            sketch_dtype=sketch_dtype,
            preconditioner=chol,
            num_passes=num_passes,
            parallel_blocks=threads,
            precond_type=precond_type,
            num_col_blocks=num_col_blocks,
            return_diagnostics=True,
        )
        t1 = time.perf_counter()
        times.append(t1 - t0)
        iters.append(diag["iterations"] if diag else None)
        bail_flag = bool(diag.get("bail_out")) if diag else False
        bail_flags.append(bail_flag)
        if bail_flag:
            info = diag.get("bail_out_details") if diag else None
            if isinstance(info, dict):
                bail_details.append(info)

    result: Dict[str, Any] = {
        "time_mean": float(np.mean(times)),
        "time_std": float(np.std(times)),
        "time_p95": float(np.percentile(times, 95)) if times else None,
        "time_p99": float(np.percentile(times, 99)) if times else None,
        "iterations_mean": float(np.mean([i for i in iters if i is not None])) if any(i is not None for i in iters) else None,
    }
    if bail_flags:
        triggered = sum(1 for flag in bail_flags if flag)
        result["bail_out"] = bool(triggered)
        result["bail_out_rate"] = float(triggered / len(bail_flags))
    else:
        result["bail_out"] = False
        result["bail_out_rate"] = 0.0
    if bail_details:
        result["bail_out_details"] = bail_details
    return result


def _run_lsqr(A, b, lam, tol, repeats) -> Dict[str, Any]:
    if scipy_lsqr is None or ScipyLinearOperator is None:
        return {"error": "scipy not available"}
    times = []
    iters = []
    ax_counts = []
    atx_counts = []

    n, d = A.shape

    for _ in range(repeats):
        num_Ax = 0
        num_ATx = 0

        def mv(v):
            nonlocal num_Ax
            num_Ax += 1
            return A @ v

        def rmv(v):
            nonlocal num_ATx
            num_ATx += 1
            return A.T @ v

        Lop = ScipyLinearOperator(shape=(n, d), matvec=mv, rmatvec=rmv, dtype=float)
        t0 = time.perf_counter()
        result = scipy_lsqr(Lop, b, damp=np.sqrt(lam), atol=tol, btol=tol, iter_lim=100000)
        t1 = time.perf_counter()
        times.append(t1 - t0)
        iters.append(int(result[2]))
        ax_counts.append(num_Ax)
        atx_counts.append(num_ATx)

    return {
        "time_mean": float(np.mean(times)),
        "time_std": float(np.std(times)),
        "time_p95": float(np.percentile(times, 95)) if len(times) > 0 else None,
        "time_p99": float(np.percentile(times, 99)) if len(times) > 0 else None,
        "iterations_mean": float(np.mean(iters)),
        "num_spmv_Ax_mean": float(np.mean(ax_counts)),
        "num_spmv_ATx_mean": float(np.mean(atx_counts)),
    }


def _run_lsmr(A, b, lam, tol, repeats) -> Dict[str, Any]:
    if scipy_lsmr is None or ScipyLinearOperator is None:
        return {"error": "scipy not available"}
    times = []
    iters = []
    ax_counts = []
    atx_counts = []

    n, d = A.shape
    for _ in range(repeats):
        num_Ax = 0
        num_ATx = 0

        def mv(v):
            nonlocal num_Ax
            num_Ax += 1
            return A @ v

        def rmv(v):
            nonlocal num_ATx
            num_ATx += 1
            return A.T @ v

        Lop = ScipyLinearOperator(shape=(n, d), matvec=mv, rmatvec=rmv, dtype=float)
        t0 = time.perf_counter()
        result = scipy_lsmr(Lop, b, damp=np.sqrt(lam), atol=tol, btol=tol, maxiter=100000)
        t1 = time.perf_counter()
        times.append(t1 - t0)
        # lsmr returns (x, istop, itn, ...); itn is iterations
        itn = int(result[2])
        iters.append(itn)
        ax_counts.append(num_Ax)
        atx_counts.append(num_ATx)

    return {
        "time_mean": float(np.mean(times)),
        "time_std": float(np.std(times)),
        "time_p95": float(np.percentile(times, 95)) if len(times) > 0 else None,
        "time_p99": float(np.percentile(times, 99)) if len(times) > 0 else None,
        "iterations_mean": float(np.mean(iters)),
        "num_spmv_Ax_mean": float(np.mean(ax_counts)),
        "num_spmv_ATx_mean": float(np.mean(atx_counts)),
    }


def _run_cgne(A, b, lam, tol, repeats) -> Dict[str, Any]:
    """CG on normal equations (unpreconditioned CGNE/CGNR)."""
    if scipy_cg is None or ScipyLinearOperator is None:
        return {"error": "scipy not available"}
    times = []
    iters = []
    ax_counts = []
    atx_counts = []
    n, d = A.shape

    for _ in range(repeats):
        num_Ax = 0
        num_ATx = 0

        def mv(v):
            nonlocal num_Ax, num_ATx
            # (A^T A + lam I) v
            Av = A @ v
            num_Ax += 1
            AtAv = A.T @ Av
            num_ATx += 1
            return AtAv + lam * v

        Lop = ScipyLinearOperator(shape=(d, d), matvec=mv, rmatvec=mv, dtype=float)
        rhs = A.T @ b
        t0 = time.perf_counter()
        # Be robust to SciPy API changes across versions
        try:
            x, info = scipy_cg(Lop, rhs, rtol=tol, atol=0, maxiter=100000)
        except TypeError:
            try:
                x, info = scipy_cg(Lop, rhs, tol=tol, atol=0, maxiter=100000)
            except TypeError:
                x, info = scipy_cg(Lop, rhs, tol=tol, maxiter=100000)
        t1 = time.perf_counter()
        times.append(t1 - t0)
        # cg does not return iters; approximate from counts: each iter calls mv once
        iters.append(num_Ax)  # approximate
        ax_counts.append(num_Ax)
        atx_counts.append(num_ATx)

    return {
        "time_mean": float(np.mean(times)),
        "time_std": float(np.std(times)),
        "time_p95": float(np.percentile(times, 95)) if len(times) > 0 else None,
        "time_p99": float(np.percentile(times, 99)) if len(times) > 0 else None,
        "iterations_mean": float(np.mean(iters)),
        "num_spmv_Ax_mean": float(np.mean(ax_counts)),
        "num_spmv_ATx_mean": float(np.mean(atx_counts)),
    }


def _run_dense_cholesky(A, b, lam, repeats) -> Dict[str, Any]:
    """Direct normal-equations solve via Cholesky (dense baseline)."""
    times = []
    sols = []
    n, d = A.shape
    for _ in range(repeats):
        t0 = time.perf_counter()
        gram = A.T @ A
        if lam and lam != 0.0:
            gram = gram + float(lam) * np.eye(d)
        c, lower = cho_factor(gram, lower=False, check_finite=False)
        rhs = A.T @ b
        x = cho_solve((c, lower), rhs, check_finite=False)
        t1 = time.perf_counter()
        times.append(t1 - t0)
        sols.append(x)
    return {
        "time_mean": float(np.mean(times)),
        "time_std": float(np.std(times)),
    }


def _run_dense_qr(A, b, lam, repeats) -> Dict[str, Any]:
    """QR-based least squares baseline; ridge via augmentation when lam>0."""
    times = []
    n, d = A.shape
    for _ in range(repeats):
        t0 = time.perf_counter()
        if lam and lam != 0.0:
            # Augmented least squares: [A; sqrt(lam) I] x ≈ [b; 0]
            A_aug = np.vstack([A, np.sqrt(float(lam)) * np.eye(d)])
            b_aug = np.concatenate([b, np.zeros(d, dtype=b.dtype)])
            x, *_ = lstsq(A_aug, b_aug, lapack_driver="gelsd")
        else:
            x, *_ = lstsq(A, b, lapack_driver="gelsd")
        t1 = time.perf_counter()
        times.append(t1 - t0)
    return {
        "time_mean": float(np.mean(times)),
        "time_std": float(np.std(times)),
    }


def main(argv=None) -> int:
    import sys

    args = _parse_args(argv if argv is not None else sys.argv[1:])
    problem = SyntheticProblem(
        num_rows=args.n,
        num_cols=args.d,
        noise_std=args.noise,
        random_seed=args.seed,
        make_sparse=args.sparse,
        density=args.density,
        spectrum_decay=str(args.spectrum),
        power_exponent=float(args.power_exp),
        exp_rate=float(args.exp_rate),
    )
    A, b, x_true = problem.make()

    rcfd = _run_rcfd(A, b, lam=args.lam, eps=args.eps, tol=args.tol, repeats=args.repeats, reuse_precond=args.reuse_precond, sketch_dtype=args.sketch_dtype, num_passes=args.num_passes, threads=args.threads, precond_type=args.precond_type, num_col_blocks=args.num_col_blocks)

    # Optional threads comparison for dense path evaluation
    threads_compare = [int(x) for x in str(args.threads_compare).split(',') if x.strip().isdigit() and int(x) >= 1]
    rcfd_threads = None
    if threads_compare:
        rcfd_threads = {}
        for nthr in threads_compare:
            rcfd_threads[str(nthr)] = _run_rcfd(A, b, lam=args.lam, eps=args.eps, tol=args.tol, repeats=args.repeats, reuse_precond=args.reuse_precond, sketch_dtype=args.sketch_dtype, num_passes=args.num_passes, threads=nthr, precond_type=args.precond_type, num_col_blocks=args.num_col_blocks)
    lsqr = _run_lsqr(A, b, lam=args.lam, tol=args.tol, repeats=args.repeats)
    lsmr = _run_lsmr(A, b, lam=args.lam, tol=args.tol, repeats=args.repeats)
    cgne = _run_cgne(A, b, lam=args.lam, tol=args.tol, repeats=args.repeats)

    dense_qr = None
    dense_chol = None
    # Decide whether to run dense baselines
    want_dense = False
    if str(args.dense_baselines) == "on":
        want_dense = True
    elif str(args.dense_baselines) == "auto":
        want_dense = not args.sparse
    # Provide direct dense baselines when desired and SciPy linalg available
    if want_dense and lstsq is not None and cho_factor is not None:
        try:
            dense_qr = _run_dense_qr(A, b, lam=args.lam, repeats=args.repeats)
            dense_chol = _run_dense_cholesky(A, b, lam=args.lam, repeats=args.repeats)
        except Exception:
            dense_qr = {"error": "dense QR failed"}
            dense_chol = {"error": "dense Cholesky failed"}

    out = {
        "n": args.n,
        "d": args.d,
        "lambda": args.lam,
        "epsilon": args.eps,
        "tol": args.tol,
        "sparse": args.sparse,
        "density": args.density if args.sparse else None,
        "repeats": args.repeats,
        "rcfd": rcfd,
        "sketch_dtype": args.sketch_dtype,
        "num_passes": args.num_passes,
        "threads": args.threads,
        "lsqr": lsqr,
        "lsmr": lsmr,
        "cgne": cgne,
        "env": collect_environment(),
    }
    if dense_qr is not None:
        out["dense_qr"] = dense_qr
    if dense_chol is not None:
        out["dense_cholesky"] = dense_chol
    if rcfd_threads is not None:
        out["rcfd_threads"] = rcfd_threads
    if args.json:
        js = json.dumps(out)
        print(js)
        if args.out_json:
            try:
                with open(args.out_json, "w", encoding="utf-8") as f:
                    f.write(js)
            except Exception:
                pass
    else:
        plus_minus = "+/-"
        approx = "~"
        if not args.ascii:
            try:
                # If console supports UTF-8, prefer nicer symbols
                import sys
                enc = (sys.stdout.encoding or "").lower() if hasattr(sys.stdout, "encoding") else ""
                if enc.startswith("utf"):
                    plus_minus = "±"
                    approx = "≈"
            except Exception:
                pass
        # ASCII-default for non-UTF consoles
        try:
            if getattr(args, "ascii_default", False):
                import sys as _sys
                enc2 = (_sys.stdout.encoding or "").lower() if hasattr(_sys.stdout, "encoding") else ""
                if not enc2.startswith("utf"):
                    plus_minus = "+/-"
                    approx = "~"
        except Exception:
            pass
        print(f"RCFD: time={rcfd['time_mean']:.3f}{plus_minus}{rcfd['time_std']:.3f}s, iters{approx}{rcfd['iterations_mean']}")
        if "error" in lsqr:
            print("LSQR: unavailable (scipy not installed)")
        else:
            print(
                f"LSQR: time={lsqr['time_mean']:.3f}{plus_minus}{lsqr['time_std']:.3f}s, iters{approx}{lsqr['iterations_mean']} "
                f"SpMVs{approx}Ax:{lsqr['num_spmv_Ax_mean']:.0f} ATx:{lsqr['num_spmv_ATx_mean']:.0f}"
            )
        if "error" in lsmr:
            print("LSMR: unavailable (scipy not installed)")
        else:
            print(
                f"LSMR: time={lsmr['time_mean']:.3f}{plus_minus}{lsmr['time_std']:.3f}s, iters{approx}{lsmr['iterations_mean']} "
                f"SpMVs{approx}Ax:{lsmr['num_spmv_Ax_mean']:.0f} ATx:{lsmr['num_spmv_ATx_mean']:.0f}"
            )
        if "error" in cgne:
            print("CGNE: unavailable (scipy not installed)")
        else:
            print(
                f"CGNE: time={cgne['time_mean']:.3f}{plus_minus}{cgne['time_std']:.3f}s, iters{approx}{cgne['iterations_mean']} "
                f"SpMVs{approx}Ax:{cgne['num_spmv_Ax_mean']:.0f} ATx:{cgne['num_spmv_ATx_mean']:.0f}"
            )
        # Dense baselines (only printed when available and non-sparse)
        if dense_qr is not None and "error" not in dense_qr:
            print(f"Dense-QR: time={dense_qr['time_mean']:.3f}{plus_minus}{dense_qr['time_std']:.3f}s")
        if dense_chol is not None and "error" not in dense_chol:
            print(f"Dense-Cholesky: time={dense_chol['time_mean']:.3f}{plus_minus}{dense_chol['time_std']:.3f}s")
    return 0


if __name__ == "__main__":
    import sys

    raise SystemExit(main())



