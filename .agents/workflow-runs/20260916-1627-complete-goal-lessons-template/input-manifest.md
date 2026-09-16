# Input manifest

- Run ID: `20260916-1627-complete-goal-lessons-template`
- Baseline: `35987be6b1edd50ba38b51055853d42f59a7ba83`
- Mode: `Targeted repair`
- Requested outcome: align `.agents/workflows/complete-goal-lessons.md` with the
  current workflow template without changing lesson or curriculum ownership.

## Required sources

| Source | Purpose | Status |
|---|---|---|
| `AGENTS.md` | repository operating contract | read |
| `.agents/rules/README.md` | governance and conflict rules | read |
| `.agents/rules/quality-gates.md` | hard gates and quality scoring | read |
| `.agents/workflows/README.md` | workflow registry/template context | read |
| `.agents/workflows/agent-dispatch-protocol.md` | dispatch, independence and finding protocol | read |
| Peer workflows in `.agents/workflows/` | structural comparison | read |
| Existing `complete-goal-lessons.md` | preserve substantive Appendix A contract | read |

## Scope guard

Allowed writes are the workflow template, its governance record, its run evidence,
the workflow registry status correction, and the derived index. Goal sources,
lesson content, curriculum architecture and shared dispatch protocol are excluded.
