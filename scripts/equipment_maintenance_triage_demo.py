"""Lab 09: guided equipment-maintenance triage and human escalation.

This fictional classroom example is deliberately unrelated to the assessed
bootcamp capstone projects. It demonstrates system boundaries, not a
production predictive-maintenance solution.
"""

from pathlib import Path

import pandas as pd


DATA = Path(__file__).resolve().parents[1] / "datasets" / "equipment_maintenance_sample.csv"


def triage(row) -> dict:
    """Return a transparent recommendation without authorising work."""

    observation = row.observation.lower()
    guidance = row.maintenance_guidance.lower()
    reasons: list[str] = []

    if "vibration" in observation and "inspect" in guidance:
        reasons.append("vibration requires technician inspection")
    if "temperature" in observation and "safe range" in guidance:
        reasons.append("temperature is outside the stated safe range")
    if "unknown" in observation or "missing" in observation:
        reasons.append("insufficient evidence")

    status = "inspection_required" if reasons else "monitor"

    return {
        "asset_id": row.asset_id,
        "status": status,
        "reasons": reasons,
        "guidance_basis": row.maintenance_guidance,
        "human_review_required": True,
    }


def main() -> None:
    print("=== LAB 09: GUIDED EQUIPMENT-MAINTENANCE CASE STUDY ===")
    df = pd.read_csv(DATA)

    required = {"asset_id", "observation", "maintenance_guidance"}
    missing = required.difference(df.columns)
    if missing:
        raise ValueError(f"Dataset is missing required columns: {sorted(missing)}")

    for row in df.itertuples(index=False):
        print("\nASSET:", row.asset_id)
        print("Observation:", row.observation)
        print("Guidance:", row.maintenance_guidance)
        print("Classroom triage:", triage(row))

    print("\nCONTROL: This script cannot authorise maintenance or equipment operation.")
    print("A qualified technician remains accountable for the operational decision.")


if __name__ == "__main__":
    main()

