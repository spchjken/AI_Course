# Trial validation report

- **Baseline:** no recorder, runtime root, schema or validator; fixed scenarios supported `0/6`.
- **Candidate:** repository-native recorder and contract.
- **Primary metric:** `6/6` fixed scenarios; all completed fixture traces valid.
- **First independent review:** `Fail`; the earlier self-check overclaimed coverage. Findings `STE-001`–`STE-007` were accepted.
- **Corrected candidate:** `6/6` fixed scenarios pass across 13 direct tests; independent re-review remains required.

## Fixed scenarios

| Scenario | Evidence | Result |
|---|---|---|
| Start known skill; record hash and HEAD | `test_full_lifecycle_and_version_hash` | `Pass` |
| Append bounded event types | `test_event_types_and_second_terminal_are_rejected` | `Pass` |
| Terminal outcomes; reject second terminal | `test_all_terminal_outcomes_validate` plus duplicate-terminal assertion | `Pass` |
| Same-second unique executions, including concurrent processes | `test_same_second_ids_are_unique`; `test_concurrent_process_ids_are_unique` | `Pass` |
| Reject unknown skill, unsafe/absolute/UNC paths, junctions, oversized/sensitive summaries and trace-root escape | `test_invalid_skill_refs_summary_and_escape_are_rejected`; both Windows junction tests | `Pass` |
| Validate exact schema/lifecycle and emit counts-only aggregate without summaries, refs or invalid dimensions | aggregate, tamper and invalid-dimension tests | `Pass` |

Additional tests cover append-prefix integrity, active/stale lock behavior, exact nested keys/types, duplicate starts, timestamp mismatch, malformed directories and invalid-trace privacy.

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
Result: 13/13 Pass

python -X utf8 <skill-validator> <each affected skill>
Result: 3/3 Pass

python -m unittest discover -s .agents/indexing/tests -v
Result: 8/8 Pass
```

The derived index is regenerated only after pre-review evidence stabilizes, then regenerated again after reviewer output before ratification handoff.
