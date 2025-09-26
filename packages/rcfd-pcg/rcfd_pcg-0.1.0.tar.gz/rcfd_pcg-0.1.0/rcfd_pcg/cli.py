from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

import numpy as np

from .rcfd import (
    rcfd_pcg_solve,
    SyntheticProblem,
    build_rcfd_preconditioner,
    save_preconditioner,
    load_preconditioner,
)
from .util import choose_epsilon_auto, recommend_rcfd_params
from . import datasets as real_datasets


def _load_matrix_any(path: str):
    import numpy as _np
    p = str(path)
    if p.startswith("mm:"):
        p2 = p[3:]
        try:
            from scipy.io import mmread  # type: ignore
        except Exception as e:
            raise RuntimeError("SciPy required for Matrix Market input: pip install scipy") from e
        return mmread(p2).tocsr()
    if p.startswith("npz:"):
        import scipy.sparse as _sp
        loader = _np.load(p[4:])
        return _sp.csr_matrix((loader["data"], loader["indices"], loader["indptr"]), shape=loader["shape"])  # type: ignore
    # fallback: assume .npy dense
    return _np.load(p)


def _write_json_report(out_path: str, shape: tuple[int, int], diag: dict) -> None:
    import json as _json
    payload = {"shape": [int(shape[0]), int(shape[1])], "diagnostics": diag}
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(_json.dumps(payload, indent=2))


def _emit_html_from_json(json_path: str, html_path: str) -> None:
    import json as _json
    try:
        with open(json_path, "r", encoding="utf-8") as f:
            data = _json.load(f)
    except Exception:
        return
    # Try to render a small summary table when benchmark keys present
    def _table_rows(d: dict) -> str:
        rows = []
        for name in ("rcfd","lsqr","lsmr","cgne"):
            if name in d and isinstance(d[name], dict):
                m = d[name]
                tm = m.get("time_mean", "")
                if isinstance(tm, (int, float)):
                    time_mean_str = f"{tm:.3f}"
                else:
                    time_mean_str = str(tm) if tm is not None else ""
                rows.append(
                    f"<tr><td>{name.upper()}</td><td>{m.get('iterations_mean','')}</td><td>{time_mean_str}</td><td>{m.get('time_p95','')}</td><td>{m.get('time_p99','')}</td></tr>"
                )
        return "\n".join(rows)

    summary = ""
    if isinstance(data, dict) and all(k in data for k in ("rcfd","lsqr")):
        summary = (
            "<h3>Summary</h3>"
            "<table border='1' cellspacing='0' cellpadding='4'>"
            "<tr><th>Method</th><th>Iters(mean)</th><th>Time(mean s)</th><th>p95</th><th>p99</th></tr>"
            f"{_table_rows(data)}" "</table>"
        )

    html = [
        "<html><head><meta charset='utf-8'><title>RCFD-PCG Report</title><style>body{font-family:system-ui,Segoe UI,Arial,sans-serif} table{border-collapse:collapse} th,td{padding:6px}</style></head><body>",
        "<h2>RCFD-PCG Report</h2>",
        summary,
        "<h3>Raw JSON</h3>",
        f"<pre>{_json.dumps(data, indent=2)}</pre>",
        "</body></html>",
    ]
    with open(html_path, "w", encoding="utf-8") as f:
        f.write("\n".join(html))

def _notify_bail_out(diag: Optional[dict], *, json_mode: bool = False) -> None:
    """Print a user-facing notice when auto bail-out skips the preconditioner.

    Uses stderr when JSON output is requested to keep stdout machine-readable.
    """
    if not diag or not diag.get("bail_out"):
        return
    info = diag.get("bail_out_details") or {}
    indicator = info.get("indicator")
    threshold = info.get("threshold")
    reason = info.get("reason", "spectral_spread")
    parts = ["Auto bail-out engaged: skipped sketch/preconditioner"]
    if isinstance(indicator, (int, float)) and isinstance(threshold, (int, float)):
        parts.append(f"(indicator={indicator:.2f} <= threshold={threshold:.2f})")
    if reason:
        parts.append(f"[{reason}]")
    parts.append("Use --no-bail-out to disable or --bail-out-threshold to tune.")
    msg = " ".join(parts)
    target = sys.stderr if json_mode else sys.stdout
    try:
        print(msg, file=target)
    except Exception:
        # Fallback to stdout if stderr is unavailable (e.g., redirected handles)
        print(msg)

def _parse_args(argv: list[str]) -> argparse.Namespace:
    p = argparse.ArgumentParser(description="RCFD-PCG solver CLI")
    sub = p.add_subparsers(dest="cmd")

    # demo command
    demo = sub.add_parser("demo", help="Run a small demo and emit report artifacts")
    demo.add_argument("--out", type=str, default="demo_report.json", help="Path to write JSON report")
    demo.add_argument("--html", type=str, default="demo_report.html", help="Path to write HTML report")

    # run command (Matrix Market / NumPy input)
    run = sub.add_parser("run", help="Run solver on provided files and emit report")
    run.add_argument("--A", required=True, help="Matrix path. Prefix with mm: for Matrix Market (.mtx/.mtx.gz), npz: for CSR npz, or raw NumPy .npy")
    run.add_argument("--b", required=True, help="Vector path (.npy)")
    run.add_argument("--out", type=str, default="report.json")
    run.add_argument("--html", type=str, default="report.html")

    # doctor command
    doctor = sub.add_parser("doctor", help="Print environment and recommendations")
    doctor.add_argument("--json", action="store_true")
    p.add_argument("--n", type=int, default=200000, help="Number of rows")
    p.add_argument("--d", type=int, default=500, help="Number of columns")
    p.add_argument("--lam", type=float, default=0.0, help="Ridge lambda >= 0")
    p.add_argument("--eps", type=str, default="auto", help="Sketch epsilon in (0,1) or 'auto'")
    p.add_argument("--tol", type=float, default=1e-6, help="Solver tolerance")
    p.add_argument("--maxit", type=int, default=200, help="Max PCG iterations")
    p.add_argument("--batch", type=int, default=1024, help="Batch size for sketch streaming")
    p.add_argument("--shrink-mult", type=int, default=2, help="Shrink buffer multiple (>=1)")
    p.add_argument("--count-spmv", action="store_true", help="Report SpMV counts")
    p.add_argument("--compression", choices=["auto","eigh","eigh_inc","rand"], default="auto", help="Compression method for buffer")
    p.add_argument("--oversampling", type=int, default=8, help="Oversampling for randomized compression")
    p.add_argument("--power-iters", type=int, default=0, help="Power iterations for randomized compression")
    p.add_argument("--sparse", action="store_true", help="Use sparse synthetic A")
    p.add_argument("--density", type=float, default=0.05, help="Density in (0,1] for sparse synthetic A (recommendation helper & synthetic generator)")
    p.add_argument("--noise", type=float, default=0.0, help="Noise std in b")
    p.add_argument("--seed", type=int, default=0, help="Random seed")
    p.add_argument("--json", action="store_true", help="Output JSON diagnostics")
    p.add_argument("--json-out", type=str, default="", help="Optional path to write diagnostics JSON when using --json")
    p.add_argument("--log-json", type=str, default="", help="Optional path to save JSON diagnostics")
    p.add_argument("--sketch-dtype", choices=["float32","float64"], default="float32", help="Sketch matrix dtype")
    p.add_argument("--num-passes", type=int, default=1, help="Number of passes over A for sketching (1 or 2)")
    p.add_argument("--threads", type=int, default=1, help="Parallel blocks for randomized compression (>=1)")
    p.add_argument("--precond-min-ridge", type=float, default=1e-7, help="Minimum ridge used to ensure SPD in preconditioner build")
    p.add_argument("--precond-warmup-solves", type=int, default=0, help="Number of dummy solves with the preconditioner to warm caches/NUMA")
    p.add_argument("--spill-dir", type=str, default="", help="Optional directory to spill the sketch buffer to disk (memmap) to reduce RAM spikes")
    p.add_argument("--dense-chunk-size", type=int, default=0, help="Override row chunk size for dense matvec parallel path (0=auto)")
    p.add_argument("--precond-type", choices=["chol","blockdiag"], default="chol", help="Preconditioner type: single Cholesky or block-diagonal by column partitions")
    p.add_argument("--num-col-blocks", type=int, default=1, help="Number of column blocks for block-diagonal preconditioner (>=1)")
    p.add_argument("--no-bail-out", action="store_true", help="Disable auto bail-out when problem appears well-conditioned")
    p.add_argument("--bail-out-threshold", type=float, default=5.0, help="Indicator threshold for auto bail-out (lower values trigger preconditioner skip)")
    p.add_argument("--record-history", action="store_true", help="Record residual history in diagnostics")
    p.add_argument("--ascii", action="store_true", help="Force ASCII-only human-readable output")
    p.add_argument("--ascii-default", action="store_true", help="Force ASCII-only symbols when console is not UTF-8 (Windows-friendly)")
    p.add_argument("--save-precond", type=str, default="", help="Path to save built preconditioner (npz)")
    p.add_argument("--load-precond", type=str, default="", help="Path to load preconditioner (npz)")
    p.add_argument("--check-precond", type=str, default="", help="Path to a preconditioner (npz) to inspect and verify, then exit")
    p.add_argument("--recommend", action="store_true", help="Print recommended params for given d/sparsity and exit")
    p.add_argument("--real-dataset", choices=["20ng","rcv1","yearmsd","cahousing","none"], default="none", help="Optional real dataset to load and solve")
    p.add_argument("--n-features", type=int, default=1024, help="Target feature dimension for text hashing (real datasets)")
    p.add_argument("--sample", type=int, default=0, help="Optional sample size for YearPredictionMSD (real datasets)")
    return p.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    if argv is None:
        argv = sys.argv[1:]
    args = _parse_args(argv)
    # Subcommands
    if getattr(args, "cmd", None) == "doctor":
        from .env import collect_environment
        env = collect_environment()
        if args.json:
            import json as _json
            print(_json.dumps({"env": env}))
        else:
            print(env)
        return 0
    if getattr(args, "cmd", None) == "demo":
        # Small synthetic sparse demo and a dense demo
        from .bench import main as bench_main
        out_js = args.out
        code = bench_main(["--n","20000","--d","200","--sparse","--eps","0.25","--tol","1e-6","--repeats","1","--json","--out-json", out_js])
        if code != 0:
            return code
        try:
            _emit_html_from_json(out_js, args.html)
        except Exception:
            pass
        print(f"Demo report: {out_js} ; HTML: {args.html}")
        return 0
    if getattr(args, "cmd", None) == "run":
        try:
            A = _load_matrix_any(args.A)
            import numpy as _np
            b = _np.load(args.b)
        except Exception as e:
            print(f"Failed to load inputs: {e}")
            return 1
        # Run a single solve and emit minimal report
        x, diag = rcfd_pcg_solve(
            A,
            b,
            ridge_lambda=0.0,
            epsilon=0.25,
            tol=1e-6,
            return_diagnostics=True,
            auto_bail_out=(not args.no_bail_out),
            bail_out_threshold=args.bail_out_threshold,
        )
        _write_json_report(args.out, A.shape, diag or {})
        if args.json_out:
            _write_json_report(args.json_out, A.shape, diag or {})
        try:
            _emit_html_from_json(args.out, args.html)
        except Exception:
            pass
        _notify_bail_out(diag, json_mode=False)
        print(f"Report: {args.out} ; HTML: {args.html}")
        return 0
    # Recommendation-only path
    if args.recommend:
        rec = recommend_rcfd_params(args.d, density=(args.density if args.sparse else None), sparse=args.sparse)
        out = {
            "d": args.d,
            "sparse": bool(args.sparse),
            "density": float(args.density) if args.sparse else None,
            **rec,
        }
        import json as _json
        print(_json.dumps(out)) if args.json else print(out)
        return 0

    # Preconditioner inspection-only path
    if args.check_precond:
        try:
            chol, meta = load_preconditioner(args.check_precond)
            out = {
                "path": args.check_precond,
                "meta": meta,
                "lower": bool(chol[1]),
                "shape": list(chol[0].shape) if hasattr(chol[0], "shape") else None,
            }
            import json as _json
            print(_json.dumps(out)) if args.json else print(out)
            return 0
        except Exception as e:
            print(f"Failed to load preconditioner '{args.check_precond}': {e}")
            return 1

    # Heuristic: set threads=2 by default for sparse tall-skinny with moderate d if user did not override
    auto_threads = False
    if args.threads == 1 and args.sparse and 128 <= args.d <= 512:
        args.threads = 2
        auto_threads = True

    # If user requested auto epsilon, also adopt other recommended params when compression is auto
    # This preserves explicit flags if user supplied them.
    if isinstance(args.eps, str) and args.eps.lower() == "auto":
        rec = recommend_rcfd_params(args.d, density=None if not args.sparse else 0.05, sparse=args.sparse)
        # Honor user-provided compression/oversampling/power unless left at defaults
        if args.compression == "auto":
            args.compression = rec["compression"]
            if args.oversampling == 8:
                args.oversampling = rec["oversampling"]
            if args.power_iters == 0:
                args.power_iters = rec["power_iters"]

    if args.real_dataset != "none":
        if args.real_dataset == "20ng":
            A, y = real_datasets.load_20newsgroups_hashed(n_features=args.n_features, subset="train")
        elif args.real_dataset == "rcv1":
            A, y = real_datasets.load_rcv1_hashed(n_features=args.n_features)
        elif args.real_dataset == "yearmsd":
            A, y = real_datasets.load_yearprediction_msd(sample=(args.sample if args.sample > 0 else None))
        elif args.real_dataset == "cahousing":
            A, y = real_datasets.load_california_housing()
        else:
            raise ValueError("unknown real dataset")
        b = y.reshape(-1)
        x_true = None
        # Override n/d from real data
        args.n = int(A.shape[0])
        args.d = int(A.shape[1])
        # For obvious dense datasets, unset sparse flag
        try:
            import scipy.sparse as _sp  # type: ignore
            args.sparse = bool(_sp.issparse(A))
        except Exception:
            args.sparse = False
    else:
        problem = SyntheticProblem(
            num_rows=args.n,
            num_cols=args.d,
            noise_std=args.noise,
            random_seed=args.seed,
            make_sparse=args.sparse,
            density=args.density,
        )
        A, b, x_true = problem.make()

    # Resolve epsilon value early for both preconditioner build and solver
    eps_value = args.eps
    if isinstance(eps_value, str) and eps_value.lower() == "auto":
        eps_value = choose_epsilon_auto(args.d)

    # Optional: load or build/save preconditioner
    precond = None
    precond_action = None
    precond_path = None
    if args.load_precond:
        precond, _meta = load_preconditioner(args.load_precond)
        precond_action = "loaded"
        precond_path = args.load_precond
    elif args.save_precond:
        precond, meta = build_rcfd_preconditioner(
            A,
            ridge_lambda=args.lam,
            epsilon=float(eps_value),
            batch_size=args.batch,
            shrink_multiple=args.shrink_mult,
            compression=args.compression,
            oversampling=args.oversampling,
            power_iters=args.power_iters,
            sketch_dtype=args.sketch_dtype,
            num_passes=args.num_passes,
            parallel_blocks=args.threads,
        precond_min_ridge=args.precond_min_ridge,
            precond_warmup_solves=args.precond_warmup_solves,
            spill_dir=(args.spill_dir or None),
        )
        save_preconditioner(args.save_precond, precond, meta)
        precond_action = "saved"
        precond_path = args.save_precond

    x, diag = rcfd_pcg_solve(
        A,
        b,
        ridge_lambda=args.lam,
        epsilon=float(eps_value),
        tol=args.tol,
        max_iter=args.maxit,
        batch_size=args.batch,
        shrink_multiple=args.shrink_mult,
        count_spmv=args.count_spmv,
        compression=args.compression,
        oversampling=args.oversampling,
        power_iters=args.power_iters,
        preconditioner=precond,
        record_history=args.record_history,
        random_state=args.seed,
        sketch_dtype=args.sketch_dtype,
        num_passes=args.num_passes,
        parallel_blocks=args.threads,
        dense_chunk_size=(args.dense_chunk_size if args.dense_chunk_size > 0 else None),
        precond_min_ridge=args.precond_min_ridge,
        precond_warmup_solves=args.precond_warmup_solves,
        spill_dir=(args.spill_dir or None),
        precond_type=args.precond_type,
        num_col_blocks=args.num_col_blocks,
        auto_bail_out=(not args.no_bail_out),
        bail_out_threshold=args.bail_out_threshold,
        return_diagnostics=True,
    )

    _notify_bail_out(diag, json_mode=bool(args.json))
    err = float(np.linalg.norm(x - x_true) / (np.linalg.norm(x_true) + 1e-30)) if x_true is not None else None
    out = {
        "iterations": diag["iterations"] if diag else None,
        "residual_norm": diag["residual_norm"] if diag else None,
        "rhs_norm": diag["rhs_norm"] if diag else None,
        "sketch_rows": diag["sketch_rows"] if diag else None,
        "relative_x_error": err,
        "n": args.n,
        "d": args.d,
        "real_dataset": (args.real_dataset if args.real_dataset != "none" else None),
        "lambda": args.lam,
        "epsilon": args.eps,
        "tol": args.tol,
        "sparse": args.sparse,
        "num_spmv_Ax": diag.get("num_spmv_Ax") if diag else None,
        "num_spmv_ATx": diag.get("num_spmv_ATx") if diag else None,
        "preconditioner": {"action": precond_action, "path": precond_path} if precond_action else None,
        "bail_out": diag.get("bail_out") if diag else None,
        "bail_out_details": diag.get("bail_out_details") if diag and diag.get("bail_out_details") is not None else None,
        "time_total": diag.get("time_total") if diag else None,
        "time_sketch": diag.get("time_sketch") if diag else None,
        "time_cholesky": diag.get("time_cholesky") if diag else None,
        "time_pcg": diag.get("time_pcg") if diag else None,
        "sketch_dtype": args.sketch_dtype,
        "num_passes": args.num_passes,
        "threads": args.threads,
        "precond_min_ridge": args.precond_min_ridge,
        "precond_warmup_solves": args.precond_warmup_solves,
        "spill_dir": (args.spill_dir or None),
        "dense_chunk_size": (args.dense_chunk_size if args.dense_chunk_size > 0 else None),
        "precond_type": args.precond_type,
        "num_col_blocks": args.num_col_blocks,
        "record_history": args.record_history,
        "threads_auto": auto_threads,
    }

    js_compact = json.dumps(out)
    if args.json_out:
        try:
            dst = Path(args.json_out)
            dst.parent.mkdir(parents=True, exist_ok=True)
            dst.write_text(json.dumps(out, indent=2), encoding="utf-8")
        except Exception:
            pass
    if args.json:
        print(js_compact)
        if args.log_json:
            try:
                with open(args.log_json, "w", encoding="utf-8") as f:
                    f.write(js_compact)
            except Exception:
                pass
        return 0
    if args.log_json:
        try:
            with open(args.log_json, "w", encoding="utf-8") as f:
                f.write(js_compact)
        except Exception:
            pass
    times = ""
    if out["time_total"] is not None:
        times = (
            f" total={out['time_total']:.3f}s"
            f" sketch={out['time_sketch']:.3f}s"
            f" chol={out['time_cholesky']:.3f}s"
            f" pcg={out['time_pcg']:.3f}s"
        )
    # Friendly Windows handling: ASCII default if requested and console not UTF-8
    try:
        import sys as _sys
        enc = (_sys.stdout.encoding or "").lower()
        # Default to ASCII on non-UTF consoles unless JSON is requested
        if not enc.startswith("utf") and not args.json:
            args.ascii = True
    except Exception:
        pass
    print(
        f"iters={out['iterations']} res_norm={out['residual_norm']:.3e} "
        f"x_rel_err={out['relative_x_error']:.3e} sketch_rows={out['sketch_rows']} sketch_dtype={args.sketch_dtype}" + times
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


