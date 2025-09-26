from __future__ import annotations

import importlib
import pytest

from rcfd_pcg.cli import main as cli_main


@pytest.mark.skipif(importlib.util.find_spec("sklearn") is None, reason="scikit-learn not installed")
def test_cli_real_dataset_cahousing_smoke(tmp_path, capsys):
    # Use cahousing which falls back to diabetes when fetch fails; keeps test offline-safe
    code = cli_main([
        "--real-dataset", "cahousing",
        "--eps", "0.25",
        "--tol", "1e-6",
        "--maxit", "20",
        "--json",
        "--json-out", str(tmp_path / "cahousing.json"),
    ])
    assert code == 0
    captured = capsys.readouterr()
    file_text = (tmp_path / "cahousing.json").read_text(encoding="utf-8")
    assert "\"real_dataset\": \"cahousing\"" in captured.out
    assert "\"real_dataset\": \"cahousing\"" in file_text


