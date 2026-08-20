---
name: accessibility
description: Review UX design intent and available implementation evidence for accessibility barriers, inclusive interaction, WCAG or Section 508 requirements, keyboard and focus behavior, semantics, dynamic announcements, content, motion, zoom/reflow, and recovery. Use when a designer asks for an accessibility review or needs accessibility behavior defined before engineering handoff.
license: MIT
metadata:
  author: Tranz007
  version: "0.1.0"
---

# Accessibility

Make accessibility part of the interaction design rather than a compliance pass at the end.

## Establish the actual target

Read `.ux/ACCESSIBILITY.md`, organizational policy, project standards, design-system accessibility documentation, and relevant platform requirements. If the project does not define a target, state what standard you are using as a review baseline rather than inventing a requirement.

## Inspect behavior, not just appearance

Review the dimensions relevant to the work, including:

- semantic structure and programmatic relationships;
- accessible names, labels, instructions, status, and errors;
- keyboard operation and visible focus;
- focus movement after navigation, validation, async updates, dialogs, and errors;
- screen-reader announcements for meaningful dynamic change;
- reading and interaction order;
- contrast when actual values can be verified;
- zoom, text resize, reflow, orientation, and responsive behavior;
- target size and pointer alternatives;
- motion, timing, auto-updating, or flashing content;
- cognitive load, error prevention, and recovery;
- alternatives for sensory-only cues;
- authentication or verification interactions that may create barriers.

Use established accessible behavior from the design system rather than redesigning it locally.

## Separate design findings from verification

A static design can reveal missing intent but cannot prove runtime accessibility. Code inspection can reveal likely behavior but does not replace keyboard, browser, screen-reader, zoom/reflow, or other appropriate testing.

Never claim WCAG or Section 508 compliance solely from a design review.

## Output

Lead with barriers that can block task completion or create exclusion. For each material issue, state the condition, expected accessible behavior, available evidence, and what must be verified in implementation.

Avoid dumping the entire WCAG checklist when most criteria are irrelevant to the artifact.

## Examples

- "Accessibility-review this flow."
- "What does engineering need to implement here for keyboard and screen readers?"
- "Check this against our 508 expectations."
- "Can I call this WCAG compliant yet?"
