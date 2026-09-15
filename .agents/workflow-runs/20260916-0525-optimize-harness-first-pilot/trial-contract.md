# Trial contract

## Authority and scope

- Decision: `Approve trial` recorded from the owner's explicit request on 2026-09-16.
- Mode: `Improvement trial`.
- Baseline SHA: `035c8c1abb7363485b412b4029db98bde1ed6141`.
- Allowed source reads: exactly the three paths in `impact-map.md` plus the pilot design note.
- Allowed writes: this run directory only.
- Forbidden: editing canonical sources, changing workflow/rules/skills, migrating metadata, building RAG/graph, network calls, secrets, personal data, or integrating into `main`.
- Timebox: 60 minutes of execution; one baseline, one candidate v0, at most one bounded repair, one candidate v1, and two deterministic reproducibility reruns. No further probe run is allowed without a new owner decision.
- Retention/expiry: retain public, synthetic run evidence through the owner outcome and one audit cycle; expire or discard the derived candidate index when the owner chooses `Reject`, `Defer`, or `No change`. Never retain secrets or personal data.

## Locked questions and expected authority

The query set contains eight synthetic questions: four positive routing questions, two negative/out-of-scope questions and two regression questions. Expected paths and `OUT_OF_SCOPE` outcomes are locked before execution in `query-set.tsv`.

## Metrics and thresholds

- Primary metric: authoritative routing accuracy over all eight queries; candidate must be greater than or equal to baseline (`>=`), with zero false-authority selections.
- Guardrail 1: candidate false-authority selections must be `0`.
- Guardrail 2: every selected source must be traceable to an exact allowed path.
- Guardrail 3: negative/out-of-scope questions must return `OUT_OF_SCOPE`.
- Secondary metric: candidate total source-file reads must be at least 20% lower than baseline while the primary metric is non-regressive.
- Run-count guardrail: the allowed execution count is exactly the bounded sequence above; reruns reproduce the locked artifact and do not expand the query set.
- Fixed evaluation: same query set, same corpus, deterministic token probe; no threshold or query changes after results.

## Stop conditions

Stop before review if a source is modified, a path is outside scope, metadata is treated as canonical, a query/threshold changes after execution, a candidate returns unsupported authority, or baseline/candidate cannot be reproduced.

## Decision status

`Approved trial`; `Ratify` is not granted. After independent review, the owner must choose `Ratify`, `Revise`, `Reject`, `Defer`, or `No change` for this run. A passing probe does not make the workflow `Active`.
