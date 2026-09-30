# Responsible AI Checklist for Beginner Projects

Use this before calling a prototype “ready”.

## Purpose
- Is the problem clearly defined?
- Do users understand what the system is for and what it is not for?
- Is AI actually needed?

## Data
- Is the data allowed to be used?
- Is sensitive data minimised?
- Are missing values, errors, bias and representativeness considered?
- Are training and evaluation data appropriately separated?

## Behaviour
- What are the most harmful plausible errors?
- Is uncertainty handled safely?
- Can the system refuse or escalate when context is insufficient?

## Security
- Are identities and permissions least-privilege?
- Are secrets kept out of prompts and source code?
- Is untrusted content treated as data rather than instruction?
- Are tool inputs and outputs validated?

## Human oversight
- What actions can happen automatically?
- What decisions need approval?
- Who is accountable when the system is wrong?

## Evaluation
- Are normal, edge, ambiguous and adversarial cases tested?
- Are regressions checked after changes?
- Is there an acceptance threshold appropriate to the use case?

## Operations
- Are logs and traces available?
- Are cost, latency, errors and drift monitored?
- Is there a fallback/rollback path?
- Is user feedback reviewed?
