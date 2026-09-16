# Repo-wide derived index tools trial

- **Status:** Closed after ratified integration and post-ratify validation.
- **Workflow:** `optimize-agent-harness-system.md` (controlled implementation trial)
- **Owner:** repository owner
- **Worker:** Codex worker (Luna max)
- **Target:** `main` after ratified integration (`54c58bd`)
- **Implementation branch:** `codex/20260916-0932-repo-index-tools` (fast-forwarded into `main`)

This run implements the five ratified design decisions for a repository-wide
derived index. It is intentionally isolated from `main`; no scheduler, workflow
hook, canonical rule, workflow, goal, or decision source is changed.

The integrated set is limited to `.agents/indexing/**`,
`.agents/generated/context-index.json`, the cache ignore rule, and the
governance/run evidence required to record ratification. The generated index
remains `derived=true` and `canonical=false`.

Post-ratify validation is recorded in `post-ratify-validation.md`. The
scheduler and automatic workflow hook remain deliberately deferred.
