# Lab 07 — Structured Output and Validation

## Purpose

Validate model-shaped data before another software component consumes it.

## Run

```bash
python scripts/structured_output_validation.py
```

## What is checked

- required fields;
- allowed status values;
- confidence type and range; and
- whether escalation is a Boolean value.

## Essential distinction

**Schema-valid does not mean factually correct.** Valid JSON can still contain the wrong entity, total, source or conclusion. Applications need content validation, business rules and human review where consequences are significant.

## Experiment

Add a required `guidance_source_id` field. Update one example so it passes and leave another invalid. Explain why failing closed is safer than silently inventing the missing field.

## Completion criterion

Describe which checks belong to schema validation and which require domain evidence.
