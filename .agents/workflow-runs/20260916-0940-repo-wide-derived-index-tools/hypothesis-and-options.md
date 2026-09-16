# Hypothesis and options

## Hypothesis

A deterministic, repository-wide derived index that stores structural metadata
and two hashes, while leaving lexical terms to a query-time search tool, can be
kept current fast enough for workflow use without weakening canonical-source
authority.

## Options considered

- **Per-file keyword lists:** rejected; they are lossy, become stale, and add
  duplicate searchable state. Query-time lexical search is the source of truth.
- **Path-only identity:** rejected; it cannot distinguish a move from a new file.
- **Content hash only:** insufficient for a stable path-level entry; it cannot
  represent two paths with identical content without ambiguity.
- **Content + path entry hash:** selected. Unique unchanged content can produce a
  move event; ambiguous duplicates remain delete/create or copy events while the
  final state stays correct.
- **Automatic scheduler/hook now:** deferred until correctness and latency are
  measured in this trial.
