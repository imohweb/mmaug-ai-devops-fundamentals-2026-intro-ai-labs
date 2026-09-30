# Lab 08 — Evaluation Datasets and Regression Tests

## Purpose

Use repeatable cases to detect whether a prompt, model, retrieval source, tool or policy change makes a system worse.

## Run

```bash
python scripts/evaluation_regression_tests.py
```

## Coverage to include

- normal requests;
- edge cases;
- ambiguous inputs;
- missing-context situations;
- restricted-data requests;
- security and prompt-injection cases; and
- failures previously observed in testing or production.

## Experiment

Change one expected answer or remove a required phrase. Run the evaluation again, observe the failure and decide whether the change is a genuine regression or whether the test needs revision.

## Interpretation

A passing automated check is evidence about the covered cases, not proof that the entire system is safe or accurate. Record dataset version, system version, scoring rule and known gaps.

