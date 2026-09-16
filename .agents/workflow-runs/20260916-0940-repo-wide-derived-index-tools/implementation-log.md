# Implementation log

## Implemented

- `index_core.py`: NFC/POSIX path normalization, UTF-8/newline normalization,
  `content_hash` and `entry_hash`, classification, title/link extraction,
  deterministic serialization, schema checks.
- `sync_index.py`: incremental/full/check modes, stat cache, unique move
  detection, delete/create semantics for move-plus-edit, duplicate-safe event
  reporting, atomic index/cache writes, exclusive lock, and unstable-read
  detection.
- `search_index.py`: query-time lexical search with Python fallback and
  optional `rg --json` accelerator; structural authority/type/status filters.
- `build_context_package.py`: task/role/query package with read/write
  allowlists, source snippets and hash verification; no source duplication.
- `tests/test_indexing.py`: eight unittest cases covering hashes, lifecycle,
  duplicates, unstable reads, exclusions, authority tamper, path bounds,
  search filtering, and stale package invalidation.
- Review fixes: authority is rechecked against config at search/package time;
  strict checks hash every source while reusing unchanged metadata; atomic
  outputs use unique fsynced temporary files and all tool targets stay inside
  the declared root.

## Deliberately deferred

Daily scheduling, workflow hooks, external dependencies, and canonical policy
changes remain out of scope.
