# Architecture

UX Skills is a practitioner-support system built from small Agent Skills. The product experience should feel simpler than the implementation.

## Layers

### Core behavior

Every skill should inherit five ideas even when it does not display them explicitly:

- **Context** — inspect the product, users, design system, engineering environment, and prior decisions before recommending work.
- **Evidence** — keep known, inferred, assumed, unknown, and conflicted information distinct.
- **System** — prefer existing components and patterns; compose before extending; extend before creating.
- **Clear** — reduce reading effort, remove generic AI language, and adapt the communication to the reader.
- **Trust** — do not invent evidence, rationale, requirements, certainty, or implementation status.

### UX practice

Skills such as `frame`, `challenge`, `flow`, `blindspots`, `state-sweep`, `critique`, `content`, `compare`, and `test-it` help a practitioner reason about the work.

### Design system

`system-fit` and `impact` help designers decide whether work belongs inside the existing system and understand consequences of changes.

### Engineering bridge

`handoff`, `contract`, `ship`, `tickets`, `pr`, and `pr-review` preserve design intent as work becomes implementation.

## Routing

The system supports two modes at the same time.

**Natural language** is the default. A designer can say "what am I missing?" or "get this ready for engineering" and the relevant skill should be discoverable from its metadata.

**Explicit invocation** is a shortcut for experienced users who know they want `state-sweep`, `system-fit`, or another named capability.

`ux-partner` is the broad router for ambiguous UX work. It should choose the smallest useful set of capabilities rather than running a fixed ceremony.

## Context is optional, not a gate

`setup-ux` creates a `.ux/` context layer in the consuming project. Skills should use it when present and remain useful when it is incomplete or absent.

Do not stop useful work simply because a context file is missing. Inspect available artifacts, label uncertainty, make conservative defaults only when safe, and ask when the answer materially changes the recommendation.

## Progressive disclosure

The Agent Skills format loads names and descriptions first, then the full `SKILL.md` only when selected. Keep routing descriptions sharp and skill bodies compact. Large reference material should remain optional.

## Composition

Skills may conceptually compose, but users should not be forced to orchestrate them. A request to ship work may require state coverage, system-fit checks, decision capture, and a handoff. The agent should perform only the checks that are relevant.

Do not create circular process dependencies or require every upstream artifact to exist before downstream help can happen.

## Boundaries

UX Skills does not claim to replace:

- user research;
- professional accessibility testing;
- design judgment;
- framework-specific engineering standards;
- security review;
- legal or regulatory review;
- product management decisions.

It can make those needs visible, preserve their outputs, and help teams act on them.
