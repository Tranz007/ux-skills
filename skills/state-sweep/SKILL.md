---
name: state-sweep
description: Find missing interface and service states such as loading, empty, partial, permission, timeout, stale data, validation, failure, interruption, and recovery. Use when a designer asks what states or edge cases are missing from a screen, component, journey, or feature.
license: MIT
metadata:
  author: Tranz007
  version: "0.1.0"
---

# State Sweep

Find behavior the happy-path design is hiding.

## Read the flow and system

Inspect the current design or implementation, relevant API or data behavior when available, design-system states, accessibility rules, and existing product patterns.

## Sweep by transition, not checklist

For each meaningful user action or system transition, ask what the user sees and can do:

- before data is available;
- while work is happening;
- when nothing exists;
- when only part succeeds;
- when input is invalid;
- when permission or eligibility blocks progress;
- when data changes or becomes stale;
- when the network, service, or dependency fails;
- when a session or operation times out;
- when the user interrupts, leaves, retries, or resumes;
- after success, including confirmation and persistence.

Also check focus, announcements, keyboard behavior, and recovery where dynamic state changes affect accessibility.

## Avoid state inflation

Do not create a separate visual state when the existing system behavior already handles the condition adequately. Reuse documented component states when possible.

## Output

Produce a concise state map. For each missing state, include the trigger, expected user-visible behavior, recovery path, and whether the design system already supports it.

Prioritize states whose absence can strand a user, lose work, create incorrect confidence, or produce inconsistent implementation.

## Examples

- "What states am I missing?"
- "State-sweep this checkout flow."
- "Engineering asked what happens when the API times out."
