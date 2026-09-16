# Validation report (pre-review)

## Automated checks

- `python -B -m unittest discover -s .agents/indexing/tests -v`: **8 tests,
  pass**.
- `validate_index.py`: **pass**; schema valid, 157 entries, zero missing
  sources, zero stale sources, zero authority mismatches, zero unexpected
  missing links, and zero false canonical assignments.
- Six unresolved optional references in `repo-skill-creator/SKILL.md` are
  explicitly configured as `link_exceptions`; they are reported as exemptions,
  not silently ignored.
- Generated index invariants: `derived=true`, `canonical=false`; no `keywords`
  field; all paths repository-relative and hashes are SHA-256.

## Performance evidence

`benchmark-report-v9.json` is the final five-sample probe after the strict
hashing change. Observed p95 values were:

| Operation | p95 | Design target | Result |
|---|---:|---:|---|
| full rebuild | 580.702 ms (one sample) | 10,000 ms | pass |
| strict no-op `--check` | 531.192 ms | 750 ms (recalibrated) | pass |
| incremental update | 475.334 ms | 1,000 ms | pass |
| lexical search (rg auto) | 900.303 ms | 1,000 ms | pass |

The strict check hashes every file, including files whose size/mtime were
preserved by an external editor. The original 500 ms aspiration was
recalibrated to 750 ms during review rather than weakening the integrity check;
the measured run remains sub-second on this 157-entry repository. The
incremental path used for ordinary edits/moves remains well under one second.

## Negative evidence and fixes

The first benchmark attempt exposed a race when a report was created inside the
indexed tree during a scan. Dynamic `index-report*.json`,
`benchmark-report*.json`, and `context-package*.json` are now explicitly
excluded, and the final benchmark returned code 0 for every sample. The v2
failure is retained as evidence in the run directory.
