# Lab 00 — Environment Setup

## Purpose

Confirm that Python, the required packages and the synthetic datasets are available before running the technical demonstrations.

## Run

From the repository root:

```bash
python scripts/environment_check.py
```

## Expected result

The script prints the Python, pandas, scikit-learn and matplotlib versions, checks each required dataset and ends with:

```text
Environment check passed.
```

## If it fails

1. Confirm that your virtual environment is active.
2. Run `pip install -r requirements.txt` again.
3. Make sure you are running the command from the repository root.
4. Read `docs/troubleshooting.md`.

## Check your understanding

- Why isolate packages in a virtual environment?
- What is the difference between Python and a Python package?
- Why must secrets never be committed to source control?

## Capstone boundary

This setup supports the introductory labs only. It does not install or reveal an implementation for any assessed capstone project.

