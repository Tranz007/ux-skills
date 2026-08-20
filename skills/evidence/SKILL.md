---
name: evidence
description: Separate UX evidence from inference, assumption, unknowns, and conflicts, and trace what supports a design or product claim. Use when a designer asks what is actually known, whether a requirement is evidence-based, what research supports a decision, or where validation is still needed.
license: MIT
metadata:
  author: Tranz007
  version: "0.1.0"
---

# Evidence

Keep confidence attached to what the team actually knows.

## Inspect available sources

Look for relevant research, analytics, support data, usability findings, requirements, prior decisions, product documentation, implementation behavior, and `.ux/` context.

Treat source authority separately from source existence. A repeated assumption in three documents is still an assumption if none of them provides evidence.

## Classify only when useful

Use:

- **Known** — supported by evidence or an authoritative source;
- **Inferred** — strongly suggested by available information;
- **Assumed** — treated as true without enough evidence;
- **Unknown** — not enough information;
- **Conflicted** — credible sources disagree.

Do not label every sentence. Apply the model to claims that affect a decision.

## Trace important claims

For each consequential claim, identify what supports it and how strong that support is. If the user asks whether something is a requirement, distinguish business mandate, technical constraint, policy, observed user need, and design convention.

## Expose the gap

When evidence is missing, recommend the smallest useful way to reduce uncertainty. That may be observing behavior, checking analytics, reviewing support contacts, talking to users, validating with engineering, or simply documenting an intentional assumption.

Do not prescribe research theater when the decision is low-risk and reversible.

## Guardrails

Never synthesize fake user quotes, sample sizes, metrics, or research findings. Never turn an inference into a known fact because it sounds plausible.

## Examples

- "What do we actually know here?"
- "Is this requirement evidence-based?"
- "Show me which parts of this design rationale are assumptions."
- "What evidence would change this decision?"
