---
name: learning-path-composition
description: Compose workshop or 1-to-1 learning paths from approved AI-native Builder goal lessons without duplicating lesson content. Use when scheduling sessions, studios, checkpoints, or paths; do not change goal definitions.
---

# Learning path composition

Compose approved goals into a feasible learner journey. A run orchestrates canonical lessons; it does not redefine or duplicate them.

## Establish the path contract

1. Read `.agents/rules/README.md`, the program plan, content architecture, curriculum map, applicable goal folders, and existing runs.
2. Record the target learner's starting capability, promised end state, delivery format, total duration, session duration, and constraints.
3. Identify required goals and optional goals from the promised outcome rather than from available time alone.
4. Confirm the intended maturity level. The three-session workshop ends at an internally verified prototype; public shipping and capstone belong to the full path.
5. Surface any request that requires changing a goal outcome or prerequisite and hand it to `$curriculum-goal-design`.

Apply the repository conflict protocol before scheduling around a disputed dependency or promise.

## Build from the dependency graph

1. Start with the terminal capability and trace prerequisites backward.
2. For each included goal, identify the incoming artifact and the artifact passed forward.
3. Preserve prerequisite order. Treat parallel goals such as tools and context as parallel only when their individual prerequisites are satisfied.
4. Detect missing prerequisites, orphan sessions, repeated outcomes, and checkpoints with no evidence.
5. If a required goal cannot fit, reduce the promised end state or expand the path; do not silently compress away practice or verification.

When combining goals in one session, justify that the learner can complete both practice loops and artifacts within the timebox. Topic similarity alone is not sufficient.

## Design each session

Give every session a contract containing:

| Field | Requirement |
|---|---|
| Primary outcome | One dominant capability for the session. |
| Goal references | Canonical `gNN` lessons used, with links. |
| Starting state | Required learner capability and incoming artifacts. |
| Learning flow | Orientation, practice, verification, and reflection blocks. |
| Time budget | Minutes per block plus transition or recovery allowance. |
| Artifact | Evidence-bearing work produced or advanced. |
| Checkpoint | How readiness for the next session is decided. |
| Recovery | What happens when the checkpoint is not met. |
| Between-session work | Optional or required work, with a time estimate. |

Use studios for integration, review, and transfer across goals, not as containers for new undeclared lesson outcomes.

## Balance the path

- Alternate new concepts with application, feedback, and consolidation.
- Keep the learner's own project continuous when continuity strengthens transfer.
- Make dependencies visible without forcing a beginner to manage unnecessary files or tools.
- Budget for setup problems, AI failure, questions, and artifact review.
- Place verification before any milestone that claims a working product.
- Place safety and permission decisions before tools, external actions, or deployment.
- Revisit code contact across goals at increasing depth; never schedule it as a detached phase.

## Author run files

Write only orchestration inside `ai-native-builder/runs/`:

- schedule, timing, goal links, artifact handoffs, checkpoints, facilitation notes, and path-specific scope;
- no copied explanations, practices, policies, templates, or full exercises from goal folders;
- links to canonical lesson and shared resources wherever content is reused.

## Output contract

Return:

1. path contract and stated assumptions;
2. session-by-session schedule;
3. coverage matrix mapping goals → sessions → artifacts → checkpoints;
4. dependency and artifact-handoff check;
5. time-budget total, including recovery allowance;
6. explicit exclusions and maturity ceiling;
7. overload, setup, or dropout risks and mitigations.

## Verify and hand off

Confirm every reference exists, session totals match the promised duration, prerequisite edges are preserved, and no lesson content is duplicated. Apply relevant gates in `.agents/rules/quality-gates.md` and use `$curriculum-quality-review` before acceptance. Send missing lesson material to `$lesson-authoring` and missing learner judgments to `$assessment-design`.
