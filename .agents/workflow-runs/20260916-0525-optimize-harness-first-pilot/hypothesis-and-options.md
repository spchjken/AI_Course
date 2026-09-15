# Hypotheses and options

## Competing hypotheses

| ID | Hypothesis | Evidence that supports it | Evidence that would falsify it |
|---|---|---|---|
| H1 | A minimal derived index improves routing effort without harming authority accuracy. | One bounded index can expose type, authority, status and keywords before source reading. | Candidate accuracy falls, returns false authority, or effort does not improve. |
| H2 | The index adds no value because the three-source corpus is already small and explicit. | Baseline and candidate have equal accuracy and equal reading effort. | Candidate safely reduces files read while preserving accuracy. |
| H3 | The real risk is scope confusion, not retrieval effort. | Negative/out-of-scope probes produce false source selections. | Negative probes are rejected and traceability remains intact. |

## Options

1. `No change`: keep direct search over the three sources.
2. `Trial`: use one derived index and a task-specific context package; do not change canonical sources.
3. `Rejected`: build RAG/graph or migrate metadata across the repository. This is outside scope and not justified by this pilot.

Selected option: `Trial`, because it is the smallest reversible change that distinguishes H1–H3.
