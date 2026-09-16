# Migration and rollback

## Migration

1. Commit `.agents/indexing/**`, `.agents/generated/context-index.json`, and
   the cache-ignore additions together.
2. Run `python -B .agents/indexing/sync_index.py --full` once on the target
   checkout. `--full` is also the recovery path if a future schema/fingerprint
   migration invalidates the previous derived index.
3. Run `validate_index.py`, lifecycle tests and the search query set before
   enabling any future workflow hook.

The current sandbox uses `.context-index-cache.json` and
`.context-index-lock` because runtime writes to hidden directories under
`.agents` are restricted; both are ignored. Deployments may pass another local
cache/lock path with `--cache` and `--lock`.

## Rollback

The index is derived and disposable. Remove only the generated index and local
cache/lock, then revert the indexing-tool commit on the integration branch.
Canonical sources and the previous run-scoped pilot index are not touched by
this rollback. Do not use a broad recursive delete.
