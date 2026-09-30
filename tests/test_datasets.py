from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]


def test_required_datasets_exist():
    for filename in [
        "service_requests.csv",
        "customer_activity.csv",
        "mini_knowledge_base.csv",
        "equipment_maintenance_sample.csv",
    ]:
        assert (ROOT / "datasets" / filename).exists()


def test_service_requests_have_expected_columns():
    df = pd.read_csv(ROOT / "datasets" / "service_requests.csv")
    assert {"request_id", "wait_minutes", "affected_users", "service_down", "priority"}.issubset(df.columns)
    assert set(df["priority"]) == {"urgent", "routine"}
