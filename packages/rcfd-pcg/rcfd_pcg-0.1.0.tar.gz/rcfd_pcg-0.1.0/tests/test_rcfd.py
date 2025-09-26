import numpy as np
import pytest

from rcfd_pcg import rcfd_pcg_solve, SyntheticProblem


def test_rcfd_pcg_converges_power_spectrum_sparse():
    problem = SyntheticProblem(
        num_rows=4000,
        num_cols=120,
        spectrum_decay="power",
        power_exponent=1.0,
        noise_std=0.0,
        random_seed=123,
        make_sparse=True,
    )
    A, b, x_true = problem.make()
    x, diag = rcfd_pcg_solve(
        A,
        b,
        ridge_lambda=1e-6,
        epsilon=0.25,
        tol=1e-8,
        max_iter=2000,
        return_diagnostics=True,
    )

    assert diag is not None
    assert diag["iterations"] > 0
    rel_err = np.linalg.norm(x - x_true) / (np.linalg.norm(x_true) + 1e-30)
    assert rel_err < 1e-2


def test_rcfd_pcg_converges_exp_spectrum_dense():
    problem = SyntheticProblem(
        num_rows=2000,
        num_cols=80,
        spectrum_decay="exp",
        exp_rate=0.01,
        noise_std=0.0,
        random_seed=42,
        make_sparse=False,
    )
    A, b, x_true = problem.make()
    x, diag = rcfd_pcg_solve(
        A,
        b,
        ridge_lambda=1e-6,
        epsilon=0.25,
        tol=1e-8,
        max_iter=2000,
        return_diagnostics=True,
    )

    assert diag is not None
    assert diag["iterations"] > 0
    rel_err = np.linalg.norm(x - x_true) / (np.linalg.norm(x_true) + 1e-30)
    assert rel_err < 1e-2




def test_rcfd_pcg_bail_out_details_triggered():
    # Identity-like matrix keeps the spectrum tight so the bail-out indicator is near 1.
    A = np.eye(64, 16)
    x_true = np.ones(16)
    b = A @ x_true
    x, diag = rcfd_pcg_solve(
        A,
        b,
        ridge_lambda=0.0,
        epsilon=0.25,
        tol=1e-8,
        max_iter=200,
        return_diagnostics=True,
        auto_bail_out=True,
        bail_out_threshold=100.0,
    )

    assert diag is not None
    assert diag["bail_out"] is True
    info = diag.get("bail_out_details")
    assert isinstance(info, dict)
    indicator = info.get("indicator")
    threshold = info.get("threshold")
    assert isinstance(indicator, (int, float))
    assert isinstance(threshold, (int, float))
    assert indicator <= threshold + 1e-6
    assert info.get("triggered") is True
    assert info.get("reason") == "spectral_spread"


def test_rcfd_pcg_bail_out_disabled():
    A = np.eye(64, 16)
    x_true = np.ones(16)
    b = A @ x_true
    x, diag = rcfd_pcg_solve(
        A,
        b,
        ridge_lambda=0.0,
        epsilon=0.25,
        tol=1e-8,
        max_iter=200,
        return_diagnostics=True,
        auto_bail_out=False,
        bail_out_threshold=0.5,
    )

    assert diag is not None
    assert diag.get("bail_out") is False
    assert "bail_out_details" not in diag or diag.get("bail_out_details") is None
