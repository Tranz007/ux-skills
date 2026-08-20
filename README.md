# UX Skills

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

UX Skills learns the project, the design system, the engineering environment, accessibility expectations, terminology, and important existing decisions.

**That's the setup.**

After that, work normally.

> Challenge this idea.
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

## What happens in the background

UX Skills quietly helps the agent:

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

## Three small context files

`setup-ux` creates only what the skills need to stop asking the same questions repeatedly:

```text
.ux/
├── CONTEXT.md
├── DESIGN-SYSTEM.md
└── DECISIONS.md
```

`CONTEXT.md` holds the useful project basics: product, users, research/evidence locations, engineering environment, accessibility expectations, terminology, and important constraints.

`DESIGN-SYSTEM.md` tells UX Skills where the real system lives and how the team expects it to be used: Figma, Storybook, packages, tokens, source-of-truth rules, and contribution expectations.

`DECISIONS.md` preserves the consequential decisions people otherwise forget. If the team already uses ADRs or another decision system, UX Skills uses that instead.

The designer does not have to keep these perfectly maintained. Skills inspect the actual project when they can and update their understanding as they work.

## The skills under the hood

| Skill | What it helps with |
|---|---|
| `setup-ux` | Learns the project once |
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
| `clear` | Keeps AI output direct, readable, and human |

Only `setup-ux` is something a designer needs to deliberately run. The rest are designed to be selected from normal language when they are useful.

## A few rules every skill follows

**Explore before asking.** If the answer is already in the project, find it.

**Don't fake evidence.** Known, inferred, assumed, and unknown are not the same thing.

**Use the system.** Reuse and compose before adding another component.

**Keep it human.** No corporate AI sludge, giant templated responses, or documentation theater.

**Don't make engineering guess.** Preserve behavior, states, accessibility intent, and rationale when work crosses the design/engineering boundary.

## Example

A designer says:

> We need a searchable station selector. Help me design it.

UX Skills may quietly determine that:

- the request needs a little framing before solutioning;
- the current design system already has `MultiSelect` and autocomplete patterns;
- the proposed behavior has missing loading, no-results, keyboard, and async states;
- extending the existing pattern has a smaller ripple than creating a new component.

The designer gets the useful answer. They do not have to orchestrate four skills themselves.

## Portable by design

UX Skills follows the open [Agent Skills](https://agentskills.io/) format. It is intended to work across agents that support the format rather than being tied to one model or one design tool.

## Principles

1. If the designer has to learn the system before it can help them, we failed.
2. The human owns the design.
3. Ask only when the answer changes the work.
4. Prefer evidence over confidence.
5. Prefer the existing system over unnecessary invention.
6. Keep the reasoning attached to the design all the way into engineering.

## Contributing

Read [`CONTRIBUTING.md`](CONTRIBUTING.md). The goal is not the largest skill library. Add something only when it solves a real, repeatable practitioner problem without making the UX of UX Skills harder.

## License

MIT © Tony Moura
