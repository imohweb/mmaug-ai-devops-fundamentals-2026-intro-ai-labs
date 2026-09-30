# Lab 02 — Classification, Regression and Clustering

## Purpose

Identify the question a model is being asked to answer and prepare the data before selecting an algorithm.

- **Classification:** which defined category?
- **Regression:** what continuous numeric value?
- **Clustering:** which records are similar when labels are not supplied?

## Dataset

`datasets/customer_activity.csv`

The file deliberately contains missing values, inconsistent capitalisation, a duplicate, invalid numeric text and an impossible negative value.

## Run

```bash
python scripts/ml_tasks_demo.py
```

## Workflow

1. Inspect shape, types, missing values and duplicates.
2. Standardise text categories.
3. Convert numeric columns safely.
4. handle invalid or missing values using an explained rule.
5. Train a classification baseline.
6. Train a regression baseline.
7. Scale selected features and form clusters.
8. Interpret results without treating the toy metrics as production evidence.

## Reflection

- Why is churn a classification target?
- Why are delivery minutes a regression target?
- Why does clustering not need a target label?
- What could leak the answer in a real churn dataset?
- Why can accuracy be misleading when one class is rare?

## Extension

Try two and four clusters. Compare the cluster summaries and explain which grouping is easier to interpret. Do not claim that a visually neat cluster is automatically fair or useful.

