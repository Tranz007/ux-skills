---
name: pr-review
description: Review a pull request or implementation diff against intended UX behavior, states, content, accessibility requirements, design-system rules, and acceptance criteria. Use when a designer wants to verify that engineering preserved design intent without pretending to perform a full framework or security code review.
license: MIT
metadata:
  author: Tranz007
  version: "0.1.0"
---

# PR Review

Review whether the implementation preserves the intended experience.

## Establish both sides

Inspect the actual PR diff and relevant implementation files. Then inspect the authoritative UX sources: handoff, behavioral contract, approved design, decision records, design-system documentation, content, accessibility expectations, and acceptance criteria.

Do not flag a difference simply because the code is structured differently from the design artifact. Review behavior and intent.

## Look for meaningful drift

Check for:

- missing or changed user-visible behavior;
- omitted states or recovery paths;
- data persistence/reset behavior that differs from the contract;
- custom UI where the approved system component was expected;
- undocumented new shared patterns or variants;
- content or terminology drift;
- focus, keyboard, semantic, announcement, or other accessibility behavior that is absent or contradicted by the implementation;
- behavior hidden behind TODOs, mocks, or incomplete wiring;
- acceptance criteria that are not represented in the change.

## Separate confidence

A code diff may not prove runtime behavior. Say when a finding requires running the experience, Storybook, tests, or assistive technology rather than presenting inference as fact.

## Output

Prioritize actionable UX implementation findings with the expected behavior, observed implementation evidence, and why the difference matters.

If implementation matches the intended UX, say so briefly rather than manufacturing issues.

## Boundary

This is not automatically a general code-quality, architecture, performance, security, or framework review. Perform those only when the user requests them and the appropriate expertise/tools are available.

Do not approve, request changes, comment on, or merge a PR unless the user authorizes that repository action.

## Examples

- "Review this PR against the design."
- "Did engineering preserve the recovery behavior?"
- "Check this implementation for UX drift."
