import sys
import subprocess
from pathlib import Path


def test_importable():
    import cpp_fwd_sorter  # noqa: F401


def test_sorter_cli_echo(tmp_path):
    # Write a small input file
    p = tmp_path / "in.cpp"
    p.write_text("class Z;\nclass A;\n")

    # Run the module as a script
    res = subprocess.run(
        [sys.executable, "-m", "cpp_fwd_sorter.sorter"],
        input=p.read_bytes(),
        stdout=subprocess.PIPE,
        check=True,
    )
    assert b"class Z;" in res.stdout
