# Antigravity Coverage & Drift Resolution Policy

This policy defines how we handle skill overlap drift during migration and prevents accidental regressions/duplication.

## Decision requirements for drifted overlaps

The following **12 drifted overlaps** require a recorded, explicit decision per skill:

1. `subagent-driven-development`
2. `airflow-dag-patterns`
3. `prompt-engineering`
4. `test-driven-development`
5. `systematic-debugging`
6. `verification-before-completion`
7. `writing-plans`
8. `executing-plans`
9. `dispatching-parallel-agents`
10. `related-skill`
11. `find-skills`
12. `skill-judge`

Each skill above MUST select exactly one action in `migration/antigravity/drift-resolution.csv`:

- `keep current`
- `replace with source`
- `merge manually`

## Drift ledger contract

All drift decisions MUST be tracked in:

- `migration/antigravity/drift-resolution.csv`

Required columns:

- `skill`
- `current_hash`
- `source_hash`
- `decision`
- `owner`
- `notes`

## Import block (adjacent skills)

To avoid accidental regressions or duplication, importing adjacent skills is blocked until drift decisions are recorded.

A skill import is allowed only when **all 12 drifted overlap rows** in `drift-resolution.csv` satisfy:

1. `decision` is populated with one of:
   - `keep current`
   - `replace with source`
   - `merge manually`
2. `owner` is populated.
3. `current_hash` and `source_hash` are populated.

If any of the above are missing for any of the 12 skills, adjacent skill imports MUST NOT proceed.
