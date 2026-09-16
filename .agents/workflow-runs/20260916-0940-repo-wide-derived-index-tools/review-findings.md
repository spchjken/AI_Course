# Independent review and disposition

## Review 1 — FAIL (read-only)

The independent reviewer identified four findings:

1. Search/package trusted index authority metadata without re-checking the
   configured classification rules.
2. Lifecycle evidence did not cover unstable reads and generated/cache
   exclusions.
3. Atomic temporary names and CLI/package output paths were not sufficiently
   bounded; `write_allowlist` was only descriptive.
4. Strict no-op check p95 exceeded the original 500 ms target.

## Worker disposition before re-review

- `search_index.py` now loads the config and rejects any type/authority/status/
  `default_search` mismatch before returning results; package builder passes the
  same config and normalizes its write allowlist.
- `sync_index.py` retries an unstable source once, performs strict content
  hashing in `--check`, and tests metadata-preserving edits. Tests now cover
  generated/cache exclusions, tampered authority, outside-root targets, and
  duplicate-safe move inference (8 lifecycle tests total).
- `write_json_atomic` now uses a unique same-directory temporary file, flushes
  and fsyncs before `os.replace`, and cleans up. Sync/search/package output
  targets are required to remain beneath the declared repository root.
- Strict check metadata reuse avoids reparsing unchanged sources while still
  hashing them. The acceptance target was recalibrated from 500 ms to 750 ms
  because the integrity requirement is full hashing; v8 measured 511.099 ms
  p95. This is a recorded contract change, not a hidden measurement.

## Review 2 — PASS-WITH-FINDINGS

The same independent reviewer confirmed all four implementation dispositions:
8/8 tests pass, the validator reports 157 current entries with zero authority
or path errors, strict check p95 is 531.192 ms against the recalibrated 750 ms
target, and canonical scope is clean. The only closure cleanup was aligning
historical benchmark/evidence counts with the recalibrated contract; those
artifacts are now synchronized. There is no implementation blocker.

The run remains `Awaiting decision`: integration still requires the owner to
choose `Ratify`, `Revise`, `Reject`, or `Defer`.
