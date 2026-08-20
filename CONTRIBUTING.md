# Contributing to UX Skills

Thank you for helping make AI-assisted design work more useful to practitioners.

This project favors small, composable skills that improve how designers think, decide, validate, communicate, and collaborate with engineering.

## Before proposing a skill

Ask whether the capability helps a designer practice UX or preserve design intent. Avoid duplicating skills whose primary purpose is simply to make an agent generate prettier UI or more frontend code.

A good UX Skill should:

- solve a repeatable practitioner problem;
- work through natural language as well as explicit invocation;
- use project context instead of repeatedly asking for known information;
- ground user claims in actual evidence without inventing personas or needs;
- stay out of the way when extra research or UX process would not change the work;
- distinguish evidence from inference and assumption;
- preserve uncertainty rather than inventing confidence;
- produce concise, readable output;
- respect the existing design system and engineering environment;
- degrade gracefully when integrations are unavailable.

## Skill shape

Each skill lives in `skills/<skill-name>/SKILL.md` and follows the Agent Skills format.

Keep the frontmatter description specific enough that an agent can route to the skill from normal designer language. Put durable examples or fixtures in the skill folder when they improve reliability.

## Pull requests

Explain the practitioner problem, what changed, how you tested the skill, and any behavior or context contract that changed. For new skills, also explain when the skill should **not** activate so the suite does not add unnecessary process to simple work.

By contributing, you agree that your contribution is licensed under the MIT License.
