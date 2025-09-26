from __future__ import annotations

import argparse
import itertools
import json
import time

import numpy as np

from .rcfd import rcfd_pcg_solve, SyntheticProblem
from .util import choose_epsilon_auto


def _parse_args(argv):
    p = argparse.ArgumentParser(description="RCFD-PCG ablation sweeps")
    p.add_argument("--n", type=int, default=20000)
    p.add_argument("--d", type=int, default=200)
    p.add_argument("--lam", type=float, default=0.0)
    p.add_argument("--eps", type=str, default="auto")
    p.add_argument("--tol", type=float, default=1e-6)
    p.add_argument("--sparse", action="store_true")
    p.add_argument("--repeats", type=int, default=1)
    p.add_argument("--json", action="store_true")
    p.add_argument("--log-json", type=str, default="", help="Optional path to save JSON results")
    p.add_argument("--out-csv", type=str, default="", help="Optional CSV path to save results")
    p.add_argument("--eps_grid", type=str, default="0.15,0.25,0.35")
    p.add_argument("--oversampling_grid", type=str, default="4,8,12")
    p.add_argument("--power_grid", type=str, default="0,1")
    p.add_argument("--compression", type=str, default="auto", help="Compression: auto|eigh|eigh_inc|rand")
    p.add_argument("--sketch_dtype_grid", type=str, default="float32")
    p.add_argument("--num_passes_grid", type=str, default="1")
    p.add_argument("--threads_grid", type=str, default="1")
    p.add_argument("--ascii", action="store_true", help="Force ASCII-only symbols in human-readable output")
    return p.parse_args(argv)


def main(argv=None) -> int:
    import sys
    args = _parse_args(argv if argv is not None else sys.argv[1:])

    eps_base = choose_epsilon_auto(args.d) if (isinstance(args.eps, str) and args.eps == "auto") else float(args.eps)
    eps_list = list({float(x) for x in args.eps_grid.split(',') if x})
    if eps_base not in eps_list:
        eps_list.append(eps_base)

    overs_list = list({int(x) for x in args.oversampling_grid.split(',') if x})
    power_list = list({int(x) for x in args.power_grid.split(',') if x})

    problem = SyntheticProblem(num_rows=args.n, num_cols=args.d, make_sparse=args.sparse)
    A, b, x_true = problem.make()

    results = []
    dtype_list = [s for s in {x.strip() for x in args.sketch_dtype_grid.split(',') if x} if s in ("float32","float64")]
    if not dtype_list:
        dtype_list = ["float32"]
    passes_list = [int(x) for x in {x.strip() for x in args.num_passes_grid.split(',') if x} if x in ("1","2")]
    if not passes_list:
        passes_list = [1]
    threads_list = [int(x) for x in {x.strip() for x in args.threads_grid.split(',') if x} if x.isdigit() and int(x) >= 1]
    if not threads_list:
        threads_list = [1]

    for eps, overs, power, sdtype, npass, nthr in itertools.product(sorted(eps_list), sorted(overs_list), sorted(power_list), dtype_list, passes_list, threads_list):
        times = []
        iters = []
        for _ in range(args.repeats):
            t0 = time.perf_counter()
            _, diag = rcfd_pcg_solve(
                A,
                b,
                ridge_lambda=args.lam,
                epsilon=eps,
                tol=args.tol,
                compression=args.compression,
                oversampling=overs,
                power_iters=power,
                sketch_dtype=sdtype,
                num_passes=npass,
                parallel_blocks=nthr,
                return_diagnostics=True,
                count_spmv=True,
                # threads controls randomized compression blocks via env-like param
            )
            t1 = time.perf_counter()
            times.append(t1 - t0)
            iters.append(diag["iterations"]) if diag else None
        row = {
            "eps": eps,
            "oversampling": overs,
            "power_iters": power,
            "sketch_dtype": sdtype,
            "num_passes": npass,
            "threads": nthr,
            "time_mean": float(np.mean(times)),
            "time_std": float(np.std(times)),
            "iters_mean": float(np.mean(iters)) if iters else None,
        }
        results.append(row)

    if args.out_csv:
        import csv
        with open(args.out_csv, "w", newline="") as f:
            # Include all emitted fields in CSV to avoid DictWriter field mismatch
            w = csv.DictWriter(
                f,
                fieldnames=[
                    "eps",
                    "oversampling",
                    "power_iters",
                    "sketch_dtype",
                    "num_passes",
                    "threads",
                    "time_mean",
                    "time_std",
                    "iters_mean",
                ],
            )
            w.writeheader()
            for r in results:
                w.writerow(r)

    if args.json:
        js = json.dumps({"results": results})
        print(js)
        if args.log_json:
            try:
                with open(args.log_json, "w", encoding="utf-8") as f:
                    f.write(js)
            except Exception:
                pass
    else:
        plus_minus = "+/-"
        approx = "~"
        if not args.ascii:
            try:
                import sys
                if hasattr(sys.stdout, "encoding") and (sys.stdout.encoding or "").lower().startswith("utf"):
                    plus_minus = "±"
                    approx = "≈"
            except Exception:
                pass
        for r in sorted(results, key=lambda x: x["time_mean"]):
            print(
                f"eps={r['eps']} overs={r['oversampling']} power={r['power_iters']} dtype={r['sketch_dtype']} passes={r['num_passes']} threads={r['threads']} "
                f"time={r['time_mean']:.3f}{plus_minus}{r['time_std']:.3f}s iters{approx}{r['iters_mean']}"
            )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


