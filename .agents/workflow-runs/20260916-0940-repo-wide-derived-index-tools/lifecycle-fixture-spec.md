# Lifecycle fixture specification

The unittest fixture creates a UTF-8 Markdown source and exercises this exact
sequence:

1. full build and deterministic no-op;
2. same-path content edit;
3. a content edit with unchanged size/mtime metadata followed by strict
   `--check` (must return stale);
4. exact move (unique unchanged content, must emit `moved`);
5. move plus edit (must emit `deleted` + `created`);
6. create, delete and copy;
7. duplicate-content ambiguity (must not infer a move);
8. case-only rename on Windows (must emit `moved`);
9. transient unstable read (must retry) and persistent metadata/config exclusion;
10. tampered authority metadata and outside-root output rejection;
11. source search filtering and stale context-package refusal.

The fixture suite is self-contained under `tempfile.TemporaryDirectory`; it
does not modify canonical repository sources.
