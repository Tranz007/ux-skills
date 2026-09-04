# UX Skills visual flows

This page collects the core flows that explain how UX Skills behaves. The same diagrams appear near the relevant concepts elsewhere so readers do not have to come here first.

## Designer experience

```mermaid
flowchart LR
    A[Install UX Skills] --> B[Run setup-ux once]
    B --> C[Talk normally]
    C --> D[Relevant UX capability activates]
```

The public experience stays simple even as the internal reasoning becomes more capable.

## Intent, context, and skills

```mermaid
flowchart TB
    U[Designer request] --> I[Intent<br/>Why, outcome, people, scope, success]
    I --> C[Context<br/>What is true about the product and environment]
    C --> S[UX Skills<br/>Relevant practitioner capability]
    S --> W[Designer + agent do the work]
```

Intent tells the agent what good means. Context tells it what is true. Skills tell it how to reason about the UX problem.

## New-project setup

```mermaid
flowchart TB
    A[setup-ux] --> B[Start with the idea in the designer's words]
    B --> C[Identify the highest-value unknown]
    C --> D[Ask one or a small number of related questions]
    D --> E{Enough intent to guide work?}
    E -->|No| C
    E -->|Yes| F[Draft INTENT.md]
    F --> G[Designer corrections override inference]
    G --> H[Create smallest supporting context]
    H --> I[Ready to work normally]
```

The loop is adaptive. It is not a fixed UX questionnaire.

## Existing-project setup

```mermaid
flowchart TB
    A[setup-ux] --> B[Inspect repo, docs, evidence, design system]
    B --> C[Separate observable behavior from intended outcome]
    C --> D[Draft product intent from authoritative evidence]
    D --> E{Material gap or conflict?}
    E -->|Yes| F[Ask only what cannot be discovered reliably]
    E -->|No| G[Write or refresh INTENT.md]
    F --> G
    G --> H[Preserve and refresh supporting context]
    H --> I[Ready to work normally]
```

## v0.1 context migration

```mermaid
flowchart LR
    A[Existing three-file .ux/] --> B[Preserve current files]
    B --> C[Draft INTENT.md from evidence]
    C --> D[Resolve only material intent gaps]
    D --> E[Four-file core context]
```

Migration should add orientation without churning established project memory.

## Progressive project context

```mermaid
flowchart LR
    R[Current request] --> I{Can purpose, outcome,<br/>scope or success change the answer?}
    I -->|Yes| N[Read INTENT.md]
    I -->|No| P[Skip intent if irrelevant]
    N --> C[Select smallest relevant project context]
    P --> C
    C --> S[Activate relevant UX skill or skills]
    S --> O[Useful response]
```

The whole `.ux/` directory is not mandatory context for every request.

## Progressive skill disclosure

```mermaid
flowchart LR
    A[Natural-language request] --> B[Skill description matches]
    B --> C[Load SKILL.md]
    C --> D{Need deeper guidance?}
    D -->|Yes| E[Load only relevant reference]
    D -->|No| F[Proceed]
    E --> F
```

A `SKILL.md` should remain the routing and reasoning core. Reference files earn their existence by reducing irrelevant context or isolating independently reusable guidance.

## Intent lifecycle

```mermaid
flowchart TB
    A[Current INTENT.md] --> B[Design, build, learn]
    B --> C[New evidence or consequential decision]
    C --> D{Does it change purpose, outcome,<br/>people, scope, constraints or success?}
    D -->|No| E[Keep intent unchanged]
    D -->|Yes| F[Update INTENT.md]
    F --> A
    E --> A
```

Routine interface changes should not create intent churn.

## Evidence status

```mermaid
flowchart TB
    A[Material claim] --> B{What supports it?}
    B --> C[KNOWN]
    B --> D[INFERRED]
    B --> E[ASSUMED]
    B --> F[UNKNOWN]
    B --> G[CONFLICTED]
    C --> H[Recommendation or decision]
    D --> H
    E --> H
    F --> H
    G --> H
```

The purpose of these statuses is not labeling ceremony. It is preventing plausible AI output from silently becoming product truth.
