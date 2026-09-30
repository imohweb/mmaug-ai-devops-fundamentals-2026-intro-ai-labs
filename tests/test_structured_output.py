import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "structured_output_validation.py"
spec = importlib.util.spec_from_file_location("structured_output_validation", SCRIPT)
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(module)


def test_valid_output_passes():
    value = {
        "asset_id": "EQ-001",
        "status": "inspection_required",
        "confidence": 0.7,
        "human_review_required": True,
    }
    assert module.validate_triage_output(value) == []


def test_invalid_output_fails():
    value = {
        "asset_id": "EQ-001",
        "status": "operate",
        "confidence": 4,
        "human_review_required": "yes",
    }
    assert len(module.validate_triage_output(value)) >= 3
