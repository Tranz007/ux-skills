# Changelog

All notable changes to UX Skills will be documented here.

## 0.1.3 — 2026-08-20

- added `user-grounding` to answer who the work is for, what is actually known about them, whether personas are useful, and what research is worth doing;
- added `User` to the shared behavior contract across every skill;
- added an explicit anti-ceremony guardrail so simple work does not trigger unnecessary research, personas, discovery, or long questionnaires;
- strengthened `setup-ux` to capture useful user/task evidence without manufacturing personas;
- added routing and authoring guidance for user grounding and non-activation on ordinary well-understood tasks.

## 0.1.2

- added concise bad/good/why contrast examples to the skills where judgment is easiest to misread: `clear`, `challenge`, `frame`, `critique`, `system-fit`, `ripple`, `decision`, `handoff`, `pr`, and `state-sweep`;
- kept examples intentionally selective so skill files stay compact and easy to scan;
- added authoring guidance for using contrast examples to teach restraint, specificity, evidence discipline, system reuse, and audience-aware communication.

## 0.1.1

- strengthened `clear` as both an explicit rewrite skill and a baseline communication behavior;
- embedded the Context, Evidence, System, Clear, and Trust contract in every installed skill so it survives installation without relying on repository-level instructions;
- added validation that rejects skills missing the shared behavior contract.

## 0.1.0

Initial open-source foundation:

- one-time `setup-ux` project discovery with a three-file `.ux/` context layer;
- automatic skills for framing, challenge, blind spots, states, critique, accessibility, UX content, design-system fit, downstream change ripple, decisions, engineering handoff, PR descriptions, and clear human communication;
- design-system-aware behavior that prefers reuse and composition before new components;
- evidence discipline that keeps known, inferred, assumed, unknown, and conflicted information distinct when it matters;
- design-to-engineering continuity focused on behavior, states, accessibility intent, and rationale;
- routing and adversarial evaluation fixtures;
- Agent Skills validation workflow;
- contribution and maintenance guidance.
