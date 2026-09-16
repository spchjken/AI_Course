# Ratification of repo-wide derived index tools

- **Decision date:** 2026-09-16
- **Owner decision:** Ratify
- **Implementation commit:** `684dd3c` (`Implement repo-wide derived index tools`)
- **Trial run:** `.agents/workflow-runs/20260916-0940-repo-wide-derived-index-tools/`
- **Scope:** `.agents/indexing/**`, `.agents/generated/context-index.json`,
  `.gitignore` cache rules, and the operational run evidence.

## Decision

The owner ratifies the repository-wide derived-index implementation after the
independent review and its disposition. The implementation may be integrated
into `main` and pushed to `origin/main`.

## Ratified invariants

- `content_hash = SHA256(normalized UTF-8 content)`.
- `entry_hash = SHA256(content_hash + NUL + normalized repository-relative path)`.
- A unique unchanged content hash may be reported as a move; move-plus-edit is
  delete plus create; duplicate hashes never force a guessed move.
- `.agents/workflow-runs/**` is indexed as operational evidence and excluded
  from default authority search.
- The committed index remains `derived=true`, `canonical=false`; it contains no
  per-file keyword list.
- Python stdlib is the required implementation; `rg` is optional acceleration.
- Scheduler, daily job, and workflow hook integration remain deferred.

## Evidence gate

The independent re-review is `PASS-WITH-FINDINGS` with no implementation
blocker. The final evidence reports 8/8 tests passing, 157 current entries,
zero stale/missing/authority mismatches/false canonical assignments, and strict
check p95 531.192 ms against the recalibrated 750 ms target. Post-ratification
validation is required after merge and before push.
