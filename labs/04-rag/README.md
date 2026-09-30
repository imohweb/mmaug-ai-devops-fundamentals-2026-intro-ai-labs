# Lab 04 — Retrieval-Augmented Generation

## Purpose

Trace how retrieval can supply external evidence before an answer is created.

## Run

```bash
python scripts/simple_rag_demo.py
```

## Flow

```text
question -> retrieve evidence -> assemble context -> produce answer -> retain source trace
```

The classroom script does not call a large language model. This is intentional: it isolates retrieval, grounding and source handling.

## Why RAG is useful

A model may not know current or private organisational information. Retrieval allows an application to fetch approved material at request time.

## What RAG does not guarantee

- The wrong document may be retrieved.
- The correct document may be outdated.
- Access controls may be applied incorrectly.
- A generated answer may still misstate the evidence.
- Retrieved content may contain malicious instructions.

## Experiment

Ask a question not covered by the miniature knowledge base. Design the refusal or clarification behaviour you would expect from a dependable system.

## Assessment boundary

The knowledge base uses neutral examples and does not include official capstone requirements or solution guidance.

