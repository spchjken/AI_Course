# Impact map

| Path | Label | Owner | Impact/reason | Check | Rollback |
|---|---|---|---|---|---|
| `ai-native-builder/goals/g09-nang-cap-harness-rules-skills-workflows/README.md` | `Reverify` | Goal owner | Canonical source used as routing target; not edited. | Link/source and authority check | No source rollback |
| `.agents/workflows/optimize-agent-harness-system.md` | `Reverify` | Workflow owner | Contract and gates under test; not edited. | State/gate reference check | No source rollback |
| `.agents/decisions/2026-09-15-agent-harness-workflow-proposed.md` | `Reverify` | Repository owner | Decision boundary for Proposed workflow; not edited. | Scope/authority check | No source rollback |
| `context-index.json` in this run | `Update` | Implementer | Derived candidate only; not canonical. | Schema, path and authority validation | Delete candidate artifact |
| `query-set.tsv` and `run_probe.ps1` in this run | `Update` | Verifier | Reproducible synthetic evaluation. | Deterministic rerun and diff | Delete run artifacts |
| `validation-report.md` and review files | `Update` | Verifier/reviewer | Evidence and handoff. | Completeness and independent review | Retain for audit |

No goal, workflow, decision, skill, rule, external system or repository-wide index is modified by this trial.
