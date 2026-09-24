# Locked trial contract

- **Owner decision:** `Approve trial` inferred from the explicit instruction “thực hiện nó bây giờ” after the missing capability was identified; this is not `Ratify`.
- **Mode:** `Improvement trial`.
- **Timebox:** current implementation session through independent review.
- **Primary metric:** all six fixed functional scenarios produce the predeclared outcome, and every completed fixture trace passes schema/lifecycle validation. Threshold: `6/6` scenarios and `100%` completed trace validity.
- **Baseline:** `0/6` scenarios are supported because no recorder/storage/schema exists.

## Fixed scenarios

1. Start a valid known skill and record its skill-file hash plus repository HEAD.
2. Append bounded `artifact`, `check`, `correction` and `retry` events without rewriting prior events.
3. Finish with each allowed terminal outcome and reject a second terminal event.
4. Create concurrent/same-second invocations with unique IDs and isolated directories.
5. Reject unknown skills, absolute/traversal references, oversized summaries and paths outside the trace root.
6. Validate all traces and emit a privacy-safe aggregate that contains counts/outcomes but no request or event summaries.

## Guardrails

- No raw prompt, chain-of-thought, secret, personal data, environment dump or full tool response field exists in the schema/CLI.
- Raw traces are local and ignored by nested policy; the derived index excludes the runtime tree.
- Existing workflow runs and curriculum behavior remain unchanged.
- The recorder uses only Python standard library and works on Windows paths.
- Missing platform hooks are stated explicitly; documentation must not call coverage automatic or complete.
- `.gitignore` and files outside the impact map are untouched.

## Task contract

```text
Objective: implement a repository-native skill execution trace mechanism
Allowed reads: repository harness, skills, workflows, indexing tools and this run
Allowed writes: paths labelled Update in impact-map.md
Canonical inputs: AGENTS.md, workflow/dispatch contracts, approved trial contract
Required skills: $workflow-orchestration, then $repo-skill-creator for skill changes
Required outputs: recorder, tests, storage/privacy contract, integration docs, decision, validation and review evidence
Acceptance: 6/6 scenarios; all guardrails; independent review Pass
Stop: user-file overlap, sensitive-data requirement, scope expansion, baseline drift, metric change or unresolved Major/Blocker
Do not: claim host-level hooks, store raw reasoning, edit curriculum, edit root .gitignore, self-ratify or integrate main
```
