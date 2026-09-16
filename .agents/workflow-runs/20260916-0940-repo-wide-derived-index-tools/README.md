# Repo-wide derived index tools trial

- **Status:** Independent review passed with no implementation blocker; awaiting owner decision.
- **Workflow:** `optimize-agent-harness-system.md` (controlled implementation trial)
- **Owner:** repository owner
- **Worker:** Codex worker (Luna max)
- **Target:** `main` at baseline `00e60d7a45ca4b395f299735afbe06d2117a8124`
- **Branch:** `codex/20260916-0932-repo-index-tools`

This run implements the five ratified design decisions for a repository-wide
derived index. It is intentionally isolated from `main`; no scheduler, workflow
hook, canonical rule, workflow, goal, or decision source is changed.

The proposed integration set is limited to `.agents/indexing/**`,
`.agents/generated/context-index.json`, and the cache ignore rule. The generated
index remains `derived=true` and `canonical=false`.
