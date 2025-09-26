import numpy as np

from rcfd_pcg import SyntheticProblem
from rcfd_pcg.rcfd import rcfd_pcg_solve


def test_ill_conditioned_converges_reasonably():
    # Exponentially decaying spectrum -> ill-conditioned
    problem = SyntheticProblem(num_rows=8000, num_cols=120, spectrum_decay="exp", exp_rate=0.05, random_seed=9, make_sparse=True)
    A, b, x_true = problem.make()
    x, diag = rcfd_pcg_solve(A, b, ridge_lambda=1e-6, epsilon=0.25, tol=1e-6, max_iter=2000, count_spmv=True, return_diagnostics=True)
    assert diag["iterations"] < 500
    rel_err = np.linalg.norm(x - x_true) / (np.linalg.norm(x_true) + 1e-30)
    assert rel_err < 1e-2


