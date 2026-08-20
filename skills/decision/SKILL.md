---
name: decision
description: Recover or preserve consequential UX and architecture rationale. Use when a designer asks why something was designed a certain way, whether a choice deserves an ADR/design decision record, or wants to capture context, evidence, alternatives, rationale, consequences, and status without documenting trivial changes.
license: MIT
metadata:
  author: Tranz007
  version: "0.1.2"
---

# Decision

Help future designers and engineers understand **why**, without creating documentation theater.

## Always

- **Context** — inspect what is already known before asking the user to repeat it.
- **Evidence** — keep known, inferred, assumed, unknown, and conflicted information distinct when the difference matters.
- **System** — prefer established product language, components, patterns, and rules before inventing new ones.
- **Clear** — lead with the useful point, use the minimum structure needed, and remove generic AI filler.
- **Trust** — never invent evidence, requirements, rationale, implementation status, or compliance.

Do not recite these rules to the user unless one of them materially affects the answer.

## When the user asks why

Search available decision records, research, requirements, issue/PR history, design-system documentation, implementation history, and `.ux/` context.

Separate:

- documented rationale;
- rationale strongly supported by artifacts;
- plausible inference;
- missing or conflicting rationale.

Current behavior proves what exists, not why it was chosen. Never invent a neat historical explanation just because one sounds plausible.

## When a new decision is being made

A durable record is useful when a choice:

- introduces or changes a shared interaction or system pattern;
- has meaningful accessibility, technical, policy, privacy, or operational consequences;
- rejects an obvious alternative for a non-obvious reason;
- affects multiple teams or journeys;
- is expensive to reverse;
- is likely to be questioned later.

Routine layout, copy, and styling changes usually do not need a decision record.

## Use the team's system

If the project has ADR, RFC, design-decision, or documentation conventions, use them. Do not introduce a competing format.

If none exists, keep it lightweight:

```text
Decision
Status
Context and evidence
Options considered
Decision and rationale
Consequences
Open questions
Related artifacts
```

Preserve what was actually known at decision time. Do not rewrite assumptions as evidence after the fact.

## Output

Answer a "why" question directly when that is all the user needs. Create or recommend a durable record only when the decision is consequential enough to justify it.

## Contrast example

Bad:
> Create an ADR documenting why the primary button was moved below the form.

Good:
> This does not need a durable decision record. It is a local layout change with no shared pattern, architectural consequence, or non-obvious tradeoff. The design or PR history is enough.

Why: the good response preserves decision records for choices future teams are likely to question or need to understand.

## Examples

- "Why was this designed this way?"
- "Does this deserve an ADR?"
- "Record why we extended the existing component instead of creating a new one."
