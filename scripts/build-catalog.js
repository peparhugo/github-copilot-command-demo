#!/usr/bin/env node

const path = require('path');
const { listSkills, writeJson } = require('../lib/skill-utils');

function main() {
  const root = process.cwd();
  const skills = listSkills(root);

  const indexPath = path.join(root, 'skills_index.json');
  const catalogPath = path.join(root, 'data', 'catalog.json');
  const aliasesPath = path.join(root, 'data', 'aliases.json');

  const catalog = skills.map((slug) => ({
    slug,
    path: `skills/${slug}/SKILL.md`,
    wave: slug.includes('/') ? slug.split('/')[0] : 'core',
  }));

  writeJson(indexPath, skills);
  writeJson(catalogPath, catalog);
  writeJson(aliasesPath, {});

  console.log(`Wrote ${skills.length} skills to catalog metadata.`);
}

main();
