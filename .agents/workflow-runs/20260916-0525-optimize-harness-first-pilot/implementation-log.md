# Implementation log

## Candidate v0

- Artifact: `context-index.json` plus deterministic `run_probe.ps1`.
- Scope check: only this run directory was written; canonical sources unchanged.
- Initial probe: `probe-results.csv` and `probe-summary.json`.
- Result: stopped before independent review because the candidate returned unsupported authority for N1 and N2.

## Candidate v1 repair

- Finding: `F-PILOT-001` — candidate accepted weak single-keyword matches and routed two out-of-scope queries to the workflow source.
- Disposition: `Accept` as a bounded implementation defect; no metric, query, source path, or threshold changed.
- Repair: require at least two distinct indexed keyword overlaps before selecting a candidate source; otherwise return `OUT_OF_SCOPE`.
- Expected evidence: N1/N2 become `OUT_OF_SCOPE`; positive/regression queries retain their expected routes; source reads remain reduced.

## Reviewer repairs

- `F-REVIEW-001` through `F-REVIEW-004` were accepted as local evidence or lifecycle defects.
- Candidate routing now reads and verifies the selected source before returning an in-scope route and records `CandidateSourceVerified` per row.
- Regression checks now persist path/title fallback, local-link integrity, and derived-index schema results in `regression-results.json`.
- Contract and rollback evidence were added without changing the locked query set, thresholds, or canonical sources.
- Canonical commit: none; this trial remains on the isolated run branch pending an explicit owner outcome.

## Ratify handoff

- Owner outcome: `Ratify` on 2026-09-16.
- Integration unit: reviewed evidence commit `ae653cd` plus the ratification decision record; no canonical goal, workflow, rule, skill, or metadata index is changed.
- The derived index remains a disposable operational artifact until a separately scoped implementation target is approved.
- Target integration: `de35d797306000b363d518f23c7829dd7b1b7c64` on local `main`; post-integration checks are recorded in `post-ratify-validation.md`.
