# Impact map

| Area | Expected effect | Authority impact | Rollback |
|---|---|---|---|
| `.agents/indexing/**` | New stdlib tools, schema, config, tests | Operational only | Delete the directory on the trial branch |
| `.agents/generated/context-index.json` | Commit a reproducible repository snapshot | `derived=true`, `canonical=false` | Remove generated file and rebuild later |
| `.context-index-cache.json`, `.context-index-lock` | Local stat/hash cache and lock (default in this sandbox) | Ignored, never canonical | Delete local cache |
| `.gitignore` | Ignore local cache only | No source authority change | Revert one rule |
| `.agents/workflow-runs/<run>` | Operational evidence | Not an authority source | Keep as audit record |

Canonical rules, workflows, goals, decisions, and lesson content are read-only
in this trial.
