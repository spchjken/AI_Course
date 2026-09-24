# Trial validation report

- **Baseline:** no recorder, runtime root, schema or validator; fixed scenarios supported `0/6`.
- **Candidate:** repository-native recorder and contract.
- **Primary metric:** `6/6` fixed scenarios; all completed fixture traces valid.
- **First independent review:** `Fail`; the earlier self-check overclaimed coverage. Findings `STE-001`–`STE-007` were accepted.
- **First corrected candidate:** re-review remained `Fail` after finding hardlink, sequence typing and contention gaps.
- **Second corrected candidate:** final re-review remained `Fail` because schema refs diverged and real Windows processes exposed a lock-file sharing race.
- **Third corrected candidate:** `6/6` fixed scenarios pass across 17 direct tests, including 12 concurrent subprocess writers; final independent re-review remains required.
- **Third re-review:** process locking passed 192/192 adversarial writes, but schema parity remained `Fail`.
- **Fourth corrected candidate:** the same 17 tests now apply invalid ref, slug and timestamp fixtures to both schemas and validator, plus stale legacy-lock migration; final independent re-review remains required.
- **Fourth re-review:** lock migration passed, but an extended canonical parity matrix remained `Fail`.
- **Fifth corrected candidate:** the two-way matrix now includes URL backslashes/case, padded slugs, malformed IPv6 and calendar-invalid timestamps; final independent re-review remains required.
- **Owner stop:** further review loops were explicitly stopped. Candidate `6ce41a4` passes all local checks below, while independent acceptance for this exact SHA remains `Not verified`.

## Fixed scenarios

| Scenario | Evidence | Result |
|---|---|---|
| Start known skill; record hash and HEAD | `test_full_lifecycle_and_version_hash` | `Pass` |
| Append bounded event types | `test_event_types_and_second_terminal_are_rejected` | `Pass` |
| Terminal outcomes; reject second terminal | `test_all_terminal_outcomes_validate` plus duplicate-terminal assertion | `Pass` |
| Same-second unique executions, including concurrent processes | `test_same_second_ids_are_unique`; `test_concurrent_process_ids_are_unique` | `Pass` |
| Reject unknown skill, unsafe/absolute/UNC paths, junctions, oversized/sensitive summaries and trace-root escape | `test_invalid_skill_refs_summary_and_escape_are_rejected`; both Windows junction tests | `Pass` |
| Validate exact schema/lifecycle and emit counts-only aggregate without summaries, refs or invalid dimensions | aggregate, tamper and invalid-dimension tests | `Pass` |

Additional tests cover successful append-prefix integrity, concurrent writers without event loss, active/stale/malformed lock behavior, hardlinked write targets, committed schema conformance, exact nested keys/types (including boolean/float sequence rejection), duplicate starts, timestamp mismatch, malformed directories and invalid-trace privacy.

## Four required layers

- **Positive:** full lifecycle and all terminal outcomes pass.
- **Negative:** unsafe refs, unknown skills, suspected secrets, oversized summaries, path escape, duplicate terminal and schema expansion are rejected.
- **Regression:** all 8 existing indexing tests and all three affected skill validators pass.
- **Comparison:** baseline `0/6`; candidate `6/6`. Candidate adds two required lifecycle commands per skill invocation; optional events are only recorded when useful.

## Privacy and operational checks

- Schema/CLI have no raw prompt, reasoning, environment or full response field.
- Secret-like summary patterns and URL credentials/query/fragment are rejected.
- `.agent-execution-runs/.gitignore` ignores raw execution directories while retaining its README/policy.
- Aggregate contains counts, outcomes and skill hashes but no request/event summaries or refs.
- Two real trial traces were created; the late-start limitation is recorded explicitly because the recorder did not exist at intake.

## Commands

```text
python -m unittest discover -s .agents/execution-tracing/tests -v
Result: 17/17 Pass

python -X utf8 <skill-validator> <each affected skill>
Result: 3/3 Pass

python -m unittest discover -s .agents/indexing/tests -v
Result: 8/8 Pass
```

The derived index is regenerated only after pre-review evidence stabilizes, then regenerated again after reviewer output before ratification handoff.
