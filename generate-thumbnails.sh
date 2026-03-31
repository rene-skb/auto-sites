#!/bin/bash
# Generate thumbnails for all demo sites
# Usage: ./generate-thumbnails.sh

DEMOS_DIR="/Users/rene/clawd/projects/auto-sites/demos"
THUMBS_DIR="/Users/rene/clawd/projects/auto-sites/thumbnails"
SCREENSHOT_JS="/Users/rene/clawd/skills/auto-site-builder/screenshot.js"
PORT=8899

mkdir -p "$THUMBS_DIR"

# Start server
cd "$DEMOS_DIR"
python3 -m http.server $PORT &
SERVER_PID=$!
sleep 2

for dir in "$DEMOS_DIR"/*/; do
  name=$(basename "$dir")
  
  # Skip if no index.html
  if [ ! -f "$dir/index.html" ]; then
    echo "⏭️  Skipping $name (no index.html)"
    continue
  fi
  
  # Skip if thumbnail already exists
  if [ -f "$THUMBS_DIR/$name.png" ]; then
    echo "✓ $name (exists)"
    continue
  fi
  
  echo "📸 $name..."
  node "$SCREENSHOT_JS" "http://localhost:$PORT/$name/index.html" "$THUMBS_DIR/$name.png" 2>/dev/null
  
  if [ -f "$THUMBS_DIR/$name.png" ]; then
    echo "✅ $name"
  else
    echo "❌ $name (failed)"
  fi
done

# Cleanup
kill $SERVER_PID 2>/dev/null

echo ""
echo "Done! Thumbnails in $THUMBS_DIR"
