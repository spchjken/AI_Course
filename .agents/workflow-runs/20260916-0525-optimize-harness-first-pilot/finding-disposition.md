# Finding disposition

## F-PILOT-001

- **Source:** G validation probe, candidate v0.
- **Mệnh đề:** Candidate selected `.agents/workflows/optimize-agent-harness-system.md` for both negative/out-of-scope queries N1 and N2.
- **Severity:** `Major` for the pilot guardrail; not a canonical-source change.
- **Evidence:** `probe-results.csv` rows N1/N2; `CandidateFalseAuthority = 2` in `probe-summary.json`.
- **Disposition:** `Accept`.
- **Owner response:** Implementer owns the candidate routing logic and accepts a local repair.
- **Repair:** add a minimum candidate keyword-overlap requirement of 2; preserve locked query set, expected paths, primary metric and guardrails.
- **Stop/re-review condition:** do not open independent governance review until the repaired probe has zero false-authority selections and is reproducible.

## F-REVIEW-001

- **Source:** independent governance review by `/root/first_pilot_governance_review_retry` on 2026-09-16.
- **Finding:** the run log did not identify a completed independent reviewer, and the review artifacts were absent.
- **Severity:** `Blocker` for the governance gate; no source mutation.
- **Disposition:** `Accept`.
- **Repair:** record the interrupted reviewer separately, record the fresh reviewer identity and outcome in `orchestration-log.md`, and add `review-findings.md` plus a final `governance-review.md`.

## F-REVIEW-002

- **Source:** independent governance review by `/root/first_pilot_governance_review_retry` on 2026-09-16.
- **Finding:** candidate source-read evidence was not demonstrated because the probe hardcoded `Reads = 1` without reading the selected canonical source.
- **Severity:** `Major` for evidence validity; no source mutation.
- **Disposition:** `Accept`.
- **Repair:** read the selected path during candidate routing, verify at least one query-token match in the selected source, and emit `CandidateSourceVerifications`.

## F-REVIEW-003

- **Source:** independent governance review by `/root/first_pilot_governance_review_retry` on 2026-09-16.
- **Finding:** closure evidence lacked an explicit timebox, retention/expiry rule, bounded run count, and migration/rollback record.
- **Severity:** `Major` for lifecycle control; no source mutation.
- **Disposition:** `Accept`.
- **Repair:** amend the trial contract with explicit lifecycle limits, add `migration-and-rollback.md`, and record that no canonical commit is created pending an owner `Ratify` decision.

## F-REVIEW-004

- **Source:** independent governance review by `/root/first_pilot_governance_review_retry` on 2026-09-16.
- **Finding:** regression evidence covered routing rows but not path/title fallback, local-link integrity, or candidate-index schema validation.
- **Severity:** `Major` for regression coverage; no source mutation.
- **Disposition:** `Accept`.
- **Repair:** run and persist `regression-results.json` with path/title, local-link, and index-schema checks, then update the validation report.
