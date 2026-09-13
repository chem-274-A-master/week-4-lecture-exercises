"""Run each exercise's tests and publish a twelve-point grading summary."""

from __future__ import annotations

import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


EXERCISES = (
    (
        "Introspection01",
        (sys.executable, "-m", "pytest", "-q", "-k", "test_introspection01"),
    ),
    (
        "DataTypes01",
        (sys.executable, "-m", "pytest", "-q", "-k", "test_DataTypes01"),
    ),
    (
        "DataTypes02",
        (sys.executable, "-m", "pytest", "-q", "-k", "test_DataTypes02"),
    ),
    (
        "DataTypes03",
        (sys.executable, "-m", "pytest", "-q", "-k", "test_DataTypes03"),
    ),
    (
        "DataTypes04",
        (sys.executable, "-m", "pytest", "-q", "-k", "test_DataTypes04"),
    ),
    (
        "DataTypes05",
        (sys.executable, "-m", "pytest", "-q", "-k", "test_DataTypes05"),
    ),
    (
        "DataTypes06",
        (sys.executable, "-m", "pytest", "-q", "-k", "test_DataTypes06"),
    ),
    (
        "DataTypes07",
        (sys.executable, "-m", "pytest", "-q", "-k", "test_DataTypes07"),
    ),
    ("CommonTools01", ("bash", "tests/test_common_tools.sh", "CommonTools01")),
    ("CommonTools02", ("bash", "tests/test_common_tools.sh", "CommonTools02")),
    ("CommonTools03", ("bash", "tests/test_common_tools.sh", "CommonTools03")),
    ("CommonTools04", ("bash", "tests/test_common_tools.sh", "CommonTools04")),
)
TEST_TIMEOUT_SECONDS = 30
RESULTS_PATH = Path("grading-results.json")


def as_text(output: str | bytes | None) -> str:
    if isinstance(output, bytes):
        return output.decode(errors="replace")
    return output or ""


def run_exercise(name: str, command: tuple[str, ...]) -> dict[str, object]:
    print(f"::group::{name}")
    print("$", " ".join(command))
    try:
        completed = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=TEST_TIMEOUT_SECONDS,
            check=False,
        )
        output = completed.stdout + completed.stderr
        status = "pass" if completed.returncode == 0 else "fail"
        exit_code = completed.returncode
    except subprocess.TimeoutExpired as error:
        output = as_text(error.stdout) + as_text(error.stderr)
        output += f"\nTest exceeded {TEST_TIMEOUT_SECONDS} seconds.\n"
        status = "timeout"
        exit_code = None

    print(output.rstrip())
    print("::endgroup::")

    return {
        "name": name,
        "command": list(command),
        "status": status,
        "points": 1 if status == "pass" else 0,
        "max_points": 1,
        "exit_code": exit_code,
    }


def markdown_summary(results: list[dict[str, object]]) -> str:
    points = sum(int(result["points"]) for result in results)
    max_points = sum(int(result["max_points"]) for result in results)
    lines = [
        "## Autograding results",
        "",
        "| Exercise | Result | Points |",
        "| --- | --- | ---: |",
    ]

    symbols = {"pass": "✅ Pass", "fail": "❌ Fail", "timeout": "⏱️ Timeout"}
    for result in results:
        lines.append(
            f"| {result['name']} | {symbols[str(result['status'])]} "
            f"| {result['points']}/{result['max_points']} |"
        )

    lines.extend(("", f"**Total: {points}/{max_points} points**", ""))
    return "\n".join(lines)


def main() -> int:
    results = [run_exercise(name, command) for name, command in EXERCISES]
    points = sum(int(result["points"]) for result in results)
    max_points = sum(int(result["max_points"]) for result in results)

    report = {
        "repository": os.environ.get("GITHUB_REPOSITORY"),
        "commit": os.environ.get("GITHUB_SHA"),
        "run_id": os.environ.get("GITHUB_RUN_ID"),
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "points": points,
        "max_points": max_points,
        "tests": results,
    }
    RESULTS_PATH.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")

    summary = markdown_summary(results)
    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary_path:
        with Path(summary_path).open("a", encoding="utf-8") as summary_file:
            summary_file.write(summary)
    print("\n" + summary)
    print(f"::notice title=Autograding complete::Points {points}/{max_points}")

    return 0 if points == max_points else 1


if __name__ == "__main__":
    raise SystemExit(main())
