# Model / Approach Selection Scenarios

For each scenario, first decide whether you need AI at all. Then choose the smallest suitable approach.

## Scenario A — Password expiry reminder
A company wants to email employees seven days before password expiry.

Questions:
- Does this require AI?
- Would a deterministic scheduled rule be better?

## Scenario B — Customer churn
A service has historical customer activity and known churn outcomes.

Questions:
- Is this classification or regression?
- What target would you predict?

## Scenario C — Policy question assistant
Employees need answers grounded in frequently updated internal policies.

Questions:
- Why might RAG be useful?
- What should happen when no relevant source is retrieved?

## Scenario D — Equipment inspection-note routing
A system can read a synthetic inspection note, retrieve approved maintenance guidance and draft a triage summary.

Questions:
- Which steps can be automated safely?
- Which operational decision should remain with a qualified technician?
- What evidence should be logged?
