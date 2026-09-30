"""Lab 01: beginner classification using synthetic IT service requests."""

from pathlib import Path

import pandas as pd
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text


DATA = Path(__file__).resolve().parents[1] / "datasets" / "service_requests.csv"


def main() -> None:
    print("=== LAB 01: MACHINE-LEARNING WORKFLOW ===")
    df = pd.read_csv(DATA)
    print("\n1) Raw synthetic examples")
    print(df.to_string(index=False))

    df["service_down"] = df["service_down"].map({"yes": 1, "no": 0})

    features = ["wait_minutes", "affected_users", "service_down"]
    X = df[features]
    y = df["priority"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.30, random_state=42, stratify=y
    )

    print(f"\n2) Train rows: {len(X_train)} | Test rows: {len(X_test)}")
    model = DecisionTreeClassifier(max_depth=2, random_state=42)
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    print("\n3) Confusion matrix")
    print(confusion_matrix(y_test, predictions))
    print("\n4) Classification report")
    print(classification_report(y_test, predictions, zero_division=0))

    print("\n5) A small view of the learned decision rules")
    print(export_text(model, feature_names=features))

    new_request = pd.DataFrame([
        {"wait_minutes": 35, "affected_users": 45, "service_down": 1}
    ])
    print("6) New synthetic service request")
    print(new_request.to_string(index=False))
    print("Prediction:", model.predict(new_request)[0])

    print("\nTEACHING CAUTION:")
    print("This tiny dataset demonstrates a workflow; it is not a production prioritisation system.")
    print("A real service desk needs policy, impact validation, monitoring and human override.")


if __name__ == "__main__":
    main()

