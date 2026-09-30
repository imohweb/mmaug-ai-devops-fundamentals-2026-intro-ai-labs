import sys
from pathlib import Path


def main() -> None:
    print("MMAUG AI & DevOps Fundamentals Bootcamp 2026")
    print("Introduction to AI Concepts and Tools - environment check\n")
    print("Python:", sys.version.split()[0])

    required = ["pandas", "sklearn", "matplotlib"]
    failed = []
    for module in required:
        try:
            imported = __import__(module)
            version = getattr(imported, "__version__", "unknown")
            print(f"{module}: {version}")
        except Exception as exc:
            failed.append((module, str(exc)))

    root = Path(__file__).resolve().parents[1]
    required_files = [
        root / "datasets" / "service_requests.csv",
        root / "datasets" / "customer_activity.csv",
        root / "datasets" / "mini_knowledge_base.csv",
        root / "datasets" / "equipment_maintenance_sample.csv",
    ]
    for path in required_files:
        print(f"dataset {path.name}:", "OK" if path.exists() else "MISSING")
        if not path.exists():
            failed.append((path.name, "missing dataset"))

    if failed:
        print("\nEnvironment check failed:")
        for name, message in failed:
            print(f"- {name}: {message}")
        raise SystemExit(1)

    print("\nEnvironment check passed.")
    print("Next: python scripts/service_request_classifier_demo.py")


if __name__ == "__main__":
    main()
