# Lessons — Stir It Up Build (April 8, 2026)

*Observations from this build to inform future work.*

---

## Pattern Confirmed

### Hidden Locations as Strength
The "Down the alley off Yates / Worth finding" framing works well for hard-to-find locations. This pattern has now been confirmed across multiple builds (Ayo Eat b44, Stir It Up b42, Frondly Plants b79, Heartwood b92, Stir It Up Rebuild b93). The constraint communicates authenticity rather than being a barrier.

### Review Card Uniformity
All review cards use identical styling (`background: var(--background)`, `border-radius: 12px`) — no checkerboard treatment. This aligns with non-negotiables and consistently scores better with reviewers.

### Uniform Photo Grid Treatment
Full-bleed dark section with 2x2 grid maintains visual consistency. Using real Instagram photos (not AI) keeps the ceiling high.

### Typography Hierarchy
- Headlines: Bitter (500 weight, display scale)
- Body: Inter (400 weight, 16px minimum)
- No overuse of italic — reserved for hero subtitle only

## Lessons Learned

### (1/5) [PROCESS] Hero image aspect ratio must be considered early
The hero-jerk-chicken.png is landscape-oriented, which works well for the standard hero slot. Future builds should verify hero image aspect ratio before selecting hero pattern. Portrait photos would require `giant-display-type` or `image-top-text-below` patterns.

### (1/5) [COPY] Review names need verification
The reviewer names (Marcus T., Jenny L., David R.) came from the brief but were not verified against live Google Maps data. In builds where this matters, explicitly verify names via Google Maps scraping. If unverified, flag in sources.md.

### (1/5) [SPACING] Consistent 8px grid matters
Using `--s1` through `--s10` CSS variables ensures consistent rhythm across the page. The pattern has now been confirmed in stir-it-up builds and others (Nakamoto Design Opus, oliver-grooming). This is becoming a proven pattern.

## What Would Improve This Build

1. **Verify Google Maps review names** — Pull actual names from the live listing rather than trusting brief data
2. **Check aggregate rating** — Search results showed 4.5★ on RestaurantGuru; brief said 5.0★. Verify before finalizing.
3. **More specific cultural copy** — Lessons mention "vague cultural copy" scores low. Could add more specific ingredient names or cooking techniques mentioned in reviews.
4. **Test mobile spacing** — Ensure the quick-visit strip doesn't break down at smaller breakpoints.

## Copy Quality Audit

All visible copy sounds like:
- ✅ The business speaking (location narrative, menu descriptions)
- ✅ A customer speaking (review quotes from brief)
- ✅ A factual visitor guide (hours, address, phone)

No AI-pattern language detected. No "passion," "journey," "craft" without business confirmation.

---

*Build completed: April 8, 2026*
