# UX context contract

The `.ux/` directory is durable project context shared by UX Skills. It is deliberately human-readable. Teams can edit it directly and review changes in version control.

## Files

### `PRODUCT.md`

Capture product purpose, major journeys, business constraints, success measures, product terminology, and important non-goals.

### `USERS.md`

Capture known user groups, access needs, environments, constraints, and links to supporting research. Do not turn assumptions into personas presented as facts.

### `DESIGN-SYSTEM.md`

Capture authoritative sources, component libraries, tokens, documented patterns, source-of-truth rules, contribution workflow, and reuse expectations.

Useful source types include repositories, Storybook, Figma libraries, component packages, documentation sites, and token files.

### `ENGINEERING.md`

Capture implementation stack, application architecture relevant to UX, repository locations, frontend conventions, test tooling, issue tracker, release workflow, and known technical constraints.

### `ACCESSIBILITY.md`

Capture the team's actual target standards, testing expectations, assistive technologies, organizational policies, and documented exceptions. Never mark a product compliant merely because a target standard is listed here.

### `RESEARCH.md`

Capture where research, analytics, customer feedback, usability findings, and service data live. Prefer links and compact findings over duplicating entire repositories of research.

### `WORKFLOW.md`

Capture how work moves from request to design to implementation, who owns decisions, what artifacts matter, and how design-system contributions are made.

### `GLOSSARY.md`

Capture domain language, preferred UI terminology, forbidden or deprecated terms, acronyms, and semantic distinctions that matter to users or implementation.

### `VOICE.md`

Capture communication rules that actually affect outputs. Favor specific behaviors over brand adjectives.

Example:

```text
Default: direct, plain language, minimal structure.
Designers: emphasize problem, evidence, alternatives, uncertainty.
Engineers: emphasize behavior, states, components, constraints, acceptance criteria.
Stakeholders: emphasize user impact, business impact, evidence, and decision needed.
Avoid: corporate filler, unexplained jargon, promotional claims, forced optimism.
```

### `DECISIONS.md`

An index of consequential decisions or links to individual decision records. Do not log trivial visual adjustments.

## Epistemic status

When useful, context entries can be marked with one of five statuses:

- `KNOWN` — supported by evidence or an authoritative source.
- `INFERRED` — strongly suggested by available information.
- `ASSUMED` — treated as true for now without sufficient evidence.
- `UNKNOWN` — unresolved.
- `CONFLICTED` — credible sources disagree.

Do not decorate every sentence with a status. Use the model when it changes how confidently the team should act.

## Setup behavior

`setup-ux` should inspect before asking. It may look at repository files, design-system documentation, package metadata, Storybook, design files available through connected tools, accessibility configuration, tests, issue templates, and existing documentation.

It should then:

1. summarize what it found;
2. identify material gaps;
3. recommend defaults where safe;
4. ask only questions whose answers materially improve the context;
5. write or update `.ux/` files without overwriting verified human decisions silently.

## Personal context

Teams may optionally maintain `.ux.local/` for individual collaboration preferences that should not be committed.

Examples include critique intensity, desired explanation depth, or whether engineering implications should be surfaced by default.

Team rules always win over personal preferences when they conflict.
