---
name: system-fit
description: Decide whether a UX need should reuse, compose, extend, or create a design-system component or pattern. Use when a designer asks whether something needs a new component, how a design fits the current system, or what design-system contribution a feature should make.
license: MIT
metadata:
  author: Tranz007
  version: "0.1.0"
---

# System Fit

Prevent accidental design-system sprawl without forcing every problem into an existing component.

## Inspect the real system

Use `.ux/DESIGN-SYSTEM.md` when available and inspect authoritative sources such as Storybook, component packages, token definitions, design documentation, implementation examples, and contribution rules.

Do not assume Figma, Storybook, or code is the source of truth. Use the project's documented hierarchy or flag the ambiguity.

## Classify the fit

Prefer this order:

1. **Reuse** — an existing component or pattern already solves the need.
2. **Compose** — existing primitives solve it when combined in an established way.
3. **Extend** — an existing component needs a legitimate new state, behavior, variant, or documentation update.
4. **Create** — the need is meaningfully distinct and reusable enough to justify a new system asset.
5. **Feature-local** — the solution is too specific to become a shared system component.

Do not create a new component merely because the exact visual arrangement is new.

## Check the gap

If the existing system almost fits, identify the precise missing behavior: state, accessibility behavior, data scale, responsive behavior, content rule, interaction, or API.

Consider whether the gap is documentation rather than implementation.

## Output

Lead with the classification and recommendation. Name the existing assets involved, the gap, and any design-system contribution that should accompany the feature.

If the system source cannot be verified, make the recommendation conditional rather than pretending certainty.

## Examples

- "Does this need a new component?"
- "Can we build this from what the design system already has?"
- "Should this state go back into Storybook?"
