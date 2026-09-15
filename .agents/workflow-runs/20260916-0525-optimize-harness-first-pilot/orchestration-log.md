# Orchestration log

## Run contract

- Scope: test the first pilot contract for retrieval routing with a minimal derived index.
- Canonical inputs: `ai-native-builder/goals/g09-nang-cap-harness-rules-skills-workflows/README.md`, `.agents/workflows/optimize-agent-harness-system.md`, `.agents/decisions/2026-09-15-agent-harness-workflow-proposed.md`, and the pilot design note.
- Allowed writes: this run directory only until a separate owner `Ratify`; no canonical source, skill, rule, or workflow changes.
- Human gate: user explicitly requested this pilot; no permission to integrate candidate into `main`.
- Stop conditions: scope expansion, source mutation, secret/sensitive data, baseline drift, changed thresholds, false authority, or missing independent review.
- Close condition: validation, independent review, disposition, and an owner outcome are recorded.

## Agent registry

| Mã | Định danh | Cha | Vai trò/đơn vị | Hành động | Tệp ghi | Trạng thái |
|---|---|---|---|---|---|---|
| A1 | `/root` | none | Orchestrator — A through G and I | `root` | Run artifacts only | `completed through G and I; H independently verified Pass; awaiting owner outcome` |
| A2 | `/root/first_pilot_governance_review` | `/root` | Governance reviewer — H | `fresh-review` | `none` | `cancelled; not-verified (runtime timeout, interrupted)` |
| A3 | `/root/first_pilot_governance_review_retry` | `/root` | Independent governance reviewer — H | `fresh-review` | `none` | `completed initial Fail and final Pass after accepted repairs` |

The reviewer must receive only the source files, trial contract, candidate index, query set, validation report and criteria. It must not inherit the implementer's conclusion as evidence. A2 was not counted as an independent review because it timed out; A3 is the fresh reviewer identity used for the initial and final evidence.
