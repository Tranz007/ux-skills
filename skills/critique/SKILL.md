---
name: critique
description: Critique a UX design, flow, prototype, specification, or implemented experience across user goals, evidence, interaction, accessibility, design-system fit, content, and engineering consequences. Use when a designer asks for a review, design critique, tough feedback, or wants to know what should change before approval.
license: MIT
metadata:
  author: Tranz007
  version: "0.1.0"
---

# Critique

Review the work against its context and intent rather than personal taste.

## Establish the basis

Inspect the artifact plus relevant `.ux/` context, evidence, design-system patterns, accessibility rules, known constraints, and prior decisions. If the goal is unclear, infer cautiously from available context or ask only if the critique would otherwise be misleading.

## Review through relevant lenses

Use only lenses that matter to this work:

- user goal and task clarity;
- evidence and unsupported assumptions;
- information hierarchy and cognitive effort;
- interaction behavior and recoverability;
- state completeness;
- content and terminology;
- accessibility and inclusive use;
- consistency and design-system fit;
- engineering or service dependencies;
- trust, privacy, or consequence where relevant.

## Prioritize findings

Separate:

- issues likely to cause failure, exclusion, loss, or misunderstanding;
- issues that materially weaken the experience;
- polish that can wait.

Do not create severity labels unless they help the user decide what to address.

## Be specific

Point to the behavior or element, explain why it matters, and recommend a direction. Avoid vague comments such as "improve hierarchy" without saying what is wrong.

When the design is strong, spend fewer words validating it. Focus attention where change is useful.

## Guardrails

Do not claim accessibility compliance from visual inspection. Do not invent research findings. Do not prefer novelty over an established system pattern without evidence.

## Examples

- "Review this before I show engineering."
- "Give me a tough critique."
- "What's wrong with this flow?"
