---
name: why
description: Reconstruct why an existing experience, component, flow, or implementation appears to have been designed a particular way by tracing decisions, research, system constraints, history, and code. Use when a designer asks "why is it like this?" or needs to separate intentional rationale from accidental design debt.
license: MIT
metadata:
  author: Tranz007
  version: "0.1.0"
---

# Why

Recover rationale without inventing a story after the fact.

## Search for evidence of intent

Inspect relevant decision records, research, requirements, issue and PR history, design-system documentation, implementation history, comments, tests, and `.ux/` context.

Current behavior proves what exists, not why it was chosen.

## Reconstruct cautiously

Separate:

- documented rationale;
- rationale strongly supported by artifacts;
- plausible inference;
- missing rationale;
- evidence that the current behavior is accidental, obsolete, or inconsistent.

If multiple sources disagree, preserve the conflict.

## Expose design debt

A missing rationale is useful information. Call out important decisions that appear to have no recoverable evidence, especially when teams are treating them as immutable constraints.

Do not label something design debt merely because you personally prefer another pattern.

## Output

Answer the user's "why" directly. Cite or point to the source artifacts when available. Finish with what is safe to change versus what requires human confirmation only if that distinction matters.

## Examples

- "Why is this designed this way?"
- "Is there a reason free-form date entry is disabled?"
- "Which parts of this flow are intentional and which look inherited?"
