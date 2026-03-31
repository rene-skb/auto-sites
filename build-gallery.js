#!/usr/bin/env node
/**
 * Build gallery with thumbnails
 * 
 * Usage: node build-gallery.js [--screenshots]
 * 
 * --screenshots: Generate missing screenshots (slow, requires puppeteer)
 */

const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

const DEMOS_DIR = path.join(__dirname, 'demos');
const THUMBS_DIR = path.join(__dirname, 'thumbnails');
const GALLERY_TEMPLATE = path.join(DEMOS_DIR, 'gallery.html');
const OUTPUT = path.join(DEMOS_DIR, 'index.html');
const BUILD_LOG = path.join(__dirname, 'build-log.md');

// Ensure thumbnails dir exists
if (!fs.existsSync(THUMBS_DIR)) {
  fs.mkdirSync(THUMBS_DIR);
}

// Parse build log for metadata
function parseBuildLog() {
  const metadata = {};
  
  if (!fs.existsSync(BUILD_LOG)) return metadata;
  
  const content = fs.readFileSync(BUILD_LOG, 'utf8');
  const buildRegex = /### (.+?) — (.+?), (.+?)$/gm;
  
  let match;
  while ((match = buildRegex.exec(content)) !== null) {
    const name = match[1].trim();
    const category = match[2].trim().toLowerCase();
    const city = match[3].trim();
    
    // Convert name to slug
    const slug = name.toLowerCase()
      .replace(/['']/g, '')
      .replace(/[^a-z0-9]+/g, '-')
      .replace(/-+/g, '-')
      .replace(/^-|-$/g, '');
    
    metadata[slug] = { name, category, city };
  }
  
  return metadata;
}

// Category mapping
function normalizeCategory(cat) {
  const map = {
    'cafe': 'food',
    'coffee': 'food',
    'restaurant': 'food',
    'bakery': 'food',
    'food truck': 'food',
    'ice cream': 'food',
    'brewery': 'food',
    'bar': 'food',
    'grocery': 'food',
    'caribbean soul food': 'food',
    
    'vintage': 'retail',
    'thrift': 'retail',
    'record shop': 'retail',
    'bookstore': 'retail',
    'florist': 'retail',
    'plant shop': 'retail',
    'grocery': 'retail',
    
    'tattoo': 'creative',
    'tattoo studio': 'creative',
    'music': 'creative',
    'artist': 'creative',
    'dj': 'creative',
    'portfolio': 'creative',
    
    'salon': 'services',
    'hair salon': 'services',
    'barber': 'services',
    'barbershop': 'services',
    'groomer': 'services',
    'grooming': 'services',
    'yoga': 'services',
    'pilates': 'services',
    'martial arts': 'services',
    'bike shop': 'services',
    'cobbler': 'services',
  };
  
  return map[cat] || 'other';
}

// Scan demos directory
function scanDemos() {
  const metadata = parseBuildLog();
  const demos = [];
  
  const dirs = fs.readdirSync(DEMOS_DIR)
    .filter(f => fs.statSync(path.join(DEMOS_DIR, f)).isDirectory())
    .filter(f => fs.existsSync(path.join(DEMOS_DIR, f, 'index.html')));
  
  for (const slug of dirs) {
    const meta = metadata[slug] || {};
    const hasThumb = fs.existsSync(path.join(THUMBS_DIR, `${slug}.png`));
    
    // Try to extract name from index.html title if not in build log
    let name = meta.name;
    if (!name) {
      try {
        const html = fs.readFileSync(path.join(DEMOS_DIR, slug, 'index.html'), 'utf8');
        const titleMatch = html.match(/<title>(.+?)</);
        if (titleMatch) {
          name = titleMatch[1].split('—')[0].split('|')[0].trim();
        }
      } catch (e) {}
    }
    
    demos.push({
      slug,
      name: name || slug.replace(/-/g, ' ').replace(/\b\w/g, c => c.toUpperCase()),
      category: normalizeCategory(meta.category || ''),
      city: meta.city || '',
      hasThumb
    });
  }
  
  // Sort alphabetically
  demos.sort((a, b) => a.name.localeCompare(b.name));
  
  return demos;
}

// Generate screenshots for sites without thumbnails
async function generateScreenshots(demos) {
  const missing = demos.filter(d => !d.hasThumb);
  
  if (missing.length === 0) {
    console.log('All thumbnails exist!');
    return;
  }
  
  console.log(`Generating ${missing.length} screenshots...`);
  
  // Start local server
  const serverProcess = require('child_process').spawn('python3', ['-m', 'http.server', '8899'], {
    cwd: DEMOS_DIR,
    stdio: 'ignore',
    detached: true
  });
  
  // Wait for server
  await new Promise(r => setTimeout(r, 2000));
  
  const SCREENSHOT_JS = path.join(__dirname, '..', 'skills', 'auto-site-builder', 'screenshot.js');
  
  for (const demo of missing) {
    console.log(`📸 ${demo.slug}...`);
    try {
      execSync(`node "${SCREENSHOT_JS}" "http://localhost:8899/${demo.slug}/index.html" "${path.join(THUMBS_DIR, demo.slug + '.png')}"`, {
        stdio: 'ignore',
        timeout: 30000
      });
      demo.hasThumb = true;
      console.log(`✅ ${demo.slug}`);
    } catch (e) {
      console.log(`❌ ${demo.slug} (failed)`);
    }
  }
  
  // Kill server
  process.kill(-serverProcess.pid);
}

// Build gallery HTML
function buildGallery(demos) {
  const template = fs.readFileSync(GALLERY_TEMPLATE, 'utf8');
  const siteData = JSON.stringify(demos, null, 2);
  const output = template.replace('SITE_DATA_PLACEHOLDER', siteData);
  
  fs.writeFileSync(OUTPUT, output);
  console.log(`\n✅ Gallery built: ${OUTPUT}`);
  console.log(`   ${demos.length} sites, ${demos.filter(d => d.hasThumb).length} with thumbnails`);
}

// Main
async function main() {
  const withScreenshots = process.argv.includes('--screenshots');
  
  console.log('Scanning demos...');
  const demos = scanDemos();
  
  if (withScreenshots) {
    await generateScreenshots(demos);
  }
  
  buildGallery(demos);
}

main().catch(console.error);
