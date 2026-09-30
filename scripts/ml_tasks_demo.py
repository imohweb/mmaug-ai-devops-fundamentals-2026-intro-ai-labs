from pathlib import Path
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.cluster import KMeans
from sklearn.metrics import classification_report, confusion_matrix, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

DATA = Path(__file__).resolve().parents[1] / "datasets" / "customer_activity.csv"
df = pd.read_csv(DATA)
print("=== LAB 02: CLASSIFICATION, REGRESSION AND CLUSTERING ===")
print("Raw data shape:", df.shape)
print("Missing values before cleaning:\n", df.isna().sum())
print("Duplicate rows:", df.duplicated().sum())

# Clean data for classroom use.
df.columns = df.columns.str.strip().str.lower()
for col in ["opened_email", "churned", "city"]:
    df[col] = df[col].astype("string").str.strip().str.lower()
df = df.drop_duplicates().copy()
for col in ["age", "monthly_spend", "visits_30d", "delivery_minutes"]:
    df[col] = pd.to_numeric(df[col], errors="coerce")
df.loc[df["monthly_spend"] < 0, "monthly_spend"] = pd.NA
yes_no = {"yes": 1, "no": 0}
df["opened_email"] = df["opened_email"].map(yes_no)
df["churned"] = df["churned"].map(yes_no)

# Classification: churn yes/no.
features = ["age", "monthly_spend", "visits_30d", "opened_email", "city"]
X = df[features]
y = df["churned"]
preprocess = ColumnTransformer([
    ("num", Pipeline([("imputer", SimpleImputer(strategy="median")), ("scale", StandardScaler())]), ["age", "monthly_spend", "visits_30d", "opened_email"]),
    ("cat", OneHotEncoder(handle_unknown="ignore"), ["city"]),
])
classifier = Pipeline([("prepare", preprocess), ("model", LogisticRegression(max_iter=1000))])
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42, stratify=y)
classifier.fit(X_train, y_train)
print("\nCLASSIFICATION: Will customer churn?")
print(confusion_matrix(y_test, classifier.predict(X_test)))
print(classification_report(y_test, classifier.predict(X_test), zero_division=0))

# Regression: delivery minutes.
X = df[["age", "monthly_spend", "visits_30d", "opened_email"]]
y = df["delivery_minutes"]
regressor = Pipeline([
    ("impute", SimpleImputer(strategy="median")),
    ("scale", StandardScaler()),
    ("model", RandomForestRegressor(n_estimators=100, random_state=42)),
])
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
regressor.fit(X_train, y_train)
pred = regressor.predict(X_test)
print("\nREGRESSION: How many delivery minutes?")
print("MAE:", round(mean_absolute_error(y_test, pred), 2))
print("R²:", round(r2_score(y_test, pred), 2))
print(pd.DataFrame({"actual_minutes": y_test, "predicted_minutes": pred.round(1)}))

# Clustering: customer segments.
cluster_pipeline = Pipeline([
    ("impute", SimpleImputer(strategy="median")),
    ("scale", StandardScaler()),
    ("model", KMeans(n_clusters=3, random_state=42, n_init="auto")),
])
cluster_features = df[["age", "monthly_spend", "visits_30d", "opened_email"]]
df["cluster"] = cluster_pipeline.fit_predict(cluster_features)
print("\nCLUSTERING: Which customers look similar?")
print(df[["customer_id", "age", "monthly_spend", "visits_30d", "cluster"]].sort_values("cluster"))

print("\nTEACHING CAUTION: This tiny dataset demonstrates task types and workflow, not production model quality.")
