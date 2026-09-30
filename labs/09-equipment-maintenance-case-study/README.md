# Lab 09 — Guided Equipment-Maintenance Case Study

## Why this scenario exists

This fictional example shows how input, operating guidance, deterministic checks, structured output and human escalation can be connected. Equipment maintenance was selected because it is **not one of the assessed bootcamp capstone projects**.

This is a guided teaching case, not a model answer for any final project.

## Run

```bash
python scripts/equipment_maintenance_triage_demo.py
```

## Dataset

`datasets/equipment_maintenance_sample.csv`

All records are synthetic. They describe fictional equipment observations and simplified maintenance guidance.

## System decomposition

| Stage | Classroom implementation |
|---|---|
| Intake | Read a short equipment observation. |
| Context | Read the associated maintenance guidance. |
| Deterministic check | Detect signals that require inspection. |
| Structured output | Return status, reasons and escalation flag. |
| Control | Prevent the script from authorising maintenance work. |
| Accountability | A qualified technician makes the operational decision. |

## What this lab intentionally does not provide

- predictive-maintenance model training;
- a production architecture;
- sensor integration;
- automated shutdown or work-order approval;
- an answer to any capstone brief.

## Reflection

1. Which fields should be validated before triage?
2. What evidence should be logged?
3. What should happen when guidance conflicts?
4. Which actions require a qualified human?
5. How would you test false reassurance and unnecessary escalation?

## Extension

Add a third synthetic asset with incomplete information. Make the safest outcome request more evidence instead of guessing.

