# Lab 01 — Machine-Learning Workflow

## Purpose

Understand machine learning as a repeatable engineering workflow rather than magic.

## Scenario

A tiny synthetic IT service-request dataset is used to demonstrate binary classification. The scenario is a compact way to teach features, labels and evaluation and is unrelated to the assessed capstone projects.

## Dataset

`datasets/service_requests.csv`

The target column is `priority`, with the classroom values `urgent` and `routine`.

## Run

```bash
python scripts/service_request_classifier_demo.py
```

## Observe

1. Inspect the rows and column meanings.
2. Convert yes/no values into numeric features.
3. Separate training and test examples.
4. Fit a deliberately small decision tree.
5. Predict held-out examples.
6. Inspect the confusion matrix and classification report.
7. Send one new synthetic service request through the model.

## Vocabulary

- **Feature:** input used by a model.
- **Target:** value the model learns to predict.
- **Training:** fitting model parameters from examples.
- **Inference:** applying the fitted model to new input.
- **Evaluation:** testing behaviour on examples not used for fitting.

## Experiment

Change the affected-user count in the new request. Record whether the prediction changes and explain why a small decision tree may react strongly.

## Limitations

The dataset is too small and simplified for real service prioritisation. A production system needs representative data, policy rules, leakage checks, calibration, monitoring, override paths and accountable human review.
