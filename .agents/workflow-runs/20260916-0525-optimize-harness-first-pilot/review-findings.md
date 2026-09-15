# Independent review findings

## Initial review

- Reviewer: `/root/first_pilot_governance_review_retry`
- Review mode: fresh, read-only, independent of the implementer.
- Date: 2026-09-16
- Outcome: `Fail` pending bounded repairs.

| ID | Severity | Finding | Evidence requested |
|---|---|---|---|
| F-REVIEW-001 | Blocker | reviewer identity and completion were missing from the run record | orchestration log and final review artifact |
| F-REVIEW-002 | Major | candidate source reads were hardcoded rather than evidenced | source read/verification field in probe output |
| F-REVIEW-003 | Major | lifecycle contract and migration/rollback evidence were incomplete | timebox, retention, run count, rollback file |
| F-REVIEW-004 | Major | regression coverage omitted path/title, link, and index-schema checks | persisted regression result |

The implementer accepted all four findings as local evidence or lifecycle repairs. The locked queries, expected authority, thresholds, canonical sources, and no-integration boundary remain unchanged.
