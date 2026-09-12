---
name: lesson-authoring
description: Create or revise one AI-native Builder lesson folder and its delivery material. Use when an approved gNN goal needs learner-facing guidance, instructor flow, practice, evidence, or package integration; do not independently approve quality, redesign goal boundaries, or compose multi-session learning paths.
---

# Lesson authoring

Build one teachable, evidence-producing lesson from an approved goal contract. Optimize for learner decisions and feedback loops, not for volume of explanation.

## Preflight

1. Read `.agents/rules/README.md` and the routed rule files.
2. Read the relevant goal definition in `curriculum-content-architecture.md`, the program plan, curriculum map, goal folder, and any run that constrains time or maturity.
3. Inspect reusable materials in `ai-native-builder/shared/`; link to canonical policy, practice, and templates instead of copying them.
4. Confirm that the requested work changes lesson delivery rather than the goal boundary. Route a boundary, prerequisite, dependency, or program-promise change through `change-curriculum-architecture`, using `$curriculum-goal-design` at that owning layer.
5. Identify claims about current tools, APIs, models, or interfaces. Verify them with `$curriculum-reference-research` before making them instructional dependencies.

Resolve material conflicts through `.agents/rules/README.md` before authoring content that depends on the disputed premise.

## Create the lesson contract

Write down these decisions before drafting prose:

- one observable learner outcome copied or faithfully derived from the approved goal;
- incoming capability and artifact prerequisites;
- the concrete problem or decision that gives the lesson a reason to exist;
- how AI participates and what the learner must decide, approve, or reject;
- the intended code contact at this point in the progression;
- the artifact and exact completion evidence;
- relevant safety boundaries and a recoverable failure path;
- the capability or artifact handed to the next goal;
- the available learner time and expected maturity level.

If these cannot fit into one coherent practice loop, report the mismatch instead of hiding it in more content.

## Design backward from evidence

1. Define what a reviewer must be able to observe in the final artifact or learner demonstration.
2. Define the decisions the learner must make to produce that evidence.
3. Create a realistic task that forces those decisions without requiring unintroduced knowledge.
4. Add only the explanation, example, template, and instructor support needed to complete the task.
5. Ensure the learner uses AI through an intentional loop: state intent → delegate a bounded task → observe output → challenge or redirect → verify → record.
6. Increase code contact only where it gives the learner ownership or diagnostic power. Never isolate code reading/editing as a detached module.

## Build the learning sequence

Use the smallest sequence that supports the outcome. A typical sequence is:

1. **Frame** — establish the learner problem, outcome, artifact, evidence, and constraints.
2. **Model** — show a short decision process or worked example, including how weak AI output is challenged.
3. **Guided attempt** — let the learner act with prompts or checkpoints that fade as competence appears.
4. **Independent decision** — require the learner to choose, explain, or revise something that AI cannot own for them.
5. **Verification** — test against criteria and deliberately inspect a plausible failure.
6. **Record and connect** — preserve the artifact, decision trail, evidence, and next-step handoff.

For every activity, state the timebox, learner action, AI action, instructor intervention trigger, and produced evidence. Do not add an activity that contributes none of these.

## Author the lesson folder

Keep `ai-native-builder/goals/gNN-*` as the canonical lesson location. Treat its `README.md` as the approved design brief rather than as the final delivery package. At minimum, the brief must make the following usable rather than merely name them:

- outcome and completion criteria;
- prerequisites and starting materials;
- AI role and learner-owned decisions;
- step-by-step practice flow with time guidance;
- code-contact expectations;
- artifact and evidence instructions;
- failure/recovery path and applicable safety rules;
- review or feedback method;
- handoff to the next goal.

When invoked from `.agents/workflows/complete-goal-lessons.md`, follow that workflow's mandatory package, work-unit boundaries, and file ownership:

- use this skill for outline integration, `lesson.md`, `practice.md`, `instructor-guide.md`, and final author-side package integration;
- use `$assessment-design` to author `assessment.md`;
- create `pilot-feedback-form.md` from the workflow specification without invoking post-pilot analysis;
- treat `references.md` as researcher-owned and return missing or disputed claims to the research phase;
- never create, prefill, or approve `review.md`; it belongs to the independent reviewer.

Outside that workflow, add separate learner, instructor, or practice files only when the material is operationally distinct from the brief. Use lowercase ASCII kebab-case filenames.

## Design failure into the lesson

Include at least one relevant failure mode, such as AI output that is incomplete, inconsistent with the spec, unsafe, non-running, or beyond scope. Require the learner to:

1. notice the failure using stated evidence;
2. explain the mismatch in plain language;
3. choose whether to revise the instruction, artifact, implementation, or expectation;
4. retry or roll back safely;
5. record the result.

Do not imply that a polished UI, successful generation, or large code diff proves capability.

## Output contract

When handing off the authored lesson, report:

- files created or changed;
- lesson outcome, timebox, artifact, and learner-owned decision;
- where code contact, verification, safety, and recovery appear;
- reused shared resources and verified time-sensitive sources;
- assumptions or known gaps;
- author-side preflight result, independent quality-review status if one exists, and remaining blockers.

## Verify and hand off

1. Run an author-side preflight against every hard gate and all eight score criteria in `.agents/rules/quality-gates.md` using concrete evidence; do not grant final `Pass` or advance maturity.
2. Do not assign a final score. Note that an independent reviewer cannot score beginner clarity or time feasibility above the rule's pre-pilot ceiling.
3. Use `$learner-artifact-design` if the artifact cannot yet expose learner reasoning.
4. Use `$assessment-design` if evidence exists but judgment and feedback criteria are incomplete.
5. Hand the completed author-owned files to a separate invocation of `$curriculum-quality-review` for acceptance after authoring.
6. Send multi-session scheduling problems to `$learning-path-composition`.

Do not declare the lesson complete while any hard gate is `Fail` or `Not verified`.
