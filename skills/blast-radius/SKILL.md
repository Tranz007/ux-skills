---
name: blast-radius
description: Trace what else a UX, flow, component, content, or design-system change could affect. Use when a designer asks "what else could this break?", "what's the blast radius?", or wants to know whether a change is local, shared, cross-journey, or system-wide before committing to it.
license: MIT
metadata:
  author: Tranz007
  version: "0.1.0"
---

# Blast Radius

Answer one question: **if we change this, what else could we accidentally affect?**

## Start from the change

Inspect the proposed change and whatever project context is available. Look for actual reuse and dependencies before speculating.

## Trace only relevant effects

Check where the change could propagate across:

- other screens or journeys;
- user roles or permissions;
- shared components, patterns, or tokens;
- states and responsive behavior;
- accessibility behavior;
- terminology and product content;
- analytics or tracking;
- APIs, data, and service behavior;
- tests, Storybook, documentation, support, or training.

Distinguish confirmed impact from possible impact that still needs verification.

## Keep it simple

Classify the overall radius as:

- **Local** — contained to this feature or surface.
- **Shared** — affects a reused component or pattern.
- **Cross-journey** — changes behavior in multiple product flows.
- **System-wide** — alters a foundational rule, component, token, or product convention.

Then name the few affected areas that actually matter and the consequence of missing them.

If a smaller change achieves the same outcome with a smaller blast radius, say so.

## Examples

- "What's the UX blast radius of changing this date picker?"
- "If we change this error pattern, what else could break?"
- "Engineering says this is a tiny change. Is it really?"
