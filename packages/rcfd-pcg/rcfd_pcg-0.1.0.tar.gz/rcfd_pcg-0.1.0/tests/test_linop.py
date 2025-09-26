import numpy as np

from rcfd_pcg import SyntheticProblem
from rcfd_pcg.linop import cg_solve_normal_eq


def test_cg_linop_rcfd_preconditioner():
    problem = SyntheticProblem(
        num_rows=4000,
        num_cols=120,
        spectrum_decay="power",
        power_exponent=1.0,
        noise_std=0.0,
        random_seed=7,
        make_sparse=True,
    )
    A, b, x_true = problem.make()
    x, diag = cg_solve_normal_eq(A, b, ridge_lambda=0.0, tol=1e-6, max_iter=200, use_rcfd_preconditioner=True, rcfd_eps=0.25)
    rel_err = np.linalg.norm(x - x_true) / (np.linalg.norm(x_true) + 1e-30)
    assert rel_err < 1e-2


