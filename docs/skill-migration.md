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

### Required migration checks

1. `python3 scripts/migration/verify-skill-completeness.py`
   - For every imported `skills/**/SKILL.md`, ensures every sibling file/folder from the corresponding source snapshot skill directory (`.github/skills/**`) is imported too.
2. `python3 scripts/migration/report-symlinks.py .github/skills`
   - Reports symlinked skills in source snapshots before import planning.

### Symlink strategy

Wave migrations **replace symlinked source skills with copied directories during import** (do not preserve symlinks in `skills/`).

Rationale:

- copied directories are portable across platforms and archive formats that do not preserve symlink metadata,
- copied content avoids runtime/tooling differences between environments with and without symlink support,
- skill completeness checks can enforce a deterministic file set in each imported skill folder.

When symlinked skills are reported (for example `anthropics/docx`, `anthropics/pdf`, `anthropics/pptx`, `anthropics/xlsx` in source snapshots), import them as normal directories containing all resolved files.

Validation for each wave:

1. Run `npm run check:skill-completeness`.
2. Run `npm run report:source-symlinks`.
3. Run `npm run normalize:frontmatter` after importing skill files.
4. Run `npm run build:catalog` to refresh metadata.
5. Run `npm run validate:skills` before opening/updating the PR.

Merge rule: only include skills scoped for that wave plus regenerated metadata, and require both migration checks to pass before merging any wave PR.
