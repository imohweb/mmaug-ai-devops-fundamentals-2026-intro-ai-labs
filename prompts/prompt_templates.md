# Prompt Templates for Classroom Exercises

These prompts are examples for learning structure. They are not a substitute for application controls.

## 1. Explain a concept to a beginner

```text
Role: You are a patient technical tutor.
Task: Explain <CONCEPT> to someone new to AI.
Constraints:
- Use plain English.
- Use one everyday analogy.
- Give one real-world example.
- State one limitation or risk.
- End with one check-for-understanding question.
```

## 2. Grounded-answer template

```text
Use only the supplied CONTEXT to answer the QUESTION.
If the context does not contain enough information, say that clearly.
Do not invent a policy, fact or citation.

CONTEXT:
<retrieved text>

QUESTION:
<user question>

Return:
1. Short answer
2. Source identifier
3. Any uncertainty
```

## 3. Structured equipment-triage template

```text
Review the synthetic equipment observation and maintenance guidance.
Do not authorise equipment operation or maintenance work.
Return JSON with exactly these fields:
- asset_id: string
- status: one of [monitor, inspection_required, more_information]
- reasons: array of strings
- guidance_basis: string
- human_review_required: boolean

If required context is missing, use status="more_information".
```

## 4. Safety challenge

```text
Before proposing an AI solution, answer:
- What is the user problem?
- What data is needed?
- What is the consequence of a wrong output?
- Can ordinary deterministic software solve it?
- What must a human approve?
- What evidence will prove the solution works?
```

## Prompting reminder
A stronger prompt can improve behaviour, but prompts are not security boundaries. Permissions, validation, isolation, approvals, monitoring and evaluation still matter.
