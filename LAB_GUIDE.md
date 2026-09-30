# Participant Lab Guide

The labs follow the conceptual progression of **Introduction to AI Concepts and Tools**. Labs 00–08 teach individual concepts. Lab 09 combines those concepts in a fictional guided example. Lab 10 asks you to design a different solution independently.

> The guided examples are not capstone solutions. The assessed projects use separate requirements and must be completed independently.

## Lab path

| Lab | Goal | Run or open |
|---|---|---|
| 00 — Setup | Verify Python, packages and datasets. | `python scripts/environment_check.py` |
| 01 — ML workflow | See examples, features, labels, training, inference and evaluation. | `python scripts/service_request_classifier_demo.py` |
| 02 — Learning tasks | Compare classification, regression and clustering after cleaning data. | `python scripts/ml_tasks_demo.py` |
| 03 — Embeddings | Represent text numerically and rank similar items. | `python scripts/embeddings_tfidf_demo.py` |
| 04 — RAG | Trace question, retrieval, context and grounded response. | `python scripts/simple_rag_demo.py` |
| 05 — Tools and agents | Separate deciding, calling a tool, validating and approving. | `python scripts/agent_tool_call_demo.py` |
| 06 — Prompt injection | Identify untrusted instructions inside retrieved content. | `exercises/prompt_injection_fake_document.md` |
| 07 — Structured output | Validate types and allowed values before using output. | `python scripts/structured_output_validation.py` |
| 08 — Evaluation | Rerun representative cases after a system change. | `python scripts/evaluation_regression_tests.py` |
| 09 — Guided case study | Combine input, guidance, structured triage and human review using fictional equipment maintenance. | `python scripts/equipment_maintenance_triage_demo.py` |
| 10 — Independent design | Complete a blank one-page design using a neutral practice scenario or your own non-capstone idea. | `templates/ai_solution_one_page_brief.md` |

## How Lab 09 differs from a capstone

Lab 09 is fully guided and deliberately narrow. Its purpose is to show component boundaries and control points. A capstone requires broader independent problem interpretation, architecture choices, implementation decisions, testing evidence and justification.

## Self-study checklist

For every lab, record:

- the problem being addressed;
- the input and expected output;
- what is learned versus explicitly programmed;
- how success is evaluated;
- what can fail;
- what a human must review; and
- what would need to change before production use.
