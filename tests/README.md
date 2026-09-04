# UX Skills evaluation

A skill is not good because its prompt sounds smart. It has to route correctly, preserve evidence integrity, produce useful practitioner output, and avoid making the user work harder than necessary.

## What to evaluate

### Routing

Does ordinary designer language select the intended capability? Do adjacent skills remain distinct?

Use `routing-cases.jsonl` as the starter corpus. Each row includes an utterance and expected primary skill.

Run it against a target agent with `python scripts/evaluate-routing.py --command '<adapter command>'`. The adapter receives one JSON object per line on standard input and returns one JSON object per line containing `predicted`. See `python scripts/evaluate-routing.py --help` for the complete protocol. The repository does not prescribe a model; record the agent and model used with the result.

### Setup behavior

`setup-ux` is explicit rather than routed from ordinary design work, so evaluate it separately with `setup-ux-cases.md`.

The setup cases cover:

- vague and well-formed greenfield ideas;
- existing projects with strong or weak documentation;
- disagreement between docs and implementation;
- projects with and without user evidence or a design system;
- migration from the v0.1 three-file `.ux/` structure;
- refreshes where intent has and has not materially changed;
- intent clarification versus implementation-driven intent drift;
- the rule that optional working state is not created during setup.

The important measure is not how many questions setup can ask. It is whether setup discovers what it can, asks only what materially changes future work, and leaves the project with useful intent and context without inventing certainty.

### User grounding

Does the agent understand who the work affects and what is actually known about them when that information can change the design?

It should not invent user needs, behaviors, personas, demographics, quotes, or pain points. It should inspect existing research and evidence before asking the designer to repeat it.

Equally important: it should **not** introduce personas, research plans, discovery exercises, or long questionnaires for simple work where the user/task context is already clear or the missing information would not materially change the decision.

### Evidence integrity

The agent must not turn assumptions, plausible inference, or repeated undocumented claims into known facts. It must not invent research, participants, metrics, rationale, requirements, implementation status, product intent, or accessibility compliance.

### Intent integrity

When `.ux/INTENT.md` exists, does the agent use it when purpose, intended outcome, people, scope, constraints, or success can materially change the answer?

It should not treat current implementation as proof of intended outcome. It should not rewrite intent because of a routine interface change. It should surface when new evidence or a consequential decision appears to invalidate the current intent.

Intent is stable, not frozen. A useful agent can make the smallest evidence-backed or human-directed clarification without regenerating the file, while refusing to rewrite intent merely to make divergent implementation look correct.

### Outcome integrity

For substantial multi-step work, does the agent continue optimizing for the intended experience rather than for task completion itself?

It should prioritize the highest-impact unresolved gap before polishing already-adequate work, re-check the result against intent when progress stalls or a meaningful phase completes, and perform an outcome check before declaring completion. A fully checked task list must not override evidence that the actual experience still fails the intended outcome.

`.ux/STATE.md` should appear only when continuity across substantial work actually benefits from it. Small tasks should not gain a phase tracker, progress dashboard, or extra project-management ceremony merely because the capability exists.

### Context behavior

A skill should inspect available context before asking the user for known information. It should remain useful when `.ux/` is incomplete and ask only when a missing answer materially changes the work.

It should also load context progressively. A small content edit should not require every `.ux/` file, and a substantial product decision should not ignore `INTENT.md` merely to save context.

### Readability

Outputs should lead with useful findings, use minimal structure, preserve necessary uncertainty, and avoid generated-document habits.

### System behavior

When a design system exists, recommendations should prefer reuse and composition before extension or creation unless the actual need justifies otherwise.

### Engineering continuity

Engineering-facing outputs should preserve behavior, states, system decisions, accessibility expectations, and unresolved questions rather than reducing the work to screenshots or generic implementation tickets.

## Fixture philosophy

Keep fixtures small enough to understand why a model passed or failed. Prefer adversarial cases that expose a specific weakness over giant realistic prompts where failure is hard to diagnose.

Include negative cases where a capability should stay out of the way. A good UX partner knows when **not** to start a UX process, when not to read unrelated context, when not to create working-state machinery, and when not to change product intent.

## Suggested evaluation loop

1. Validate every skill against the Agent Skills specification and shared UX behavior contract.
2. Run routing cases against the target agent/model.
3. Run `setup-ux-cases.md` against greenfield, existing-project, migration, refresh, intent-integrity, and working-state behavior.
4. Run skill-specific adversarial fixtures.
5. On substantial tasks, include at least one case where every planned task is complete but the intended experience is still not, and verify that the agent does not declare success.
6. Compare output against explicit must/must-not criteria.
7. Test on real design work before expanding the catalog.

The repository intentionally does not declare one model the reference implementation. Cross-model portability is a product requirement.
