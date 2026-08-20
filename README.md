# UX Skills

**Your AI design partner should know UX.**

UX Skills is an open-source suite of Agent Skills for working designers, researchers, design-system teams, and design engineers.

Most design skills teach an agent how to generate UI. UX Skills takes a different position: **the human owns the design. The skills help the human understand the problem, challenge assumptions, find blind spots, use the design system, preserve decisions, validate behavior, and carry design intent through engineering.**

## Try it

```bash
npx skills@latest add Tranz007/ux-skills
```

Then talk normally:

> What am I missing?
>
> Challenge this idea.
>
> Does this need a new component?
>
> Review this flow before I show it to engineering.
>
> Get this ready for a PR.
>
> I just inherited this project. Help me understand it.

You can invoke individual skills explicitly, but **commands are shortcuts, not the interface**. Natural language is the interface.

## Start here

Run `setup-ux` once in a project. It explores before it asks questions and creates a lightweight `.ux/` context layer from what it can actually discover.

```text
.ux/
├── PRODUCT.md
├── USERS.md
├── DESIGN-SYSTEM.md
├── ENGINEERING.md
├── ACCESSIBILITY.md
├── RESEARCH.md
├── WORKFLOW.md
├── GLOSSARY.md
├── VOICE.md
└── DECISIONS.md
```

Missing information is allowed. UX Skills records it as unknown and asks only when it matters. Configuration happens through use.

## The core behavior

Every skill follows five rules:

**Context** — understand the product and environment before recommending work.

**Evidence** — distinguish known, inferred, assumed, unknown, and conflicted information.

**System** — reuse and compose existing patterns before proposing new ones.

**Clear** — write like a practitioner, not a generated document.

**Trust** — never invent evidence, rationale, requirements, implementation status, or confidence.

## The skills

### Start something

| Skill | Use it for |
|---|---|
| `ux-partner` | Natural-language router and design partner for ambiguous UX work |
| `setup-ux` | Learn a project, design system, engineering stack, and working rules |
| `orient` | Understand an inherited product, repo, design system, or project |
| `frame` | Turn a request or idea into the actual problem, outcome, constraints, and unknowns |
| `challenge` | Make an idea earn the right to exist before execution begins |
| `evidence` | Separate what is known from what is assumed and identify evidence gaps |

### Explore and review

| Skill | Use it for |
|---|---|
| `flow` | Work through journeys, branches, interruptions, and recovery paths |
| `blindspots` | Find people, conditions, contexts, and consequences nobody has considered |
| `state-sweep` | Find missing loading, empty, error, partial, permission, timeout, and recovery states |
| `critique` | Review work across user, product, accessibility, system, and engineering perspectives |
| `compare` | Compare alternatives against explicit decision criteria rather than aesthetics |
| `content` | Review UX copy, terminology, timing, cognitive load, errors, and recovery language |
| `test-it` | Turn decisions, risks, and assumptions into a focused validation plan |

### Work with the system

| Skill | Use it for |
|---|---|
| `system-fit` | Decide whether to reuse, compose, extend, or create a component/pattern |
| `impact` | Trace the downstream effects of a design or system change |
| `why` | Reconstruct why something appears to have been designed this way |
| `decision` | Capture consequential design or architecture decisions without documenting trivia |

### Bridge to engineering

| Skill | Use it for |
|---|---|
| `handoff` | Create an implementation-ready design handoff focused on behavior and intent |
| `contract` | Express behavior as a precise design-to-engineering contract |
| `ship` | Check completeness and package approved work for engineering |
| `tickets` | Break design intent into buildable engineering work without losing UX context |
| `pr` | Create a PR description engineers can actually review |
| `pr-review` | Review implementation changes against design intent, states, accessibility, and system rules |

### Communication

| Skill | Use it for |
|---|---|
| `clear` | Remove AI slop, reduce reading effort, preserve meaning, and tailor communication to the reader |

## The UX context model

UX Skills never requires a perfect configuration file before it can help. If `.ux/` exists, skills read the relevant context. If it does not, they inspect what is available and proceed carefully.

Information is treated as:

- **Known** — supported by evidence or an authoritative source.
- **Inferred** — strongly suggested by available information.
- **Assumed** — currently treated as true without sufficient evidence.
- **Unknown** — not enough information yet.
- **Conflicted** — credible sources disagree.

These labels are surfaced only when the distinction matters. The system should not turn every response into a taxonomy.

See [`docs/context.md`](docs/context.md) for the full context contract.

## Design to merged PR

UX Skills is intentionally not a frontend-generation framework. It protects design intent as work crosses into implementation.

```text
request / idea
     ↓
frame → evidence → challenge
     ↓
flow → system-fit → state-sweep
     ↓
critique → test-it → decision
     ↓
handoff → contract → tickets
     ↓
implementation
     ↓
pr → pr-review
```

Use only what the work needs. The router should not run a ceremony because a diagram says it can.

## Why this exists

A design loses information every time it changes hands. Research becomes a summary. A decision becomes a Figma comment. Behavior becomes a screenshot. Engineering gets a ticket. Six months later nobody remembers why anything works the way it does.

UX Skills is designed to keep the reasoning attached to the work without making the designer become a documentation machine.

## Portability

UX Skills follows the open [Agent Skills](https://agentskills.io/) format. Each skill is a directory containing a `SKILL.md` with portable metadata and instructions. Vendor-specific features are optional rather than required.

Validate a skill with the reference implementation:

```bash
skills-ref validate ./skills/frame
```

## Principles

1. If a designer has to learn how UX Skills works before it can help, we failed.
2. Explore before asking questions.
3. Ask only when the answer changes the work.
4. Commands are shortcuts, not the interface.
5. Do not replace practitioner judgment with process theater.
6. Prefer evidence over confidence.
7. Prefer the existing system before creating a new one.
8. Preserve behavior and rationale, not pixels alone.
9. Make the output easier to read than the input.
10. Stay with the design from the first question to the merged PR.

## Project status

UX Skills is early and intentionally opinionated. The first goal is a small, high-quality foundation that can be evaluated against real design work before the catalog grows.

See [`docs/roadmap.md`](docs/roadmap.md) for what is next.

## Contributing

Read [`CONTRIBUTING.md`](CONTRIBUTING.md). New skills should solve a real practitioner problem, be composable, route well from natural language, and avoid duplicating capabilities already in the suite.

## License

MIT © Tony Moura
