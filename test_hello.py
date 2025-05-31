import subprocess, sys, pathlib

def test_prints_hello_world():
    """main.py must print 'Hello, World!' (case– and whitespace-exact)."""
    repo_root = pathlib.Path(__file__).resolve().parents[1]
    result = subprocess.run(
        [sys.executable, repo_root / "main.py"],
        capture_output=True, text=True
    )
    assert result.returncode == 0, "Program exited with an error"
    assert result.stdout.strip() == "Hello, World!"
