---
name: ship
description: Check whether UX work is ready for engineering and package only the artifacts the team actually needs. Use when a designer says "get this ready for engineering", "can we ship this?", or wants a final completeness pass across states, system fit, accessibility, decisions, handoff, tickets, or PR preparation.
license: MIT
metadata:
  author: Tranz007
  version: "0.1.0"
---

# Ship

Make the design buildable without inventing ceremony.

## Determine what "ready" means here

Read `.ux/WORKFLOW.md`, engineering conventions, issue and PR templates, design-system rules, and the current work. Different teams require different artifacts; do not impose a universal checklist.

## Run the smallest useful readiness pass

Check for material gaps in:

- problem and user outcome;
- approved behavior and important states;
- unresolved assumptions or decisions;
- design-system fit and required system contributions;
- content and terminology;
- accessibility behavior that engineering must implement;
- dependencies and data/service conditions;
- validation status when the risk warrants it;
- acceptance behavior and links to authoritative artifacts.

If a missing item does not affect implementation, do not block the handoff for it.

## Package the work

Create or recommend only what the team's workflow calls for: handoff, behavioral contract, tickets, decision record, Storybook update, PR description, or another project-specific artifact.

Do not generate duplicate documents that say the same thing in different formats.

## Output

Give a clear readiness judgment: ready, ready with named follow-ups, or not ready because specific decisions would force engineering to guess.

Then create or outline the minimum package needed to move forward.

## Examples

- "Get this ready for engineering."
- "Can this ship?"
- "What still needs to be resolved before a developer picks this up?"
