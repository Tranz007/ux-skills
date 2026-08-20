---
name: decision
description: Decide whether a consequential UX or architecture choice deserves a durable decision record and capture the context, evidence, options, decision, rationale, consequences, and status without documenting trivial design changes. Use for ADRs, design decision records, or important cross-team pattern choices.
license: MIT
metadata:
  author: Tranz007
  version: "0.1.0"
---

# Decision

Preserve consequential reasoning without creating documentation theater.

## Decide whether to record it

A durable record is useful when a choice:

- introduces or changes a shared interaction or system pattern;
- has meaningful accessibility, technical, policy, privacy, or operational consequences;
- rejects an obvious alternative for a non-obvious reason;
- affects multiple teams or journeys;
- is expensive to reverse;
- is likely to be questioned later.

Do not create a record for routine layout, copy, or styling decisions unless their consequences make them significant.

## Use the team's format

If the project has ADR, RFC, design-decision, or documentation conventions, follow them. Do not introduce a competing format unnecessarily.

If no convention exists, use a lightweight structure:

```text
Decision
Status
Context
Evidence
Options considered
Decision and rationale
Consequences
Open questions
Related artifacts
```

## Preserve evidence status

Document what was actually known at decision time. Do not rewrite history by converting assumptions into evidence after the decision is made.

Capture meaningful dissent or tradeoffs when they explain why the choice may need revisiting.

## Output

Create the record only when warranted. Otherwise explain briefly why normal design or PR documentation is sufficient.

## Examples

- "Does this deserve an ADR?"
- "Record why we extended the existing component instead of creating a new one."
- "Create a design decision record for this authentication pattern."
