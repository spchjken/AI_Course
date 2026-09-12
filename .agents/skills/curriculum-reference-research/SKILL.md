---
name: curriculum-reference-research
description: Research, compare, and maintain authoritative external evidence for curriculum design. Use once for every gNN after its learning design and content trace exist but before lesson prose is authored, and use targeted follow-up when a material claim about pedagogy, tools, APIs, safety, or user-supplied sources needs verification.
---

# Curriculum reference research

Verify claims that can change curriculum design, learner instructions, safety, or tool behavior. Produce decision-ready evidence, not a bibliography.

## Run one baseline scan per goal

Run the baseline scan after `learning-design-contract.md` and `content-trace.md` exist, but before authoring `lesson.md`, `practice.md`, `instructor-guide.md`, `assessment.md`, or `pilot-feedback-form.md`.

1. Compare the proposed audience, outcome, scope, sequence, practice, learner artifact, and evidence with maintained curricula or guidance from accountable institutions.
2. Find official sources or original research for pedagogical, technical, or safety assumptions that could change the design.
3. Seek at least one credible limitation, counterexample, or narrower alternative for each high-impact decision.
4. Record similarities, differences, and applicability. Judge the current design from its goal, audience, constraints, logic, and evidence; do not copy an external curriculum merely because it exists.
5. Close the baseline scan before authoring. If authoring later reveals a new material claim, run only a targeted follow-up for that claim rather than repeating the landscape scan.

## Use available search and browsing tools

Use the environment's available web search and browsing capability; do not depend on one vendor-specific tool name.

1. Search the web with several narrow queries combining the audience, outcome, source type, and limitation being tested.
2. Open the original page, official documentation, or full paper. Never use a search snippet, search-results page, or AI-generated summary as evidence.
3. For product behavior, prefer official documentation, specifications, policies, and release notes.
4. For scientific claims, prefer original papers, appropriate systematic reviews, and first-party datasets; inspect population, task, method, and limitations.
5. For curriculum precedents, prefer maintained material from accountable institutions. Treat course structure as design precedent, not proof of pedagogical effectiveness.
6. If search is unavailable, the original source cannot be opened, or required access is missing, return `Inconclusive` or `Not verified` as appropriate. Do not substitute model memory for an inspectable source.

## Apply the default search budget

For one baseline scan, normally use three to five query groups and inspect about four to eight promising original sources. Extend by at most two query groups when sources conflict, counterevidence is still missing, or the decision has high learner or safety impact.

Stop when the relevant curriculum precedent has been checked where available, every material claim has suitable original or official evidence, credible counterevidence or limitations have been sought, and new sources no longer change the comparison or verdict. Also stop at the budget limit and record remaining uncertainty instead of forcing a conclusion.

Source count does not establish consensus. One directly applicable primary source may outweigh several derivative sources.

## Frame the research decision

1. Read `.agents/rules/README.md` and `.agents/rules/safety-and-currency.md`.
2. State the exact claim, disputed premise, or instruction to verify in falsifiable language.
3. State why the answer matters, which curriculum files it may affect, and how current the evidence must be.
4. Separate factual claims from product preferences and pedagogical choices. Evidence may inform a trade-off but cannot choose a preference for the user.
5. Define what evidence would support, weaken, or falsify each important claim before searching.

Do not continue into dependent implementation while a material conflict remains unresolved under the central conflict protocol.

## Build a claim ledger

Use one row per claim:

| Field | Content |
|---|---|
| Claim | A precise proposition, not a broad topic. |
| Claim type | Product behavior, technical mechanism, research finding, standard, market fact, or curriculum precedent. |
| Decision impact | What changes if the claim is true or false. |
| Required currency | Stable, version-bound, or rapidly changing. |
| Supporting evidence | Evidence expected to confirm the claim. |
| Falsifying evidence | Evidence expected to contradict or limit it. |

Prioritize claims with high learner impact, high uncertainty, or rapid change. Do not expand into a survey of tools that does not affect a decision.

## Select sources

Prefer sources in this order when applicable:

1. official product documentation, specifications, standards, policies, or release notes;
2. original research papers and first-party datasets;
3. maintained curricula or guidance from accountable institutions;
4. reputable secondary analysis for context, not as a substitute for available primary evidence.

For every source, check authorship, authority, publication or update date, version, scope, methodology where relevant, and direct support for the claim. Treat vendor marketing, search snippets, unsourced summaries, and generated text as leads rather than proof.

When the user supplies a source, inspect it directly and test it with the same rigor. Do not accept or reject it based on reputation alone.

## Investigate both directions

1. Search for the strongest evidence supporting the proposition.
2. Search for credible counterevidence, limitations, failure cases, or a narrower interpretation.
3. Compare sources that discuss the same version, population, task, and conditions.
4. Resolve apparent contradictions by checking definitions, dates, experimental setup, and applicability.
5. Distinguish what a source states directly from what is inferred for this curriculum.
6. Record uncertainty when evidence is incomplete or not transferable to beginners using AI-native workflows.

Do not manufacture consensus from source count. One directly applicable primary source may outweigh several derivative summaries.

## Reach a calibrated verdict

Give each claim one verdict:

- `Supported` — adequate evidence directly supports the claim in the relevant scope;
- `Partially supported` — a narrower or conditional version is supported;
- `Not supported` — available evidence does not establish the claim;
- `Contradicted` — credible evidence supports the opposite;
- `Inconclusive` — evidence is insufficient or materially conflicting.

State confidence, applicability limits, and what new evidence would change the verdict.

## Output contract

Return:

1. research question and decision context;
2. curriculum-precedent comparison covering audience, outcome, structure, practice, evidence, similarities, differences, and applicability;
3. claim ledger with verdicts;
4. evidence table containing source title, direct link, authority, publication/update date, checked date, version/scope, evidence direction, and supported claim;
5. strongest supporting and falsifying evidence;
6. curriculum implication stated as a proposed change, no change, warning, or unresolved decision;
7. uncertainty and recheck trigger for unstable information.

Keep quotations minimal and paraphrase faithfully. Place citations next to the claim they support. When recording evidence in the repository, store the concise takeaway and recheck metadata near the dependent content rather than copying manuals.

## Hand off

- Send evidence about goal boundaries or order to `$curriculum-goal-design`.
- Send verified instructional facts to `$lesson-authoring`.
- Send unresolved currency or safety risk to `$curriculum-quality-review` as a blocker or limitation.

Research is complete only when a curriculum decision can be made honestly from the evidence or explicitly left unresolved.
