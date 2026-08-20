# AGENTS.md

This repository contains portable Agent Skills for UX practitioners.

## Product intent

UX Skills should help human designers think, discover, decide, validate, communicate, and preserve design intent through implementation. Do not turn the project into a UI-generation framework, an app, or a generic prompt library.

The user experience is intentionally small: install the suite, run `setup-ux` once, then work in natural language. Most skills are internal capabilities the model should select automatically when their descriptions match the task.

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
- inspect available context before asking the user to repeat it;
- use `.ux/` context when present but degrade gracefully when absent;
- never invent research findings, user needs, personas, or accessibility compliance;
- recommend user research only when it reduces an uncertainty that could materially change the work;
- prefer reuse and composition of established patterns before creating new ones;
- preserve designer control over consequential decisions.

## Agent Skills format

Each skill lives at `skills/<name>/SKILL.md` and must use valid Agent Skills frontmatter. Keep skill names lowercase and hyphenated. Keep descriptions specific enough for reliable natural-language routing.

Prefer a compact `SKILL.md`. Put only genuinely reusable deeper material in `references/` or `assets/`.

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

## Writing

Use sentence-case headings. Avoid forced lists, excessive bolding, motivational filler, canned conclusions, and generic phrases such as "key considerations" when the content can simply be stated.

`clear` is the explicit rewrite/repair skill, but its communication principles are not optional cleanup. They are embedded in every skill through the shared `## Always` contract.

## Engineering bridge

`handoff`, `pr`, and implementation-aware `critique` preserve UX intent as work reaches engineering. They are not substitutes for framework-specific architecture, security, performance, or code-quality review unless the user explicitly asks for those disciplines too.
