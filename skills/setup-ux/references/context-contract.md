# Context contract

Keep project context small, explicit, and useful. These files are memory aids for UX Skills, not another documentation system.

## Ownership

`INTENT.md` owns **why and toward what**: intended outcome, people affected, core experience, scope, non-goals, material constraints, success, and unresolved intent assumptions.

`CONTEXT.md` owns **what environment is true now**: product mechanics, major journeys, evidence locations, engineering workflow, accessibility expectations, terminology, and stable project facts.

`DESIGN-SYSTEM.md` owns **what system should be reused**: Figma, Storybook, packages, tokens, source-of-truth rules, and contribution expectations.

`DECISIONS.md` owns **what consequential choices should persist**: a compact index or pointers to the project's existing ADR/RFC system.

Do not duplicate the same paragraph across files. Link or point to the authoritative location instead.

## INTENT.md

```markdown
# Intent

## Why
Why this product or capability should exist.

## Intended outcome
What should become meaningfully better or newly possible.

## People affected
Who is affected, using only supported knowledge and material assumptions.

## Core experience
The essential task, job, or experience the product must enable.

## Scope
What is in scope now.

## Non-goals
Adjacent things deliberately not being solved now.

## Constraints
Only constraints that materially shape the experience.

## Success
How success is understood or measured, when known.

## Evidence, assumptions, and unknowns
Only items that materially affect confidence or future decisions.
```

Keep `INTENT.md` short enough to scan. It is not a PRD, roadmap, backlog, requirements catalog, or implementation plan.

## CONTEXT.md

```markdown
# Project context

## Product mechanics
Observable capabilities and major journeys that help orient future work.

## Users and evidence
Useful user/task context plus pointers to research, analytics, support feedback, and other evidence.

## Engineering
Frontend stack, relevant repos, Storybook/testing, issue and PR workflow, and technical constraints that affect UX.

## Accessibility
Actual standards, policies, and testing expectations used by the team.

## Terminology
Important product terms, acronyms, and semantic distinctions.

## Material unknowns
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

Small decisions can remain inline. A larger decision can point to a dedicated record when its rationale, evidence, alternatives, or consequences need more room.

## Evidence status

For claims about people, user behavior, research or analytics, policy or accessibility requirements, consequential decisions, intent, and material unknowns, use `KNOWN`, `INFERRED`, `ASSUMED`, `UNKNOWN`, or `CONFLICTED` when the distinction materially affects confidence.

Include a source or location for `KNOWN` claims when practical. Do not label observable mechanics merely for ceremony, and do not write an unsupported claim as an ordinary fact because tagging it feels cumbersome.

## Progressive context

The four core files are a starting point, not a schema that every project must expand.

Create a smaller focused file only when information has become dense, repeatedly useful, or independently owned. Examples:

```text
.ux/users/tasks.md
.ux/users/journeys.md
.ux/evidence/research.md
.ux/evidence/analytics.md
.ux/constraints/accessibility.md
.ux/constraints/technical.md
```

Do not create empty folders or placeholder files. Do not copy full research reports, component documentation, or policy text into `.ux/`; point to the source.

Future skills should read `INTENT.md` when purpose, outcome, people, scope, or success can change the answer, then load only the additional context relevant to the task.

## Migration from v0.1

When `.ux/` already contains `CONTEXT.md`, `DESIGN-SYSTEM.md`, and `DECISIONS.md`:

1. Preserve existing content and links.
2. Draft `INTENT.md` from authoritative evidence already available.
3. Keep current behavior separate from inferred intent.
4. Ask only for material intent gaps that cannot be discovered reliably.
5. Move content out of `CONTEXT.md` only when ownership is clearly improved; do not churn files just to match a template.
