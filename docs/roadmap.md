# Roadmap

UX Skills should grow because real designers expose a missing capability, not because a large catalog looks impressive.

## v0.1 — foundation

- install the suite;
- run `setup-ux` once;
- let normal designer language activate the right capability;
- understand who the work serves and what user evidence actually exists without forcing UX ceremony;
- understand the team's real design system;
- challenge assumptions and catch blind spots/states/accessibility issues;
- keep AI output clear and human;
- preserve UX intent through handoff and PR descriptions;
- validate skill format and routing examples.

## v0.2 — intent and progressive context

- support both greenfield and existing products through the same `setup-ux` entry point;
- capture a small `INTENT.md` that separates intended outcome from current implementation;
- preserve known, inferred, assumed, unknown, and conflicted information without turning every sentence into metadata;
- load project context progressively instead of treating the whole `.ux/` directory as mandatory prompt context;
- split context into smaller files only when density or repeated use justifies it;
- keep `SKILL.md` files compact and move deeper reusable guidance to references only when retrieval benefits from the split;
- document major flows visually with Mermaid;
- preserve the original three-file `.ux/` context when migrating existing installations;
- add setup-specific evaluation cases and realistic example contexts.

## Next — prove the architecture with real work

- test greenfield intent capture with designers starting from vague and well-formed product ideas;
- test existing-product setup against repos with strong docs, weak docs, conflicting docs/code, and varying levels of research evidence;
- test natural-language activation across multiple skills-compatible agents and models;
- measure whether progressive context reduces repeated questions and irrelevant context without weakening recommendations;
- improve design-system discovery for Storybook, Figma, packages, and tokens;
- add more realistic examples only where they teach behavior that documentation does not;
- tighten skill descriptions when the wrong capability activates or nothing activates;
- capture issues from external adopters before expanding the skill catalog.

## Later

Add another skill only when it solves a repeatable practitioner problem that the current suite cannot handle cleanly.

Potential areas include deeper research synthesis, workshop support, service design, localization, and deeper design-system governance. None of these are commitments.

## What we will not optimize for

- the largest skill count;
- a UX Skills app or platform;
- mandatory ceremony;
- personas or research artifacts without a decision need;
- replacing research with synthetic certainty;
- agent-generated visual novelty for its own sake;
- copying every vendor-specific agent pattern;
- vendor lock-in.
