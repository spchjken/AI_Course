# Harness discovery/validation split — implementation record

- **Date:** 2026-09-24
- **Status:** `Closed` — independent re-review `Pass`; no unresolved `Blocker` or `Major`
- **Decision:** [`../../decisions/2026-09-24-separate-harness-discovery-from-validation.md`](../../decisions/2026-09-24-separate-harness-discovery-from-validation.md)
- **Scope:** create `$harness-improvement-discovery`, rename and narrow the validation workflow, synchronize current navigation/design links, and update the portable harness pattern note.
- **Owner gate:** repository owner already approved the architecture and implementation request; final acceptance depends on independent review findings being resolved.
- **Excluded:** skill-invocation telemetry implementation, workflow promotion to `Active`, historical run rewrites, `.gitignore`, commit and push.

## Evidence

- `orchestration-log.md` — work ownership and independent-review lifecycle.
- `governance-review.md` — independent verdict and limitations.
- `review-findings.md` — reviewer-owned findings, if any.
- `finding-disposition.md` — implementer response and repair evidence.
- Deterministic checks are recorded in the final implementation handoff after review.

Historical records retain the former workflow name because they describe the baseline at the time of execution.

## Final validation

- Skill validation: `Pass` with Python UTF-8 mode.
- Indexing tests: `8/8 Pass`.
- Affected Markdown links: `Pass`.
- Independent review: first verdict `Fail`; HDS-001 and HDS-002 were accepted, repaired and re-reviewed `Resolved`; latest verdict `Pass`.
- Derived index before closure: `validate_index.py` returned `pass: true` with no missing/stale sources or links; `sync_index.py --check` returned `0`. The closed-status hash is regenerated as the final mechanical step.
