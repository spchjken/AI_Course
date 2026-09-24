# Git baseline

- **Target branch:** `main`
- **Baseline full SHA:** `a65e86caff89feb4e7c065fa5a22443a83d4d23e`
- **Trial branch:** `codex/20260924-skill-execution-traces`
- **Isolation:** same worktree on a dedicated branch; no target integration before owner `Ratify`.
- **Pre-existing dirty state:** `.gitignore` modified before this trial; excluded from allowed writes and commits.
- **Drift rule:** stop before integration if `main` no longer points to the reviewed baseline or if an overlapping user change appears.
- **Rollback:** before integration, delete/abandon only the trial branch after explicit owner direction; after integration, revert the exact ratified commit with a new commit. Never reset or overwrite `.gitignore`.
