# UX Skills evaluation

A skill is not good because its prompt sounds smart. It has to route correctly, preserve evidence integrity, produce useful practitioner output, and avoid making the user work harder than necessary.

## What to evaluate

### Routing

Does ordinary designer language select the intended capability? Do adjacent skills remain distinct?

Use `routing-cases.jsonl` as the starter corpus. Each row includes an utterance and expected primary skill.

### User grounding

Does the agent understand who the work affects and what is actually known about them when that information can change the design?

It should not invent user needs, behaviors, personas, demographics, quotes, or pain points. It should inspect existing research and evidence before asking the designer to repeat it.

Equally important: it should **not** introduce personas, research plans, discovery exercises, or long questionnaires for simple work where the user/task context is already clear or the missing information would not materially change the decision.

### Evidence integrity

The agent must not turn assumptions, plausible inference, or repeated undocumented claims into known facts. It must not invent research, participants, metrics, rationale, requirements, implementation status, or accessibility compliance.

### Context behavior

A skill should inspect available context before asking the user for known information. It should remain useful when `.ux/` is incomplete and ask only when a missing answer materially changes the work.

### Readability

Outputs should lead with useful findings, use minimal structure, preserve necessary uncertainty, and avoid generated-document habits.

### System behavior

When a design system exists, recommendations should prefer reuse and composition before extension or creation unless the actual need justifies otherwise.

### Engineering continuity

Engineering-facing outputs should preserve behavior, states, system decisions, accessibility expectations, and unresolved questions rather than reducing the work to screenshots or generic implementation tickets.

## Fixture philosophy

Keep fixtures small enough to understand why a model passed or failed. Prefer adversarial cases that expose a specific weakness over giant realistic prompts where failure is hard to diagnose.

Include negative cases where a capability should stay out of the way. A good UX partner knows when **not** to start a UX process.

## Suggested evaluation loop

1. Validate every skill against the Agent Skills specification.
2. Run routing cases against the target agent/model.
3. Run skill-specific adversarial fixtures.
4. Compare output against explicit must/must-not criteria.
5. Test on real design work before expanding the catalog.

The repository intentionally does not declare one model the reference implementation. Cross-model portability is a product requirement.
