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

- **Context** — inspect what is already known before asking the user to repeat it. Use `.ux/INTENT.md` when product purpose or outcome can change the answer, and load only the additional project context the task needs.
- **User** — ground the work in the people affected, their goal, task, context, and available evidence. Do not invent user needs, behaviors, or personas.
- **Evidence** — keep known, inferred, assumed, unknown, and conflicted information distinct when the difference matters.
- **System** — prefer established product language, components, patterns, and rules before inventing new ones.
- **Clear** — lead with the useful point, use the minimum structure needed, and remove generic AI filler.
- **Trust** — never invent evidence, requirements, rationale, implementation status, or compliance.
- **Outcome** — for substantial multi-step work, keep intent active, use a small `.ux/STATE.md` only when continuity needs it, prioritize the highest-impact unresolved gap before polishing, and verify the actual experience against intent before declaring completion.

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

## Long-horizon work

Do not expose an agent-management methodology to the designer. The human should state the goal and work normally; the agent owns decomposition and continuity.

For substantial work with multiple meaningful phases:

1. Read the relevant `INTENT.md` and identify the actual outcome, not just the requested task list.
2. Break the work into meaningful phases only when decomposition helps execution.
3. Work the highest-impact unresolved gap before polishing already-adequate work.
4. Re-check the current result against intent when a phase completes, progress stalls, or implementation choices materially change the experience.
5. Before declaring completion, perform an outcome check: would the actual user experience now satisfy the intended outcome, core experience, constraints, and success criteria that matter to this work?

A completed checklist does not prove the problem is solved. If every planned task is done but the outcome check fails, continue or surface the unresolved gap.

Agents may use sub-agents, parallel work, or other execution machinery when the environment supports it, but UX Skills does not prescribe an agent topology, agent count, dashboard, or model-specific command. Parallelize only work that is sufficiently independent to benefit from it.

Use `.ux/STATE.md` only when a long task is likely to lose continuity across phases, a long session, or multiple sessions. Keep it small and disposable. It may hold the current objective, current phase, completed work, highest-impact unresolved gap, risks or blockers, next action, and last intent check. Do not treat it as product truth, a roadmap, or another backlog. Delete or stop maintaining it when the work no longer needs it.

## Intent changes

Treat `.ux/INTENT.md` as stable, not frozen. Routine UI and implementation changes should not rewrite it.

Existing intent is the default. Change it only when explicit human direction or authoritative evidence shows that intent itself changed. Make the smallest useful edit. A clarification may refine already-established meaning; a consequential change should preserve the decision or evidence that caused it in `DECISIONS.md` or the project's existing ADR/RFC system.

Never rewrite intent to justify current implementation, remove an inconvenient constraint, or make completed work appear aligned after the fact. Agent inference alone does not override established intent.

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

`STATE.md`, when temporarily useful, is working memory rather than core context and should not be created during setup by default.

Do not duplicate content across these files. Do not treat `.ux/` as a replacement for research repositories, requirements systems, design-system docs, or source code.

## Writing

Use sentence-case headings. Avoid forced lists, excessive bolding, motivational filler, canned conclusions, and generic phrases such as "key considerations" when the content can simply be stated.

`clear` is the explicit rewrite/repair skill, but its communication principles are not optional cleanup. They are embedded in every skill through the shared `## Always` contract.

## Visual documentation

Use Mermaid diagrams when a flow, branching behavior, routing model, or lifecycle is materially easier to understand visually. Keep diagrams close to the concept they explain and use `docs/flows.md` as the consolidated visual reference.

Do not add a diagram when prose is clearer or the diagram merely restates a list.

## Engineering bridge

`handoff`, `pr`, and implementation-aware `critique` preserve UX intent as work reaches engineering. They are not substitutes for framework-specific architecture, security, performance, or code-quality review unless the user explicitly asks for those disciplines too.
