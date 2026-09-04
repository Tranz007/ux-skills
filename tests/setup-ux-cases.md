# setup-ux evaluation cases

Use these cases to evaluate setup behavior manually or through a model-specific harness. The target is not identical wording. The target is the behavioral contract.

For every case, record the agent/model, what context was available, questions asked, files created or changed, and whether each must/must-not criterion passed.

## 1. Greenfield — vague idea

**Starting point**

> I want to build something that helps people plan trips with AI. Run setup-ux.

**Must**

- recognize that this is greenfield;
- begin with the idea rather than pretending project evidence exists;
- ask one or a small number of high-value questions at a time;
- clarify why the product should exist, who is affected, and the core outcome before hardening implementation detail;
- preserve unsupported user claims as inferred, assumed, or unknown;
- create `INTENT.md` only once there is enough clarity to guide work.

**Must not**

- run a long fixed discovery questionnaire;
- invent a traveler persona, research finding, market demand, or success metric;
- create a large folder tree of empty UX artifacts.

## 2. Greenfield — well-formed idea

**Starting point**

The user provides a concise product concept, target users, primary task, explicit scope, constraints, and success measure, then runs `setup-ux`.

**Must**

- use the supplied information instead of asking the user to repeat it;
- ask only for a missing answer that would materially change future UX work;
- write a compact `INTENT.md` and supporting context.

**Must not**

- manufacture extra discovery work merely because setup is greenfield;
- require every optional intent heading to be complete.

## 3. Existing product — strong documentation

**Starting point**

A repository contains a clear README, product brief, research links, Storybook, accessibility guidance, and ADRs. No `.ux/` directory exists.

**Must**

- inspect those sources first;
- create intent and context primarily from evidence already present;
- point to authoritative sources instead of copying large documents;
- ask only about material gaps or contradictions.

**Must not**

- ask the designer to explain the product before inspecting it;
- create a competing decision-record system when ADRs already exist.

## 4. Existing product — code with weak documentation

**Starting point**

The repository has a working product but sparse product documentation and no research.

**Must**

- derive observable mechanics and journeys from the implementation when possible;
- distinguish those mechanics from inferred product intent;
- ask concise questions about material intent that code cannot establish;
- leave unsupported user needs or success criteria unknown.

**Must not**

- claim that current implementation proves why the product exists;
- convert interface behavior into user research.

## 5. Existing product — docs conflict with implementation

**Starting point**

The product brief says password login only. The current implementation includes password and SSO. There is no decision record explaining the change.

**Must**

- mark the relevant context as conflicted;
- distinguish observable implementation from documented intent;
- ask only if resolving the conflict could materially change future UX recommendations.

**Must not**

- silently choose whichever source is newer or more convenient;
- rewrite intent as if SSO was always intended.

## 6. Existing product — no user evidence

**Starting point**

The team has product documentation and a design system but no research, analytics, support evidence, or validated personas.

**Must**

- record what is actually known about affected people from authoritative product decisions;
- preserve user-behavior claims as assumptions or unknowns;
- allow setup to finish if the missing evidence does not block useful work.

**Must not**

- invent personas, pain points, quotes, behaviors, or research findings;
- demand research before any UX work can begin.

## 7. Existing product — research-rich

**Starting point**

The project has multiple research reports, analytics, and support data.

**Must**

- point to authoritative evidence rather than copying reports into `.ux/`;
- keep the four core files small;
- split to something like `.ux/evidence/research.md` only if repeated use or density makes the split useful.

**Must not**

- summarize every study during setup;
- create optional evidence files just because evidence exists.

## 8. Existing product — no design system

**Starting point**

The repository has one-off components but no formal Storybook, Figma library, tokens package, or design-system rules.

**Must**

- record that no authoritative design system was found;
- point to reusable product patterns that actually exist when useful;
- preserve uncertainty around contribution rules.

**Must not**

- pretend a design system exists;
- turn setup into a design-system creation project.

## 9. Migration — v0.1 context exists

**Starting point**

```text
.ux/
├── CONTEXT.md
├── DESIGN-SYSTEM.md
└── DECISIONS.md
```

The files contain useful project-specific information.

**Must**

- preserve all existing useful content and links;
- add `INTENT.md` from authoritative evidence;
- move content only when ownership becomes clearly better;
- ask only for material intent gaps.

**Must not**

- delete and regenerate `.ux/`;
- rewrite the three existing files merely to fit the v0.2 template.

## 10. Refresh — routine design change

**Starting point**

`INTENT.md` exists. The team changed a modal layout and runs `setup-ux` to refresh context.

**Must**

- preserve intent unless the change actually alters purpose, people, outcome, scope, constraints, or success;
- refresh only context that materially changed.

**Must not**

- rewrite `INTENT.md` because a UI implementation changed.

## 11. Refresh — product intent changed

**Starting point**

The original product was designed for individual consumers. A documented strategy decision now makes enterprise administrators the primary buyer and introduces a distinct administrator workflow.

**Must**

- surface that the current intent may no longer describe the product accurately;
- update `INTENT.md` using the documented decision and preserve material uncertainty;
- keep implementation details in context rather than overloading intent.

**Must not**

- retain stale intent merely because it was written first;
- treat the strategy shift as a minor UI decision.

## 12. Progressive context — simple task after setup

**Starting point**

A complete `.ux/` directory includes intent, context, design system, decisions, research pointers, journeys, and technical constraints. The designer asks:

> Rewrite this validation message so it is clearer.

**Must**

- use only the smallest relevant context, such as current UI content and established terminology;
- activate content/clear behavior as needed.

**Must not**

- load every project-context file merely because it exists;
- force product discovery into a small copy-editing task.

## 13. Progressive context — consequential product decision

**Starting point**

The same project. The designer asks:

> Should we remove guest checkout and require an account before purchase?

**Must**

- use `INTENT.md` because user outcome, scope, and success can change the recommendation;
- retrieve relevant user/evidence and journey context;
- surface uncertainty where evidence is incomplete.

**Must not**

- answer from design-system patterns alone;
- treat a consequential journey change as a visual preference.

## 14. Refresh — intent clarification

**Starting point**

`INTENT.md` says the product should let first-time applicants understand permit requirements before submitting. New usability evidence confirms that users need to know which documents are required before they begin the form. This makes an existing intent more precise without changing the product direction.

**Must**

- preserve the existing intent and make only the smallest clarification needed;
- cite or point to the new evidence when practical;
- keep the refinement focused on the intended experience rather than implementation detail.

**Must not**

- regenerate the whole intent file;
- treat a clarification as a new product strategy;
- change unrelated intent sections.

## 15. Refresh — implementation tries to rewrite intent

**Starting point**

`INTENT.md` says a user must be able to complete checkout without creating an account. The implementation now requires account creation because it was easier to build, and no product decision changed the intended outcome.

**Must**

- preserve the existing guest-checkout intent;
- identify the implementation as drift rather than evidence of changed intent;
- surface the conflict for correction or an explicit consequential product decision.

**Must not**

- rewrite intent to match the implementation;
- remove the guest-checkout constraint because it is inconvenient;
- claim that shipped code proves the product direction changed.

## 16. Setup — working state stays optional

**Starting point**

A designer runs `setup-ux` on a large existing product with extensive documentation.

**Must**

- create or refresh only the four durable core context files unless progressive context is genuinely justified;
- document the product and environment without creating execution tracking.

**Must not**

- create `.ux/STATE.md` merely because the product is large;
- create a checklist, phase tracker, progress dashboard, or long-horizon plan during setup;
- treat working state as durable project context.
