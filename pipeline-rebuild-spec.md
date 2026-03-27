# Pipeline Rebuild Spec — March 25, 2026
*Scott's FigJam diagram + our discussion. Use this to rebuild SKILL.md from scratch.*

## Overview
13 phases, 6 version files (v0-v5 + index.html), honest iterations. Each version is a real distinct build.

## File Architecture
- **non-negotiables.md** — Scott's rules. Electric fence. Human-controlled only. Overrides everything.
- **design-knowledge.md** — Proven universals (5+ builds to enter). Auto-checked against non-negotiables before any addition. Merge lucy-feedback-mar23.md into this. Monthly human review.
- **lessons.md** — Working memory. Observations and patterns. Pruned monthly (rolling 30 days, <3 occurrences deleted). Lucy WRITES to this, never deletes. Rene prunes nightly at 9:45pm.
- **build-log.md** — Tracks all builds. Includes hero pattern, typography pairing, review layout for rotation tracking.
- **build-queue.md** — Pre-picked businesses. Populated by us during the day.

## Onboarding (every build)
Lucy reads:
1. non-negotiables.md (always, first)
2. design-knowledge.md (always, second)
3. build-queue.md (to get tonight's assignment)
That's it. Three files. Lean.

## Phase 0 — Discovery
Check in this order:
1. Read build-queue.md — any businesses not yet in demos/ folder?
2. If yes → use the first unbuilt one. Done.
3. If queue empty or all built → discover a new business within Canada with social presence but no website.
4. Cross-check against build-log.md to avoid duplicates.
Output: Business name + social links

## Phase 1 — Brand Research (Lucy, 5 min cap)
Study their social presence (Instagram, Facebook, Google listing, reviews, photos).
Extract: brand colors, vibe, personality, what makes them different.
Output: Brand research brief (colors, typography direction, vibe, key differentiators)

## Phase 2 — Creative Direction (WHY panel: Jobs + Cagan)
Input: Brand research brief. NO site yet.
Action: Panel gives directional guidance — "what should this feel like, what's the conviction, what's the emotional hook?"
Output: Creative direction for Lucy
*Direction BEFORE building. This is new and critical.*

## Phase 3 — First Build (Lucy)
Input: Creative direction + brand research + non-negotiables + design knowledge
Action: Check build-log.md for last 3 builds. Hero pattern, typography pairing, and review layout must ALL be different from last 3. Generate images. Build v0.
Output: v0.html + images
*If browser available: Lucy views her own work*

## Phase 4 — WHY Critique (Jobs + Cagan)
Input: v0.html (viewed in browser if possible, code if needed)
Action: Review actual site against the direction they gave. "Does it land? Does it feel inevitable?"
Output: Feedback only (no version file — this is critique, not building)

## Phase 5 — Second Build (Lucy)
Input: v0 + WHY critique feedback
Action: Lucy thinks about the feedback and iterates.
Output: v1.html

## Phase 6 — WHAT Critique (Norman + Krug + Nielsen)
Input: v1.html
Action: Structure, clarity, usability, scannability. "Does a first-time visitor understand without thinking?"
Output: Feedback only

## Phase 7 — Third Build (Lucy)
Input: v1 + WHAT critique feedback
Action: Lucy thinks about the feedback and iterates.
Output: v2.html

## Phase 8 — HOW Critique (Vignelli + Spiekermann + Rams + Emil suggests motion)
Input: v2.html
Action: Grid, typography, craft, reduction. Emil identifies WHERE motion should go and WHAT type. Craft critics can push back on unnecessary motion.
Output: Feedback + motion plan

## Phase 9 — Fourth Build (Lucy)
Input: v2 + HOW critique feedback
Action: Lucy iterates on craft.
Output: v3.html

## Phase 10 — MOTION Critique (Emil reviews v3)
Input: v3.html
Action: Emil reviews what's there and finalizes motion recommendations.
Output: Final motion implementation plan

## Phase 11 — Fifth Build / Motion Implementation (Lucy)
Input: v3 + Emil's motion plan
Action: Implement scroll reveals, stagger animations, button feedback (scale 0.97 on active), custom easing curves. NO hover zoom on images or non-interactive elements. prefers-reduced-motion respected.
Output: v4.html

## Phase 12 — Lucy's Self Review
Input: v4 + ALL accumulated feedback from all phases
Action: Lucy reads all feedback one more time, looks at the whole thing holistically. Final judgment call. Catches anything missed. If browser available, views the rendered site.
Output: v5.html (true final)

## Phase 13 — Outputs
- Save v0-v5 + index.html (copy of v5) = 7 files minimum
- Append to build-log.md: business name, category, city, hero pattern, typography pairing, review layout, baseline score → final score, date built
- Note observations in lessons.md (tagged with build name + date)

## Lessons Lifecycle
1. Build completes → Lucy notes observation in lessons.md
2. Seen in 3 builds → promote to "Pattern"
3. Seen in 5+ builds → promote to "Proven"
4. Check: conflicts with non-negotiables? YES → discard. NO → add to design-knowledge.md
5. Pruning (monthly rolling): observations older than 30 days with fewer than 3 occurrences → delete
6. Rene handles pruning + promotion nightly at 9:45pm

## Roles
- **Lucy** — brand research, building, self-review. Writes to lessons.md (never deletes).
- **Rene** — prunes lessons.md nightly, promotes patterns, checks non-negotiables gate.
- **Scott** — reviews design-knowledge.md monthly, manages non-negotiables.md.

## Rotation Tracking (checked in Phase 3, logged in Phase 13)
- Hero pattern — can't repeat within last 3 builds
- Typography pairing — can't repeat within last 3 builds
- Review section layout — can't repeat within last 3 builds
Options for hero: full-viewport-bg, split-image-right, centered-minimal, giant-display-type, image-top-text-below, editorial-spread, dark-immersive, asymmetric-collage

## Non-Negotiables (current list — Scott manages)
❌ NO checkerboard review cards — ALL cards same treatment
❌ NO fake storefronts, interiors, or building exteriors
❌ NO hover zoom on non-clickable images — scroll-reveal only
❌ NO reusing the same image twice on one page
❌ NO body text blocks longer than 2-3 sentences
❌ NO double stats bars stacked
❌ Asymmetric grids: both sides end at same baseline
❌ Review cards MUST have first name + last initial
❌ Hero = "why should I come here?" not origin story
❌ Noise texture: very fine grain only. When in doubt, skip.

## Future Upgrades (parked)
- Visual self-review via browser screenshots at each phase
- Adaptive panel (Lucy chooses which experts to consult) — risk of gaming
- Iris handles brand research separately
- Brand color extraction from screenshots

## Key Principle
The panel should refine the creative vision, not replace it. If a build starts with a bold, business-specific direction, the panel should make that direction better — not default it back to a safe template.

---
*Designed by Scott in FigJam, documented by Rene. March 25, 2026.*
*Next step: Fresh session → rebuild SKILL.md from this spec.*
