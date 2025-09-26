from __future__ import annotations

import sys

from rcfd_pcg.cli import main as cli_main


def test_cli_ascii_flag_runs_smoke(capsys):
    # Minimal run with ASCII flag; ensure it exits 0 and prints a line
    code = cli_main([
        "--n", "2000",
        "--d", "80",
        "--sparse",
        "--eps", "0.25",
        "--tol", "1e-6",
        "--maxit", "5",
        "--ascii",
    ])
    assert code == 0
    out = capsys.readouterr().out
    assert "iters=" in out


