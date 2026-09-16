# Evidence intake

## User decisions in scope

The owner approved all five implementation decisions:

1. Commit the global derived JSON index; ignore only local cache/lock state.
2. Use Python standard library; use `rg` only as an optional search accelerator.
3. Index `.agents/workflow-runs/**` as `operational-evidence`, excluded from
   default authority search.
4. Treat move-plus-edit as delete plus create; infer a move only for a unique
   unchanged `content_hash`.
5. Defer daily scheduler and workflow integration until the tools are proven.

## Previous evidence

The first pilot was ratified in `.agents/decisions/2026-09-16-optimize-agent-harness-first-pilot-ratified.md`.
That decision explicitly kept its three-entry index run-scoped and did not
authorize repository-wide migration. This run is the separately authorized
implementation trial for the five decisions above.

## Boundary

No canonical source is edited. The worker may write only the indexing tools,
generated derived index, `.gitignore` cache rule, and this new run directory.
