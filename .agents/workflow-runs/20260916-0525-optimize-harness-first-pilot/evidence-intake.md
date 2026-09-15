# Evidence intake

## Trigger

`Owner-requested exploration`: the owner asked to run the first controlled pilot of `optimize-agent-harness-system` against its first-pilot design note. This is an authorized exploration, not evidence that the candidate is already useful.

## Problem statement

Can a minimal derived index help a new agent route a bounded set of questions to the correct authoritative source with no increase in false authority, while reducing source-reading effort?

## Expected and observed baseline behavior

- Expected: source selection is traceable to one of three exact canonical inputs; out-of-scope questions are rejected rather than guessed.
- Baseline method: inspect/search all three allowed source files using the locked query set, then select a source or `OUT_OF_SCOPE`.
- Candidate method: inspect the derived index first, select one source entry or `OUT_OF_SCOPE`, then read only the selected source.
- Initial observed issue: without an explicit index, the operator must inspect all three sources for each query; the pilot plan hypothesizes that a small index reduces this effort.

## Evidence limits and privacy

The probe uses only public repository Markdown and synthetic queries. No secrets, personal data, account data, hidden prompts, or external systems are used. The deterministic probe measures routing mechanics, not general model quality.
