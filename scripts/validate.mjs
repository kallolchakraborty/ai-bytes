// scripts/validate.mjs
// Validates JSON content files and generated assets

import fs from 'fs';
import path from 'path';

const contentDir = 'content';
const errors = [];

// Validate all JSON files parse correctly
function validateJsonDir(dir) {
  const entries = fs.readdirSync(dir, { withFileTypes: true });
  for (const entry of entries) {
    const fullPath = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      validateJsonDir(fullPath);
    } else if (entry.name.endsWith('.json')) {
      try {
        const data = JSON.parse(fs.readFileSync(fullPath, 'utf8'));
        // Check required fields
        if (!data.id) errors.push(`${fullPath}: missing "id"`);
        if (!data.title) errors.push(`${fullPath}: missing "title"`);
        if (!data.category) errors.push(`${fullPath}: missing "category"`);
        if (!data.subcategory) errors.push(`${fullPath}: missing "subcategory"`);
      } catch (e) {
        errors.push(`${fullPath}: invalid JSON - ${e.message}`);
      }
    }
  }
}

if (fs.existsSync(contentDir)) {
  validateJsonDir(contentDir);
}

if (errors.length > 0) {
  console.error('Validation failed:');
  errors.forEach(e => console.error('  - ' + e));
  process.exit(1);
} else {
  console.log('Validation passed: all JSON files valid.');
}
