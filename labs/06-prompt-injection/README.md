# Lab 06 — Prompt Injection

## Purpose

Recognise that content retrieved from a document, website, email or user is data, not automatically trusted instruction.

## Exercise

Open `exercises/prompt_injection_fake_document.md` and inspect it as though an AI assistant retrieved it.

## Discuss

- Which instructions belong to the application developer?
- Which text comes from an untrusted source?
- What damage could occur if the assistant obeyed the document?
- Which permissions would reduce the impact?
- What evidence should be logged?

## Defensive principles

- separate trusted instructions from untrusted content;
- give tools the least privilege required;
- validate tool arguments and outputs;
- require approval for high-impact actions;
- prevent retrieved text from redefining identity or permissions;
- rerun known attack cases after changes; and
- retain enough trace information for investigation.

## Completion criterion

Explain why no prompt alone can replace identity, authorisation, validation and operational controls.

