# Scott Bell Sonnet Fresh — Rationale

## Slug
- `scott-bell-sonnet-fresh`

## Direction
**The Long View**

This pass deliberately avoids the chapter-card rhythm and dark editorial structure used in the last two builds.

Instead it leads with:
- a **typographic numbers-first hero** (`14 / 24 / 6`)
- a **quiet editorial layout** with more open space
- **light-background case studies** instead of dark proof blocks
- a **table-style current work section** instead of project cards
- a warmer, more authored palette built around **Fraunces + DM Sans** and a brick accent

The goal was to make Scott feel like a seasoned designer who now ships his own tools, without recycling the same hero line, same pacing, or same visual tropes.

## What is most different from the last two builds

### Versus `scott-bell-portfolio-proof`
- No chapter-head component
- No purple accent, no feature-card framing
- No current-work card grid
- Hero is typographic and numerical instead of prose-led
- Selected work lives on a light paper field, not a dark proof section

### Versus `scott-bell-sonnet-proof`
- No amber/Cormorant/Space Grotesk direction
- No ribbon interlude
- No repeated chapter-number motif
- Current work is presented as an editorial list, not a visual gallery/card set
- Overall tone is quieter, less art-directed, more profile-piece/editorial

## Structural intent
The page answers four hiring questions in order:
1. **How much depth is here?** → `14 / 24 / 6`
2. **What proof exists at scale?** → Strike, AIOZ, Fountain, KOHO
3. **What is he building now?** → six recent self-initiated releases
4. **How does he think?** → the about/close section

## Panel workflow
Produced files:
- `index-v0.html`
- `index-v1.html`
- `index-v2.html`
- `index-v3.html`
- `index-v4.html`
- `index-v5.html`
- `index.html` (copy of final)

### v0 — Creative direction
Established the new concept:
- numbers-first hero
- Fraunces + DM Sans
- brick/cream palette
- light selected-work section
- editorial current-work table

### v1 — WHY critique
Main structural corrections:
- upgraded hero from tentative to assertive
- surfaced **6 recent builds** as a real top-line signal
- dissolved the floating philosophy section into the close/about section
- gave Strike more weight and KOHO more narrative substance

### v2 — WHAT critique
Content corrections:
- removed repeated company mentions inside the hero
- replaced weaker phrasing like `built on his own`
- cleaned KOHO copy
- improved alternation between light/dark sections
- sharpened the about language and current-work descriptions

### v3 — HOW critique
Execution corrections:
- fixed the project-table structure
- added KOHO metrics treatment
- strengthened the closing quote treatment
- added reveal motion and polished responsiveness

### v4 — Motion / self-review
Polish corrections:
- cleaned load behavior and visual rhythm
- normalized section-label treatment
- improved keyboard focus states
- tightened hero and footer behavior

### v5 — Final
Final copy and implementation cleanup:
- tightened hero and section subcopy
- fixed reveal logic to avoid fragile selectors
- polished selected-work framing
- exported final as `index.html`

## Self-scored panel scores
These are **self-scored** since no external panel tool was run in this subagent pass.

- **WHY:** 8.6/10
- **WHAT:** 8.4/10
- **HOW:** 8.7/10
- **Motion / self-review:** 8.5/10
- **Final average:** **8.55/10**

## Fact inventory used
- `14 years` and `24 products` → prior Scott portfolio demos / established portfolio framing
- `6 recent self-initiated releases` → current brief
- Strike: `450 screens`, `1.5M users`, `65 countries`, `5 months` → prior Scott portfolio demos
- AIOZ: `8 products`, `$13M to $1.38B`, `100× growth` → prior Scott portfolio demos
- Fountain: `full rebuild in five months`, `Apple featured twice` → prior Scott portfolio demos
- KOHO: `employee #1`, `0 to 100K+ users`, `$800M+ valuation` → prior Scott portfolio demos
- auto-sites: `80+ demos` → prior Scott portfolio demos / current repo context

## Copy decisions Scott should review
1. **`14 / 24 / 6`** — confirm he still wants those exact counts as the lead framing.
2. **`The last year looks different`** in the hero copy — this is factual framing, but he may want a less time-bound line.
3. **`80+ demos built and deployed`** for auto-sites — confirm the current number.
4. **`Mix'd`** spelling/canonical product naming — confirm whether this should stay `Mix'd`, `Mix'd`, or `mix-id`.
5. **Third-person voice** — this pass intentionally reads like an editorial profile rather than a first-person portfolio. If he wants more direct first-person voice, that would be the first thing to swap.

## Lessons learned promoted or added
- **None promoted or added in this pass.**

## Deployment target
Expected live route after push:
- `https://auto-sites.pages.dev/demos/scott-bell-sonnet-fresh/`
