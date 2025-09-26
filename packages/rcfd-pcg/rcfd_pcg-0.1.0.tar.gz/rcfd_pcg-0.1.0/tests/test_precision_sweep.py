import numpy as np

from rcfd_pcg import SyntheticProblem
from rcfd_pcg.rcfd import rcfd_pcg_solve


def test_precision_sweep_float32_vs_float64_close():
    problem = SyntheticProblem(num_rows=2000, num_cols=60, random_seed=3, make_sparse=False)
    A, b, _ = problem.make()
    # Float64 run
    x64, _ = rcfd_pcg_solve(A.astype(np.float64), b.astype(np.float64), ridge_lambda=1e-6, epsilon=0.25, tol=1e-8, max_iter=500, sketch_dtype="float64")
    # Float32 run
    x32, _ = rcfd_pcg_solve(A.astype(np.float32), b.astype(np.float32), ridge_lambda=1e-6, epsilon=0.25, tol=1e-6, max_iter=500, sketch_dtype="float32")
    # Compare in float64
    diff = np.linalg.norm(x64 - x32.astype(np.float64)) / (np.linalg.norm(x64) + 1e-30)
    assert diff < 1e-2


