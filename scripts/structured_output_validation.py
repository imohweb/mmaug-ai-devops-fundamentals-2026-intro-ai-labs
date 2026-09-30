"""Lab 07: validate machine-readable AI output before downstream use."""

import json

REQUIRED_FIELDS = {"asset_id", "status", "confidence", "human_review_required"}
ALLOWED_STATUSES = {"monitor", "inspection_required", "more_information"}


def validate_triage_output(obj: dict) -> list[str]:
    errors: list[str] = []
    missing = REQUIRED_FIELDS - set(obj)
    if missing:
        errors.append(f"Missing fields: {sorted(missing)}")

    if obj.get("status") not in ALLOWED_STATUSES:
        errors.append("Status must be one of: " + ", ".join(sorted(ALLOWED_STATUSES)))

    confidence = obj.get("confidence")
    if not isinstance(confidence, (int, float)) or isinstance(confidence, bool) or not 0 <= confidence <= 1:
        errors.append("Confidence must be a number between 0 and 1")

    if not isinstance(obj.get("human_review_required"), bool):
        errors.append("human_review_required must be true or false")

    return errors


def main() -> None:
    print("=== LAB 07: STRUCTURED OUTPUT VALIDATION ===")
    examples = [
        '{"asset_id":"EQ-001","status":"inspection_required","confidence":0.71,"human_review_required":true}',
        '{"asset_id":"EQ-002","status":"operate","confidence":2.4}',
    ]

    for raw in examples:
        data = json.loads(raw)
        errors = validate_triage_output(data)
        print("\nOutput:", data)
        print("VALID" if not errors else "INVALID: " + "; ".join(errors))

    print("\nREMEMBER: Correct JSON structure does not prove that the facts inside it are correct.")


if __name__ == "__main__":
    main()
