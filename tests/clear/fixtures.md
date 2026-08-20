# Clear fixtures

## Fixture 1 — corporate AI slop

### Input

> In today's rapidly evolving digital landscape, creating a seamless and intuitive booking experience is more important than ever. By leveraging a holistic, user-centric approach, we can unlock meaningful opportunities to enhance the overall customer journey. Key considerations include usability, accessibility, and technical feasibility. Ultimately, this initiative has the potential to drive engagement, improve satisfaction, and deliver meaningful business value.

### Must

- remove generic scene-setting;
- remove unsupported outcome claims;
- reduce word count materially;
- preserve any real claims that remain.

### Must not

- replace the paragraph with different promotional language;
- invent evidence or metrics;
- add a motivational conclusion.

## Fixture 2 — overstructured handoff

### Input

A handoff contains eight top-level headings, every paragraph begins with bold inline labels, and the same recovery behavior is explained in Overview, User Experience, Edge Cases, Engineering Notes, and Acceptance Criteria.

### Must

- consolidate duplicate behavior;
- put actionable implementation information first;
- retain required acceptance behavior;
- keep unresolved decisions visible.

### Must not

- delete a behavior because it is repetitive if no authoritative version remains;
- turn technical requirements into vague prose.

## Fixture 3 — uncertainty laundering

### Input

> Users prefer receiving proactive notifications because it reduces anxiety and improves trust. We should therefore notify them immediately whenever a schedule change occurs.

Context: there is no user research in the project; the statement came from a stakeholder brainstorm.

### Must

- preserve the proposed idea but identify the preference claim as unsupported;
- avoid presenting reduced anxiety or improved trust as known outcomes.

### Must not

- make the unsupported statement sound more polished and therefore more credible.

## Fixture 4 — engineer audience

### Input

A designer provides three paragraphs about how an error state should "feel reassuring" but does not state whether entered form data persists, where focus moves, whether retry is possible, or how server errors map to messages.

### Must

- surface the missing behavior before polishing the prose;
- organize the output around implementation-relevant questions.

### Must not

- invent the missing behavior.
