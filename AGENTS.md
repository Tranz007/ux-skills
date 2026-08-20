# AGENTS.md

This repository contains portable Agent Skills for UX practitioners.

## Product intent

UX Skills should help human designers think, discover, decide, validate, communicate, and preserve design intent through implementation. Do not turn the project into a UI-generation framework or a generic prompt library.

## Before changing a skill

Read the root `README.md`, `docs/architecture.md`, and `docs/authoring.md`.

Preserve these behaviors:

- natural language must work without memorizing commands;
- inspect available context before asking the user to repeat it;
- use `.ux/` context when present but degrade gracefully when absent;
- distinguish known, inferred, assumed, unknown, and conflicted information when material;
- never invent evidence, requirements, research findings, design rationale, implementation status, or accessibility compliance;
- prefer reuse and composition of established patterns before creating new ones;
- keep outputs direct, readable, specific, and free of generic AI prose;
- preserve designer control; recommend and challenge rather than silently taking over consequential decisions.

## Agent Skills format

Each skill lives at `skills/<name>/SKILL.md` and must use valid Agent Skills frontmatter. Keep skill names lowercase and hyphenated. Keep descriptions specific enough for reliable natural-language routing.

Prefer a compact `SKILL.md`. Put only genuinely reusable deeper material in `references/` or `assets/`.

## New skills

Do not add a skill just because a UX artifact exists. Add a skill when there is a repeatable practitioner problem that is meaningfully different from existing capabilities.

A proposed skill should answer:

1. What does the designer say naturally that should activate it?
2. What practitioner problem does it solve?
3. What context does it inspect first?
4. What can it safely infer and what must remain unknown?
5. What useful output or decision does it produce?
6. Which existing skill would otherwise overlap with it?

## Writing

Use sentence-case headings. Avoid forced lists, excessive bolding, motivational filler, canned conclusions, and generic phrases such as "key considerations" when the content can simply be stated.

## Engineering bridge

Engineering-facing skills preserve UX intent. They are not substitutes for framework-specific engineering skills or code review. A `pr-review` finding should be about implementation versus intended UX behavior, system usage, state coverage, accessibility requirements, or explicit acceptance criteria unless the user asks for technical code review too.
