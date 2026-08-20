---
name: contract
description: Express UX intent as a precise design-to-engineering behavioral contract using triggers, system responses, user-visible outcomes, persistence, recovery, and acceptance behavior. Use when screenshots are insufficient and engineering or QA needs to know exactly what happens under each important condition.
license: MIT
metadata:
  author: Tranz007
  version: "0.1.0"
---

# Contract

Describe behavior precisely enough that design, engineering, and QA can detect disagreement.

## Start from approved intent

Inspect the flow, states, design-system behavior, content, accessibility requirements, service constraints, and existing implementation contract if one exists.

Do not invent missing product decisions. Mark unresolved behavior explicitly.

## Write behavior as conditions and outcomes

For each meaningful transition, capture:

```text
When <trigger or condition>
→ the system <behavior>
→ the user sees/hears/can do <outcome>
→ relevant data or state <persists/resets/changes>
→ recovery is <behavior>
```

Include only dimensions that matter. A contract is not a screenplay for every click.

## Cover consequential states

Pay special attention to asynchronous work, validation, partial success, stale data, service failures, retries, session expiration, destructive actions, and dynamic accessibility behavior.

## Make testability visible

Phrase behavior so it can become acceptance criteria or tests. Avoid subjective requirements such as "feels intuitive" or "loads quickly" without a defined measure.

## Respect system ownership

Reference existing component behavior rather than restating it unless the feature intentionally changes or constrains that behavior.

## Output

Produce a compact contract grouped by meaningful behavior. Highlight unresolved clauses that must be decided before implementation.

## Examples

- "Write the behavioral contract for this flow."
- "Tell engineering exactly what happens after an expired code."
- "Turn these screens into testable UX behavior."
