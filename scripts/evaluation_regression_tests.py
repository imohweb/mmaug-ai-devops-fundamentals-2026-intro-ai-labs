"""Lab 08: tiny deterministic evaluation cases for a classroom AI workflow."""

TEST_CASES = [
    {
        "name": "requires_source",
        "answer": "According to KB003, abnormal equipment readings require technician review.",
        "must_include": "KB003",
    },
    {
        "name": "refuses_no_context",
        "answer": "I do not have enough source material to answer that safely.",
        "must_include": "not have enough",
    },
    {
        "name": "structured_equipment_triage",
        "answer": '{"asset_id":"EQ-001","status":"inspection_required"}',
        "must_include": "asset_id",
    },
]


def run_evaluations() -> list[str]:
    failures: list[str] = []
    for case in TEST_CASES:
        passed = case["must_include"].lower() in case["answer"].lower()
        if not passed:
            failures.append(case["name"])
        print(f"{case['name']}: {'PASS' if passed else 'FAIL'}")
    return failures


def main() -> None:
    print("=== LAB 08: EVALUATION AND REGRESSION TESTS ===")
    failures = run_evaluations()
    if failures:
        raise SystemExit(f"Regression tests failed: {failures}")
    print("All classroom regression tests passed.")
    print("\nEXTENSION: change one expected phrase or answer and observe how a regression test catches the change.")


if __name__ == "__main__":
    main()
