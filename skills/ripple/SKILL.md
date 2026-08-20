---
name: ripple
description: Trace what else a UX, flow, component, content, or design-system change could affect. Use when a designer asks "if we change this, what else moves?", "what else could this affect?", or wants to understand downstream UX impact before committing to a change.
license: MIT
metadata:
  author: Tranz007
  version: "0.1.0"
---

# Ripple

Answer one question: **if we change this, what else moves?**

## Start from the change

Inspect the proposed change and whatever project context is available. Look for actual reuse and dependencies before speculating.

## Trace the ripple

Check only the areas that are relevant:

- other screens and journeys;
- user roles or permissions;
- shared components, patterns, or tokens;
- states and responsive behavior;
- accessibility behavior;
- terminology and product content;
- analytics or tracking;
- APIs, data, and service behavior;
- tests, Storybook, documentation, support, or training.

Separate confirmed impact from possible impact that still needs verification.

## Keep it useful

Tell the designer whether the change looks contained, shared, cross-journey, or foundational. Then name the few downstream effects that actually matter and why.

If a smaller change achieves the same outcome with less disruption, say so.

## Examples

- "If we change this date picker, what else moves?"
- "What else could this error-pattern change affect?"
- "This looks like a tiny change. Is it really?"
