import numpy as np

from rcfd_pcg import SyntheticProblem
from rcfd_pcg.sklearn import RCFDRidge


def test_rcfd_ridge_fit_predict():
    problem = SyntheticProblem(
        num_rows=4000,
        num_cols=120,
        spectrum_decay="power",
        power_exponent=1.0,
        noise_std=0.0,
        random_seed=11,
        make_sparse=False,
    )
    A, b, x_true = problem.make()
    model = RCFDRidge(lam=0.0, eps=0.25, tol=1e-6, max_iter=1000, fit_intercept=False, sketch_dtype='float32')
    model.fit(A, b)
    yhat = model.predict(A)
    # Check training reconstruction error is small
    rel_res = np.linalg.norm(A @ model.coef_ - b) / (np.linalg.norm(b) + 1e-30)
    assert rel_res < 1e-3
    # Coefficients close to ground truth
    rel_x_err = np.linalg.norm(model.coef_ - x_true) / (np.linalg.norm(x_true) + 1e-30)
    assert rel_x_err < 1e-2


