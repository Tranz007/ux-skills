---
name: compare
description: Compare two or more UX directions against explicit criteria derived from user goals, evidence, accessibility, design-system fit, complexity, risk, and engineering consequences. Use when a designer asks which option is better and wants a decision rather than an aesthetic preference.
license: MIT
metadata:
  author: Tranz007
  version: "0.1.0"
---

# Compare

Compare alternatives against the problem, not against taste.

## Establish criteria

Derive decision criteria from available context before judging the options. Relevant criteria may include:

- ability to achieve the user outcome;
- support from evidence;
- cognitive and interaction effort;
- accessibility and inclusive use;
- error prevention and recovery;
- consistency with established patterns;
- implementation and maintenance complexity;
- risk, reversibility, and downstream impact.

Do not weight every criterion equally. Say which criteria dominate and why.

## Compare fairly

Evaluate each option against the same important criteria. Do not invent advantages that are not visible in the design or context.

If an option depends on an unvalidated assumption, expose that dependency instead of scoring it as fact.

## Allow "neither"

Do not force a winner. Recommend neither option when both preserve the wrong premise or introduce unacceptable tradeoffs.

## Output

Give the recommendation first when confidence is sufficient, then the decisive tradeoffs. Use a compact matrix only when it improves comparison.

If the decision hinges on unresolved evidence, say what small validation would discriminate between the options.

## Examples

- "Compare A and B. Which should we ship?"
- "Don't tell me which looks nicer. Which works better for this problem?"
- "Are either of these actually good solutions?"
