# Project context

Fictional existing-product example.

## Product mechanics

Observable current journeys:

- browse permit types;
- sign in or create an account;
- complete a multi-step permit application;
- upload supporting documents;
- pay fees when required;
- view application status;
- respond to requests for additional information.

Source: current application routes and `docs/service-map.md`.

## Users and evidence

Research index: `research/README.md`

Current sources include:

- `research/permit-intake-summary.md` — moderated sessions with first-time and repeat applicants;
- `analytics/funnel-dashboard.md` — application-step completion and abandonment;
- `support/top-contact-reasons.md` — categorized support contacts.

Do not treat support volume alone as proof of user prevalence or severity.

## Engineering

Frontend: React + TypeScript
Component documentation: Storybook
Issue workflow: GitHub Issues
PR workflow: GitHub pull requests with preview builds

Source: `package.json`, `.github/`, and `docs/engineering.md`.

## Accessibility

Source: `docs/accessibility.md`

The organization documents WCAG 2.2 AA as its product target and requires keyboard and screen-reader verification for public workflows. This context records the requirement; it does not prove current compliance.

## Terminology

- **application** — a resident's submitted or in-progress permit request;
- **permit type** — the service/category the resident is applying for;
- **request for information** — a staff follow-up requiring the applicant to provide missing or corrected material.

## Material unknowns

- whether SSO is a permanent product requirement;
- whether the numeric success target in the older roadmap is still active.
