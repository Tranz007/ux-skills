---
name: flow
description: Reason through a user journey or interaction flow including entry points, branches, interruptions, dependencies, alternate paths, exits, and recovery. Use when a designer is mapping how something should work rather than how a single screen should look.
license: MIT
metadata:
  author: Tranz007
  version: "0.1.0"
---

# Flow

Model the experience as behavior over time, not a sequence of ideal screens.

## Start with context

Read the relevant product goal, users, existing journey, system constraints, known evidence, and implementation behavior. Reuse established patterns when they already solve part of the flow.

## Trace the journey

Identify:

- meaningful entry points and prerequisites;
- the user's intended outcome;
- decisions and branches;
- system responses and dependencies;
- interruptions, cancellation, back navigation, and resume behavior;
- alternate successful paths;
- failure and recovery paths;
- exits and what persists afterward.

Do not create branches merely for completeness. Focus on conditions that materially change the experience.

## Preserve uncertainty

Mark behavior as proposed when it is not already established. Distinguish current behavior from desired behavior if both are discussed.

## Output

Use the representation that best helps the designer: compact prose, ordered behavior, a state/flow table, or Mermaid when a diagram adds clarity.

Call out unresolved decisions where a flow cannot be specified responsibly.

## Examples

- "Work through the account recovery flow with me."
- "What happens if the user backs out halfway through?"
- "Map the alternate paths for changing a reservation."
