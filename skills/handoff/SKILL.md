---
name: handoff
description: Turn approved UX work into an engineering-readable handoff that preserves user intent, behavior, states, design-system usage, accessibility requirements, dependencies, and unresolved questions. Use when a designer needs to hand work to engineering without relying on screenshots or Figma links alone.
license: MIT
metadata:
  author: Tranz007
  version: "0.1.0"
---

# Handoff

Transfer design intent, not just appearance.

## Gather the source of truth

Inspect the approved design, relevant flow and state decisions, design-system components, content, accessibility requirements, known constraints, decision records, and current implementation context.

Do not describe proposed behavior as approved if its status is unclear.

## Explain what engineering needs

Prioritize:

- user goal and outcome;
- entry conditions and primary behavior;
- meaningful branches and recovery;
- component and pattern usage;
- states and data conditions;
- responsive behavior when relevant;
- content rules and terminology;
- accessibility behavior such as focus, announcements, semantics, and keyboard interaction when established;
- dependencies and known technical constraints;
- analytics or instrumentation requirements when documented;
- unresolved questions that could change implementation.

Avoid pixel-by-pixel prose that duplicates the design artifact.

## Point to authoritative sources

Link or reference the actual design, component, decision, requirement, and research sources when available. Name which source wins if there are conflicts.

## Check completeness

Before finalizing, look for missing states, ambiguous transitions, unsupported new components, and decisions that engineering would otherwise have to guess.

## Output

Create a handoff an engineer can review quickly. Put unresolved decisions near the relevant behavior instead of hiding them at the bottom.

## Examples

- "Get this ready to hand to engineering."
- "Turn this approved flow into an implementation handoff."
- "Engineering shouldn't have to guess what happens here."
