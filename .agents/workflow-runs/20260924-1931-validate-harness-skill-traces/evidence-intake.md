# Evidence intake

- **Trigger:** `Owner-nominated hypothesis`.
- **Problem statement:** Without a universal execution record for repository-local skills, later audits cannot distinguish whether a skill was invoked, which version ran, what evidence it produced, whether it needed retries/corrections, or how it ended.
- **Expected behavior:** Each invocation can be reconstructed from a bounded, machine-readable local trace and selectively summarized without storing raw prompts or hidden reasoning.
- **Observed behavior:** `.agents/workflow-runs/` records workflow orchestration only; no trace root, schema or recorder exists for standalone skill use.
- **Direct evidence:** repository search on 2026-09-24 found workflow-run references and design text mentioning skill traces, but no `execution-runs` implementation or recorder.
- **Counterevidence:** Git history and conversation may indirectly show some skill use; workflow orchestration logs may name required skills. Neither proves invocation lifecycle or skill-version-specific outcome.
- **Initial impact:** `Medium` — it blocks systematic learning from skill behavior but is not an active safety incident.
- **Forbidden data:** raw prompts, chain-of-thought, secrets, personal data, full external responses, environment dumps and unrestricted file content.
- **Decision owner:** repository owner.
