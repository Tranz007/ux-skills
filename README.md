# UX Skills

[![Validate Agent Skills](https://github.com/Tranz007/ux-skills/actions/workflows/validate.yml/badge.svg)](https://github.com/Tranz007/ux-skills/actions/workflows/validate.yml)

**Your AI design partner should know UX.**

UX Skills is an open-source set of Agent Skills for working designers. It does not try to replace the designer or turn the agent into an autonomous design machine. It helps the designer think better, catch what they missed, work with the real design system, and carry UX intent into engineering.

## Install it

From your project folder:

```bash
npx skills add Tranz007/ux-skills --all
```

Then run once:

```text
setup-ux
```

UX Skills learns the project, who it serves, existing user/research evidence, the design system, engineering environment, accessibility expectations, terminology, and important existing decisions.

**That's the setup.**

After that, work normally.

> Challenge this idea.
>
> Who are we actually designing this for?
>
> What am I missing?
>
> Does this need a new component?
>
> Review this before I show engineering.
>
> If I change this, what else moves?
>
> Get this ready for engineering.
>
> Write the PR description.

You do not need to know which skill handles the request. The agent chooses the relevant UX Skills automatically.

## See it in action

A designer says:

> We need an AI trip recommendation feature. Help me design it.

A useful UX Skills response starts by testing the premise instead of immediately drawing the feature:

> Before designing it, two assumptions matter. I don't see evidence yet that travelers need recommendations rather than better comparison. And recommendations will only be useful if the system knows enough about the traveler to make a defensible suggestion. Define what data it uses, how confidence is shown, and what happens when it's wrong before choosing the interaction. If the design system already has recommendation or card patterns, reuse those first.

The agent may quietly use user grounding, framing, challenge, design-system fit, evidence discipline, and Clear behavior to produce that answer. The designer does not orchestrate those capabilities.

## What happens in the background

UX Skills quietly helps the agent:

- ground work in the people affected and the evidence that actually exists;
- challenge weak assumptions instead of immediately designing them;
- separate evidence from guesses;
- catch missing states, edge conditions, and accessibility concerns;
- reuse the existing design system before inventing new components;
- see downstream effects of a UX change;
- improve UI content and terminology;
- keep explanations and documentation clear and human;
- preserve consequential design decisions;
- create engineering handoffs that explain behavior, not just pixels;
- write PR descriptions that engineers can actually review.

These are separate skills internally because that makes routing and maintenance reliable. **They are not a menu the designer has to learn.**

Every installed skill also carries the same six background rules: **Context, User, Evidence, System, Clear, and Trust.** User-centered does not mean process-heavy: the skills do not introduce research, personas, or discovery work when the user and task are already clear or the missing information would not change the work.

## Three small context files

`setup-ux` creates only what the skills need to stop asking the same questions repeatedly:

```text
.ux/
├── CONTEXT.md
├── DESIGN-SYSTEM.md
└── DECISIONS.md
```

`CONTEXT.md` holds the useful project basics: product, people and tasks, research/evidence locations, engineering environment, accessibility expectations, terminology, and important constraints. Research-backed personas or segments can be referenced when useful; UX Skills does not invent them just to fill the file.

`DESIGN-SYSTEM.md` tells UX Skills where the real system lives and how the team expects it to be used: Figma, Storybook, packages, tokens, source-of-truth rules, and contribution expectations.

`DECISIONS.md` preserves the consequential decisions people otherwise forget. If the team already uses ADRs or another decision system, UX Skills uses that instead.

The designer does not have to keep these perfectly maintained. Skills inspect the actual project when they can and update their understanding as they work.

`.ux/` improves continuity, but it is not a prerequisite. Each installed skill remains useful on its own when project context or the rest of the suite is unavailable; it should inspect what it can and preserve the resulting uncertainty.

## The skills under the hood

| Skill | What it helps with |
|---|---|
| `setup-ux` | Learns the project once |
| `user-grounding` | Asks who this is for and what we actually know — only when it matters |
| `frame` | Finds the real problem behind a request |
| `challenge` | Pushes on assumptions and weak premises |
| `blindspots` | Finds important things nobody considered |
| `state-sweep` | Finds missing states and recovery behavior |
| `critique` | Reviews UX against the actual context, not taste |
| `accessibility` | Makes accessible behavior part of the design |
| `content` | Improves UI language and terminology |
| `system-fit` | Reuse, compose, extend, or create? |
| `ripple` | Shows what else moves when something changes |
| `decision` | Preserves consequential rationale |
| `handoff` | Carries UX behavior and intent to engineering |
| `pr` | Writes useful UX-aware PR descriptions |
| `clear` | Repairs existing content; its clarity rules also run across every skill |

Only `setup-ux` is something a designer needs to deliberately run. The rest are designed to be selected from normal language when they are useful.

## A few rules every skill follows

**Explore before asking.** If the answer is already in the project, find it.

**Ground in users, not UX theater.** Understand the people, task, and context when they can change the design. Do not force personas, research, or discovery work onto simple tasks that do not need them.

**Don't fake evidence.** Known, inferred, assumed, unknown, and conflicted are not the same thing.

**Use the system.** Reuse and compose before adding another component.

**Keep it human.** Lead with the useful point. Use only the structure the reader needs. No corporate AI sludge, canned praise, repetitive summaries, or documentation theater.

**Don't make engineering guess.** Preserve behavior, states, accessibility intent, and rationale when work crosses the design/engineering boundary.

## Portable by design

UX Skills follows the open [Agent Skills](https://agentskills.io/) format. It is intended to work across agents that support the format rather than being tied to one model or one design tool.

## Principles

1. If the designer has to learn the system before it can help them, we failed.
2. The human owns the design.
3. Ask only when the answer changes the work.
4. Be user-centered without making UX process the price of simple work.
5. Prefer evidence over confidence.
6. Prefer the existing system over unnecessary invention.
7. Keep the reasoning attached to the design all the way into engineering.

## Contributing

Read [`CONTRIBUTING.md`](CONTRIBUTING.md). The goal is not the largest skill library. Add something only when it solves a real, repeatable practitioner problem without making the UX of UX Skills harder.

## License

MIT © Tony Moura
