---
name: blindspots
description: Find important users, contexts, constraints, dependencies, consequences, and conditions that a design discussion has not considered at all. Use when a designer asks "what am I missing?", wants edge perspectives beyond UI states, or needs a pre-review scan for overlooked experience risks.
license: MIT
metadata:
  author: Tranz007
  version: "0.1.0"
---

# Blindspots

Look outside the frame the team is already using.

## Inspect first

Understand the current problem, intended users, evidence, system, and proposed direction. Do not produce a generic accessibility-and-edge-cases checklist detached from the product.

## Search for omitted dimensions

Consider only dimensions relevant to the work, including:

- people with different abilities, familiarity, language, age, roles, permissions, or support needs;
- real-world context such as interruption, urgency, shared devices, travel, connectivity, time zones, or environmental constraints;
- policy, privacy, trust, consent, safety, or financial consequences;
- upstream and downstream services;
- multi-user or organizational behavior;
- lifecycle effects after the happy path ends;
- unusual but plausible data, inventory, account, or entitlement conditions;
- support and recovery burden;
- conflicts with established product or design-system conventions.

## Prioritize

Do not dump every imaginable edge case. Rank blind spots by likelihood, consequence, and cost of discovering them late.

Separate a true blind spot from a state already handled in the design.

## Output

Lead with the few omissions most likely to change the design. Explain why each matters and what would resolve it.

## Guardrails

Do not invent vulnerable populations, regulations, or product requirements. Raise them as questions when context does not establish them.

## Examples

- "What are we not thinking about?"
- "Blindspots on this booking flow?"
- "Who or what does this design accidentally ignore?"
