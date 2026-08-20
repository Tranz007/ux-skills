---
name: tickets
description: Break approved UX intent into buildable engineering tickets while preserving behavior, states, design-system usage, accessibility requirements, dependencies, and acceptance criteria. Use when a designer asks to turn a design or handoff into Jira, GitHub, Linear, Azure DevOps, or local implementation work.
license: MIT
metadata:
  author: Tranz007
  version: "0.1.0"
---

# Tickets

Break work down without breaking the UX intent apart.

## Read the team's workflow

Use `.ux/WORKFLOW.md`, engineering context, issue templates, labels, and existing ticket conventions when available. Match the project's tracker and level of detail instead of inventing a new process.

## Start from approved behavior

Inspect the handoff or behavioral contract, design-system decisions, accessibility requirements, dependencies, and implementation boundaries.

Do not create tickets from unresolved design guesses. Surface decisions that must happen first.

## Slice by buildable behavior

Prefer tickets that can be implemented and reviewed coherently. Avoid both extremes:

- one giant "build the new experience" ticket;
- dozens of tickets split by individual UI elements that cannot be validated independently.

Keep shared design-system work explicit when it should be reviewed separately from feature-local work.

## Preserve the why

Each ticket should carry enough context for an engineer to understand the user outcome, intended behavior, relevant states, authoritative design/system references, dependencies, and acceptance criteria.

Do not copy entire research reports or design specs into every ticket. Link to durable sources.

## Writes require authorization

If tools can create or modify tracker items, prepare the proposed set first and perform writes only when the user has authorized that action. Never invent project IDs, labels, assignees, or milestones.

## Examples

- "Break this into engineering tickets."
- "Turn this handoff into Jira-ready work."
- "How should we slice this without losing the UX behavior?"
