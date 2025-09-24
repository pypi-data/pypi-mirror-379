from pathlib import Path
import sys
import argparse
import subprocess
from typing import Any

try:
    from tomllib import load as load_toml  # type: ignore
except ImportError:
    from tomli import load as load_toml  # type: ignore


def find_pyproject() -> Path:
    current_dir = Path.cwd()
    for path in [current_dir] + list(current_dir.parents):
        pyproject_path = path / "pyproject.toml"
        if pyproject_path.exists():
            return pyproject_path
    print("pyproject.toml not found")
    sys.exit(1)


def load_jobs(pyproject_path: Path) -> dict[str, str]:
    with pyproject_path.open("rb") as f:
        data: dict[str, Any] = load_toml(f)
    jobs = data.get("tool", {}).get("jobs", {})
    return jobs


def main(argv=None) -> None:
    parser = argparse.ArgumentParser(description="Run jobs from pyproject.toml")
    parser.add_argument("job", help="The job name to run")
    args = parser.parse_args(argv)

    pyproject_path = find_pyproject()
    jobs = load_jobs(pyproject_path)

    if args.job not in jobs:
        print(f"Job '{args.job}' not found in [tool.jobs] section of {pyproject_path}")
        sys.exit(1)

    subprocess.run(jobs[args.job], shell=True)


if __name__ == "__main__":
    main()
