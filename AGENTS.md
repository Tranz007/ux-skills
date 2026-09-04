# AGENTS.md

This repository contains portable Agent Skills for UX practitioners.

## Product intent

UX Skills should help human designers think, discover, decide, validate, communicate, and preserve design intent through implementation. Do not turn the project into a UI-generation framework, an app, or a generic prompt library.

The user experience is intentionally small: install the suite, run `setup-ux` once, then work in natural language. Most skills are internal capabilities the model should select automatically when their descriptions match the task.

The internal architecture separates three things:

- **Intent** — why the product or capability exists, for whom, toward what outcome, and within what scope.
- **Context** — what is true about the product, evidence, environment, design system, constraints, and prior decisions.
- **Skills** — the practitioner capability useful for the current request.

Intent tells the agent what good means. Context tells it what is true. Skills tell it how to reason.

## Before changing a skill

Read the root `README.md`, `docs/architecture.md`, and `docs/authoring.md`.

Every installed `SKILL.md` must carry the same small `## Always` contract so the behavior survives installation without depending on repository-level instructions:

- **Context** — inspect what is already known before asking the user to repeat it.
- **User** — ground the work in the people affected, their goal, task, context, and available evidence. Do not invent user needs, behaviors, or personas.
- **Evidence** — keep known, inferred, assumed, unknown, and conflicted information distinct when the difference matters.
- **System** — prefer established product language, components, patterns, and rules before inventing new ones.
- **Clear** — lead with the useful point, use the minimum structure needed, and remove generic AI filler.
- **Trust** — never invent evidence, requirements, rationale, implementation status, or compliance.

Do not make users learn or see this contract. It is background behavior.

Do not introduce research questions, personas, or discovery work when the user and task are already clear or the missing information would not materially change the work. User-centered does not mean process-heavy.

Also preserve these product rules:

- natural language must work without memorizing commands;
- `setup-ux` is the only skill designers should need to deliberately invoke;
- `setup-ux` must support both new and existing projects under the same command;
- new-project setup should capture intent through an adaptive conversation, not a fixed questionnaire;
- existing-project setup should inspect before asking and should not confuse implementation with intended outcome;
- use `.ux/INTENT.md` when purpose, outcome, people, scope, constraints, or success can materially change the answer;
- load only the additional `.ux/` context relevant to the current task rather than treating the whole directory as mandatory prompt context;
- allow project context to split into smaller files only when density, repeated use, or distinct ownership justifies it;
- do not generate empty research, persona, journey, or constraints structures for ceremony;
- use `.ux/` context when present but degrade gracefully when absent;
- never invent research findings, user needs, personas, intent, or accessibility compliance;
- recommend user research only when it reduces an uncertainty that could materially change the work;
- prefer reuse and composition of established patterns before creating new ones;
- preserve designer control over consequential decisions.

## Agent Skills format

Each skill lives at `skills/<name>/SKILL.md` and must use valid Agent Skills frontmatter. Keep skill names lowercase and hyphenated. Keep descriptions specific enough for reliable natural-language routing.

Prefer a compact `SKILL.md`. Treat it as the routing and reasoning core, not an encyclopedia. Put only genuinely reusable deeper material in `references/` or `assets/`, and instruct the agent to read only the reference relevant to the current task.

Do not create a `references/` folder merely to make a skill look complete. Progressive disclosure is useful only when it reduces irrelevant context or separates material that is independently reusable.

## New skills

Do not add a skill just because a UX artifact exists. Add one when there is a repeatable practitioner problem that is meaningfully different from existing capabilities.

A proposed skill should answer:

1. What would a designer naturally say that should activate it?
2. What practitioner problem does it solve?
3. What context should it inspect first?
4. What can it safely infer and what must remain unknown?
5. What useful decision or output does it produce?
6. Could an existing skill handle this without becoming confusing?
7. What is the stop condition that keeps the skill from adding unnecessary UX process?
8. Does deeper material belong in a task-specific reference rather than the main skill?

## Project context

The core `.ux/` layer is:

```text
.ux/
├── INTENT.md
├── CONTEXT.md
├── DESIGN-SYSTEM.md
└── DECISIONS.md
```

Keep ownership clear:

- `INTENT.md` owns why/outcome/people/core experience/scope/non-goals/material constraints/success/material uncertainty.
- `CONTEXT.md` owns observable operating context, evidence locations, engineering, accessibility expectations, terminology, and stable project facts.
- `DESIGN-SYSTEM.md` owns pointers and rules for the actual design system.
- `DECISIONS.md` owns consequential decision records or pointers to an existing ADR/RFC system.

Do not duplicate content across these files. Do not treat `.ux/` as a replacement for research repositories, requirements systems, design-system docs, or source code.

## Writing

Use sentence-case headings. Avoid forced lists, excessive bolding, motivational filler, canned conclusions, and generic phrases such as "key considerations" when the content can simply be stated.

`clear` is the explicit rewrite/repair skill, but its communication principles are not optional cleanup. They are embedded in every skill through the shared `## Always` contract.

## Visual documentation

Use Mermaid diagrams when a flow, branching behavior, routing model, or lifecycle is materially easier to understand visually. Keep diagrams close to the concept they explain and use `docs/flows.md` as the consolidated visual reference.

Do not add a diagram when prose is clearer or the diagram merely restates a list.

## Engineering bridge

`handoff`, `pr`, and implementation-aware `critique` preserve UX intent as work reaches engineering. They are not substitutes for framework-specific architecture, security, performance, or code-quality review unless the user explicitly asks for those disciplines too.
