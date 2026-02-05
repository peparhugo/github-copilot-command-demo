#!/usr/bin/env node

const path = require('path');
const { listSkills, readJson } = require('../lib/skill-utils');

function fail(message) {
  console.error(`ERROR: ${message}`);
  process.exit(1);
}

function main() {
  const root = process.cwd();
  const expected = readJson(path.join(root, 'skills_index.json'), []);
  const actual = listSkills(root);

  if (!Array.isArray(expected)) {
    fail('skills_index.json must be a JSON array.');
  }

  const missing = actual.filter((skill) => !expected.includes(skill));
  const stale = expected.filter((skill) => !actual.includes(skill));

  if (missing.length || stale.length) {
    if (missing.length) console.error(`Missing index entries: ${missing.join(', ')}`);
    if (stale.length) console.error(`Stale index entries: ${stale.join(', ')}`);
    fail('skills_index.json is out of date. Run: npm run build:catalog');
  }

  console.log(`Validated ${actual.length} skill(s) against skills_index.json.`);
}

main();
