# Impact map

| Path | Label | Owner | Reason | Verification | Rollback |
|---|---|---|---|---|---|
| `.agents/execution-tracing/**` | `Update` | Implementer | Recorder, validator and tests | Unit/CLI tests | Revert trial commit |
| `.agent-execution-runs/README.md` and nested `.gitignore` | `Update` | Implementer | Writable runtime location, privacy and retention contract | Ignore/path tests | Revert trial commit |
| `AGENTS.md` | `Update` | Implementer + governance review | Universal invocation rule | Contract review and scenarios | Revert trial commit |
| `.agents/workflows/agent-dispatch-protocol.md` | `Update` | Implementer + governance review | Carry trace id/path in delegated work | Link/contract review | Revert trial commit |
| `.agents/skills/workflow-orchestration/SKILL.md` | `Update` | Implementer using `$repo-skill-creator` | Require trace handoff for selected skills | Skill validation | Revert trial commit |
| `.agents/skills/harness-improvement-discovery/SKILL.md` | `Update` | Implementer using `$repo-skill-creator` | Read actual trace source and aggregates | Skill validation | Revert trial commit |
| `.agents/skills/repo-skill-creator/SKILL.md` | `Update` | Implementer using `$repo-skill-creator` | Preserve central trace compatibility for future skills | Skill validation | Revert trial commit |
| `README.md`, `.agents/workflows/README.md` | `Update` | Implementer | Discovery and navigation | Link validation | Revert trial commit |
| `.agents/indexing/index-config.json`, generated index | `Update` | Implementer | Exclude ignored raw traces; index recorder/docs | Index tests/validator | Rebuild from baseline config |
| `.agents/decisions/2026-09-24-skill-execution-traces.md` | `Update` | Implementer; owner ratifies | Governance rationale and migration | Independent review | Revert trial commit |
| `temp/generalizable-agent-harness-patterns.md` | `Update` | Implementer | Portable bootstrap instructions | Manual/link review | Local restore; file remains ignored |
| Curriculum files and root `.gitignore` | `No change` | Existing owners | Outside scope/user-owned dirty state | `git status` and diff | Not applicable |
