# Validation report

## Contract and execution

- Contract: `trial-contract.md`.
- Probe: `run_probe.ps1`.
- Query set: `query-set.tsv`, locked before execution.
- Candidate: `context-index.json` plus `context-package.md`.
- Baseline: deterministic overlap search across all three allowed source files.
- Candidate: index-first routing with minimum score 2, then one selected source read and token-evidence verification for each in-scope route.
- Execution command: `powershell -NoProfile -ExecutionPolicy Bypass -File .agents/workflow-runs/20260916-0525-optimize-harness-first-pilot/run_probe.ps1`.
- Reproducibility: two consecutive runs produced identical `probe-results.csv` SHA-256 `4B383BDA5E726CEADD400810EB3942CAF3189293B71AEBE60B03C8273C9F6AAC`.
- Canonical-source diff check: `PASS`; the three `Reverify` paths are unchanged from baseline.

## Initial candidate v0 and bounded repair

The first probe selected the workflow for both negative queries. `CandidateCorrect = 6/8`, `CandidateFalseAuthority = 2`; this triggered `F-PILOT-001` and stopped review. The worker accepted the local implementation finding and added a minimum overlap of 2 without changing the query set, expected paths, primary metric or guardrails. The original evidence is retained in `probe-results-v0.csv` and `probe-summary-v0.json`.

## Final comparison

| Metric | Baseline | Candidate v1 | Contract result |
|---|---:|---:|---|
| Authoritative routing accuracy | 1/8 (12.5%) | 8/8 (100%) | `Pass` — candidate non-regressive |
| False-authority selections | n/a | 0 | `Pass` |
| Negative/out-of-scope correct | 0/2 | 2/2 | `Pass` |
| Canonical source traceability | 8/8 selected from allowed corpus | 6/6 source routes from allowed corpus; 2/2 `OUT_OF_SCOPE` | `Pass` — each selected route was verified by reading the exact source |
| Canonical source-file reads | 24 | 6 | `Pass` — 75% reduction, threshold 20% |

`probe-summary.json` records `CandidateSourceVerifications = 6`; the candidate did not claim source authority for either negative query.

## Four required layers

### Positive

P1–P4 route to the expected goal, workflow or decision source after the repair.

### Negative

N1–N2 return `OUT_OF_SCOPE`; no skill, plugin, production deployment or graph authority is fabricated.

### Regression

R1–R2 preserve routing to the workflow and decision sources. Existing path/heading search remains available because no canonical source was edited.

`regression-results.json` records `PathTitleFallback = true`, `LinkIntegrity = true`, `IndexSchema = true`, and `RegressionPass = true`.

### Comparison

Both methods use the same eight questions and the same three-source corpus. Baseline inspects three source files per query; candidate reads the derived index and one selected source for six in-scope queries, and no source for two rejected queries.

## Deterministic checks

- `context-index.json | ConvertFrom-Json`: `PASS`.
- Expected paths exist: `PASS`.
- Candidate files are marked derived/non-canonical: `PASS`.
- `regression-results.json`: `PASS` for path/title fallback, local Markdown-link integrity, and index schema.
- `git diff --quiet -- <three canonical paths>`: `PASS`.
- Sensitive-pattern scan: initial grep produced only documented false positives in prose/code words such as `secrets`, `token` and `password`; no secret value or personal data is present. Manual review: `PASS`.

## Limitations

This is a deterministic routing-mechanics probe over eight synthetic questions, not a general model-quality study. It does not establish performance across other goals, models, query distributions or repositories. It does not justify repository-wide metadata migration, RAG/graph adoption, or workflow `Active` status.

## Verification state

- G result: `Pass` after accepted bounded repair.
- Independent governance review: initial fresh review `Fail` with F-REVIEW-001..004; after accepted repairs, fresh reviewer A3 returned `Pass` with no remaining Blocker/Major/Minor findings.
- Owner outcome: `Ratify` recorded on 2026-09-16; post-integration validation `Pass` is recorded in `post-ratify-validation.md`.
