# Candidate context package

- Package: `pilot-0.1`
- Derived from: `context-index.json`
- Canonical status: `Not canonical`; disposable until a separate `Ratify`.
- Task scope: route the eight locked queries to one of three allowed sources or `OUT_OF_SCOPE`.

## Routing contract

1. Read the derived index first.
2. Select a source only when at least two indexed keyword overlaps support the route.
3. Return `OUT_OF_SCOPE` when the minimum is not met.
4. Read the selected canonical source only after routing.
5. Never infer a source, status or permission not present in the selected source.

## Allowed sources

- `ai-native-builder/goals/g09-nang-cap-harness-rules-skills-workflows/README.md` — canonical goal design.
- `.agents/workflows/optimize-agent-harness-system.md` — proposed operational workflow.
- `.agents/decisions/2026-09-15-agent-harness-workflow-proposed.md` — repository governance decision.
