# Troubleshooting

## `python: command not found`
Try `python3` on macOS/Linux or `py` on Windows.

## `No module named pandas` / `sklearn`
Activate your virtual environment, then run:

```bash
pip install -r requirements.txt
```

## Wrong Python environment
Check:

```bash
python --version
python -m pip --version
```

The paths shown should point to the same environment.

## PowerShell blocks activation
You can use Command Prompt, another shell, or invoke the virtual environment's Python directly. If you change PowerShell execution policy, follow your organisation's security policy rather than weakening controls globally.

## Jupyter does not open
Run:

```bash
python -m jupyter lab
```

## A model score looks bad
That is expected. These datasets are intentionally tiny. The objective is to understand the workflow, not optimise the metric.

## `ValueError` during train/test split
Do not delete too many rows from a tiny dataset. Stratified splitting needs enough examples of each class.

## Still stuck?
Capture:

- your OS;
- `python --version`;
- `python -m pip --version`;
- the exact command; and
- the complete error text.
