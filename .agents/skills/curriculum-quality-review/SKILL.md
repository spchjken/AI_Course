---
name: curriculum-quality-review
description: Audit an AI-native Builder lesson, artifact, goal system, or learning path against repository rules, hard gates, and quality score. Use before accepting curriculum content or when diagnosing a quality concern; do not author broad revisions unless requested.
---

# Curriculum quality review

Audit curriculum behavior and consistency with traceable evidence. Do not infer quality from the presence of headings or from the author's confidence.

## Set review scope and independence

1. State whether the review covers a lesson, artifact, goal-system change, run, or whole learning path.
2. Read `.agents/rules/README.md`, all routed rules, relevant canonical documents, implementation files, and any prior review or pilot evidence.
3. State the claimed quality status using the canonical values: `Needs revision`, `Pilot-ready`, `Release-ready`, or `Validated`.
4. List files and evidence included and excluded. Mark inaccessible or missing evidence as a limitation.
5. Separate review from repair. Diagnose first; edit only when the user explicitly asks for fixes.
6. Confirm reviewer independence. An author may self-check, but the same author cannot be the sole authority granting hard-gate `Pass` or advancing maturity for their own output. If no independent reviewer is available, report a preflight result and keep the content at `Needs revision`.

If canonical sources conflict, report the conflict before scoring dependent content and follow the central conflict-resolution protocol.

## Build an evidence ledger

For each claim, record the exact file, section, activity, artifact field, link, or pilot observation that supports it. Distinguish:

- `Observed` — directly present in content or pilot data;
- `Inferred` — likely consequence requiring validation;
- `Missing` — required evidence is absent;
- `Out of scope` — not assessed by this review.

A heading named “verification” is not evidence that the learner verifies anything. Inspect the required behavior, instructions, and resulting artifact.

## Run hard gates

Evaluate every gate in `.agents/rules/quality-gates.md` as `Pass`, `Fail`, or `Not verified`:

1. Alignment
2. Observable outcome
3. Prerequisite
4. Learner ownership
5. Evidence
6. Verification
7. Safety
8. Consistency

Use `Fail` when inspected evidence is absent or does not meet the gate. Use `Not verified` when evidence may exist but cannot be inspected, or when it requires a future pilot/runtime observation. Do not convert uncertainty into `Pass`, and do not label an access limitation as a content defect without evidence. One failed or unverified hard gate blocks acceptance regardless of score.

For every `Not verified`, record the cause, missing evidence or access, evidence owner/next step, and exact re-review scope.

Check the gate at the appropriate layer. For example, a run's alignment depends on canonical goal links and time allocation, while a lesson's evidence gate depends on actual learner behavior and artifacts.

## Score curriculum quality

Score all eight criteria from 0 to 2 using concrete evidence:

- Beginner clarity
- Practice quality
- AI-native interaction
- Code contact
- Time feasibility
- Reusability
- Currency
- Progression

Explain every score, including full scores. Enforce the pre-pilot ceiling of `1` for beginner clarity and time feasibility unless the review includes target-learner pilot evidence. Never increase a score to reach a desired status.

## Test cross-layer consistency

Trace:

- plan promise → goal outcome → lesson activity → artifact → assessment → run checkpoint;
- prerequisite goal/artifact → consuming lesson or session;
- shared policy/practice → linked use rather than copied content;
- tool- or API-specific claim → authoritative source and check date;
- pilot finding → proposed change and claimed validation status.

Flag dangling references, copied lesson content, unused artifacts, hidden prerequisites, and maturity claims that exceed the evidence.

## Prioritize findings

Classify each finding:

- `Blocker` — hard-gate failure, safety risk, false maturity claim, or structural inconsistency;
- `Major` — likely prevents the target learner from reaching or demonstrating the outcome;
- `Minor` — reduces clarity, efficiency, maintainability, or evidence strength without blocking the core outcome;
- `Open question` — requires evidence or a user-owned product decision.

For every blocker or major finding, state the consequence and the smallest credible correction. Do not prescribe a broad rewrite when a local correction is sufficient.

## Output contract

Use the report structure in `.agents/rules/quality-gates.md` and add:

1. review scope and claimed status;
2. evidence limitations, including the cause and owner of every `Not verified` result;
3. findings ordered by severity, with file references;
4. hard-gate table;
5. quality-score table;
6. cross-layer consistency findings;
7. final status and mandatory corrections;
8. recommended re-review scope after repair or evidence access is restored.

If asked to fix issues, retain the original findings, apply the appropriate authoring skill, then re-run every affected gate. Do not label content `Validated` without qualifying target-learner evidence about outcome, clarity, and time feasibility.
