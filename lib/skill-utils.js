const fs = require('fs');
const path = require('path');

function listSkills(rootDir = process.cwd()) {
  const skillsDir = path.join(rootDir, 'skills');
  if (!fs.existsSync(skillsDir)) {
    return [];
  }

  const skills = [];
  const walk = (relative = '') => {
    const dir = path.join(skillsDir, relative);
    for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
      if (entry.name.startsWith('.')) continue;
      const relPath = path.join(relative, entry.name);
      const fullPath = path.join(skillsDir, relPath);

      if (entry.isDirectory()) {
        const skillFile = path.join(fullPath, 'SKILL.md');
        if (fs.existsSync(skillFile)) {
          skills.push(relPath.replace(/\\/g, '/'));
          continue;
        }
        walk(relPath);
      }
    }
  };

  walk();
  return skills.sort();
}

function readJson(filePath, fallback = null) {
  if (!fs.existsSync(filePath)) return fallback;
  return JSON.parse(fs.readFileSync(filePath, 'utf8'));
}

function writeJson(filePath, value) {
  const content = `${JSON.stringify(value, null, 2)}\n`;
  fs.mkdirSync(path.dirname(filePath), { recursive: true });
  fs.writeFileSync(filePath, content, 'utf8');
}

module.exports = {
  listSkills,
  readJson,
  writeJson,
};
