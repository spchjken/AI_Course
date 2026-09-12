---
name: learner-artifact-design
description: Design or refine a concrete artifact that demonstrates a learner decision or capability, such as a product brief, spec, system map, harness, agent plan, decision log, or verification record. Use when a lesson needs evidence of learning; do not design grading systems for the whole course.
---

# Learner artifact design

Design an artifact that makes learner capability inspectable and remains useful in later work. An artifact is evidence-bearing work, not merely the product AI generated.

## Establish the artifact's job

1. Read `.agents/rules/README.md`, the approved goal, the lesson contract, and relevant shared templates.
2. State the observable outcome and learner-owned decision the artifact must reveal.
3. Identify who will use it next and what decision or task it must enable.
4. Separate three possible purposes: guide the learner's work, preserve a decision trail, and prove completion. State which are required.
5. Confirm that artifact design, rather than goal design or assessment design, is the actual issue.

If the goal has no stable outcome or its boundary is disputed, stop and hand it to `$curriculum-goal-design` before creating a template.

## Define the artifact contract

Specify:

| Field | Question to answer |
|---|---|
| Purpose | Why must this artifact exist after the activity ends? |
| Inputs | Which prior artifacts, observations, or constraints does it consume? |
| Learner-owned fields | Which decisions must the learner make, justify, or approve? |
| AI contribution | What may AI draft, transform, critique, or check? |
| Minimum schema | What is the smallest set of fields that exposes the outcome? |
| Evidence | What entries, annotations, diffs, tests, or demonstrations prove capability? |
| Verification | How will the learner detect an incorrect or unsupported entry? |
| Failure handling | What is recorded when a check fails or evidence is inconclusive? |
| Safety | What data, secrets, permissions, or external actions must be excluded or controlled? |
| Consumer | Which later goal, session, reviewer, or system uses it? |

Make authorship legible. Mark AI proposals separately from learner decisions, and require the learner to record approval, rejection, revision, or evidence. Do not require a transcript when a compact decision log is sufficient.

## Design the learner interaction

1. Give a short instruction that states the problem, constraints, and expected artifact.
2. Provide prompts or field-level questions that elicit decisions rather than predetermined answers.
3. Include a bounded way for AI to critique missing assumptions or contradictions.
4. Require at least one learner revision or explicit acceptance backed by evidence.
5. Include an example only when it reduces ambiguity; label it so learners do not mistake it for the required answer.
6. Set a realistic timebox and a maximum useful size.

Prefer progressive disclosure for beginners. Make the minimum completion path obvious and optional depth visibly optional.

## Define evidence without grading it

Describe evidence in observable terms, such as:

- a requirement linked to a user need;
- a component boundary justified by a constraint;
- a test result linked to an acceptance criterion;
- an AI proposal rejected with a reason;
- a failed attempt followed by a verified correction.

Do not create performance levels or final grading policy here. Pass the artifact contract to `$assessment-design` for judgment and feedback criteria.

## Reject weak artifact designs

Revise an artifact when it:

- can be completed by copying AI output without a learner decision;
- rewards polish or length while hiding reasoning;
- duplicates information already canonical elsewhere;
- requests data that later work never consumes;
- takes most of the lesson to format rather than decide;
- lacks a way to record failure, uncertainty, or verification;
- exposes real credentials or sensitive data.

## Output and verification

Return the artifact contract, learner-facing template or instructions, one minimal example if needed, estimated completion time, and links to its producer and consumer goals. Explain where learner ownership and verification are visible.

Check applicable hard gates in `.agents/rules/quality-gates.md`. The design is not complete until the artifact can demonstrate the stated outcome and fit the lesson timebox.
