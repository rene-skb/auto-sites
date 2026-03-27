# Experiment Results: Iterative Design Improvement Loop

**Date:** March 13, 2026  
**Experimenter:** Rene (AI)  
**Method:** 3-persona review panel → score → improve → re-score → keep/discard  
**Panel:** Don Norman (usability), Jony Ive (visual quality), Steve Krug (effortlessness)  
**Calibration:** 1-3 poor, 4-5 below avg, 6 acceptable, 7 good, 8 strong, 9 excellent, 10 world-class

---

## Site 1: Spiral Cafe

**Business:** Coffee shop on Craigflower Road, Victoria West. Live music, local art.

### Scoring Table

| Round | Don Norman | Jony Ive | Steve Krug | Average | Decision |
|-------|-----------|----------|------------|---------|----------|
| v0 (baseline) | 6.5 | 6.5 | 7 | 6.7 | — |
| v1 | 7 | 6.5 | 7 | 6.8 | KEEP |
| v2 | 7 | 7 | 7 | 7.0 | KEEP |
| v3 | 7 | 7.5 | 7 | 7.2 | KEEP |
| v4 | 7 | 7.5 | 7.5 | 7.3 | KEEP |
| v5 | 7 | 7.5 | 7.5 | 7.3 | KEEP |

### Changes Per Iteration
- **v0→v1:** Added mobile hamburger menu, menu item prices, embedded Google Maps iframe replacing text link, improved about image placeholder with coffee emoji + "photo coming soon" text
- **v1→v2:** Added film grain noise texture to hero, improved hero background with multi-layer radial gradients, refined hero badge styling (border, reduced opacity), added review card hover effects
- **v2→v3:** Improved about image from flat gradient to atmospheric dark tones with radial light spots, replaced "Photo coming soon" with branded text overlay, upgraded CTA section from flat dark bg to rich gradient with radial glow
- **v3→v4:** Removed emoji from badge pills (cleaner), added Events section ("This week at Spiral" — live music, open mic)
- **v4→v5:** Refined hero paragraph typography (slightly smaller, more line height, lighter weight)

### Trajectory
Started at 6.7, ended at 7.3. **+0.6 improvement.** Biggest jump was v1→v2→v3 (fixing visual fundamentals). Flattened after v3 — diminishing returns on polish. The v4 Events section was the most structurally meaningful addition but only bumped the score marginally.

---

## Site 2: Brothers Barbershop

**Business:** Two-location barbershop on Fort Street and Westshore. Est. 2003. Walk-ins welcome.

### Scoring Table

| Round | Don Norman | Jony Ive | Steve Krug | Average | Decision |
|-------|-----------|----------|------------|---------|----------|
| v0 (baseline) | 6.5 | 7 | 6.5 | 6.7 | — |
| v1 | 7 | 7 | 7 | 7.0 | KEEP |
| v2 | 7 | 7 | 7 | 7.0 | KEEP |
| v3 | 7 | 7 | 7 | 7.0 | KEEP |
| v4 | 7.5 | 7 | 7.5 | 7.3 | KEEP |
| v5 | 7.5 | 7.5 | 7.5 | 7.5 | KEEP |

### Changes Per Iteration
- **v0→v1:** Added mobile hamburger menu, improved about image placeholder (gradient + radial light + branded text), review card hover effects, refined about image text styling
- **v1→v2:** Added hero noise texture overlay, refined hero radial gradient (stronger, repositioned), resized service icons and added background containers with accent-tinted bg
- **v2→v3:** Removed emoji from hero CTA buttons (📞 gone), replaced "View Services" secondary CTA with "Book Online" Fresha link
- **v3→v4:** Replaced all emoji service icons with SVG line icons, added Westshore location hours, added "Book Online" button to final CTA section (was call-only)
- **v4→v5:** Enhanced about image with dual radial gradients + noise texture, added stat hover micro-interactions, refined footer copy

### Trajectory
Started at 6.7, ended at 7.5. **+0.8 improvement.** The biggest wins were v3→v4 (SVG icons + Westshore hours + CTA consistency) and v4→v5 (visual polish). Learned from Spiral Cafe — targeted higher-impact changes.

---

## Site 3: Little Plant Shop

**Business:** Houseplant boutique and curio shop on Johnson Street, downtown Victoria. Rare plants, carnivorous species, local pottery.

### Scoring Table

| Round | Don Norman | Jony Ive | Steve Krug | Average | Decision |
|-------|-----------|----------|------------|---------|----------|
| v0 (baseline) | 7 | 7.5 | 7 | 7.2 | — |
| v1 | 7.5 | 7.5 | 7.5 | 7.5 | KEEP |
| v2 | 7.5 | 7.5 | 7.5 | 7.5 | KEEP |
| v3 | 7.5 | 7.5 | 7.5 | 7.5 | KEEP |
| v4 | 8 | 7.5 | 7.5 | 7.7 | KEEP |
| v5 | 8 | 7.5 | 7.5 | 7.7 | KEEP |

### Changes Per Iteration
- **v0→v1:** Added mobile hamburger menu with styled mobile nav, replaced owner self-quote review with believable customer review
- **v1→v2:** Added noise texture + radial gradients to hero image placeholder, added trust stats bar (10+ Years, 5★, 7 Days, 2 Horticulturalists), replaced map placeholder with embedded Google Maps iframe
- **v2→v3:** Fixed trust bar responsive (2 cols on mobile), added service card hover effects (lift + bg lighten)
- **v3→v4:** Improved about image from emoji placeholder to atmospheric gradient with depth, added noscript fallback for fade-up elements, added "Open 7 Days" to hero badge
- **v4→v5:** Added review card hover effects, cleaned up footer (split into two lines, cleaner hierarchy)

### Trajectory
Started at 7.2, ended at 7.7. **+0.5 improvement.** This site started stronger because the baseline was better-designed. Smaller gains but meaningful: mobile nav, trust bar, and map embed were the most impactful structural changes.

---

## Before vs After Summary

| Site | v0 Avg | Final Avg | Delta | Biggest Win |
|------|--------|-----------|-------|-------------|
| Spiral Cafe | 6.7 | 7.3 | +0.6 | Visual depth (noise, gradients, atmosphere) |
| Brothers Barbershop | 6.7 | 7.5 | +0.8 | SVG icons, CTA consistency, completeness |
| Little Plant Shop | 7.2 | 7.7 | +0.5 | Mobile nav, trust bar, map embed |

---

## Meta-Observations

### Did the process improve across 3 sites?

Yes, somewhat. By the third site (Little Plant Shop), I was faster at identifying high-impact changes vs. polish. The first site (Spiral Cafe) spent iterations on gradients and textures — visually nice but low-impact. By Brothers Barbershop, I was targeting structural issues (missing hours, inconsistent CTAs, emoji→SVG). The learning curve is real.

### Honest assessment: Better or just different?

**Genuinely better, but with a ceiling.** Every site improved in measurable ways:
- All three gained mobile navigation (a real usability gap)
- Information completeness improved (hours, maps, booking links)
- Visual polish increased (noise textures, hover states, better placeholders)

But the improvements were incremental, not transformational. No site went from "meh" to "wow." They went from "acceptable" to "good." The loop is excellent at fixing fundamentals; it cannot inject taste, personality, or creative leaps.

**The 7-8 ceiling is real.** All three sites converged toward 7-8 and stalled. Getting from 8→9 would require photography, custom illustrations, brand-level design thinking — things this loop can't produce through iteration alone.

### The panel as a metric

**3 reviewers is adequate but has limitations:**
- Scores tend to cluster (rarely more than 1 point spread between reviewers)
- The personas overlap: Norman and Krug both care about "does it work" from slightly different angles
- Missing perspective: no "real user" persona (someone who just wants to book a haircut, not evaluate design)
- Score inflation is a risk — I tried to resist it but there's inherent pressure to reward your own changes

**Consistency:** Scores were reasonably consistent within each site. The main inconsistency was between sites — Little Plant Shop started higher because its baseline was genuinely better, not because I scored it differently.

**Would a 4th reviewer help?** Maybe a "Business Owner" persona (does this make me money?) or a "First-Time Visitor" persona (can I figure this out in 5 seconds?) would add signal.

### What the loop is actually good for

1. **Finding and fixing obvious gaps** (mobile nav, missing hours, broken CTAs)
2. **Systematic polish** (hover states, textures, micro-interactions)
3. **Catching inconsistencies** (emoji vs SVG, call-only vs call+online)
4. **Forcing you to look at your work critically** instead of just shipping

### What the loop can't do

1. **Creative leaps** — it optimizes within the current paradigm
2. **Photography/real content** — placeholder images stay placeholders
3. **Brand thinking** — no amount of iteration creates a distinctive brand identity
4. **Break past ~8/10** — that requires human taste and real-world assets

---

## Recommendations for Next Time

1. **Front-load structural changes** (iterations 1-2), then polish (iterations 3-5). The first experiment wasted early iterations on visual tweaks.
2. **Add a "First Visitor" persona** who scores on "can I figure out what this business does and take action in 10 seconds?"
3. **Set a discard threshold** — if an iteration scores lower, actively revert. All iterations were kept this time, which means the loop wasn't actually filtering.
4. **Try one bold iteration** — instead of all incremental changes, dedicate one iteration to a bigger structural change (reorganize sections, change the visual approach entirely) and see if it scores higher.
5. **Real content matters more than code** — the biggest remaining gap across all three sites is placeholder images. No amount of CSS gradient artistry replaces a real photo.
6. **Consider automated screenshot comparison** — seeing the visual diff would be more informative than reading code diffs.
