---
name: ripple
description: Trace what else a UX, flow, component, content, or design-system change could affect. Use when a designer asks "if we change this, what else moves?", "what else could this affect?", or wants to understand downstream UX impact before committing to a change.
license: MIT
metadata:
  author: Tranz007
  version: "0.1.3"
---

# Ripple

Answer one question: **if we change this, what else moves?**

## Always

- **Context** — inspect what is already known before asking the user to repeat it.
- **User** — ground the work in the people affected, their goal, task, context, and available evidence. Do not invent user needs, behaviors, or personas.
- **Evidence** — keep known, inferred, assumed, unknown, and conflicted information distinct when the difference matters.
- **System** — prefer established product language, components, patterns, and rules before inventing new ones.
- **Clear** — lead with the useful point, use the minimum structure needed, and remove generic AI filler.
- **Trust** — never invent evidence, requirements, rationale, implementation status, or compliance.

Do not recite these rules to the user unless one of them materially affects the answer.

Do not introduce research questions, personas, or discovery work when the user and task are already clear or the missing information would not materially change the work.

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

## Contrast example

Bad:
> This change could affect accessibility, responsive design, analytics, documentation, engineering, support, and other user journeys. Review all dependencies before proceeding.

Good:
> **Shared ripple.** The date picker is reused in booking and trip-change flows, so changing free-form entry affects both. Storybook documents keyboard behavior for the current version, which will also need review. I found no evidence that analytics depend on the input method; treat that as unverified rather than affected.

Why: the good response traces real reuse, separates confirmed from possible impact, and does not inflate the answer with every imaginable dependency.

## Examples

- "If we change this date picker, what else moves?"
- "What else could this error-pattern change affect?"
- "This looks like a tiny change. Is it really?"
