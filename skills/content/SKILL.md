---
name: content
description: Review and improve product UX content including labels, instructions, errors, empty states, confirmations, terminology, and content timing. Use when a designer asks whether UI copy is clear, consistent, accessible, actionable, appropriately human, or aligned with the product glossary and context.
license: MIT
metadata:
  author: Tranz007
  version: "0.1.0"
---

# Content

Treat words as part of the interaction, not decoration added after the design.

## Start with context

Read the relevant user goal, flow, glossary, voice guidance, design-system content patterns, localization constraints, and known accessibility requirements.

## Review the job the content must do

Check for:

- clear action and outcome;
- terminology consistency;
- information shown at the moment it is needed;
- unnecessary instructions the interface could make obvious instead;
- labels that describe destinations or actions accurately;
- error language that explains what happened and how to recover;
- confirmation language proportional to consequence;
- technical or organizational jargon exposed to users;
- blame, ambiguity, coercion, or false reassurance;
- strings likely to fail with translation, expansion, dynamic values, or assistive technology.

## Prefer the product language

Use the established glossary and existing patterns unless there is a reason to challenge them. If terminology is inconsistent across authoritative sources, flag the conflict instead of choosing silently.

## Rewrite carefully

Preserve factual meaning, legal requirements, and uncertainty. Do not make a message friendlier by making it less precise.

For high-consequence actions, clarity wins over personality.

## Output

Lead with the content problems that change comprehension or behavior. Provide revised strings when the user wants actionable copy, and explain only the decisions that are not obvious.

## Examples

- "Review the copy in this recovery flow."
- "Are these error messages actually useful?"
- "Make this UI content clearer without making it sound like AI."
