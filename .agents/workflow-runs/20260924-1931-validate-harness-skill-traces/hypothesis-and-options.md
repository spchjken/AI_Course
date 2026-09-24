# Hypothesis and options

## Competing explanations

1. **Missing storage/tooling:** skills leave no trace because the repo has no shared recorder or storage contract.
2. **Instruction-only gap:** a folder and schema would be unnecessary if skill instructions consistently wrote existing workflow logs.
3. **Platform-hook gap:** repository code cannot observe skill activation automatically; only the host platform could make tracing complete without agent cooperation.

Evidence supports (1) and (3): there is no recorder, and repo code has no platform event hook. Explanation (2) cannot cover standalone skills and would mix workflow orchestration with skill efficacy evidence.

## Options

- **No change:** cheapest, but discovery remains blind to standalone skill behavior.
- **Instruction-only logging:** add prose to every skill; low code cost but duplicated, inconsistent and hard to validate.
- **External telemetry service:** stronger automation, but adds credentials, privacy and unavailable infrastructure.
- **Selected minimum:** one deterministic local recorder, one ignored runtime root, one central invocation contract, workflow handoff fields, validator/tests and a privacy-safe aggregate export.

The selected option cannot honestly claim platform-level automatic capture. It makes tracing mandatory and cheap inside this repo, reports missing/unfinished traces, and leaves a clear upgrade path if the host later exposes hooks.
