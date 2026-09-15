# Git baseline

- Baseline commit: `035c8c1abb7363485b412b4029db98bde1ed6141`
- Target branch: `main`
- Run branch: `codex/20260916-0525-optimize-harness-first-pilot`
- Baseline checked after branch creation: `git status --short` empty before run artifacts.
- Candidate writes: limited to `.agents/workflow-runs/20260916-0525-optimize-harness-first-pilot/`.
- Integration path: owner `Ratify` recorded on 2026-09-16; reviewed evidence commit `ae653cd` was fast-forwarded to local `main` as target commit `de35d797306000b363d518f23c7829dd7b1b7c64` after a clean drift check.
- Rollback: delete/revert only the run artifacts or candidate commit; no canonical source is changed.
