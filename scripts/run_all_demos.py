"""Convenience runner used by participants and CI to verify every core demo."""

from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
DEMOS = [
    "environment_check.py",
    "service_request_classifier_demo.py",
    "ml_tasks_demo.py",
    "embeddings_tfidf_demo.py",
    "simple_rag_demo.py",
    "agent_tool_call_demo.py",
    "structured_output_validation.py",
    "evaluation_regression_tests.py",
    "equipment_maintenance_triage_demo.py",
]


def main() -> None:
    failures = []
    for demo in DEMOS:
        print("\n" + "=" * 78)
        print("RUNNING", demo)
        print("=" * 78)
        result = subprocess.run([sys.executable, str(ROOT / "scripts" / demo)], cwd=ROOT)
        if result.returncode != 0:
            failures.append(demo)

    if failures:
        raise SystemExit(f"Failed demos: {failures}")
    print("\nAll core demos completed successfully.")


if __name__ == "__main__":
    main()
