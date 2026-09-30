# Lab 05 — Tools and Agents

## Purpose

Distinguish ordinary text generation from a system that can select and call approved tools.

## Run

```bash
python scripts/agent_tool_call_demo.py
```

## Boundaries to observe

The demonstration separates:

1. interpreting a request;
2. choosing an allowed tool;
3. validating tool arguments;
4. executing the tool;
5. reading the result; and
6. requiring approval before a consequential action.

## Why controls matter

Incorrect text is harmful, but an incorrect action can change records, send messages, expose information or affect infrastructure. Useful controls include least privilege, allow-listed tools, schema validation, approval gates, timeouts, logging and safe failure behaviour.

## Experiment

Propose a new tool that changes a record. Write down the exact permissions, validation, evidence and human approval required before implementing it. Do not add a capstone-specific action.

