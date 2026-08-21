---
name: setup-ux
description: Set up or refresh UX Skills for a project by learning the product, users and research evidence, design system, engineering environment, accessibility expectations, terminology, and existing decisions. Use only when the user explicitly asks to set up, initialize, connect, learn, or refresh UX Skills/project context; do not activate during ordinary UX work.
license: MIT
metadata:
  author: Tranz007
  version: "0.1.3"
  ux-skills-invocation: "explicit"
---

# Setup UX

Learn the project before asking the designer to configure it.

## Always

- **Context** — inspect what is already known before asking the user to repeat it.
- **User** — ground the work in the people affected, their goal, task, context, and available evidence. Do not invent user needs, behaviors, or personas.
- **Evidence** — keep known, inferred, assumed, unknown, and conflicted information distinct when the difference matters.
- **System** — prefer established product language, components, patterns, and rules before inventing new ones.
- **Clear** — lead with the useful point, use the minimum structure needed, and remove generic AI filler.
- **Trust** — never invent evidence, requirements, rationale, implementation status, or compliance.

Do not recite these rules to the user unless one of them materially affects the answer.

Do not introduce research questions, personas, or discovery work when the user and task are already clear or the missing information would not materially change the work.

## Explore first

Inspect whatever is available: README and product docs, existing user research, analytics and support evidence, package files, Storybook, components, tokens, design-system docs, Figma or other connected design sources, accessibility guidance, issue/PR templates, and existing decisions.

Do not ask the user for information you can discover reliably.

## Keep the context small

Create or refresh only:

```text
.ux/
├── CONTEXT.md
├── DESIGN-SYSTEM.md
└── DECISIONS.md
```

### CONTEXT.md

Keep the useful basics together: what the product does; who it serves; user goals, tasks, and meaningful groups when supported by evidence; important journeys; evidence/research locations; engineering stack and workflow; accessibility expectations; terminology; and material unknowns.

Do not manufacture personas or demographic detail simply to fill the file. If the project has useful, research-backed personas or behavioral segments, reference them. Otherwise describe only what is actually known about the people and tasks that matter.

### DESIGN-SYSTEM.md

Record the actual design-system sources and rules: Storybook, Figma, component packages, tokens, source-of-truth order, reuse expectations, and contribution path.

### DECISIONS.md

Keep a lightweight index of consequential UX or architecture decisions. If the project already has ADRs or another decision system, point to that instead of creating a competing one.

## Missing information is allowed

Do not block setup because something is unknown. Ask only when an answer would materially change future recommendations.

Never turn assumptions into facts. Label claims about people, evidence, requirements, decisions, and material unknowns as known, inferred, assumed, unknown, or conflicted; ordinary product mechanics do not need labels.

## Finish usefully

Tell the designer what you learned, the few important gaps you found, and whether the user context and design system are sufficiently understood to start working.

Then stop. Do not turn setup into an audit or a discovery workshop.
