# Migration and rollback

## Migration if ratified

1. Effective from the ratified commit; do not fabricate or backfill historical skill invocations.
2. Every later repository-local skill invocation opens/closes a trace according to `AGENTS.md`.
3. Workflow task contracts carry `execution_id`/`trace_path`; absence is `Not verified`, not implicit success.
4. Raw traces remain local/ignored with default 30-day retention. An owner/auditor may export a counts-only aggregate to a workflow run.
5. `$harness-improvement-discovery` validates traces before analysis and reports coverage limits where the host has no platform hook.

## Rollback

- Before ratification/integration: retain the trial branch and evidence; do not alter `main`.
- After integration: revert only the ratified commit with a new commit, then run skill/index validators.
- Raw traces created under the contract are operational evidence. Rollback does not silently delete them; the owner may retain them through expiry or remove individually after inspection.
- Never modify or reset the pre-existing `.gitignore` change during rollback.

## Invalidation

- Changing manifest/event schema, runtime root, privacy fields or terminal outcomes invalidates validator evidence for the changed surface and requires a new decision/migration.
- Changing a skill creates a new `skill_sha256`; old traces remain valid for their recorded version and must not be rewritten.
