import numpy as np

from rcfd_pcg import SyntheticProblem
from rcfd_pcg.rcfd import rcfd_pcg_solve


def test_residual_history_monotone_nonincreasing():
    problem = SyntheticProblem(num_rows=3000, num_cols=80, random_seed=5, make_sparse=False)
    A, b, _ = problem.make()
    x, diag = rcfd_pcg_solve(A, b, ridge_lambda=1e-6, epsilon=0.25, tol=1e-6, max_iter=200, return_diagnostics=True, record_history=True)
    hist = diag.get("residual_history")
    assert hist is not None and len(hist) > 5
    # Allow tiny numerical increases but ensure generally nonincreasing
    for i in range(1, len(hist)):
        assert hist[i] <= hist[i-1] * 1.001


def test_probe_auto_tuning_runs_dense_and_sparse():
    # Dense case
    rng = np.random.default_rng(0)
    A = rng.standard_normal((256, 64))
    b = rng.standard_normal(256)
    x, diag = rcfd_pcg_solve(A, b, ridge_lambda=1e-6, epsilon=0.25, tol=1e-6, max_iter=50, return_diagnostics=True)
    assert diag is not None and diag["dimension"] == 64

    # Sparse-like case (still dense ndarray with many zeros)
    A2 = (rng.random((256, 64)) < 0.05).astype(float) * rng.standard_normal((256, 64))
    b2 = rng.standard_normal(256)
    x2, diag2 = rcfd_pcg_solve(A2, b2, ridge_lambda=1e-6, epsilon=0.25, tol=1e-6, max_iter=50, return_diagnostics=True)
    assert diag2 is not None and diag2["dimension"] == 64

