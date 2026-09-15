# Post-ratify validation

## Integration record

- Owner outcome: `Ratify`, explicitly received on 2026-09-16.
- Reviewed evidence commit: `ae653cd`.
- Target branch: local `main`.
- Target baseline before integration: `035c8c1abb7363485b412b4029db98bde1ed6141`.
- Integrated target commit: `de35d797306000b363d518f23c7829dd7b1b7c64`.
- Target drift check before integration: `PASS`; `main` and `origin/main` both matched the recorded baseline.
- Integration allowlist: the ratification decision record and this pilot's `.agents/workflow-runs/` evidence only.

## Affected checks

- Command: `powershell -NoProfile -ExecutionPolicy Bypass -File .agents/workflow-runs/20260916-0525-optimize-harness-first-pilot/run_probe.ps1`
- Candidate routing: `8/8` correct.
- False authority: `0`.
- Candidate source reads: `6`; baseline reads: `24`; reduction: `75%`.
- Source verifications: `6`.
- Reproducibility: two consecutive post-integration runs produced the same `probe-results.csv` SHA-256 `4B383BDA5E726CEADD400810EB3942CAF3189293B71AEBE60B03C8273C9F6AAC`.
- Regression results: `PathTitleFallback=true`, `LinkIntegrity=true`, `IndexSchema=true`, `RegressionPass=true`.
- Canonical diff from baseline: `PASS` for G09 README, optimize workflow, and the 2026-09-15 decision record.
- Sensitive-data check: `PASS`; synthetic/public evidence only.

## Closure

The ratified operational record is integrated and the run is `Closed`. The candidate index and context package remain derived and run-scoped; no workflow `Active` promotion, repository-wide metadata migration, RAG/graph adoption, or canonical source edit occurred.
