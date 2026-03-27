#!/bin/bash
# Auto-Sites Discovery Script
# Finds local businesses in Victoria BC that might need websites
# Uses Google Maps API (or manual research) to identify leads

# USAGE: ./discovery-script.sh "cafes" "Victoria BC"
# Outputs a CSV of businesses without websites

CATEGORY="${1:-cafes}"
LOCATION="${2:-Victoria BC}"
OUTPUT_DIR="leads"

mkdir -p "$OUTPUT_DIR"
OUTPUT_FILE="$OUTPUT_DIR/${CATEGORY// /-}-$(date +%Y%m%d).csv"

echo "name,address,phone,has_website,has_instagram,has_facebook,google_rating,review_count,notes" > "$OUTPUT_FILE"

echo "=== Auto-Sites Discovery ==="
echo "Category: $CATEGORY"
echo "Location: $LOCATION"
echo "Output: $OUTPUT_FILE"
echo ""
echo "MANUAL DISCOVERY PROCESS:"
echo "1. Search Google Maps: '$CATEGORY near $LOCATION'"
echo "2. For each result, check:"
echo "   - Does it have a website link? (if no = LEAD)"
echo "   - Does it have Instagram/Facebook? (if yes = we can pull content)"
echo "   - What's the rating and review count?"
echo "3. Add qualifying businesses to $OUTPUT_FILE"
echo ""
echo "QUALIFYING CRITERIA:"
echo "- No website OR terrible website (single Facebook page counts as no website)"
echo "- Has some social media presence (Instagram preferred — visual content)"
echo "- 4+ star rating (quality business worth our time)"
echo "- Active business (recent reviews, posts)"
echo ""
echo "OUTSCRAPER (when ready):"
echo "- Sign up at outscraper.com"
echo "- Search: '$CATEGORY $LOCATION'"
echo "- Filter: website field empty"
echo "- Export CSV and merge with this file"
echo ""
echo "=== Known Leads (Victoria) ==="
echo "Spiral Cafe - 418 Craigflower Rd - Facebook only, no website - DEMO BUILT"
