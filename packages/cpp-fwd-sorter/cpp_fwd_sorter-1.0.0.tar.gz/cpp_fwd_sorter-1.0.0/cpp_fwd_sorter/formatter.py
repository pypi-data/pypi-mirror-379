#!/usr/bin/env python3
import os
import sys
import subprocess
import pathlib
import glob
import platform


def find_bundled_clang_format():
    home = pathlib.Path.home()
    base = home / ".vscode" / "extensions"
    exe = "clang-format.exe" if platform.system() == "Windows" else "clang-format"

    # Find cpptools extension dirs; sort so newest versions come first
    candidates = sorted(glob.glob(str(base / "ms-vscode.cpptools-*")), reverse=True)
    for cand in candidates:
        path = pathlib.Path(cand) / "LLVM" / "bin" / exe
        if path.exists():
            return str(path)
    return None


def main():
    clang_format = find_bundled_clang_format()
    if not clang_format:
        sys.stderr.write("Could not locate bundled clang-format\n")
        sys.exit(1)

    # Example call-through:
    ret = subprocess.run([clang_format, *sys.argv[1:]], stdout=subprocess.PIPE)

    script_path = os.path.dirname(os.path.abspath(__file__))
    ret = subprocess.run(
        [sys.executable, f"{script_path}/sorter.py", *sys.argv[1:]],
        input=ret.stdout,
        stdout=subprocess.PIPE,
    )

    sys.stdout.buffer.write(ret.stdout)
    sys.exit(ret.returncode)


if __name__ == "__main__":
    main()
