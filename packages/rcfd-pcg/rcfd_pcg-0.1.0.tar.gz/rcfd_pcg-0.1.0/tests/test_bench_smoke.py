from rcfd_pcg.bench import main as bench_main


def test_bench_smoke():
    # Small, quick run to ensure the entrypoint executes
    code = bench_main(["--n","1000","--d","60","--repeats","1","--sparse","--ascii","--json","--out-json","bench_smoke.json","--sketch-dtype","float32"])
    assert code == 0

def test_bench_reuse_precond_smoke():
    code = bench_main(["--n","1000","--d","60","--repeats","2","--sparse","--reuse-precond","--ascii"]) 
    assert code == 0



