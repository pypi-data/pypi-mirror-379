from __future__ import annotations

import json
import pytest

from rcfd_pcg.cli import main as cli_main


@pytest.mark.usefixtures("capsys")
def test_cli_json_emits_bail_out(monkeypatch, tmp_path, capsys):
    # Force the spectral indicator to be tiny so the guardrail always fires.
    monkeypatch.setattr(
        "rcfd_pcg.rcfd.estimate_spectral_spread_indicator",
        lambda *args, **kwargs: 1.0,
    )
    argv = [
        "--n",
        "128",
        "--d",
        "16",
        "--eps",
        "0.25",
        "--tol",
        "1e-6",
        "--json",
        "--json-out",
        str(tmp_path / "bail.json"),
    ]
    code = cli_main(argv)
    assert code == 0
    captured = capsys.readouterr()
    payload = json.loads(captured.out)
    file_payload = json.loads((tmp_path / "bail.json").read_text(encoding="utf-8"))
    assert payload["bail_out"] is True
    details = payload["bail_out_details"]
    file_details = file_payload["bail_out_details"]
    assert details["triggered"] is True
    assert file_details["triggered"] is True
    assert details["reason"] == "spectral_spread"
    assert file_details["reason"] == "spectral_spread"
    assert "Auto bail-out engaged" in captured.err
