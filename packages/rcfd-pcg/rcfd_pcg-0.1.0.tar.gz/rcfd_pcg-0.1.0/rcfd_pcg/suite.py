from __future__ import annotations

import argparse
import itertools
import json
import os
from datetime import datetime
from typing import List

from .bench import main as bench_main
from .env import collect_environment


def _parse_args(argv: List[str] | None) -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Run a benchmark suite and save artifacts")
    p.add_argument("--n", type=int, default=20000)
    p.add_argument("--d", type=int, default=200)
    p.add_argument("--sparse", action="store_true")
    p.add_argument("--density_list", type=str, default="0.05", help="Comma list of densities for sparse A")
    p.add_argument("--eps_list", type=str, default="0.25")
    p.add_argument("--repeats", type=int, default=3)
    p.add_argument("--tol", type=float, default=1e-6)
    p.add_argument("--sketch_dtypes", type=str, default="float32")
    p.add_argument("--num_passes_list", type=str, default="1")
    p.add_argument("--threads_list", type=str, default="1")
    p.add_argument("--precond_type_list", type=str, default="chol", help="Comma list of preconditioner types (chol,blockdiag)")
    p.add_argument("--num_col_blocks_list", type=str, default="1", help="Comma list of column block counts for block-diag preconditioner")
    p.add_argument("--export", type=str, default="", help="Optional path to export a reproducibility pack (zip)")
    p.add_argument("--out_root", type=str, default="results")
    return p.parse_args(argv)


def _ensure_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def main(argv: List[str] | None = None) -> int:
    import sys

    args = _parse_args(argv if argv is not None else sys.argv[1:])

    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    out_dir = os.path.join(args.out_root, f"bench_{ts}")
    _ensure_dir(out_dir)

    # Save environment snapshot
    env = collect_environment()
    with open(os.path.join(out_dir, "environment.json"), "w", encoding="utf-8") as f:
        json.dump(env, f, indent=2)

    def parse_list(s: str) -> List[str]:
        return [x.strip() for x in s.split(',') if x.strip()]

    eps_values = parse_list(args.eps_list)
    dtype_values = [x for x in parse_list(args.sketch_dtypes) if x in ("float32","float64")]
    if not dtype_values:
        dtype_values = ["float32"]
    num_passes_values = [x for x in parse_list(args.num_passes_list) if x in ("1","2")]
    if not num_passes_values:
        num_passes_values = ["1"]
    threads_values = [x for x in parse_list(args.threads_list) if x.isdigit() and int(x) >= 1]
    if not threads_values:
        threads_values = ["1"]

    # Cartesian product of configurations
    density_values = parse_list(args.density_list)
    if not density_values:
        density_values = ["0.05"]

    precond_types = [x for x in parse_list(args.precond_type_list) if x in ("chol","blockdiag")]
    if not precond_types:
        precond_types = ["chol"]
    num_col_blocks_values = [x for x in parse_list(args.num_col_blocks_list) if x.isdigit() and int(x) >= 1]
    if not num_col_blocks_values:
        num_col_blocks_values = ["1"]

    for eps, sdtype, npass, nthr, dens, ptype, ncb in itertools.product(eps_values, dtype_values, num_passes_values, threads_values, density_values, precond_types, num_col_blocks_values):
        tag = f"n{args.n}_d{args.d}_sparse{int(args.sparse)}_dens{dens}_eps{eps}_dtype{sdtype}_passes{npass}_thr{nthr}_ptype{ptype}_ncb{ncb}"
        out_json = os.path.join(out_dir, f"bench_{tag}.json")
        bench_args = [
            "--n", str(args.n),
            "--d", str(args.d),
            "--tol", str(args.tol),
            "--repeats", str(args.repeats),
            "--eps", str(eps),
            "--density", str(dens),
            "--sketch-dtype", sdtype,
            "--num-passes", str(npass),
            "--threads", str(nthr),
            "--precond-type", str(ptype),
            "--num-col-blocks", str(ncb),
            "--json",
            "--out-json", out_json,
        ]
        if args.sparse:
            bench_args.append("--sparse")
        code = bench_main(bench_args)
        if code != 0:
            print(f"Warning: bench failed for {tag} with exit code {code}")

    # Summarize into a simple index file with list of files produced
    index = {
        "out_dir": out_dir,
        "files": sorted([fn for fn in os.listdir(out_dir) if fn.endswith(".json")]),
        "n": args.n,
        "d": args.d,
        "sparse": args.sparse,
        "repeats": args.repeats,
        "tol": args.tol,
    }
    with open(os.path.join(out_dir, "index.json"), "w", encoding="utf-8") as f:
        json.dump(index, f, indent=2)
    print(json.dumps(index, indent=2))

    # Optional export pack
    if args.export:
        try:
            import zipfile
            pack_path = args.export
            with zipfile.ZipFile(pack_path, 'w', compression=zipfile.ZIP_DEFLATED) as zf:
                # Include environment and index
                zf.write(os.path.join(out_dir, "environment.json"), arcname="environment.json")
                zf.write(os.path.join(out_dir, "index.json"), arcname="index.json")
                # Include all bench JSONs
                for fn in index["files"]:
                    zf.write(os.path.join(out_dir, fn), arcname=os.path.join("results", fn))
            print(json.dumps({"exported": pack_path}))
        except Exception as e:
            print(json.dumps({"export_error": str(e)}))
    return 0


if __name__ == "__main__":
    import sys
    raise SystemExit(main(sys.argv[1:]))


