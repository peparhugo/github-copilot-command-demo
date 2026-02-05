# Skill migration waves

This repository migrates skills in waves so infra and content changes can be reviewed independently.

## Wave PR-0: Infrastructure only

PR-0 imports shared migration tooling and metadata only:

- metadata validators (`scripts/validate_skills.py`, `scripts/validate-skills.js`)
- catalog/frontmatter generators (`scripts/build-catalog.js`, `scripts/normalize-frontmatter.js`)
- utility helpers (`lib/skill-utils.js`)
- metadata snapshots (`skills_index.json`, `data/catalog.json`, `data/aliases.json`)

Validation for PR-0:

1. `npm run validate:skills:pr0`
2. `npm run build:catalog`
3. `npm run validate:skills`

Merge rule: no `skills/*` directory content is included in PR-0.

## Wave PR-1+ : Skill content batches

Each subsequent wave imports a bounded set of skills and updates catalog metadata.

Validation for each wave:

1. Run `npm run normalize:frontmatter` after importing skill files.
2. Run `npm run build:catalog` to refresh metadata.
3. Run `npm run validate:skills` before opening/updating the PR.

Merge rule: only include skills scoped for that wave plus regenerated metadata.
