# Authoring UX Skills

A UX Skill is not a prompt template for producing a UX artifact. It is a reusable practitioner capability.

## Start with the trigger

Write down what a designer would naturally say before naming the skill.

Good triggers:

- "What am I missing?"
- "Does this really need a new component?"
- "Challenge this before I start designing."
- "Engineering needs to understand how this behaves."

Weak triggers are artifact names alone, such as "create a persona" or "make a journey map." Those often describe outputs rather than practitioner problems.

## Keep invocation invisible

With the exception of `setup-ux`, skills should be designed for model-driven activation from normal language. Do not require the designer to memorize the skill name.

`setup-ux` is intentionally explicit because it initializes or refreshes project context. Its metadata records `ux-skills-invocation: "explicit"`; this is descriptive portable metadata, not a vendor-specific requirement.

## Frontmatter

Use valid Agent Skills metadata.

```yaml
---
name: state-sweep
description: Find missing UI and service states such as loading, empty, partial, permission, timeout, failure, and recovery. Use when a designer asks what states, edge cases, or recovery behavior are missing from a flow, screen, component, or feature.
license: MIT
metadata:
  author: Tranz007
  version: "0.1.1"
---
```

The description is routing metadata. Include both what the skill does and when ordinary language should activate it.

## Shared behavior is part of every skill

Repository-level instructions are not guaranteed to travel with an installed skill. For portability, every `SKILL.md` includes the same compact `## Always` section:

```markdown
## Always

- **Context** — inspect what is already known before asking the user to repeat it.
- **Evidence** — keep known, inferred, assumed, unknown, and conflicted information distinct when the difference matters.
- **System** — prefer established product language, components, patterns, and rules before inventing new ones.
- **Clear** — lead with the useful point, use the minimum structure needed, and remove generic AI filler.
- **Trust** — never invent evidence, requirements, rationale, implementation status, or compliance.

Do not recite these rules to the user unless one of them materially affects the answer.
```

Keep this section identical across skills unless the project deliberately changes the shared contract. `scripts/validate-skills.sh` enforces its presence.

`clear` remains a normal skill for rewriting existing material, but Clear is also a baseline behavior for every other skill. The goal is to produce readable work the first time rather than clean up AI prose afterward.

## Skill anatomy

Most skills should contain:

1. **Purpose** — the practitioner problem.
2. **Always** — the shared UX behavior contract.
3. **Start with context** — what to inspect before asking questions.
4. **Method** — the reasoning sequence.
5. **Output** — what useful result to produce.
6. **Guardrails** — what not to invent or overreach on.
7. **Examples** — a few natural-language triggers.

Do not add sections merely to match a template when they do not improve the skill.

## Shared output behavior

Every skill should keep output readable:

- lead with the useful finding, not a preamble;
- use the minimum structure needed for scanning;
- avoid generic praise and AI filler;
- prefer concrete observations to UX jargon;
- expose evidence status when it changes confidence;
- preserve material uncertainty;
- adapt detail to the likely reader;
- do not end with a generic summary that repeats the response.

## Ask less

Inspect available project context before questioning the user. If information is missing but the task can proceed safely, proceed and label the gap. Ask only when the answer changes the work materially.

## Do not over-orchestrate

A skill may use reasoning associated with another capability, but avoid turning every task into a fixed workflow. A quick content review should not demand a problem statement, research plan, ADR, and handoff package.

## Evaluate routing and usefulness

A skill should be tested against:

- phrases that should activate it;
- adjacent phrases that should activate a different skill;
- incomplete context;
- conflicting context;
- attempts to make the agent invent evidence;
- outputs that are technically correct but unreadably verbose.

See `tests/README.md` for the first evaluation fixtures.
