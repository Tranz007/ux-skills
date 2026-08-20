---
name: handoff
description: Prepare UX work for engineering by preserving user intent, behavior, states, design-system usage, accessibility requirements, dependencies, acceptance behavior, and unresolved questions. Use when a designer says "get this ready for engineering", needs a handoff, behavioral contract, implementation-ready ticket content, or wants to stop engineering from guessing.
license: MIT
metadata:
  author: Tranz007
  version: "0.1.1"
---

# Handoff

Transfer design intent, not just appearance.

## Always

- **Context** — inspect what is already known before asking the user to repeat it.
- **Evidence** — keep known, inferred, assumed, unknown, and conflicted information distinct when the difference matters.
- **System** — prefer established product language, components, patterns, and rules before inventing new ones.
- **Clear** — lead with the useful point, use the minimum structure needed, and remove generic AI filler.
- **Trust** — never invent evidence, requirements, rationale, implementation status, or compliance.

Do not recite these rules to the user unless one of them materially affects the answer.

## Gather the source of truth

Inspect the approved design, relevant flow and state decisions, design-system components, content, accessibility requirements, constraints, decision records, and the team's existing engineering workflow.

Do not describe proposed behavior as approved if its status is unclear.

## Check readiness

Before packaging the work, look for anything that would force engineering to guess:

- missing states or recovery;
- ambiguous transitions;
- unsupported new components or patterns;
- unresolved content or terminology;
- accessibility behavior that has not been defined;
- data or service conditions that materially change the experience;
- consequential decisions that are still open.

Do not block handoff for documentation that does not affect implementation.

## Explain behavior

Prioritize what engineering actually needs:

- user goal and outcome;
- entry conditions and primary behavior;
- meaningful branches and recovery;
- component and pattern usage;
- states and data conditions;
- responsive behavior when relevant;
- content rules and terminology;
- accessibility behavior such as focus, announcements, semantics, and keyboard interaction when established;
- dependencies and constraints;
- unresolved questions.

When precision helps, describe behavior as:

```text
When <condition>
→ the system <behavior>
→ the user <sees/hears/can do>
→ relevant state <persists/resets/changes>
→ recovery <behavior>
```

## Fit the team's workflow

If the team needs Jira, GitHub Issues, Linear, Azure DevOps, or another ticket format, turn the handoff into buildable work without splitting it into meaningless UI fragments.

If the user only needs a handoff, do not create ticket-shaped output just because you can.

## Output

Create the smallest engineering package that makes the intended experience clear and testable. Point to authoritative design-system, decision, research, or design sources rather than duplicating them.

## Examples

- "Get this ready for engineering."
- "Turn this approved flow into an implementation handoff."
- "Write the behavior so engineering and QA can test it."
- "Break this into buildable tickets without losing the UX intent."
