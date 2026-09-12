---
name: pilot-feedback-analysis
description: Analyze pilot-session evidence and learner feedback to identify curriculum improvements. Use after a workshop or lesson pilot when deciding whether content is validated, needs revision, or should trigger a goal/path change.
---

# Pilot feedback analysis

Turn observed learner behavior into cautious, testable curriculum improvements. Do not overfit one learner's preference or confuse instructor interpretation with observed fact.

## Establish the evidence set

1. Read `.agents/rules/README.md`, `.agents/rules/quality-gates.md`, the piloted lesson or path, its prior review, artifact and assessment contracts, target learner definition, and planned timebox.
2. Record cohort size and fit, delivery conditions, AI/tool versions, instructor, date, and deviations from the intended plan.
3. Inventory available evidence: observation notes, timing, learner artifacts, assessment results, learner quotes, tool failures, and instructor reflections.
4. Mark missing, selectively collected, or unreliable data. Do not infer absence of a problem from absence of observation.
5. State which claims the pilot can and cannot validate.

If participant identity or artifacts contain sensitive data, minimize and anonymize them according to `.agents/rules/safety-and-currency.md`.

## Normalize observations

For every relevant event, record:

| Field | Content |
|---|---|
| Expected behavior | What the lesson or assessment predicted. |
| Observed behavior | What the learner actually did or produced. |
| Evidence type | Observation, artifact, timing, result, or quote. |
| Context | Prompt, support, tool state, and session conditions. |
| Deviation | The gap between expected and observed behavior. |

Keep quotations and observations separate from interpretation. “The learner asked for help three times” is observation; “the explanation was unclear” is a hypothesis.

## Diagnose rather than jump to a fix

1. Trace each meaningful deviation across prerequisite → instruction → activity → AI interaction → artifact → assessment → timing.
2. Generate at least two credible explanations when causality is uncertain.
3. Seek evidence that supports and falsifies each explanation.
4. Classify the likely source:
   - missing prerequisite;
   - unclear framing or instruction;
   - weak practice or scaffolding;
   - artifact or assessment mismatch;
   - tool/version/environment failure;
   - excessive scope or time pressure;
   - facilitation effect;
   - goal or path design problem.
5. State confidence as high, medium, or low and explain the basis.

Do not redesign the goal because one activity was confusing when a local instruction fix explains the evidence better.

## Evaluate impact

Classify findings:

- `Blocker` — prevents outcome evidence, creates safety risk, or invalidates the session.
- `High-impact friction` — multiple learners or strong evidence indicate substantial unnecessary difficulty.
- `Minor friction` — local cost or confusion without material outcome loss.
- `Positive evidence` — observed behavior supports a claimed strength.
- `Unknown` — evidence is too weak or conflicting to classify.

For each finding, note affected learners, reproducibility, consequence, and whether it changes a hard gate or quality score. Preserve positive evidence; improvement analysis is not only defect collection.

## Propose changes as hypotheses

For every blocker or high-impact finding:

1. propose the smallest change that addresses the leading explanation;
2. name the owning layer: goal, lesson, artifact, assessment, path, shared resource, or environment;
3. state the expected behavioral improvement;
4. identify possible regressions or downstream effects;
5. define evidence for the next pilot that would confirm or reject the change.

Avoid bundling several causal hypotheses into one large rewrite. Prioritize by learner impact, confidence, effort, safety, and reversibility.

## Update maturity honestly

- Re-evaluate affected hard gates and scores using actual pilot evidence.
- Permit `2` for beginner clarity or time feasibility only when qualifying target learners and inspected evidence support it.
- Do not label content `Validated` from instructor review, expert testing, self-testing, satisfaction alone, or a pilot that did not observe the claimed outcome.
- State sample limitations; validation is scoped to the tested audience, setting, content version, and tools.

## Output contract

Return:

1. pilot context and evidence inventory;
2. normalized observation table;
3. findings with severity, confidence, competing explanations, and evidence;
4. positive evidence and unchanged assumptions;
5. prioritized change hypotheses with owning layer;
6. proposed quality-status change, if justified;
7. next-pilot measurement plan;
8. limitations and unresolved questions.

Update curriculum files only when requested. Use `$lesson-authoring`, `$learner-artifact-design`, `$assessment-design`, `$learning-path-composition`, or `$curriculum-goal-design` for the owning layer, then request `$curriculum-quality-review` after changes.
