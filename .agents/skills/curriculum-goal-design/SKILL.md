---
name: curriculum-goal-design
description: Design, split, merge, order, or revise learning goals for the AI-native Builder curriculum. Use when Codex needs to change gNN goal boundaries, prerequisites, dependency order, curriculum maps, or goal-level scope; do not use for authoring lesson content or composing sessions from approved goals.
---

# Curriculum goal design

Turn program intent into a coherent dependency graph of observable learning goals. Treat a goal as a capability contract, not a topic heading.

## Establish authority and scope

1. Read `.agents/rules/README.md` and every rule it routes to.
2. Read `AI-native-builder-curriculum-plan.md`, `curriculum-content-architecture.md`, and `ai-native-builder/curriculum-map.md`.
3. Inspect every existing goal and run that may produce, consume, or reference the affected capability.
4. Classify the request as `add`, `split`, `merge`, `reorder`, `rename`, `retire`, or `clarify`. A request may contain more than one operation.
5. Decide which layer owns the change:
   - change the plan only for program purpose, audience, scope, duration, or promised outcomes;
   - change the content architecture for goal definitions or dependencies;
   - change the curriculum map for teaching order and relationships;
   - change goal folders only after the goal contract is approved;
   - change runs only to reflect approved goal order and coverage.

If the sources or participants disagree on a premise that changes the design, apply the conflict-resolution protocol in `.agents/rules/README.md`. Do not mutate dependent files until the conflict is resolved and recorded.

## Diagnose the proposed change

State the problem before proposing a new structure:

- What learner failure or program constraint does the change address?
- Is the issue truly a missing goal, or is it missing practice, evidence, scaffolding, or session time?
- What can the learner already do immediately before this point?
- What new decision or behavior must become possible immediately after it?
- Which later goal consumes the resulting capability or artifact?

Do not create a goal solely because a topic is important. Keep a capability cross-cutting when it must recur inside several goals, as with reading and intervening in code.

## Write the goal contract

Define each affected goal with all fields below:

| Field | Requirement |
|---|---|
| Learner problem | A concrete obstacle faced at this point in the progression. |
| Observable outcome | One primary behavior the learner can demonstrate. |
| Boundary | What belongs here and what explicitly belongs elsewhere. |
| Prerequisites | Prior capabilities and incoming artifacts actually consumed. |
| Learner decisions | Important choices the learner must own rather than delegate to AI. |
| AI role | How AI proposes, executes, critiques, or converses in support of the outcome. |
| Code contact | What the learner observes, explains, reviews, changes, or diagnoses; use `none` when justified. |
| Artifact | A reviewable object that persists beyond the activity. |
| Completion evidence | Observable proof that the artifact demonstrates the outcome. |
| Failure and safety | Likely failure modes and relevant risk boundaries. |
| Enables | The exact capability or artifact supplied to later goals. |

Use one dominant outcome per goal. Split a goal when its outcomes have different prerequisites, artifacts, or evidence. Merge goals when they express the same learner decision and cannot produce independent evidence.

## Validate the dependency graph

1. Trace every prerequisite backward to a goal or an explicit in-lesson scaffold.
2. Trace each artifact forward to the goal or run that consumes it.
3. Detect cycles, orphan goals, duplicated outcomes, unused artifacts, and unsupported jumps in difficulty.
4. Preserve the canonical progression unless evidence justifies a change: orientation → spec → system map → harness → agent control → verification → tools/context → advanced harness → ship → capstone.
5. Confirm that the workshop can still end at an internally verified prototype and that the full path can still reach the promised capstone.
6. Treat `gNN` as a stable identity. Do not renumber existing goals to express order. Assign a new goal the next unused ID and a lowercase ASCII kebab-case slug.

For a reorder, explain both edges: why the goal no longer depends on its old predecessor and why its new predecessor is sufficient.

## Present the design before implementation

Return a design review containing:

1. **Decision** — the proposed operation and why it solves the diagnosed problem.
2. **Before/after** — affected goals and dependency edges.
3. **Goal contracts** — complete contracts for added or materially changed goals.
4. **Impact map** — canonical documents, goal folders, runs, shared assets, and reviews affected.
5. **Alternatives** — credible alternatives considered and why they were rejected.
6. **Uncertainty** — unresolved evidence, assumptions, and product preferences requiring the user's decision.

Do not treat a provisional suggestion as approval to edit the curriculum.

## Apply an approved design

1. Update canonical documents from highest to lowest authority.
2. Create, rename, or retire the matching `ai-native-builder/goals/gNN-*` folder only within the approved operation.
3. Update affected runs by reference; never copy lesson content into `runs/`.
4. Preserve stable identifiers and unrelated user content.
5. Record decisions where future authors can discover why the structure changed.

## Verify and hand off

- Run the architecture-relevant hard gates and quality criteria in `.agents/rules/quality-gates.md` with file-level evidence.
- Confirm canonical documents agree and every referenced path exists.
- Use `$learner-artifact-design` when the artifact contract needs detailed design.
- Use `$lesson-authoring` only after the goal boundary is approved.
- Use `$learning-path-composition` to schedule approved goals without changing them.
- Use `$curriculum-quality-review` for independent acceptance.

The work is not complete while a dependency is unexplained, a goal duplicates another capability, or canonical sources disagree.
