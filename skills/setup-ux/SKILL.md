---
name: setup-ux
description: Discover a project's product, users, design system, engineering environment, accessibility rules, research sources, workflow, terminology, and communication preferences, then create or refresh a lightweight .ux context layer. Use when setting up UX Skills in a repo or when project context has gone stale.
license: MIT
metadata:
  author: Tranz007
  version: "0.1.0"
---

# Setup UX

Build useful project context with the least possible user effort.

## Explore before asking

Inspect what is available first. Depending on access, look for:

- `AGENTS.md`, `CLAUDE.md`, README files, architecture and product docs;
- package manifests and framework configuration;
- component libraries, Storybook, design tokens, CSS variables, theme files, and design-system packages;
- Figma or other design sources available through connected tools;
- accessibility tooling, standards, tests, and documented policies;
- research, analytics, customer feedback, product requirements, issue templates, and decision records;
- Git remotes, issue trackers, PR templates, release workflows, and test conventions;
- domain terms used repeatedly in code and documentation.

Do not ask the user to identify information you can discover reliably.

## Build the context layer

Create or refresh:

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

Keep files short and source-aware. Link to authoritative material instead of duplicating large documents.

Do not silently overwrite verified human decisions. When refreshing, preserve confirmed information and call out meaningful conflicts.

## Handle uncertainty

Missing information is not a setup failure. Record material gaps as unknown and continue.

Use these distinctions when useful:

- KNOWN — supported by evidence or an authoritative source;
- INFERRED — strongly suggested by available information;
- ASSUMED — treated as true for now without enough evidence;
- UNKNOWN — unresolved;
- CONFLICTED — credible sources disagree.

Ask only questions whose answers materially improve future UX work. Lead each question with the best recommendation or discovered default so the user can answer quickly.

## Finish with immediate value

Summarize what the system now understands, not just that setup succeeded.

Include a compact context-health view such as Product, Users, Design System, Accessibility, Research, Engineering, Terminology, and Workflow. Use qualitative levels like strong, partial, weak, or unknown; do not imply mathematical precision.

Call out one to three useful discoveries or risks if present.

## Examples

- "Set up UX Skills for this project."
- "Learn this repo before we start designing."
- "Refresh your UX context."
- "Connect our design system."
