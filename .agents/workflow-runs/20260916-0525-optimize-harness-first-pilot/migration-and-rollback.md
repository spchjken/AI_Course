# Migration and rollback

## Current trial

- No canonical migration is approved or performed.
- `context-index.json` and the probe outputs are derived, disposable run artifacts; they are not a replacement for a canonical goal, workflow, rule, or decision source.
- No commit changes `g09`, `optimize-agent-harness-system.md`, the decision record, or `main`.

## Rollback

- If the owner chooses `Reject`, `Defer`, or `No change`, close the run and discard the derived candidate artifacts after the retention window. The canonical tree requires no rollback because it was not modified.
- If a run commit is created, rollback means reverting that isolated run commit or removing only this run directory after retention approval; do not use a broad reset or alter unrelated work.
- If any unexpected canonical mutation is detected, stop, record the path and baseline diff, and restore only that exact mutation through an approved, reviewable change.

## Future migration gate

An owner `Ratify` decision would start a separate migration change. That change must recheck baseline drift, define exact file ownership, preserve the no-RAG/no-graph boundary, create a reviewable commit, and rerun the affected validation and independent review before any `Active` status is considered.

## Handoff

- Owner outcome: `Ratify` on 2026-09-16.
- Derived index expiry remains tied to the ratified run's retention policy and one audit cycle; no derived artifact becomes canonical by retention alone.
- If the ratified pattern is later implemented at a canonical target, that is a separate change with its own target, commit, review, drift check and rollback record.
