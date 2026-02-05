# Antigravity migration manifest

This folder is the canonical manifest for skill migration work in this repository.

## Merge policy

- `skip`: source and local skill are an exact match.
- `manual-review`: same skill name exists, but `SKILL.md` content has drifted.
- `import`: source skill is missing locally and should be ported.

Use this manifest as the only source of truth for all subsequent migration PRs.
