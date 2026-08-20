---
name: impact
description: Trace the downstream UX, design-system, content, accessibility, analytics, documentation, and engineering effects of a proposed design or component change. Use when a designer asks what else will break or change, who is affected, or how large a seemingly local change really is.
license: MIT
metadata:
  author: Tranz007
  version: "0.1.0"
---

# Impact

Make the blast radius visible before the change becomes expensive.

## Inspect dependencies

Start from the proposed change and inspect available usage, design-system references, product journeys, implementation references, content, analytics events, tests, and documentation.

Distinguish confirmed usage from likely usage that has not been verified.

## Trace consequences

Look for relevant effects across:

- other screens, journeys, and user roles;
- shared components, tokens, and patterns;
- states and responsive behavior;
- accessibility semantics or keyboard behavior;
- product terminology and content;
- analytics or instrumentation;
- API, data, or service assumptions;
- tests, Storybook stories, documentation, and training/support material.

Do not inflate impact with speculative dependencies that cannot be tied to the change.

## Identify migration needs

If a shared pattern changes, note whether existing usage can remain, must migrate, or needs a deprecation path.

## Output

Lead with the practical blast radius: local, shared, cross-journey, or system-wide. List the concrete affected areas and the highest-risk consequence of missing each one.

Recommend a smaller change when it achieves the goal with materially less system impact.

## Examples

- "If we change this component, what else does it affect?"
- "What's the blast radius of this pattern change?"
- "Engineering says this is a small change. Is it?"
