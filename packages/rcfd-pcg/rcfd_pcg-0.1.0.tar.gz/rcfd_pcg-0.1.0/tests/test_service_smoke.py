from __future__ import annotations

import importlib
import pytest


@pytest.mark.skipif(
    importlib.util.find_spec("fastapi") is None or importlib.util.find_spec("starlette.testclient") is None,
    reason="fastapi/starlette not installed",
)
def test_service_solve_endpoint_smoke(tmp_path):
    # Import service module by file path to avoid package path issues
    import importlib.util
    import pathlib
    svc_path = pathlib.Path(__file__).resolve().parents[1] / "examples" / "service.py"
    spec = importlib.util.spec_from_file_location("svc_module", str(svc_path))
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)  # type: ignore[attr-defined]
    app = module.app  # type: ignore
    from starlette.testclient import TestClient  # type: ignore

    client = TestClient(app)
    # Health
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json().get("status") == "ok"

    # Solve small problem
    A = [[1.0, 2.0], [3.0, 4.0]]
    b = [1.0, 0.0]
    payload = {
        "A": A,
        "b": b,
        "lam": 0.0,
        "eps": 0.25,
        "tol": 1e-6,
        "max_iter": 50,
        "threads": 1,
    }
    r2 = client.post("/solve", json=payload)
    assert r2.status_code == 200
    js = r2.json()
    assert "x" in js and isinstance(js["x"], list)
    assert "diagnostics" in js


