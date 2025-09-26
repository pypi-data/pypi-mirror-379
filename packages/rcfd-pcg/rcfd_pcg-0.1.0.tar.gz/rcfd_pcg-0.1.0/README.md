# RCFD-PCG MVP

➡️ Browse recent results and plots: `results/index.html`

A minimal Python package implementing Ridge-Corrected Frequent-Directions (RCFD) preconditioning and a PCG solver for tall-skinny least-squares.

## Why RCFD-PCG is a no-brainer for tall-skinny least squares

- Reuse wins now: `results/bench_sparse_reuse.json` and `results/single_vs_reuse.html` capture end-to-end time dropping from ~0.31 s to ~0.17 s with 36 PCG iterations, while LSQR/LSMR still burn >100 iterations.
- Ill-conditioned proof on demand: `results/bench_ill_cond.json` shows RCFD converging in 3 iterations where LSQR takes 309+, matching dense Cholesky accuracy without dense costs.
- Deterministic, inspectable collateral: CLI runs emit shareable JSON/HTML (`results/demo_report.html`) so buyers can embed metrics in review decks without notebooks.
- Drop-in for ML stacks: `rcfd_pcg.sklearn.RCFDRidge` slots into sklearn pipelines, joblib persistence, and `docs/RegimeCookbook.md` narrates parameter picks per regime.

## Ten-minute proof path

1. Install (`pip install -e .` or grab the wheel artifacts produced by CI).
2. Run `python -m rcfd_pcg.cli demo --out results/demo_report.json --html results/demo_report.html` to preheat the solver and generate the HTML summary.
3. Run the canonical sparse benchmark twice to surface reuse wins:
   - `python -m rcfd_pcg.bench --n 20000 --d 200 --sparse --eps 0.25 --tol 1e-6 --repeats 3 --json --out-json results/bench_sparse_single.json`
   - `python -m rcfd_pcg.bench --n 20000 --d 200 --sparse --eps 0.25 --tol 1e-6 --repeats 3 --reuse-precond --json --out-json results/bench_sparse_reuse.json`
4. Open `results/index.html` (or `results/single_vs_reuse.html`) to walk stakeholders through the before/after artifacts.
5. Optional: drop in a real dataset with `rcfd-pcg --real-dataset 20ng --json` to show a like-for-like baseline.
6. Run `python -m examples.proof_pack --results results --out-json results/proof_pack.json --out-html results/proof_pack.html` to bundle the JSON + HTML summary (`results/proof_pack.html`). See `docs/ProofPack.md` for a shareable runbook. You can also automate everything with `python scripts/proof_pack_pipeline.py`.

Share the `results/` directory or the prebuilt plots in `plots/` as your proof-pack; everything is deterministic so another laptop reproduces the story. The solver JSON surfaces `bail_out` and `bail_out_details` so it's obvious when the auto guardrail skips sketching.


[![CI](https://github.com/your-org/RCFD/actions/workflows/ci.yml/badge.svg)](https://github.com/your-org/RCFD/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/your-org/RCFD/branch/main/graph/badge.svg)](https://codecov.io/gh/your-org/RCFD)

## North star

- Let any user prove “iterations ↓ ~4×; wall‑clock ↓ 1.5–3×” for tall‑skinny least‑squares on their laptop in under 10 minutes, with zero meetings. Convert that proof into design partners and a first paid pilot.

## Status and how to run

### What’s in the repo and works today
- CLIs and self‑serve spine
  - `rcfd-pcg demo`: one‑command demo; emits JSON + HTML report. DONE
  - `rcfd-pcg run`: run on local files (`mm:matrix.mtx`, `npz:csr.npz`, `.npy`). DONE
  - `rcfd-pcg doctor`: environment/compat check in JSON or text. DONE
- Solver and APIs
  - Deterministic RCFD‑PCG with bail‑out to LSQR/LSMR when not a fit; JSON diagnostics. DONE
  - sklearn wrapper `rcfd_pcg.sklearn.RCFDRidge`; joblib save/load. DONE
- Benchmarks and artifacts
  - Suite runner and plotting: `rcfd_pcg.suite`, `examples/plot_benchmarks.py`. DONE
  - Canonical synthetic sparse benchmarks saved (single‑shot and reuse) with time_p95/p99: `results/bench_sparse_single.json`, `results/bench_sparse_reuse.json`
- Docs (start here)
  - `docs/StartHere.md`, `docs/BenchmarkGuide.md`, `docs/RegimeCookbook.md`
  - Trust pages: `docs/WhenNotToUse.md`, `docs/Privacy.md`; Support: `docs/Troubleshooting.md`
  - GPU envelope: `docs/GPUEnvelope.md` (experimental); Spark recipe: `examples/spark_recipe.md`
- Packaging
  - GitHub Actions wheels workflow present. IN PROGRESS
  - CPU `Dockerfile` present; local build works; publish pending.
- Service
  - `examples/service.py` (FastAPI) with request limits, timeout, optional token, and `/metrics`. DONE
- Code health
  - Tests passing locally (Windows). Lints clean for edited files.

### Guardrails and how we steer around them
- Single-shot, small/moderate d: iteration wins lead, but wall-clock may hinge on sketch overhead. Lead with the reuse story (`rcfd_pcg.bench --reuse-precond`) or let the built-in bail-out keep LSQR/LSMR when they finish faster; docs/BenchmarkGuide.md captures the playbook, and you can tune it with `--bail-out-threshold` or disable via `--no-bail-out`.
- GPU path is intentionally prototypical; keep it off unless you opt into the envelope in `docs/GPUEnvelope.md` while we complete the CuPy integration.
- Wheels and Docker publishing are baking: run `pip install -e .` or build straight from the repo today while the release workflow marches toward tagged PyPI pushes (see Roadmap launch lane).
- Spark connector remains a recipe; teams use `examples/spark_recipe.md` until the packaged connector ships.


### How to run the essentials
- Demo (JSON + HTML):

```powershell
python -m rcfd_pcg.cli demo --out results/demo_report.json --html results/demo_report.html
```

- Single solve from files:

```powershell
python -m rcfd_pcg.cli run --A mm:path/to/matrix.mtx --b vec.npy --out report.json --html report.html
```

- Doctor:

```powershell
python -m rcfd_pcg.cli doctor --json
```

- Suite + plots (small demo):

```powershell
python -m rcfd_pcg.suite --n 2000 --d 200 --sparse --eps_list 0.15,0.25 --sketch_dtypes float32 --num_passes_list 1 --threads_list 1 --repeats 1 --out_root results
python -m examples.plot_benchmarks --input results/<printed out_dir> --out plots
```

- Canonical sparse single‑shot/reuse (already used):

```powershell
python -m rcfd_pcg.bench --n 20000 --d 200 --sparse --eps 0.25 --tol 1e-6 --repeats 3 --json --out-json results/bench_sparse_single.json
python -m rcfd_pcg.bench --n 20000 --d 200 --sparse --eps 0.25 --tol 1e-6 --repeats 3 --reuse-precond --json --out-json results/bench_sparse_reuse.json
```

- Service (optional):

```powershell
uvicorn examples.service:app --host 0.0.0.0 --port 8000
```

### Risks and how to avoid them
- “Iterations win but time doesn’t”: present two tracks (single‑shot vs reuse) and lead with reuse time wins.
- Windows console and package friction: prefer `--json` or `--ascii-default`; ship wheels and MSI/winget notes; signed wheels page.
- Variability: pin BLAS threads (`OPENBLAS_NUM_THREADS=1` etc.), warmup runs, use a “contention‑safe” preset.
- Large d memory: use `--precond-type blockdiag --num-col-blocks K` or spill to disk.

### Where to look
- Roadmap: `ROADMAP.md`
- Solver: `rcfd_pcg/rcfd.py`; CLI: `rcfd_pcg/cli.py`; Bench: `rcfd_pcg/bench.py`
- Trust/support: `docs/WhenNotToUse.md`, `docs/Privacy.md`, `docs/Troubleshooting.md`
- Start here: `docs/StartHere.md`
- Docker: `Dockerfile`
- Spark recipe: `examples/spark_recipe.md`
- Results/plots: `results/`, `plots/`
  - Artifact index: `results/index.html` (generated via `python -m examples.generate_results_index`)

### Docker (CPU) quickstart
Build locally and run the demo without a local Python install:

```powershell
docker build -t rcfd-pcg:cpu -f Dockerfile .
docker run --rm -v ${PWD}:/work -w /work rcfd-pcg:cpu \
  python -m rcfd_pcg.cli demo --out results/demo_report.json --html results/demo_report.html
```

## Install

### From PyPI (releases >=0.1.0)

```bash
pip install rcfd-pcg
```

### From GHCR (Docker)

```bash
docker pull ghcr.io/your-org/rcfd:latest
docker run --rm -v ${PWD}:/work -w /work ghcr.io/your-org/rcfd:latest rcfd-pcg demo --json
```

For pinned versions, replace `latest` with your tag (e.g., `ghcr.io/your-org/rcfd:v0.1.0`).

### From source (dev mode)

```bash
pip install -e .[dev]
```

### From wheels (CI artifacts)

Prebuilt wheels are still produced on tags via GitHub Actions. Download from the workflow artifacts or your release assets:

```bash
pip install rcfd-pcg-*.whl
```

## CLI quickstart

```bash
rcfd-pcg --n 200000 --d 500 --eps 0.25 --lam 0 --tol 1e-6 --sparse --json
```

Real dataset quickstart (requires scikit-learn):

```bash
rcfd-pcg --real-dataset 20ng --n-features 1024 --eps 0.25 --tol 1e-6 --json --json-out results/bench_20ng.json
rcfd-pcg --real-dataset rcv1 --n-features 1024 --eps 0.25 --tol 1e-6 --json --json-out results/bench_rcv1.json
rcfd-pcg --real-dataset yearmsd --sample 100000 --eps 0.25 --tol 1e-6 --json --json-out results/bench_yearmsd.json
rcfd-pcg --real-dataset cahousing --eps 0.25 --tol 1e-6 --json --json-out results/bench_cahousing.json
```

Auto mode example (auto epsilon and tuned compression):

```bash
rcfd-pcg --n 20000 --d 200 --sparse --eps auto --json
```

### Canonical benchmarks

Use the helper script to run consistent comparisons and optionally save JSON.

Sparse scenario (n≈20k, d≈200):

```bash
python -m examples.benchmark_canonical --scenario synthetic_sparse \
  --n 20000 --d 200 --repeats 3 --eps 0.25 --threads-compare 1,2 --json \
  --out-json bench_canonical_sparse.json
```

Dense scenario (n≈5k, d≈400):

```bash
python -m examples.benchmark_canonical --scenario synthetic_dense \
  --n 5000 --d 400 --repeats 2 --eps 0.25 --threads-compare 1,2 --json \
  --out-json bench_canonical_dense.json
```

Recsys-like tall-skinny scenario (n≈500k, d≈200):

```bash
python -m examples.benchmark_canonical --scenario recsys_like \
  --n 500000 --d 200 --repeats 3 --eps 0.25 --threads-compare 1,2 --json \
  --out-json results/bench_recsys_like.json
```

Ill-conditioned dense scenario (n≈20k, d≈200):

```bash
python -m examples.benchmark_canonical --scenario ill_conditioned \
  --n 20000 --d 200 --repeats 3 --eps 0.25 --threads-compare 1,2 --json \
  --out-json results/bench_ill_cond.json
```

Recommendation helper (choose ε/compression/threads for your regime):

```bash
rcfd-pcg --d 200 --sparse --density 0.05 --recommend --json
```

### Demo service (optional)

```bash
pip install fastapi uvicorn
uvicorn examples.service:app --host 0.0.0.0 --port 8000
```

Hardening knobs (env):
- `RCFD_SERVICE_MAX_BODY` (bytes, default 5_000_000)
- `RCFD_SERVICE_SOLVE_TIMEOUT_S` (float seconds, default 15.0)
- `RCFD_SERVICE_REQUIRE_TOKEN=1` and `RCFD_SERVICE_TOKEN=...`

Example request:

```bash
curl -X POST "http://localhost:8000/solve" \
  -H "Content-Type: application/json" \
  -H "x-token: $RCFD_SERVICE_TOKEN" \
  -d '{"A": [[1.0,2.0],[3.0,4.0]], "b": [1.0,0.0], "eps": 0.25, "tol": 1e-6}'
```

## Regime chooser (quick guidance)

- Sparse, moderate d (128 ≤ d ≤ 512; density ≤ 0.05)
  - Use: `--eps auto` (→ ε≈0.15), randomized compression with oversampling≈12 and power≈1, `--threads 2`
  - Example: `rcfd-pcg --n 20000 --d 200 --sparse --eps auto --json`
- Larger d or denser matrices
  - Use: `--eps auto` (ε≈0.25 up to d<2048, else 0.35), randomized compression with oversampling 8–12, power 0–1, `--threads 1`
  - Example: `rcfd-pcg --n 100000 --d 1000 --sparse --eps auto --json`
- Exact compression fallback
  - For small dense d<256, exact eigendecomp (`--compression eigh`) can be competitive; an incremental variant `--compression eigh_inc` is also available.
- Preconditioner ridge floor
  - Keep `--precond-min-ridge 1e-7` unless you see SPD failures (raise slightly) or oversmoothing (lower slightly).

## Python API

```python
import numpy as np
from rcfd_pcg import build_rcfd_sketch, rcfd_pcg_solve, SyntheticProblem

problem = SyntheticProblem(num_rows=200_000, num_cols=500, noise_std=0.0, make_sparse=True)
A, b, x_true = problem.make()
x, diag = rcfd_pcg_solve(A, b, ridge_lambda=0.0, epsilon=0.25, tol=1e-6, return_diagnostics=True, count_spmv=True)
print(diag)

### SciPy LinearOperator drop-in

```python
from rcfd_pcg.linop import cg_solve_normal_eq
x, diag = cg_solve_normal_eq(A, b, ridge_lambda=0.0, tol=1e-6, max_iter=200, use_rcfd_preconditioner=True, rcfd_eps=0.25)
```

### scikit-learn style API

```python
from rcfd_pcg.sklearn import RCFDRidge
model = RCFDRidge(lam=0.0, eps=0.25, tol=1e-6, max_iter=200, fit_intercept=False)
model.fit(A, b)
pred = model.predict(A)
```

### scikit-learn persistence (save/load)

```python
from rcfd_pcg.sklearn import RCFDRidge
import joblib

model = RCFDRidge(lam=0.0, eps=0.25, tol=1e-6, fit_intercept=False)
model.fit(A, b)
model.save("rcfd_ridge.joblib")  # requires: pip install joblib

loaded = RCFDRidge.load("rcfd_ridge.joblib")
pred = loaded.predict(A)
```

## Ablations

```bash
rcfd-ablate --n 20000 --d 200 --sparse --repeats 1

# Save CSV
rcfd-ablate --n 20000 --d 200 --sparse --repeats 1 --out-csv ablation.csv
```

## Preconditioner reuse (save/load) with JSON

Saving and reusing the preconditioner can reduce total runtime when solving multiple times on the same `A`.

```powershell
# First run: build and save preconditioner
rcfd-pcg --n 20000 --d 200 --sparse --eps 0.25 --tol 1e-6 --save-precond pre.npz --json

# Subsequent run: load and reuse preconditioner
rcfd-pcg --n 20000 --d 200 --sparse --eps 0.25 --tol 1e-6 --load-precond pre.npz --json
```

Example JSON (truncated) showing reduced sketch/Cholesky times on reuse:

```json
{
  "iterations": 36,
  "time_total": 0.312,
  "time_sketch": 0.158,
  "time_cholesky": 0.042,
  "time_pcg": 0.108,
  "preconditioner": {"action": "saved", "path": "pre.npz"}
}
```

```json
{
  "iterations": 36,
  "time_total": 0.173,
  "time_sketch": 0.0,
  "time_cholesky": 0.0,
  "time_pcg": 0.171,
  "preconditioner": {"action": "loaded", "path": "pre.npz"}
}
```

### Pipeline example with sparse CSR features

```python
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from rcfd_pcg.sklearn import RCFDRidge

df = pd.DataFrame({
    "cat": ["a", "b", "a", "c"],
    "num1": [0.1, 1.2, -0.3, 2.4],
    "num2": [5.0, 3.3, 1.1, 0.0],
})
y = np.array([1.0, 0.0, 1.0, 0.0])

pre = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore", sparse_output=True), ["cat"]),
        ("num", StandardScaler(with_mean=False), ["num1", "num2"])  # keep sparse-friendly
    ],
    sparse_threshold=0.1,
)

pipe = Pipeline([
    ("prep", pre),
    ("model", RCFDRidge(lam=0.0, eps=0.25, tol=1e-6, fit_intercept=False, sketch_dtype="float32")),
])

# Direct fit (auto bail-out is enabled by default)
pipe.fit(df, y)
print("bail_out?", pipe.named_steps["model"].diagnostics_.get("bail_out"))
pred = pipe.predict(df)

# Optional hyperparameter search: tune epsilon and the bail-out guardrail
search = GridSearchCV(
    pipe,
    param_grid={
        "model__eps": [0.15, 0.25],
        "model__bail_out_threshold": [4.0, 5.0],
        "model__auto_bail_out": [True],
    },
    cv=3,
    scoring="neg_mean_squared_error",
    n_jobs=1,
)
search.fit(df, y)
print("best params:", search.best_params_)
best_model = search.best_estimator_.named_steps["model"]
print("bail_out after search?", best_model.diagnostics_.get("bail_out"))


## Changelog

- 0.1.0
  - GA prep: add one-command proof-pack pipeline (`scripts/proof_pack_pipeline.py`) and integrate proof-pack aggregator into docs and quickstarts.
  - Guardrails: expose `--bail-out-threshold`, surface `bail_out`/`bail_out_details` in CLI/bench outputs, add sklearn knobs and cookbook examples.
  - Packaging: bump version to 0.1.0; CI workflows publish to TestPyPI on `*-rc` tags and PyPI on final tags with attestations; GHCR workflow tags `latest` only on final tags.
  - Proof-pack artifacts refreshed; `results/index.html` regenerated; plots updated.

- 0.0.3
  - CLI: fix HTML summary table rendering in demo/report output.
  - Benchmarks: clarify canonical sparse single-shot and reuse commands; refreshed artifacts.
  - Packaging: version bump and local wheel/sdist build verification.
- 0.0.2
  - Add BLAS thread limiting during Python-parallel regions to avoid oversubscription.
  - Bench: add Dense-QR and Dense-Cholesky baselines (toggle with `--dense-baselines on|off|auto`).
  - Heuristics: prefer oversampling≈12 for moderate d (128–512).
  - Fix ablation CSV headers and plumb `--threads_grid` through to solver (`parallel_blocks`).
  - Bench CLI: pass `atol=0` to SciPy `cg` to avoid deprecation warnings.
  - sklearn: include `sketch_dtype` in `get_params` for proper round-tripping.
  - CI: add GitHub Actions for tests (Windows/Ubuntu) with coverage; add wheel build workflow for releases.
- 0.0.1
  - Initial MVP: solver/CLIs, docs, tests, notebooks.

### Windows consoles
On Windows, prefer `--json`, or pass `--ascii`/`--ascii-default`, or set UTF-8 encoding to avoid Unicode issues in CLI output:

```powershell
$env:PYTHONIOENCODING='utf-8'; [Console]::OutputEncoding = [System.Text.UTF8Encoding]::new(); chcp 65001 | Out-Null
rcfd-bench --n 20000 --d 200 --sparse --eps 0.25 --tol 1e-6 --repeats 3 --json
```

## Notes
- Deterministic single-pass sketch; preconditioner from B^T B + λ I.
- PCG on normal equations; 2 SpMVs/iter.
- For large d, consider batching/shrink cadence tuning.

## Docs index
- Benchmark Guide: `docs/BenchmarkGuide.md`
- Start here: `docs/StartHere.md`
- Regime Cookbook: `docs/RegimeCookbook.md` (parameter tables and commands)
- Dataset Gallery: `docs/Datasets.md`
- API Reference: `docs/API.md`
- Preconditioner Cache: `docs/PreconditionerCache.md`
- Support Matrix: `docs/SupportMatrix.md`
- Threading & BLAS Guide: `docs/ThreadsAndBLAS.md`
 - Verification (hash/digest): `docs/Verification.md`
 - Weights/WLS notes: `docs/WeightsWLS.md`

## Release checklist (maintainers)
- Bump version in `pyproject.toml` and update changelog/README highlights.
- Ensure `PYPI_API_TOKEN` secret is set for the repo (pypi `__token__` scoped to the project).
- Create and push tag `vX.Y.Z`; the wheels workflow will publish to PyPI automatically.
- Trigger the Docker workflow (auto on tag, or `gh workflow run docker.yml --ref vX.Y.Z`) to push `ghcr.io/your-org/rcfd` images.
- Verify artifacts: install from PyPI (`pip install rcfd-pcg==X.Y.Z`) and pull the GHCR image (`docker pull ghcr.io/your-org/rcfd:vX.Y.Z`).
- Regenerate `results/index.html`/plots if benchmarks changed, then update `README.md` and `ROADMAP.md` as needed.
