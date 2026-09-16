# Post-ratify validation

- **Decision:** Ratify
- **Decision record:** `.agents/decisions/2026-09-16-repo-wide-derived-index-tools-ratified.md`
- **Implementation commit:** `684dd3c`
- **Integration commit:** `54c58bd9b069c0768fe7d32f6290997bda02d66b`
- **Validated branch:** `main`
- **Validation baseline:** `54c58bd9b069c0768fe7d32f6290997bda02d66b`

The ratified implementation was fast-forwarded into `main`. The following
post-ratify checks were run against that integrated tree:

| Check | Result |
|---|---|
| `sync_index.py --full --baseline-commit 54c58bd9b069c0768fe7d32f6290997bda02d66b` | exit 0; 158 indexed entries |
| `sync_index.py --check` | exit 0; no stale sources |
| `validate_index.py` | exit 0; valid schema, no missing/stale sources, no authority mismatches, no false canonical entries |
| `python -B -m unittest discover -s .agents/indexing/tests -v` | 8/8 tests pass |
| Repeat full rebuild hash comparison | deterministic: `true` |

The generated artifact reports `derived=true` and `canonical=false`. The six
missing links from `repo-skill-creator/SKILL.md` remain the configured optional
reference exemptions; they are reported explicitly by the validator. No
canonical curriculum, rule, workflow, goal, or decision source was changed.

The remaining scheduler/daily job/workflow-hook automation is intentionally
deferred and is outside this ratified trial's scope. After this record is
committed, the index is refreshed once more against the closure commit and
then `main` is pushed to `origin/main`.
