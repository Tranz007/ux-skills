# UX context

UX Skills keeps a small amount of project context so designers do not have to re-explain the product and design system in every conversation.

`setup-ux` creates only three files:

```text
.ux/
├── CONTEXT.md
├── DESIGN-SYSTEM.md
└── DECISIONS.md
```

## CONTEXT.md

Keep the useful project basics together:

- what the product does and the major journeys;
- known users and important contexts;
- where research, analytics, and customer evidence live;
- engineering stack and workflow relevant to UX;
- accessibility expectations;
- important terminology;
- real constraints and material unknowns.

This is not a product requirements document. Keep it short and point to authoritative sources instead of copying them.

## DESIGN-SYSTEM.md

Tell UX Skills how the real design system works:

- Figma, Storybook, repository, package, or documentation locations;
- which source is authoritative for components, tokens, behavior, and visual design;
- existing component and pattern conventions;
- reuse and composition expectations;
- how new variants, patterns, or components get contributed.

The purpose is simple: stop the agent from casually inventing a parallel design system.

## DECISIONS.md

Keep only consequential UX or architecture decisions that future designers or engineers are likely to question.

If the project already uses ADRs, RFCs, or another decision-record system, point to it instead of duplicating it.

## Evidence and uncertainty

All skills should distinguish evidence from inference when it matters. A repeated assumption does not become a user fact because it appears in several documents.

Useful distinctions are:

- **Known** — supported by evidence or an authoritative source.
- **Inferred** — strongly suggested by what is available.
- **Assumed** — being treated as true without enough evidence.
- **Unknown** — not enough information yet.
- **Conflicted** — credible sources disagree.

Do not label everything. Surface these only when the distinction affects the decision.

## Setup behavior

`setup-ux` explores first. It should learn as much as possible from the repo, design-system sources, connected design tools, accessibility guidance, research, issue/PR conventions, and existing documentation before asking the designer anything.

Missing information is fine. Ask only when the answer materially changes how UX Skills should behave.

The files are memory aids, not configuration bureaucracy. The actual project remains the source of truth.
