# MMAUG AI & DevOps Fundamentals Bootcamp 2026
## Introduction to AI Concepts and Tools — Participant Labs

> **Learn. Innovate. Build.**

This repository is the hands-on companion to MMAUG's **Introduction to AI Concepts and Tools** session. It contains small, runnable exercises for beginners who want to see how data, models, retrieval, tools, evaluation and human controls fit together.

## Important boundary: these are teaching examples, not capstone solutions

The repository deliberately uses **fictional scenarios that are separate from the assessed bootcamp capstone projects**. No lab provides an implementation, architecture or recommended answer for a capstone brief. Participants must interpret the official capstone requirements and design their own solution.

The guided equipment-maintenance example in Lab 09 demonstrates how previously taught components can be combined. It is not an assessed project and should not be copied as a capstone answer.

## Learning outcomes

After completing the labs, you should be able to:

- inspect and clean a small dataset before modelling;
- distinguish classification, regression and clustering;
- separate training, inference and evaluation;
- explain embeddings and similarity-based retrieval;
- trace a simple Retrieval-Augmented Generation workflow;
- distinguish a model response from a tool call or agent action;
- identify prompt-injection risk;
- validate structured output before software consumes it;
- use repeatable evaluation cases to detect regressions;
- assemble a guided, non-capstone decision-support example; and
- create an independent one-page AI solution design without receiving a model answer.

## Repository map

```text
datasets/       Small synthetic classroom data
docs/           Glossary, safety guidance and references
exercises/      Discussion and threat-modelling activities
labs/           Numbered participant instructions
notebooks/      Interactive alternatives where available
prompts/        Reusable prompt patterns
scripts/        Runnable Python demonstrations
templates/      Blank design artefacts
tests/          Repository checks
```

## Setup

### macOS or Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python scripts/environment_check.py
```

### Windows PowerShell

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python scripts/environment_check.py
```

Continue with [START_HERE.md](START_HERE.md) and [LAB_GUIDE.md](LAB_GUIDE.md).

## Recommended order

| Lab | Topic | Approx. time |
|---|---|---:|
| 00 | Environment setup | 10 min |
| 01 | Machine-learning workflow using service requests | 15 min |
| 02 | Classification, regression and clustering | 25 min |
| 03 | Embeddings and vector similarity | 15 min |
| 04 | Simple RAG | 20 min |
| 05 | Tools and agents | 15 min |
| 06 | Prompt injection | 15 min |
| 07 | Structured output | 15 min |
| 08 | Evaluation and regression tests | 15 min |
| 09 | Guided equipment-maintenance case study | 25 min |
| 10 | Independent solution-design practice | 20 min |

## Classroom safety rules

- Use only the bundled synthetic data.
- Never paste credentials or real personal, financial, employment, health or customer data into the exercises.
- Do not treat toy-model metrics as production evidence.
- Do not automate consequential decisions using these scripts.
- Keep human accountability, security, privacy and rollback visible in every design.

## Community

- [MMAUG website](https://mmaug.com/)
- [MMAUG Meetup](https://www.meetup.com/malta-microsoft-ai-user-group/)
- [Bootcamp page](https://mmaug.com/bootcamp)

## Licence

Code and original educational material are provided under the [MIT License](LICENSE), unless a file states otherwise. Third-party resources remain subject to their own licences and terms.

---

**MMAUG — A Global Community for AI, Cloud, Infra, DevOps and Tech Enthusiasts**
