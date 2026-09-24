# Implementation log

- **Implementer:** `/root`
- **Branch:** `codex/20260924-skill-execution-traces`
- **Baseline:** `a65e86caff89feb4e7c065fa5a22443a83d4d23e`
- **Candidate implementation commit:** `1f93bde1371b9b87efa3b8d211efcafb793a0ee8`
- **Initial evidence commit:** `cd811a4d8ff8fb6d0374d16985d6f13f60758f63`
- **Corrective commit after first review:** `956e742a81a6d3e0ee63c481f75545809ea1aa3b`
- **Second corrective commit:** `f416cc0`
- **Third corrective commit:** `20ab1c9`
- **Fourth corrective commit:** `053df34`
- **Fifth corrective commit:** pending

## Implemented

- Added a standard-library recorder, schema, tests and operator guide under `.agents/execution-tracing/`.
- Added local runtime storage `.agent-execution-runs/` with nested ignore policy; raw execution directories are not tracked or indexed.
- Added the universal invocation contract to `AGENTS.md` and trace handoff to workflow dispatch/orchestration.
- Updated `$repo-skill-creator`, `$workflow-orchestration` and `$harness-improvement-discovery` without adding per-skill competing schemas.
- Added counts-only aggregate export grouped by skill, `skill_sha256`, lifecycle status and outcome.
- Updated navigation, index configuration, governance decision and portable harness guidance.

## Deviations and corrections

- The design draft initially named `.agents/execution-runs/`. A subprocess write test from prior index work and the current sandbox policy showed `.agents/` writes require elevated permission. Runtime storage moved to `.agent-execution-runs/` at repository root so ordinary skill invocation remains fast; code/schema stay under `.agents/`. This does not change metrics or privacy guardrails.
- The first unit run exposed that the initial `started` append tried to read a nonexistent `events.jsonl`; five tests errored. The implementer accepted the local defect, treated a missing file as an empty log only inside locked append, and reran the full suite successfully.
- The validator was then hardened to reject extra manifest/event fields, validate repository/skill/privacy shapes, expose malformed trace directories and report skill-version drift.
- Independent review rejected the first candidate with `STE-001`–`STE-007`. All findings were accepted. The correction rejects Windows junction/reparse writes, enforces exact schema/lifecycle invariants, excludes invalid dimensions from aggregate output, adds guarded stale-lock recovery and expands direct tests from 7 to 13.
- Re-review reopened hardlink safety, boolean sequence typing, schema parity, concurrent append and malformed-lock recovery. The second correction adds handle-level hardlink rejection, exact integer checks, a machine-readable event schema, schema parity fixtures, 30-second bounded contention retry with in-process serialization, and stale malformed-lock recovery.
- The next re-review found schema ref/slug drift and a Windows sharing race caused by contenders reading an active lock file. The third correction uses an atomic lock-directory, delays metadata reads until stale, adds true multi-process append verification, and applies the same safe ref grammar to manifest and event schemas.
- The following re-review confirmed 192/192 process writes but found validator-accepted noncanonical refs/timestamps and a legacy lock-file migration case. The fourth correction makes validator and schemas share canonical ref/timestamp acceptance, exercises rejection in both directions, and reclaims stale legacy lock files.
- The targeted re-review extended parity cases to URL backslashes/case, padded slugs and invalid calendar values. The fifth correction rejects every case across recorder, validator and schemas and turns malformed bracketed URL parsing into controlled failure.

## Self-check boundaries

The implementation cannot create a host-level hook. It provides a mandatory repository contract and detects missing/invalid/open traces after the fact. Coverage claims must retain this limitation.
