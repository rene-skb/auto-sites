#!/bin/zsh
set -euo pipefail
for v in 0 1 2 3 4 5; do
  node /Users/rene/clawd/skills/auto-site-builder/screenshot.js \
    file:///Users/rene/clawd/projects/auto-sites/demos/moon-ink/index-v${v}.html \
    /Users/rene/clawd/projects/auto-sites/demos/moon-ink/screenshot-v${v}.png
done
