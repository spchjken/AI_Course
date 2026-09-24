# Finding disposition

| Finding | Disposition | Action |
|---|---|---|
| STE-001 | Accept | Reject symlink, junction and reparse points before writes; bounded cleanup; Windows junction fixture. |
| STE-002 | Accept | Enforce exact manifest/event keys and types, lifecycle cardinality and monotonic/matching timestamps. |
| STE-003 | Accept | Invalid traces contribute only to fixed aggregate counts; no raw dimensions are exported. |
| STE-004 | Accept | Expand direct coverage for concurrency, append-prefix integrity, Windows paths/junctions, tampering, refs and invalid aggregates; withdraw the earlier unsupported 6/6 claim pending rerun. |
| STE-005 | Accept | Add PID/time lock metadata and guarded stale-lock recovery. |
| STE-006 | Accept | State that missing invocation requires an independent expected roster; otherwise coverage is `Not verified`. Portable file remains a local ignored export. |
| STE-007 | Accept | Add the required Skill trace field and paths; close the orchestration trace before final handoff. |
