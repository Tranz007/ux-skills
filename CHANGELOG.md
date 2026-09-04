# Changelog

All notable changes to UX Skills will be documented here.

## Unreleased

Nothing yet.

## 0.2.0 — 2026-09-04

- added intent-first project context with `.ux/INTENT.md` as a small north-star artifact for why, intended outcome, people affected, core experience, scope, non-goals, material constraints, success, and uncertainty;
- split `setup-ux` into adaptive greenfield and inspect-first existing-project paths without adding another user-facing setup skill;
- added migration behavior that preserves the original three-file `.ux/` structure and adds intent without unnecessary context churn;
- documented progressive project-context loading so skills read intent when it can change the answer and load only the additional context relevant to the current task;
- documented progressive skill disclosure so compact `SKILL.md` files can route to deeper references only when those references are actually needed;
- added Mermaid architecture and lifecycle diagrams plus a consolidated `docs/flows.md` visual reference;
- added setup-specific evaluation cases and greenfield/existing-product example contexts;
- added a model-agnostic routing runner so the routing corpus can measure activation against a chosen target agent;
- made local shared-contract validation run even when the optional Agent Skills specification validator is unavailable;
- strengthened provenance requirements for claims stored in project context;
- require `critique` to surface an inferred goal before evaluating a design against it;
- documented that individual installed skills remain useful without `.ux/` or the full suite.

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
