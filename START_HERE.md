# Start Here

Use this page if Python, GitHub or machine learning is new to you.

## 1. Understand what this repository is

These are guided introductory exercises. They are **not solutions to the bootcamp capstone projects**. The scenarios are synthetic and intentionally small so that you can inspect every step.

## 2. Prerequisites

- Python 3.10 or later
- A code editor such as Visual Studio Code
- Internet access for the initial package installation
- Git, or the repository downloaded as a ZIP file

No cloud subscription, API key or GPU is required.

## 3. Create a virtual environment

### macOS or Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Windows PowerShell

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

## 4. Install and verify

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
python scripts/environment_check.py
```

The final line should say `Environment check passed`.

## 5. Begin with Lab 01

```bash
python scripts/service_request_classifier_demo.py
```

Synthetic service-request prioritisation is used as a compact supervised-learning example. It is unrelated to the assessed capstone projects and is not a production service-desk policy.

Focus on the workflow:

```text
inspect data -> define features and target -> split -> train -> predict -> evaluate
```

## 6. Recommended learning routine

For each lab:

1. Read its README before running code.
2. Inspect the dataset or input.
3. Predict the output.
4. Run the script.
5. Explain the result in your own words.
6. Change one safe parameter.
7. Run it again and compare.
8. Answer the reflection questions.

## 7. Troubleshooting

See [docs/troubleshooting.md](docs/troubleshooting.md). When asking for help, include your operating system, Python version, command and complete error message. Never share passwords or API keys.
