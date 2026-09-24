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

## Re-review disposition

Re-review commit `956e742` reopened `STE-001`, `STE-002` and `STE-004`, left `STE-005` unresolved, and partially resolved `STE-007`. All were accepted: the next candidate rejects hardlinks using path and open-handle link counts, rejects boolean/float sequence values, aligns manifest/event schemas, serializes in-process writers while retrying cross-process contention, recovers stale malformed locks, and adds direct fixtures for every reopened condition. `STE-007` remains a final-handoff action until the workflow trace can truthfully close.

Final re-review commit `f416cc0` kept `STE-002`, `STE-004` and `STE-005` open. All were accepted. The next candidate aligns ref/slug schema constraints with the validator, replaces the Windows-racy lock file with an atomic lock-directory whose active metadata contenders never open, and adds a real multi-process append fixture that requires every writer to succeed without event loss or orphan lock. `STE-007` remains deferred only to truthful final handoff.
