---
name: assessment-design
description: Design learner assessment, rubrics, checkpoints, and feedback criteria for AI-native Builder lessons or paths. Use when defining how learner outcomes are judged; do not use to audit the curriculum's own quality gates.
---

# Assessment design

Judge learner capability through observable evidence, not through the polish or quantity of AI output. Keep learner assessment separate from curriculum quality review.

## Establish the assessment claim

1. Read `.agents/rules/README.md`, the approved goal, lesson contract, artifact contract, and relevant run constraints.
2. State the exact capability the assessment is allowed to claim.
3. Identify the evidence available during the lesson and what cannot be inferred from it.
4. Confirm that prerequisites have been taught; do not assess hidden technical knowledge.
5. Choose the assessment purpose: formative checkpoint, end-of-lesson decision, path milestone, or capstone judgment.

If the artifact cannot expose learner decisions, return it to `$learner-artifact-design`. If the outcome itself is unstable, return it to `$curriculum-goal-design`.

## Build an evidence blueprint

Map each assessed outcome using this structure:

| Element | Definition |
|---|---|
| Outcome | Observable behavior from the approved goal. |
| Task | What the learner must do under stated conditions. |
| Evidence | Artifact section, demonstration, explanation, or revision observed. |
| Criterion | The quality that distinguishes adequate from inadequate evidence. |
| Method | Artifact review, conversation, live demonstration, test, or observation. |
| Feedback | A diagnosis and next action the learner can use. |
| Retry | What may be revised and what new evidence is required. |

Use the smallest set of evidence that supports the claim. Prefer direct performance over self-report and prefer several connected evidence signals over one superficial proxy.

## Assess AI-native ownership

When AI contributes to the work, require evidence that the learner can:

- state the intended result and relevant constraints;
- identify at least one important decision they own;
- inspect or challenge an AI proposal;
- verify output against a criterion;
- diagnose and recover from a plausible failure;
- explain what evidence changed their decision.

Do not ban AI merely to make authorship easier to judge. Make the learner's judgment visible through annotations, diffs, demonstrations, or targeted questions. Avoid surveillance-heavy requirements such as complete chat histories unless they are genuinely necessary.

## Create criteria and performance levels

Use criterion-referenced levels with concrete observable differences. Prefer three levels when no stronger reason exists:

- `Not yet` — required evidence is missing, incorrect, unsafe, or cannot support the outcome.
- `Meets` — evidence is sufficient, relevant, verified, and shows the required learner decision.
- `Extends` — evidence is transferable, handles meaningful edge cases, or shows justified trade-offs beyond the minimum.

For every criterion, include common failure signals and feedback that points to the next action. Do not average away a critical failure in safety, verification, or learner ownership.

## Calibrate burden and fairness

1. Fit assessment inside the lesson or checkpoint timebox.
2. Use plain language suitable for a learner who began with web chat only.
3. Judge the stated capability, not writing fluency, visual polish, typing speed, or prior coding vocabulary unless explicitly part of the goal.
4. Allow equivalent evidence formats when they preserve the same capability claim.
5. State what support, templates, AI access, and retries are allowed.
6. Avoid criteria that depend on unstable product interfaces unless they have current verified sources.

## Output contract

Return:

1. the assessment claim and purpose;
2. the outcome-to-evidence blueprint;
3. rubric criteria and observable performance levels;
4. administration instructions, timebox, and allowed support;
5. feedback and retry protocol;
6. critical failure conditions;
7. assumptions and evidence limitations.

Cross-check alignment with the lesson and artifact. Do not copy the repository's quality score into the learner rubric: `.agents/rules/quality-gates.md` judges curriculum quality, while this skill judges learner progress.
