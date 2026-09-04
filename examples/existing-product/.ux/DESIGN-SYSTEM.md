# Design system

Fictional existing-product example.

## Sources

Figma: `design/figma-links.md`
Storybook: `apps/web/.storybook/`
Repository/package: `packages/ui/`
Tokens/docs: `packages/tokens/` and Storybook foundations

## Source of truth

- component behavior and supported variants: `packages/ui/` + Storybook;
- visual design and composition examples: Figma library referenced in `design/figma-links.md`;
- tokens: `packages/tokens/`.

If sources disagree, do not silently choose one. Surface the conflict and follow the contribution process.

## Working rules

Reuse an existing component or compose existing primitives before proposing a new component. New reusable variants require a design-system issue and review before product-local implementation becomes the new convention.

## Known gaps

The file-upload pattern has inconsistent error and progress behavior across two product areas. Track the existing design-system issue rather than creating another local pattern.
