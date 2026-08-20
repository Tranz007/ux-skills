---
name: orient
description: Rapidly orient a designer who has inherited an unfamiliar product, repository, design system, or project. Use when someone asks what is going on, where to start, how the product works, what the team appears to value, or what UX risks and inconsistencies are visible before changing anything.
license: MIT
metadata:
  author: Tranz007
  version: "0.1.0"
---

# Orient

Help the practitioner form a trustworthy mental model before they start changing things.

## Inspect first

Use `.ux/` if present, but verify it against current artifacts when possible. Explore the product structure, key journeys, design-system sources, implementation stack, research and analytics sources, workflow, terminology, open issues, and recent consequential decisions.

Do not pretend that repository structure alone reveals user needs or business intent.

## Build the mental model

Explain, in the smallest useful form:

- what this product appears to do and for whom;
- the major journeys or surfaces;
- what the design system and engineering stack appear to be;
- how design work reaches implementation;
- what is established versus inconsistent or undocumented;
- where evidence lives;
- the largest UX, system, accessibility, or handoff risks visible now.

Separate observed facts from inference. If a product purpose or team intention is inferred, say so.

## Recommend where to start

Suggest the smallest high-leverage first moves. Favor understanding and risk reduction over immediately redesigning visible screens.

If the user is joining a team, highlight questions worth asking humans because the answer is unlikely to exist reliably in artifacts.

## Communication

Sound like a practitioner handing another practitioner a useful briefing. Avoid a giant audit unless the user asks for one.

## Examples

- "I just inherited this repo. What the hell is going on?"
- "Help me understand this product before I touch anything."
- "Where should a new principal designer start here?"
- "Give me the UX lay of the land."
