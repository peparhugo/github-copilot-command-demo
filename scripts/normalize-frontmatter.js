#!/usr/bin/env node

const fs = require('fs');
const path = require('path');
const { listSkills } = require('../lib/skill-utils');

function normalizeSkillFile(filePath) {
  const raw = fs.readFileSync(filePath, 'utf8');
  const normalized = raw.replace(/\r\n/g, '\n').replace(/[ \t]+\n/g, '\n');

  if (normalized !== raw) {
    fs.writeFileSync(filePath, normalized, 'utf8');
    return true;
  }
  return false;
}

function main() {
  const root = process.cwd();
  const skills = listSkills(root);
  let changed = 0;

  for (const slug of skills) {
    const filePath = path.join(root, 'skills', slug, 'SKILL.md');
    if (normalizeSkillFile(filePath)) changed += 1;
  }

  console.log(`Normalized ${changed} skill file(s).`);
}

main();
