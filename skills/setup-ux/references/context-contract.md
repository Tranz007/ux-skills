# Context templates

Keep these small. They are memory aids for UX Skills, not another documentation system.

## CONTEXT.md

```markdown
# Project context

## Product
What it does, major journeys, important outcomes and constraints.

## Users and evidence
Known users and contexts. Where research, analytics, support feedback, and other evidence live.

## Engineering
Frontend stack, relevant repos, Storybook/testing, issue and PR workflow, technical constraints that affect UX.

## Accessibility
Actual standards, policies, and testing expectations used by the team.

## Terminology
Important product terms, acronyms, and semantic distinctions.

## Unknowns
Only unresolved things that could materially change future UX recommendations.
```

## DESIGN-SYSTEM.md

```markdown
# Design system

## Sources
Figma:
Storybook:
Repository/package:
Tokens/docs:

## Source of truth
Which source owns components, behavior, tokens, and visual design?

## Working rules
Reuse/composition expectations and contribution path.

## Known gaps
Only gaps that matter to current work.
```

## DECISIONS.md

```markdown
# Decisions

Record only consequential decisions, or point to the project's existing ADR/RFC location.
```

When evidence status matters, use `KNOWN`, `INFERRED`, `ASSUMED`, `UNKNOWN`, or `CONFLICTED`. Do not tag ordinary statements unnecessarily.
