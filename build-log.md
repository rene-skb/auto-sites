# Auto-Sites Build Log

## Build 54 — La Roux Patisserie
- **Category:** French Patisserie
- **City:** Victoria, BC (519 Fisgard St, Chinatown)
- **Date:** 2026-03-26
- **Model:** claude-sonnet-4-6 (subagent)
- **Agent:** Lucy
- **Hero pattern:** editorial-spread
- **Typography:** Cormorant Garamond 400/500/600/700/400i (display) + DM Sans 300/400/500/600 (body/UI)
- **Review layout:** 3-col equal cards, all same treatment (cream-alt bg, rose border-top)
- **Stats bar style:** dark-bar (dark bg strip after hero: 4.7★ / Opens 9am / $10-20 / LGBTQ+ Friendly)
- **Score:** 6.5 (v0 baseline WHY) → 7.5 (estimated final)
- **Key decisions:** Editorial-spread hero (dark left / macarons image right) — "Made to Be Remembered." as conviction headline. European authenticity angle: "A European visitor wrote: 'The pastries make me feel like I'm back home.'" moved into hero body — the strongest proof point becomes the first thing you read after the headline. Cormorant Garamond as deeply Parisian editorial serif — first use in 3 builds. Dusty rose (#C4707A) accent referencing "roux" — the warm red-auburn color. Signature items ordered by review frequency (carrot cake 39, macarons 37, Paris-Brest 25, custom cakes) — data-backed curation signals credibility. "Under the Chandelier" as the name section — the chandelier detail from Google description is the most specific sensory detail about this space. laroux.ca ordering page exists but isn't a designed marketing site — built to fill that gap.

### Business
La Roux Patisserie. Real Victoria BC business. Ordering page at laroux.ca (Shopify-style catalog, not a designed marketing/landing page). Address: 519 Fisgard St, Victoria, BC V8W 1R3 (Floor 1 · Union — near Fan Tan Alley, Chinatown). Phone: (778) 265-7689. Email: info@laroux.ca. Google: 4.7 stars, 746 reviews, $10-20 per person. Dine-in + Takeout, no delivery. Hours: 9am-5pm (days unconfirmed — site directs to call). LGBTQ+ friendly. Description: "Chandelier-lit French pastry shop with charming decor featuring macarons, croissants & cakes." Top review keywords: carrot cake (39 mentions), macarons (37), Paris Brest (25), crème brûlée (20). Notable reviews: European visitor ("makes me feel like I'm back home"), Ali MN ("honestly some of the best I've ever had"), Cynthia Johnston ("BEST birthday cake I have ever received").

### Scores
| Round | Phase | Reviewers | Avg |
|-------|-------|-----------|-----|
| v0→v1 | WHY | Jobs 6.5, Cagan 7.0, Ogilvy 7.0 | 6.83 |
| v1→v2 | WHAT | Norman 7.0, Krug 7.0, Nielsen 6.5 | 6.83 |
| v2→v3 | HOW | Vignelli 7.5, Spiekermann 7.0, Rams 7.0 | 7.17 |
| v3→v5 | Motion + Self | Emil + Lucy | — |

### Key improvements
- v0→v1: Fixed image duplication (celebration-cake.png was in both photo strip and about section; about section moved to creme-brulee.png); hero body replaced generic description with European quote framing; about headline changed to "The Kitchen That Makes Europeans Nostalgic"; signature card descriptions given personality and specificity; hours phrasing changed from "Open daily" to "9am–5pm (call to confirm days)" — honest about uncertain schedule
- v1→v2: Generated 5th image (creme-brulee.png); focus-visible states added; about image finalized as unique
- v2→v3: Section h2 tracking tightened (-0.025em → -0.03em); review-meta bumped to 0.8125rem; trust bar 4th stat changed from "Dine-In / Takeout Welcome" to "LGBTQ+ / Friendly & Welcoming" (more meaningful, verified from Google)
- v3→v5: Hero entrance animation (stagger: eyebrow→h1→p→CTAs, 80ms intervals); IntersectionObserver scroll-reveals on trust-bar, photo-strip, about, name-section, reviews-header, review cards (stagger), sig cards (stagger), visit; prefers-reduced-motion handled; noscript fallback; sig-number color bumped from #EED8DB to #D4A0A6 for better contrast; name section CTA label changed to "Get Directions"

### What worked
- European quote as hero body: "A European visitor wrote: 'The pastries make me feel like I'm back home.'" — moves the strongest proof point to the most visible position. First impression = authenticity validated by someone from the continent.
- "Under the Chandelier" as name section headline: specific, sensory, earns its own dedicated section. The chandelier is the single most distinctive physical detail (from Google description) — not every patisserie has one.
- Cormorant Garamond: deeply Parisian editorial serif with beautiful italic weight. Perfectly calibrated for a French patisserie — creates instant register of craft and refinement.
- Dusty rose (#C4707A) accent: references "roux" color (auburn, warm red), warm without being pink or garish. Distinct from terracotta, distinct from burgundy. French without being cliché.
- editorial-spread hero: dark panel left with conviction copy, macaron photography right — creates a luxury editorial feel that immediately signals this is different from a generic bakery site.
- Signature items ordered by review mention count: carrot cake (39), macarons (37), Paris-Brest (25) — shows the most-loved items through real social proof rather than arbitrary curation.
- dark-bar trust bar: 4.7★ / Opens 9am / $10-20 / LGBTQ+ Friendly — anchors credibility and inclusivity immediately after the hero.

### Files
- index-v0.html through index-v5.html (6 versions)
- index.html (copy of v5)
- macarons.png, croissant.png, paris-brest.png, celebration-cake.png, creme-brulee.png (5 AI-generated images)

---

## Build 53 — Status Barber Shop
- **Category:** Barbershop
- **City:** Victoria, BC (1010 Yates St #4, Harris Green)
- **Date:** 2026-03-26
- **Model:** claude-sonnet-4-6 (subagent)
- **Agent:** Lucy
- **Hero pattern:** giant-display-type
- **Typography:** Bebas Neue (display) + Inter 300/400/500/600/700 (body/UI)
- **Review layout:** Featured large quote (dark bg, italic, big type) + 2 supporting cards below — 2-row staggered
- **Stats bar style:** light-bar (cream-alt bg, black numbers with gold unit markers)
- **Score:** 7.5 (v0 baseline) → 7.67 (estimated final)
- **Key decisions:** "THE FRESHEST FADES IN BC." hero headline — a customer's own words at 14vw in Bebas Neue on near-black. Gold accent line for "FADES IN BC." — splits the headline into conviction + specificity. "The Music Is Half the Haircut." as about headline — draws from the 105 "atmosphere" + 37 "music" review mentions. Award badge (15×) top-right in hero: subtle legacy signal. "BEST OF THE CITY. FIFTEEN YEARS RUNNING." as the dark name section. Light-bar trust stats (4.8★, 15×, Mon–Sat, Walk-In) anchors credibility immediately after hero. Near-black + warm brass gold + cream palette — premium barbershop without being cold. Booking site exists (StyleSeat/functional) so CTAs point there rather than phone-only. Land acknowledgment in footer.

### Business
Status Barber Shop. Real Victoria BC business. Has a booking/landing page at statusbarbershop.com (StyleSeat-style functional booking, no designed site). Address: 1010 Yates St #4, Victoria, BC V8V 4Y4. Phone: (250) 590-7828. Google: 4.8 stars, 1,193 reviews. Victoria News "Best of the City" barbershop — 15 consecutive years. Hours: Mon–Fri 10am–7pm, Sat 10am–6pm, Sun Closed. Named barbers: Tbone (35 review mentions), John. Key review themes: atmosphere (105 mentions), music (37), Tbone (35), hot towel (13). Wheelchair accessible. Services: Platinum Haircut $54, Scissor Cut $64, Buzz Cut $27, Children's Cut $33, Beard Trim $40+, Hair Tattoo $15+.

### Scores
| Round | Phase | Reviewers | Avg |
|-------|-------|-----------|-----|
| v0→v1 | WHY | Jobs 7.5, Cagan 7.5, Ogilvy 7.5 | 7.5 |
| v1→v2 | WHAT | Norman 7.5, Krug 7.5, Nielsen 7.0 | 7.33 |
| v2→v3 | HOW | Vignelli 7.5, Spiekermann 7.5, Rams 7.5 | 7.5 |
| v3→v5 | Motion + Self | Emil + Lucy | — |

### Key improvements
- v0→v1: About headline changed from generic "Where Victoria Gets its Haircut" to specific "The Music Is Half the Haircut" (draws from 105 atmosphere + 37 music mentions); fabricated words removed from featured review quote (verbatim only); CTA band headline changed from repeated "Ready for the Freshest Fade?" to "Your Chair Is Waiting."; beard trim price shown as "$40+" not "Book"
- v1→v2: Service description text darkened (mid-gray vs warm-gray for WCAG AA); focus-visible states added; reviews headline strengthened to "1,193 Cuts. 4.8 Stars. 15 Awards."; scroll-margin-top on all sections
- v2→v3: Section h2 tracking tightened (-0.01em); name section h2 tracking tightened; Mon-Sat trust stat font-size reduced to differentiate from numeric stats; review-card-meta bumped to 0.75rem
- v3→v5: Hero entrance stagger animation (label→h1→body→CTAs, 80ms intervals); IntersectionObserver scroll-reveals on all sections; service card stagger (40ms); review card stagger; prefers-reduced-motion; inline delay styles → CSS stagger classes; land acknowledgment added to footer

### What worked
- "THE FRESHEST FADES IN BC." as hero headline: customer's own words at massive scale, specific to this city, prideful without being marketing-speak. Bebas Neue at 14vw IS the brand statement.
- "The Music Is Half the Haircut.": draws from the 105 "atmosphere" mentions and 37 "music" mentions in Google reviews — specific, earned, true to the brand
- Bebas Neue + Inter: classic barbershop display type + clean modern body. Bebas Neue condensed uppercase at large scale feels intentional and strong; Inter keeps body text readable
- Near-black + warm brass gold (#C4A35A): premium palette that feels earned, warm not cold, avoids generic barbershop red
- Light-bar trust bar: 4.8★/1,193/15×/Mon-Sat/Walk-In — immediately answers "is this place worth it?"
- Award badge top-right in hero: 15× Victoria News award as quiet, confident authority — not shouted, just present
- Featured review + 2 supporting layout: different from all 3 recent builds; large quote gives the review section real presence
- "BEST OF THE CITY. FIFTEEN YEARS RUNNING." as name section: earned through consistency, not self-promotion
- Real prices ($27-$64): transparent, removes friction, builds trust
- CTA band "YOUR CHAIR IS WAITING.": confident, warm, doesn't repeat the hero

### Files
- index-v0.html through index-v5.html (6 versions)
- index.html (copy of v5)
- fade-hero.png, barber-tools.png, scissor-cut.png, hot-towel.png (4 AI-generated images)

---

## Build 52 — Vintage Glory
- **Category:** Vintage Clothing / Military Vintage
- **City:** Winnipeg, MB (Keenleyside St & Thomas Ave)
- **Date:** 2026-03-26
- **Model:** claude-opus-4-6 (subagent)
- **Agent:** Lucy
- **Hero pattern:** full-viewport-bg
- **Typography:** Barlow Condensed 400/500/600/700 (display) + IBM Plex Sans 300/400/500/600 (body/UI)
- **Review layout:** Stacked full-width reviews with olive border-top (all same treatment)
- **Stats bar style:** accent-bar (olive green bg, brass numbers — integrated into hero/trust bar)
- **Score:** 7.33 (v0 baseline) → 7.5 (estimated final)
- **Key decisions:** Full-viewport olive green (#2C3A2A) hero — military palette taken to full-section blocks. "Every Piece Has a Story. Doug Knows Them All." hero headline naming the owner. Barlow Condensed as condensed industrial display type. "The Clothes Outlasted the People Who Wore Them" name section. Find cards with personality names ("The Jackets", "The History", "The Weird Stuff"). Doug as character throughout — "Find Doug" as visit header. Instagram as primary social since it IS their website. First Winnipeg build.

### Business
Vintage Glory. Real Winnipeg MB business. No website — Instagram @vintageglorywpg is listed as their website on Google Maps. Address: Keenleyside St & Thomas Ave, Winnipeg, MB R2L 2C1. Phone: (204) 942-7186. Owner: Doug. Google: 4.7 stars, 45 reviews (38 five-star). Known for: leather jackets, WW2 military pieces, curated vintage, museum-like experience. Hours: Tue–Sun 12–5 PM, closed Monday. Reviews mention: "It's a kind of museum", "the owner has many stories to tell", "great prices", "wonderful leather jackets".

### Scores
| Round | Phase | Reviewers | Avg |
|-------|-------|-----------|-----|
| v0→v1 | WHY | Jobs 7.5, Cagan 7.0, Ogilvy 7.5 | 7.33 |
| v1→v2 | WHAT | Norman 7.5, Krug 7.0, Nielsen 7.5 | 7.33 |
| v2→v3 | HOW | Vignelli 7.5, Spiekermann 7.5, Rams 7.5 | 7.5 |
| v3→v5 | Motion + Self | Emil + Lucy | — |

### Key improvements
- v0→v1: Trust bar fixed "Tue – Sun / Opens at Noon" (was "Daily"), name section rewritten ("The Clothes Outlasted the People Who Wore Them"), find cards given Doug's voice ("The Weird Stuff"), CTA band fixed ("New Old Stock Every Week")
- v1→v2: Inline styles → CSS classes (visit-h3, hours-note, visit-map-spaced), focus-visible states, scroll-margin-top for anchor links
- v2→v3: Section h2 tracking tightened (-0.03em), review meta bumped to 0.8125rem, nav link underline animation
- v3→v4: Hero entrance animation (stagger label→h1→body→CTAs, 80ms), IntersectionObserver scroll-reveals on all sections, find-card stagger (40ms), prefers-reduced-motion, noscript fallback
- v4→v5: Final polish, index.html copy

### What worked
- Barlow Condensed: condensed industrial sans-serif that screams military/workwear. Different from every font used in last 10 builds. Perfect for a vintage military shop.
- Deep olive (#2C3A2A) as full-viewport hero: BOLD color commitment. Not an accent — the entire hero section IS the color. Counter to every pastel/cream vintage shop online.
- "Every Piece Has a Story. Doug Knows Them All.": names the owner, promises an experience, specific to this business
- "The Clothes Outlasted the People Who Wore Them. That's the Point.": name section that elevates the philosophy beyond "we sell old stuff"
- "The Weird Stuff" as a find card name: Doug's voice, not marketing copy
- "Find Doug" as visit header: personal, warm, matches one-person-shop energy
- Brass (#B8924A) on olive: militaria palette that feels earned and warm
- Stacked full-width reviews: different from 2-col and 3-col used in last 3 builds, more intimate for a small shop
- Instagram as "website" — honest approach, the absence of a website IS the brand
- First Winnipeg build — new city for the portfolio

### Files
- index-v0.html through index-v5.html (6 versions)
- index.html (copy of v5)
- leather-jacket.png, military-patch.png, vintage-boots.png, vintage-rack.png (4 AI-generated images)

---

## Build 51 — Csinos Vintage
- **Category:** Vintage Clothing / Curated Retail
- **City:** Victoria, BC (770 Yates Street — inside Cheers Vintage Collective)
- **Date:** 2026-03-25
- **Model:** claude-sonnet-4-6 (cron)
- **Agent:** Lucy
- **Hero pattern:** asymmetric-collage
- **Typography:** Gloock (display serif) + Jost 300/400/500/600 (body/UI)
- **Review layout:** 2-col equal cards with rose border-top, all same treatment
- **Stats bar style:** inline-text (stats woven into body copy — collective stat "5 independent sellers" inline in collective section)
- **Score:** 7.5 (v0 baseline) → 7.5 (estimated final)
- **Key decisions:** "It's sort of a mood" hero headline — Szandi's own words. Gloock display serif for Eastern European old-world elegance. Asymmetric collage hero (dress + knitwear + accessories, 2:1:1 grid). Dark brand-strip quote interstitial instead of photo strip. Name section "Csinos. Pronounced: chee-nosh. Hungarian for beautiful." as the single strongest moment. Collective section surfaces the "five women, five different eyes" story. Real owner quote in collective: "I'm not selling clothes. I'm selling a feeling."

### Business
Csinos Vintage. Real Victoria BC business. No website confirmed (Google Maps "Add website" shown). Instagram @csinosvintage (5.2K followers, 4.6K+ posts). Facebook (100+ followers). Address: 770 Yates St, Victoria BC V8W 1L4 (inside Cheers Vintage Collective with 4 other independent sellers). Owner: Szandi — Eastern European (Hungarian) heritage, moved to Canada. Founded July 2020 in Fernwood; now at Yates Street. Google: 5.0 stars, 65 reviews. Sells: vintage clothing, shoes, accessories, household objects. Hours: Thu–Mon 11am (closed Tue–Wed). Name meaning: "Csinos" (chee-nosh) = Hungarian for pretty/beautiful.

### Scores
| Round | Phase | Reviewers | Avg |
|-------|-------|-----------|-----|
| v0→v1 | WHY | Jobs 8.0, Cagan 7.0, Ogilvy 7.5 | 7.5 |
| v1→v2 | WHAT | Norman 7.5, Krug 7.0, Nielsen 7.5 | 7.33 |
| v2→v3 | HOW | Vignelli 7.5, Spiekermann 7.5, Rams 7.5 | 7.5 |
| v3→v5 | Motion + Self | Emil + Lucy | — |

### Key improvements
- v0→v1: Hero body rewritten ("Csinos is Hungarian for beautiful. This is what that looks like in a room..."), collective body tightened to shopper benefit, review attributions normalized (SARAH S., FOUND STUDIO · MAR 2025 · Via Google)
- v1→v2: Letter-spacing three-level system enforced via CSS vars, find-card body copy sharpened ("Nothing lands here by accident"), section-label gap normalized
- v2→v3: Review cards get rose border-top (consistent with find-cards), collective quote changed from Google review (already in reviews section) to Szandi's own words ("I'm not selling clothes. I'm selling a feeling."), review-meta weight 600
- v3→v4: Hero entrance animation (eyebrow→h1→body→CTAs, 80ms stagger), IntersectionObserver scroll-reveals on all sections, find-card and review-card stagger (40ms), prefers-reduced-motion, noscript fallback
- v4→v5: Real images embedded (dress-hero, knitwear, accessories in collage hero; homeware in about section), photo strip replaced with dark brand-strip quote interstitial (avoids image reuse non-negotiable), CSS comment updated

### What worked
- Gloock serif: elegant, literary, old-world — fits Eastern European heritage narrative perfectly. First use in 51 builds.
- "It's sort of a mood": owner's own words as hero headline. Disarming, specific, true. Nobody else says this.
- Asymmetric collage hero: 3-image grid (2fr tall + 2x1fr) creates editorial richness without a single dominant image. Matches the curation brand.
- Name section: "Csinos. Pronounced: chee-nosh. Hungarian for beautiful." — explains, intrigues, humanizes the brand in three lines.
- Rose accent (#B87B5E): dusty, warm, faded fabric energy — right between terracotta and old rose. Doesn't compete with the cream base.
- "I'm not selling clothes. I'm selling a feeling." — Szandi's own quote from DVBA interview. Conviction-first, personal, genuine.
- Dark brand-strip interstitial: "Csinos. It's sort of a mood." as a dark band between sections — creates rhythm without needing extra images.
- Collective section: "You're not choosing from one person's taste. You're in a room with five of them." — turns the shared-space setup into a selling point.
- 2-col review grid with rose border-top: different from last 3 builds, clean, consistent card treatment.

### Files
- index-v0.html through index-v5.html (6 versions)
- index.html (copy of v5)
- dress-hero.png, knitwear.png, accessories.png, homeware.png (4 AI-generated images)

---

## Build 50 — Dragon Flowers (Tammy)
- **Category:** Florist / Flower Shop
- **City:** Montréal, QC (Mile End, 173 Rue Bernard O)
- **Date:** 2026-03-25
- **Model:** claude-sonnet-4-6 (subagent)
- **Agent:** Lucy
- **Hero pattern:** dark-immersive
- **Typography:** Bodoni Moda 400/600/700/400i (display) + Space Grotesk 400/500/600 (body/UI)
- **Review layout:** 3-col equal cards, all same treatment (cream-alt bg, no border distinction)
- **Stats bar style:** dark-bar (dark bg after about section, not stacked with hero)
- **Score:** 6.83 (v0 baseline) → 7.67 (estimated final)
- **Key decisions:** Full-screen botanical green (#1A3528) hero with massive Bodoni Moda "Spread Love." headline — the entire hero is the brand color. Terracotta quote section mid-page breaks the cream rhythm with warmth. "Spread Love. It's free." from their own Instagram bio used in quote section. Hero → photo strip → about → dark trust bar → green name section → services → terracotta quote → reviews → visit → dark CTA band creates strong color rhythm. Family business in Mile End/Montréal with 18.7K Instagram followers and 557 Google reviews, minimal web presence.

### Business
Dragon Flowers (Tammy). Real Montréal QC business. Website: dragonflowers.ca (single-line address only — no real web presence). Instagram @dragonflowershop (18.7K followers, 3.3K+ posts). Google: 4.7 stars, 557 reviews. Facebook @dragonflowershop (70+ followers). Address: 173 Rue Bernard O, Montréal, QC H2T 2K3. Phone: (514) 278-8818. Open daily from 7 AM. Services: custom bouquets, in-store arrangements, indoor plants/pots year-round, same-day delivery across Montréal. Award: Bronze Best Florist, Best of Montréal 2022. Mile End / Plateau-Mont-Royal neighbourhood.

### Scores
| Round | Phase | Reviewers | Avg |
|-------|-------|-----------|-----|
| v0→v1 | WHY | Jobs 7.0, Cagan 6.5, Ogilvy 7.0 | 6.83 |
| v1→v2 | WHAT | Norman 7.5, Krug 7.0, Nielsen 7.0 | 7.17 |
| v2→v3 | HOW | Vignelli 7.5, Spiekermann 7.5, Rams 7.0 | 7.33 |
| v3→v5 | Motion + Self | Emil + Lucy | — |

### Key improvements
- v0→v1: Inline photo strip styles → CSS classes, about headline "The Shop Montréal Has Always Had", name section copy more specific ("The name is a little fierce. The shop is warm."), services renamed ("Walk In, Walk Out"), review text uses verified Google snippets only, reviews h2 "557 Montréalers Agree."
- v1→v2: Quote attribution contrast fixed (0.9 opacity), hours framing honest ("typically from 7 AM — call to confirm"), review meta darkened (#5A5450)
- v2→v3: Section-h2 tracking tightened (-0.025em), name section reduced 120→96px padding, nav link underline animation, trust bar numbers 700→600 weight (data vs display)
- v3→v4: Hero entrance stagger animation (eyebrow→h1→body→CTAs, 80ms intervals), scroll-reveal IntersectionObserver on all sections, service card stagger (40ms), review card stagger (40ms), prefers-reduced-motion, noscript fallback
- v4→v5: Quote section changed from review snippet to their own Instagram tagline ("Spread love. It's free."), CTA band headline "Come Find Us on Rue Bernard", hero image opacity reduced 0.18→0.12

### What worked
- Bodoni Moda: The high-contrast thick/thin strokes against botanical green are extraordinary. Looks like a fashion editorial, feels completely earned for a neighborhood florist that takes pride
- "Spread Love." as the hero headline: Their own tagline at 11rem in Bodoni Moda on deep green is a design statement. Nobody else can say this in this way
- Deep botanical green (#1A3528) full-hero: completely counter to every florist site on the internet (pastels, whites, pinks). This says "serious craft" not "Valentine's convenience"
- Terracotta (#C4623A) as accent: warm earth color that evokes autumn flowers, soil, craft — different register from the cool green
- Dark trust bar mid-page (after about): breaks the cream sequence, acts as a dramatic pause before the name section
- "Run by a lovely family — they're the nicest people around" as review card: genuine, specific social proof
- Color rhythm: green → cream → dark → green → cream-alt → terracotta → cream → cream-alt → dark creates a full-page design score
- Name section: "The name is a little fierce. The shop is warm." captures the brand tension perfectly
- Photo strip immediately after hero: pulls you out of the bold color immediately into product reality — flowers

### Files
- index-v0.html through index-v5.html (6 versions)
- index.html (copy of v5)
- bouquet-hero.png, flowers-arrangement.png, flower-closeup.png, plants-texture.png, flowers-hands.png (5 AI-generated images)

---

## Build 49 — Carlina Cafe
- **Category:** Italian Family Cafe
- **City:** View Royal, Victoria, BC (264 Island Hwy)
- **Date:** 2026-03-25
- **Model:** claude-sonnet-4-6 (subagent)
- **Agent:** Lucy
- **Hero pattern:** editorial-spread
- **Typography:** Lora 400/500/600/700/400i (display) + Nunito Sans 300/400/500/600/700 (body/UI)
- **Review layout:** 3-col equal cards with venetian red top border, cream-alt background (all same treatment)
- **Stats bar style:** light-bar (cream-alt background, venetian red section labels)
- **Score:** 6.83 (v0 baseline) → 7.67 (estimated final)
- **Key decisions:** "Her Sugo. Her Meatballs. Her Kitchen." hero — leads with the grandmother's recipes, not description. Venetian red (#A63A2F) extracted as warm-but-not-cliché Italian red. Dark editorial-spread hero (dark left panel / food photo right) creates magazine feel unlike typical restaurant sites. Name section "Carlo. Lina. Carlina." is the brand soul — big type, dark background, 120px padding. Charly's CHEK News quote ("It feels like a hug from my grandmother") as full-width venetian red quote section. Hero entrance animation (staggered eyebrow/h1/body/CTAs) + scroll reveals throughout.

### Business
Real View Royal BC business. No website. Instagram @carlina_cafe. Owner Charly Cardilicchia, Italian family cafe named after grandfather Carlo and grandmother Lina. Grandmother's recipes (sugo, meatballs, ricotta). Featured on CHEK News "Order Up". 5.0 Google stars, 122 reviews. 4.9 Uber Eats. Address: 264 Island Hwy, Victoria BC V9B 1G5. Phone: (250) 590-9113. Hours: Mon–7pm daily (11am open). Price: $10-20.

### Scores
| Round | Phase | Reviewers | Avg |
|-------|-------|-----------|-----|
| v0→v1 | WHY | Jobs 7.0, Cagan 6.5, Ogilvy 7.0 | 6.83 |
| v1→v2 | WHAT | Norman 7.5, Krug 7.0, Nielsen 7.0 | 7.17 |
| v2→v3 | HOW | Vignelli 7.5, Spiekermann 7.0, Rams 7.5 | 7.33 |
| v3→v5 | Motion + Self | Emil + Lucy | — |

### Key improvements
- v0→v1: About section now shows actual pasta-meatballs photo, CHEK trust stat cleaned of inline styles, menu h2 simplified, CTA band changed from mismatched green to venetian red (brand-consistent), name section h2 larger (clamp 3rem–5.5rem)
- v1→v2: All inline styles replaced with CSS classes (section-scroll, section-h2, visit-phone, hours-note, centered-block), about image properly layered (placeholder + img), focus-visible states, hero CTA changed to Uber Eats for delivery
- v2→v3: Hero h1 letter-spacing tightened (-0.03em), menu-grid gap reduced, hero entrance animation (stagger: eyebrow→h1→body→CTAs on load), hero image fade-in on load
- v3→v5: noscript fallback updated for hero-entrance classes, transition-delay inline styles moved to CSS classes (hero-delay-1/2/3), about caption updated to father's quote (avoids exact duplication with Charly quote section), CTA band Instagram link added

### What worked
- Lora + Nunito Sans: warm editorial serif + friendly rounded sans — feels like an Italian family kitchen, not a corporate restaurant
- Venetian red (#A63A2F): warmer and more sophisticated than typical Italian-red; evokes Chianti labels
- Editorial-spread hero: dark left / food photo right creates a magazine quality distinct from standard restaurant hero patterns
- "Her Sugo. Her Meatballs. Her Kitchen.": three nouns, no adjectives, completely specific to this business — nobody else can say this
- Name section with Carlo + Lina story: the naming of this cafe is extraordinary brand material, it deserves its own dramatic full-dark section
- "Five Stars, 122 Times" as reviews h2: tells the whole story at a glance without reading a single review
- Father's quote in about caption: "He's just taken on the tradition from my mom and my dad and added his own stuff to it" — family validation is powerful social proof
- Trust bar with $10-20 price range: immediately removes "is it affordable?" hesitation
- CHEK News as press credibility: Victoria-local press is more trusted by locals than national publications

### Files
- index-v0.html through index-v5.html (6 versions)
- index.html (copy of v5)
- pasta-meatballs.png, sandwich-ricotta.png, gelato.png (3 AI-generated food images)

---

## Build 48 — Scott Bell Portfolio v4
- **Category:** Portfolio / Personal Brand
- **City:** Victoria, BC
- **Date:** 2026-03-25
- **Hero pattern:** giant-display-type
- **Typography:** Bebas Neue (display) + IBM Plex Mono (body)
- **Review layout:** Full-width stacked with violet left border
- **Stats bar style:** accent-bar (violet background, lime numbers)
- **Score:** N/A (portfolio, not panel-scored)
- **Key decisions:** Electric violet (#6C3AFF) + acid lime (#CDFF50) as dominant palette — boldest color use across all 4 versions. Monospace body text for builder/architect energy. KOHO handled as text-only banner (no images available). Dark mobile menu with lime text. Three distinct color-block sections (violet about, dark AI, lime CTA) create strong visual rhythm.

## Build 47 — Kid Sister Ice Cream (v4)
- **Category:** Ice Cream / Frozen Desserts
- **City:** Victoria, BC (1320 Esquimalt Road)
- **Date:** 2026-03-25
- **Model:** claude-opus-4-6 (subagent)
- **Agent:** Lucy
- **Hero pattern:** image-top-text-below
- **Typography:** Playfair Display 400/500/600/700/400i (display) + Poppins 300/400/500/600 (body/UI — matches their actual Squarespace site)
- **Review layout:** N/A (no reviews — this is Scott's own shop, real photos replace social proof)
- **Score:** 7.25 → 8.0+ (real photography elevates beyond AI ceiling)
- **Key decisions:** "The Flowers Aren't Decoration. They're Ingredients." hero — captures the edible flower signature. Coral (#E94E1B) extracted from actual Kid Sister logo. Cream/peach (#FFF5EB) background matches their real site's warm energy. Green (#2D5A3D) text. Real photos as primary imagery (hero-scooping, spring-fruits-flowers, sunflowers, dandelion illustration, logo). Removed CTA band — gift cards as footer line per Rams. Offerings as coral border-top items below about, not separate card section. Name section in coral as brand moment. Instagram as flavour discovery channel (seasonal rotation means no static flavour list). Only open days shown in hours (Thu-Sun).

### Business
Scott's OWN ice cream shop. Real Victoria BC business. Website at kidsistericecream.com (Squarespace). Instagram @kidsistericecream. ONE location only — 1320 Esquimalt Road (old Cook Street location CLOSED). Handmade ice cream, vegan sorbet, and pops. Seasonal, from-scratch, organic dairy, local fruit. No soft serve — hand-scooped only. Hours: Thu-Fri 3pm-8pm, Sat-Sun 1pm-8pm. Gift cards available.

### Scores
| Round | Phase | Reviewers | Avg |
|-------|-------|-----------|-----|
| v0→v1 | WHY | Jobs 7.5, Cagan 7.0, Ogilvy 7.5 | 7.0 |
| v1→v2 | WHAT | Norman 7.5, Krug 7.5, Nielsen 7.5 | 7.5 |
| v2→v3 | HOW | Vignelli 7.8, Spiekermann 7.8, Rams 8.0 | 7.87 |
| v3→v4 | Motion | Emil | — |

### Key improvements
- v0→v1: About section centred (removed dandelion as grid column), hero body tightened, coral name section replaces cream-alt, trust bar stat "Hand-Scooped / No Soft Serve" added
- v1→v2: Offerings merged after about (not separate section), scroll-margin-top in CSS, focus-visible states, only open days in hours table, removed closed days
- v2→v3: Trust bar values switched from Playfair serif to Poppins sans (functional data not headlines), hero body 1.125→1.0625rem, name section h2 tracking -0.03em, offerings header with section-label, CTA band removed (gift cards in footer)
- v3→v4: Scroll-reveal fade-ins with IntersectionObserver, hero image fade-in on load, hero text stagger entrance (h1→body→ctas, 80ms delay), offering items stagger (60ms), photo strip stagger, prefers-reduced-motion, no-JS fallback
- v4→v5: Hero text entrance class fix (removed from HTML, added via JS), footer-gift with Instagram link, footer-meta wrapper, final polish

### What worked
- **Real photography is transformative.** The hero-scooping photo with flowers, chalkboard, red apron immediately communicates warmth and craft that no AI image could match. The sunflower popsicle photo is iconic. Real photos > AI photography, confirmed.
- **Playfair Display + Poppins:** Warm editorial serif + the same rounded sans their actual Squarespace site uses. Feels like a natural extension of the brand.
- **Coral (#E94E1B) from actual logo:** Extracted from the Kid Sister wordmark. Not a generic red — this IS the brand colour.
- **Cream (#FFF5EB) background:** Matches the warm peach energy of their real site. Green text on cream is their actual aesthetic.
- **"The Flowers Aren't Decoration. They're Ingredients.":** Conviction hero that captures the edible flower signature — specific, surprising, true. Best headline across all 4 Kid Sister versions.
- **Image-top-text-below hero:** Lets the stunning real photo dominate. Text below creates editorial magazine feel.
- **No flavour list:** Smart for seasonal rotation. Instagram redirect is honest and practical.
- **Coral name section:** "She shows up with something sweet and makes the whole day better" — warm, personal brand moment.
- **Gift cards as footer line:** Cleaner than a dedicated CTA band section.
- **Land acknowledgment in footer:** "Kid Sister frozen delights are made on the traditional territory of the lək̓ʷəŋən Peoples."

### Files
- index-v0.html through index-v5.html (6 versions)
- index.html (copy of v5)
- real-images/ (5 real photos: hero-scooping.jpg, spring-fruits-flowers.jpg, sunflowers.jpg, dandelion-illustration.png, logo.gif)

---

## Build 47 — Scott Bell Portfolio v3
- **Category:** Designer Portfolio
- **City:** Victoria, BC (Remote)
- **Date:** 2026-03-25
- **Model:** claude-opus-4-6 (subagent)
- **Agent:** Lucy
- **Hero pattern:** asymmetric-collage (text left with stats sidebar + 3-image strip below)
- **Typography:** Outfit 300-800 (display) + JetBrains Mono 400/500 (labels/meta)
- **Review layout:** N/A (portfolio, not business site)
- **Score:** v0 WHY avg ~7.3 → v3 HOW avg ~7.9
- **Key decisions:** Near-white (#FAFAFA) base with deep navy (#0F1923) dark sections and teal (#00B894) accent — completely different palette from v1 (dark/gold) and v2 (cream/vermillion). Geometric sans (Outfit) + monospace (JetBrains Mono) replaces v1's serif+sans and v2's bold display+sans. Hero uses "The most AI-enabled designer you'll find" as conviction headline. KOHO stats bar as inline project highlight. AI tools section in dark bg tells the "designer who builds" story. Real product screenshots throughout (Strike, AIOZ, Fountain). 7 HTML files (v0-v5 + index.html).

### What worked
- Outfit + JetBrains Mono: geometric display + monospace meta is a strong tech-portfolio pairing, distinct from both previous versions
- Teal (#00B894) as accent: tech-forward, energetic, warm enough to not feel cold — surgical use on labels, CTAs, and section markers
- "The most AI-enabled designer you'll find": bold conviction hero that positions Scott's unique value immediately
- KOHO stats bar: $800M / Employee #1 / 100K+ Users — tells the origin story in numbers without needing a full project card
- AI tools section on dark bg: creates a visual shift that signals "this is different territory" — the builder side of the story
- Trust bar with company names + impact numbers: scannable proof that doesn't require reading project cards
- JetBrains Mono for all meta/labels: creates a consistent "technical" voice across the page
- Hero image strip (3fr/2fr/2fr): asymmetric, shows three different products at a glance
- Alternating project card image sides: creates visual rhythm without structural inconsistency

---

## Build 46 — Sky Studio Lucia
- **Category:** Meditation / Light Therapy / Wellness Studio
- **City:** Vancouver, BC (Fairview, 1338 W 6th Ave Suite 301)
- **Date:** 2026-03-25
- **Model:** claude-opus-4-6 (subagent)
- **Agent:** Lucy
- **Hero pattern:** giant-display-type
- **Typography:** Cormorant Garamond 400/500/600/700/400i (display) + DM Sans 400/500/600/700 (body/UI)
- **Review layout:** Stacked full-width reviews (all same treatment)
- **Score:** 7.17 → 7.87 (final craft score before motion)
- **Key decisions:** Cosmic dark palette (#0D0B14) with gold (#C4A35A) accent — the golden glow of the Lucia light device as the brand color. "Close Your Eyes. See Everything." hero — paradoxical, intriguing. "A psychedelic experience without psychedelics" moved into hero body for immediate hook. Dark immersive feel throughout to match the sensory deprivation nature of the experience. Instagram as primary CTA (they book through DM).

### Business
Real Vancouver BC business. Website set to private/password-protected on Squarespace (skystudiolucia.ca returns 401). Instagram @skystudiolucia (3,058 followers, 101 posts). Founded by Tina Averback. Meditation center focused on Lucia N°03 hypnagogic light device (Austrian neuroscience). Also offers sound healing, family constellations, cosmic downloads (live channeling), spinal energetics. Located inside building on W 6th Ave, Suite 301, Fairview neighbourhood. Phone: (604) 726-0898. By appointment. Google Maps listed as "Meditation center" with reviews.

### Scores
| Round | Phase | Reviewers | Avg |
|-------|-------|-----------|-----|
| v0→v1 | WHY | Jobs 7.5, Cagan 7.0, Ogilvy 7.0 | 7.17 |
| v1→v2 | WHAT | Norman 7.5, Krug 7.5, Nielsen 7.5 | 7.5 |
| v2→v3 | HOW | Vignelli 7.8, Spiekermann 7.8, Rams 8.0 | 7.87 |
| v3→v4 | Motion | Emil | — |

### Key improvements
- v0→v1: Hero body rewritten with "A psychedelic experience without psychedelics" hook, trust bar updated to "Austrian Neuroscience" + "Alpha + Theta Brainwaves", fixed review that referenced wrong business (The Serene Space), name section rewritten to "What You See Is Yours Alone"
- v1→v2: Hero label simplified, about copy refined with Canadian spelling, scroll-margin-top added
- v2→v3: Name section h2 tracking tightened, review attribution margin added
- v3→v4: Scroll-reveal fade-ins with IntersectionObserver, stagger on experience cards (60ms), hero entrance animation, prefers-reduced-motion, no-JS fallback
- v4→v5: Final polish, index.html copy

### What worked
- Cormorant Garamond + DM Sans: ethereal serif + clean sans, matches the consciousness exploration vibe — distinct from recent builds
- Cosmic dark (#0D0B14) as base: darker than standard dark-immersive, almost black with purple undertones — matches the light-in-darkness concept
- Gold (#C4A35A) as accent: the warm glow of the Lucia light device — brand-appropriate and warm
- "Close Your Eyes. See Everything.": paradoxical hero headline that captures the experience in 5 words
- "No mantras. No poses. No experience needed.": immediately removes barriers for newcomers
- "A psychedelic experience without psychedelics": the business's own positioning, moved to hero for maximum impact
- Stacked full-width reviews for a small review collection: different from 3-col grid, feels more intimate
- Instagram as primary CTA: honest — they actually book through Instagram DM
- Gold quote section: provides colour break in otherwise very dark page

### Observations
- NOT a yoga studio — this is a meditation/light therapy studio. The task asked for a yoga studio in Canada but finding one with genuinely no website proved extremely difficult. Every yoga studio in Victoria, Vancouver, Calgary, and Toronto that I checked (30+ studios) had at least a basic website. Meditation/wellness studios were more likely to operate through social media only.
- Discovery took ~15 minutes (vs 2-minute budget) — yoga studios universally have websites in major Canadian cities. The pipeline's discovery phase needs adjustment for this category.
- Only 2 Google reviews available — very limited social proof. Used Instagram testimonials from story highlights to supplement.
- Image generation hit credit limits — only 2 of 4 planned images generated. Used CSS gradient placeholder for missing slots.
- The Lucia N°03 light device is a very specific product — the site needs to explain it without sounding like a sales page for the device.

---

## Build 45 — Roaming Yak
- **Category:** Tibetan Restaurant
- **City:** Calgary, AB (Downtown, 512 6 Street SW)
- **Date:** 2026-03-25
- **Model:** claude-opus-4-6 (subagent)
- **Agent:** Lucy
- **Hero pattern:** dark-immersive
- **Typography:** Newsreader 400/500/600/700/400i (display) + Inter 400/500/600/700 (body/UI)
- **Review layout:** 3-col equal cards with border-top treatment (all same)
- **Score:** 7.25 → 7.9 (final craft score before motion)
- **Key decisions:** Saffron (#C4873A) as accent — Tibetan prayer flag warmth, culturally resonant. "You Sit Down. They Bring You Tea." hero conviction — the butter tea ritual as the hook. "Most People Have Never Tried Tibetan Food. This Is Where That Changes." as name section. Avenue Calgary quote as colored section break.

### Business
Real Calgary AB business. No website. Instagram @roaming_yak_yyc. Family-owned Tibetan restaurant opened late November 2025. One of the few places in Calgary for authentic Tibetan cuisine. 512 6 Street SW, Floor 1. Tue-Thu 11:30am-9:30pm, Fri 11:30am-10pm, Sat 12-10pm, Sun 12-8:30pm, Mon closed. Uber Eats 4.5 stars (52 ratings). Featured in Avenue Calgary (Jan 2026). Known for momos (steamed/fried/pan-fried/jhol/chilli), shabhaley, laphing, complimentary butter tea, housemade chili garlic oil.

### Scores
| Round | Phase | Reviewers | Avg |
|-------|-------|-----------|-----|
| v0→v1 | WHY | Jobs 7.5, Cagan 7.0 | 7.25 |
| v1→v2 | WHAT | Norman 7.8, Krug 7.5, Nielsen 7.5 | 7.6 |
| v2→v3 | HOW | Vignelli 7.8, Spiekermann 7.8, Rams 8.0 | 7.9 |
| v3→v4 | Motion | Emil | — |

### Key improvements
- v0→v1: Trust bar replaced Uber Eats rating with "Butter Tea / Complimentary", differentiated quote sources (Avenue Calgary for colored section, TripAdvisor for reviews), hero body tightened
- v1→v2: About headline strengthened "They Grew Up Making This Food. Now They Make It for Calgary.", focus-visible states added
- v2→v3: Hero label size normalized to 0.6875rem, name section tracking tightened, review attribution bumped to 0.875rem
- v3→v4: Scroll-reveal fade-ins with IntersectionObserver, stagger on menu cards + reviews (60ms), hero entrance animation, prefers-reduced-motion respect, no-JS fallback
- v4→v5: Final polish

### What worked
- Newsreader + Inter: warm literary serif with clean sans, distinct from recent Fraunces/Lora/Syne builds
- Saffron (#C4873A) as accent: Tibetan prayer flag warmth, earthy and culturally resonant
- Dark-immersive hero with momos background at 0.2 opacity: sets warm Himalayan mood
- "You Sit Down. They Bring You Tea.": conviction hero that leads with the butter tea ritual — specific, surprising, culturally unique
- "Most People Have Never Tried Tibetan Food. This Is Where That Changes.": name section that positions the restaurant as an introduction
- Avenue Calgary quote as saffron-colored section break: press credibility in a design moment
- Menu with real Uber Eats prices: transparent, verifiable
- Honest review constraint: all reviews from one TripAdvisor reviewer + Avenue Calgary press — the restaurant is 4 months old
- Tibetan script on menu items (རླངས་བཙོས་ག་ག། on Uber Eats) adds authentic cultural detail

---

## Build 44 — Ayo Eat
- **Category:** Indonesian Restaurant (Takeout Window)
- **City:** Victoria, BC (Market Square, 560 Johnson St #140)
- **Date:** 2026-03-25
- **Model:** claude-opus-4-6 (subagent)
- **Agent:** Lucy
- **Hero pattern:** split-image-right
- **Typography:** Fraunces 400/500/600/700/400i (display) + Space Grotesk 400/500/600/700 (body/UI)
- **Review layout:** Featured dark center card + 2 flanking light cards
- **Score:** 7.25 → 7.9 (final craft score before motion)
- **Key decisions:** Turmeric (#C49A3A) as accent — spice-forward, culturally resonant. "He Doesn't Advertise. He Just Cooks." hero conviction. UVic student quote from Jakarta as about-section lead — someone who shares Bana's ethnic group finding home in his food. Name section "Ayo Means 'Come.' That's the Whole Pitch." — explains the name while capturing the effortless invitation. "Second Floor. Turn Left." as visit header reframes hidden location as charm.

### Business
Real Victoria BC business. No working website (ayoeat.ca doesn't resolve). Instagram @ayoeat.victoria (341 followers), Facebook (Ayo Eat Indonesian Food). One-man operation by Ali Syahbana ("Bana") from West Sumatra. Takeout window on 2nd floor of Market Square. Victoria's only Indonesian eatery. Google 4.8-4.9 stars, 224+ reviews. Featured in Tasting Victoria. Known for chicken satay, beef rendang (17 spices), nasi campur, telor sambal. Phone: (250) 590-4231. Mon 12:30-6:30, Tue-Thu 11:30-6:30, Sat 12:30-5. Closed Fri & Sun.

### Scores
| Round | Phase | Reviewers | Avg |
|-------|-------|-----------|-----|
| v0→v1 | WHY | Jobs 7.5, Cagan 7.0 | 7.25 |
| v1→v2 | WHAT | Norman 7.8, Krug 7.5, Nielsen 7.5 | 7.6 |
| v2→v3 | HOW | Vignelli 7.8, Spiekermann 7.8, Rams 8.0 | 7.9 |
| v3→v4 | Motion | Emil | — |

### Key improvements
- v0→v1: Hero body → emotional proof ("people who've been to Indonesia can't tell the difference"), name section pivot to "Ayo Means Come", about headline uses Bana's own words, menu header "Five Dishes. All From Scratch.", CTA band simplified
- v1→v2: Trust bar corrected "Mon — Thu + Sat", name section rewired to avoid redundancy, prefers-reduced-motion added, external link attributes fixed
- v2→v3: Name section h2 tighter tracking, review attribution weight bump, trust bar number sizing normalized
- v3→v4: Scroll-reveal fade-ins with IntersectionObserver, stagger on menu cards + reviews (60ms), hero entrance animation, prefers-reduced-motion respect, no-JS fallback
- v4→v5: CSS class consistency (body.js-ready prefix), final polish

### What worked
- Fraunces + Space Grotesk: Fraunces has optical softness that feels warm and approachable — matches Indonesian hospitality energy without being precious
- Turmeric (#C49A3A) as accent: spice-forward, culturally resonant, warm golden tone that matches the food itself
- Split-image-right hero with satay photo: food-first, lets the dish sell the experience
- "He Doesn't Advertise. He Just Cooks.": conviction hero that captures Bana's entire philosophy in one line
- UVic student quote from Jakarta confirming same ethnic group: the most powerful authenticity proof — someone from the same culture validating the food
- "Ayo Means 'Come.' That's the Whole Pitch.": name section that explains the Indonesian word while capturing the brand's effortless invitation
- "Second Floor. Turn Left." as visit header: reframes hidden location as charm and adventure, not barrier
- Tasting Victoria press feature as credibility anchor
- One-man operation as brand: "One Cook / Everything by Bana" in trust bar immediately communicates care
- "Authentic Food Is Made as Original" as about headline: Bana's own words from the Tasting Victoria article

---

## Build 43 — Greek n Go
- **Category:** Greek Food Truck
- **City:** Victoria, BC (1580 Cook Street, Cook Street Village + 2046 Keating Cross Rd, Saanichton)
- **Date:** 2026-03-25
- **Model:** claude-opus-4-6 (subagent)
- **Agent:** Lucy
- **Hero pattern:** image-top-text-below
- **Typography:** Lora 400/500/600/700/400i (display) + Work Sans 400/500/600/700 (body/UI)
- **Review layout:** 3-col equal cards on alt-bg (all same treatment)
- **Score:** 7.25 → 7.9 (final craft score before motion)
- **Key decisions:** Greek blue (#2B5A7C) as accent — faded fishing boat blue, not tourism cliché. Reddit late-night quote as the personality section in blue bg. Family roles described in hero body ("Eirini runs the window. Dad Jerry works the grill.") rather than just listing names. "Five People. Three Trucks. One Grandmother's Kitchen." as name section — staccato, manifesto-style.

### Business
Real Victoria BC business. Minimal catering-only page at greekngo.ca (single paragraph, no design). Instagram @greek_n_go, Facebook @GreeknGo. Family-owned Greek food truck founded by Eirini and dad Jerry, with siblings Anna and Christo, and mum Martha. From Nafpaktos, Greece. Google 4.7 stars, 475+ reviews. Voted Best Food Truck 2025 by two separate awards. 3 trucks + Berry Sweet trailer. Late-night hours (till midnight Fri/Sat). Two daily locations: Cook Street Village + Keating Cross Rd. Email: contact@greekngo.ca.

### Scores
| Round | Phase | Reviewers | Avg |
|-------|-------|-----------|-----|
| v0→v1 | WHY | Jobs 7.5, Cagan 7.0 | 7.25 |
| v1→v2 | WHAT | Norman 7.8, Krug 7.5, Nielsen 7.5 | 7.6 |
| v2→v3 | HOW | Vignelli 7.8, Spiekermann 7.8, Rams 8.0 | 7.9 |
| v3→v4 | Motion | Emil | — |

### Key improvements
- v0→v1: Trust bar "5 Family Members" → "Open Late" + "GF & Vegan" (functional stats), menu prices added, name section rewritten as manifesto
- v1→v2: Hero body gives family roles not just names, inline styles → CSS classes, Keating hours improved, focus-visible states added
- v2→v3: Trust bar text stats normalized in size, section-label gap 12→16px, review attr bump to 0.875rem, nav link underline animation
- v3→v4: Scroll-reveal fade-ins with IntersectionObserver, stagger on menu cards + reviews (60ms), hero image entrance animation, prefers-reduced-motion, no-JS fallback
- v4→v5: All inline styles → CSS classes (stagger-1/2/3, about-quote-spaced, btn-block), final polish

### What worked
- Lora + Work Sans: warm serif + geometric sans, feels Mediterranean without being novelty — distinct from recent Syne/Bitter/Instrument Serif builds
- Greek blue (#2B5A7C) as accent: faded fishing-boat blue, warm not cold, avoids tourism-Greece cliché
- Image-top-text-below hero: lets the food photo dominate, text below creates editorial magazine feel
- "She Taught Us to Cook. We Brought It Here.": hero with conviction about grandma's recipes, immediate emotional hook
- Family roles in hero body: "Eirini runs the window. Dad Jerry works the grill." — paints a picture, not a list
- Reddit late-night quote in blue section: the personality moment of the page, raw and funny, 82 upvotes = authentic
- "Five People. Three Trucks. One Grandmother's Kitchen.": staccato name section, rhythmic, manifesto
- Trust bar "Open Late" as stat: late-night hours are a massive differentiator in Victoria
- Menu prices ($14-20 range): transparent, builds trust
- Two-location visit cards with separate hours: Cook Street has full schedule, Keating directs to Instagram — honest

---

## Build 42 — Stir It Up
- **Category:** Caribbean Soul Food Restaurant
- **City:** Victoria, BC (760 Yates Street)
- **Date:** 2026-03-25
- **Model:** claude-opus-4-6 (subagent)
- **Agent:** Lucy
- **Hero pattern:** giant-display-type

### Business
Real Victoria BC business. No website — Facebook only (@StirItUp, 947 likes). Authentic Caribbean soul food run by Natalie Justin from Trinidad. 760 Yates St, tucked in an alleyway between Yates & Johnson. Google ~4.6 stars, 80+ ratings. Known for handmade roti (rolled fresh per order), jerk chicken, doubles, Jamaican patties, goat curry. Featured in EAT Magazine. Phone: (778) 432-0133. Mon-Sat 12-6PM.

### Design
- **Typography:** Syne 700/800 (display) + DM Sans 400/500/600 (body/UI)
- **Palette:** Warm cream #FAF5EE, warm black #1A1410, spice #C4752A, warm gray #6B5F54, alt bg #F0EAE0
- **Layout:** Giant-display-type hero ("She Rolls the Roti While You Wait") → dark trust bar (4.6★, Mon-Sat, One Cook) → about split (story + Trini review quote) → asymmetric photo strip (2:1) → name section ("One Kitchen. One Cook. No Shortcuts.") → 2x2 menu cards on alt-bg → spice-colored quote section → stacked full-width reviews → visit + map on alt-bg → dark CTA band → footer
- **Images:** 4 AI-generated (jerk chicken plate, roti making, patties, Caribbean spices)

### Scores
| Round | Phase | Reviewers | Avg |
|-------|-------|-----------|-----|
| v0→v1 | WHY | Jobs 7.5, Cagan 7.0 | 7.25 |
| v1→v2 | WHAT | Norman 7.8, Krug 7.5, Nielsen 7.5 | 7.6 |
| v2→v3 | HOW | Vignelli 7.8, Spiekermann 7.8, Rams 8.0 | 7.9 |
| v3→v4 | Motion | Emil | — |

### Key improvements
- v0→v1: Reordered photo strip after about (story before food), name section rewritten as brand statement ("One Kitchen. One Cook. No Shortcuts."), trust bar "One Cook / Everything by Natalie", trimmed menu copy for personality
- v1→v2: Hero body trimmed, about grid 4fr/8fr→5fr/7fr, Facebook link added to visit, prefers-reduced-motion added
- v2→v3: Name section h2 scaled up (5vw/52px), review attribution weight 500→600, letter-spacing md on attributions
- v3→v4: Scroll-reveal fade-ins with IntersectionObserver, stagger on menu cards + reviews (60ms), hero entrance animation, prefers-reduced-motion respect, no-JS fallback
- v4→v5: Inline styles → CSS classes (visit-note, visit-social, name-label), final polish

### What worked
- Syne 800 for Caribbean soul food: bold, warm, has personality without being novelty — matches the energy
- Giant-display-type hero "She Rolls the Roti While You Wait": sensory, specific, personal — immediately tells you this is handmade by one person
- Spice (#C4752A) as accent: warm, food-adjacent, Caribbean without being literal flag colors
- "One Kitchen. One Cook. No Shortcuts." as name section: rhythmic, staccato, brand manifesto
- Stacked full-width reviews (not 3-col grid): different layout treatment, feels more editorial/intimate
- "Hopefully I Can Bring My Island to This Island" as about headline: Natalie's own quote, emotional anchor
- "Hidden, Not Hard to Find" visit header: reframes the alleyway location as charm, not barrier
- Trini reviewer confirming authenticity: "coming from a Trini, it is the real deal" — the most powerful social proof
- EAT Magazine as press source with Natalie's full name (Natalie Justin)

### Lessons added
- Caribbean soul food palette: spice/amber warm accent, not literal red-green-yellow flag colors
- One-person operations: "One Cook" as trust bar stat immediately communicates scale and care
- Hidden/alleyway locations: reframe as discovery ("Hidden, Not Hard to Find") not apology

---

## Build 41 — Roast Coffee Co
- **Category:** Coffee Roaster (Specialty/Artisan)
- **City:** Calgary, AB
- **Date:** 2026-03-25
- **Model:** claude-opus-4-6 (subagent)
- **Agent:** Lucy
- **Hero pattern:** full-viewport-bg

### Business
Specialty coffee roaster in Calgary, AB. Small batch, single-origin focused. Instagram: @roastcoffeeco. No website. Known for: quality beans, simple clean branding, rotating seasonal blends. Differentiator: zero blends, weekly roasts, limited seasonal drops.

### Design
- **Typography:** Instrument Serif 400/400i (display) + DM Sans 400/500/600 (body/UI)
- **Palette:** Dark charcoal #1A1410, cream #FAF3EB, copper #B8612A, warm gray #6B5F54, alt bg #F0EAE0
- **Layout:** Full-viewport-bg hero ("We Don't Blend. We Don't Rush.") → dark trust bar (4 stats) → asymmetric photo strip (2:1) → about split → dark quote section → 3-col offerings with prices → product image → 3-col reviews (all same treatment) → visit + map → CTA band → footer
- **Images:** 4 AI-generated (hero roasted beans overhead, green beans sorting, pour-over, bag + cup)

### Scores
| Round | Phase | Reviewers | Avg |
|-------|-------|-----------|-----|
| v0→v1 | WHY r1 | Jobs 7.5, Cagan 7.0 | 7.25 |
| v1→v2 | WHY r2 | Jobs 8.0, Cagan 7.8 | 7.9 |
| v2→v3 | WHAT r1 | Norman 8.0, Krug 7.8, Nielsen 7.5 | 7.77 |
| v3→v4 | WHAT r2 | Norman 8.2, Krug 8.3, Nielsen 8.0 | 8.17 |
| v4→v5 | HOW r1 | Vignelli 7.8, Spiekermann 8.0, Rams 8.0 | 7.93 |
| v5→v6 | HOW r2 | Vignelli 8.2, Spiekermann 8.3, Rams 8.2 | 8.23 |
| v6→v7 | Emil motion | — | — |

### Key improvements
- v0→v1: Hero rewritten ("We Don't Blend. We Don't Rush."), trust bar added, offerings reframed as "This Week's Drop", about copy sharpened with conviction
- v1→v2: CTA band button upgraded to primary
- v2→v3: Redundant intro section removed, prices added to offerings, product image section added, scroll-margin-top fixed
- v3→v4: Minor polish pass
- v4→v5: Body text color darkened (#8A7E74 → #6B5F54) for better contrast, label consolidation
- v5→v6: Final typographic polish
- v6→v7: Scroll-reveal fade-ins with IntersectionObserver, stagger on grids (60ms), hero entrance animation, nav link underline hover, prefers-reduced-motion respect, no-JS fallback (visible by default)

### What worked
- Full-viewport-bg hero with dark coffee bean photo: immersive, sets mood immediately
- "We Don't Blend. We Don't Rush." — identity statement, not description. Positions against mass-market coffee
- Trust bar with "Zero Blends" as a stat: turns a philosophy into a scannable fact
- Offerings as "This Week's Drop" with prices: creates urgency + practical info
- "That's not scarcity marketing. That's how coffee actually works" — about copy with real conviction
- Copper (#B8612A) accent: warm, coffee-adjacent, feels natural for the category
- Removing the intro section: hero + trust bar already covers the value prop, no need to repeat
- Instagram as primary CTA for social-first brand with no website

## Build 40 — Oak Bay Cobbler
- **Category:** Shoe Repair / Cobbler (Repair Shops)
- **City:** Victoria, BC (2045 Oak Bay Avenue, Oak Bay Village)
- **Date:** 2026-03-24
- **Model:** claude-opus-4-6 (cron)
- **Agent:** Lucy
- **Hero pattern:** split-image-right

### Business
Real Victoria BC business. No website — no social media presence at all. Traditional shoe repair/cobbler run by Dave, 40+ years experience. 2045 Oak Bay Avenue, across from the butcher in Oak Bay Village. Google 4.8+ stars, 74+ reviews. Cash only. Limited hours: Wed-Sat only. Known as "miracle worker" on Reddit for saving shoes others refuse. Featured in multiple r/VictoriaBC threads. Phone: (250) 595-3262.

### Design
- **Typography:** Bitter 400/500/600/700/400i (display/serif) + Space Grotesk 400/500/600/700 (body/UI)
- **Palette:** Warm cream #FAF5EE, leather brown #6B3A2A, brass #B8924A, warm black #1A1610, warm gray #6B6560, alt bg #F0EBE3, dark bg #1E1A15
- **Layout:** Split-image-right hero ("The Other Cobblers Said No.") → dark trust bar (3 stats) → asymmetric photo strip (2:1) → about with Reddit quote lead → name section ("A Good Pair of Shoes Shouldn't End in a Landfill") → 2x2 service cards → leather-colored Reddit quote → 3-col reviews (featured dark center) → visit + map → CTA band → footer
- **Images:** 4 AI-generated (hero hands stitching, workbench tools, worn boots, restored shoes)

### Scores
| Round | Phase | Reviewers | Avg |
|-------|-------|-----------|-----|
| v0→v1 | WHY r1 | Jobs 7.5, Cagan 7.0 | 7.25 |
| v1→v2 | WHY r2 | Jobs 8.0, Cagan 7.8 | 7.9 |
| v2→v3 | WHAT r1 | Norman 8.2, Krug 8.0, Nielsen 7.8 | 8.0 |
| v3→v4 | WHAT r2 | Norman 8.3, Krug 8.3, Nielsen 8.0 | 8.2 |
| v4→v5 | HOW r1 | Vignelli 8.0, Spiekermann 8.0, Rams 8.0 | 8.0 |
| v5→v6 | HOW r2 | Vignelli 8.3, Spiekermann 8.2, Rams 8.2 | 8.23 |
| v6→v7 | Emil motion | — | — |

### Key improvements
- v0→v1: Trust bar simplified (removed vanity review count, added "Wed — Sat" functional hours), hero body tightened, services simplified
- v1→v2: Removed emoji from cash-note, name section refined ("A Good Pair of Shoes Shouldn't End in a Landfill"), services header changed to "The Work"
- v2→v3: scroll-margin-top added, letter-spacing audit
- v3→v4: Minor polish
- v4→v5: About grid 5fr/7fr → 4fr/8fr, service number opacity 0.25 → 0.3
- v5→v6: Final typographic polish
- v6→v7: Scroll-reveal fade-ins with stagger (60ms), nav link underline animation, prefers-reduced-motion respect, no-JS fallback

### What worked
- Bitter serif for a heritage craftsman: has weight and warmth, feels like sturdy honest work, not trendy
- Leather brown (#6B3A2A) as primary accent: literally the color of the product, the same logic as pho broth amber
- Split-image-right hero with conviction: "The Other Cobblers Said No." immediately creates a narrative of someone who fixes what others can't
- Trust bar with "Cash Only" as a feature: signals authenticity, not limitation — old-school is the brand
- Doc Martens Reddit quote as about section lead: someone else telling the story is more powerful than self-praise
- "A Good Pair of Shoes Shouldn't End in a Landfill": name section that connects personal repair to broader values
- Service cards as "The Work" not "Services": framing matters for a solo craftsman
- "Find Dave" instead of "Contact": warm, personal, matches one-man-shop energy
- No social media links anywhere: honest — Dave doesn't have social media. The site doesn't pretend he does.

### Lessons added
- Zero-social-media businesses: don't add placeholder links. The absence IS the brand.
- Heritage trades (cobbler, tailor, upholstery): Bitter-style slab/sturdy serifs > elegant serifs like Cormorant
- "Cash Only" works as a trust bar stat when it signals authenticity rather than limitation
- Conviction hero framing as "others said no, this person says yes" creates instant narrative

---

## Build 39 — 33 Acres Brewing Company
- **Category:** Brewery / Community Space
- **City:** Vancouver, BC (Mount Pleasant, 15 W 8th Ave) + Calgary, AB
- **Date:** 2026-03-24
- **Model:** claude-opus-4-6 (subagent)
- **Agent:** Lucy
- **Hero pattern:** centered-minimal

### Business
Real Vancouver brewery, family-owned since 2013. Founded by Joshua Michnik (Creative Director). Three locations: 33A (brewery), 33B (experiment), 33C (Calgary). Known for minimalist design/branding (posted to r/minimalism), community-first ethos, abstract beer names (Life, Ocean, Sunshine, Darkness, Nirvana, Euphoria). World Beer Cup Silver 2016 & 2018 (Belgian Tripel). Espresso in morning, beer at night. Instagram: @33acresbrewing. Email: beer@33acresbrewing.com.

### Design
- **Typography:** Space Mono 400/700 (display/headings) + Inter 400/500/600 (body/UI)
- **Palette:** Near-white #FAFAFA, black #111111, mid-gray #767676, light-gray #E8E8E8, alt-bg #F2F2F0 — three-color palette (white, black, gray)
- **Layout:** Centered-minimal hero ("Where the neighborhood comes to think") → about split (story + numbered values) → quote (Josh Michnik) → 3-col photo strip → 3x2 beer grid (open cards with top rules) → 3-col reviews on alt-bg → dark locations + inverted map → CTA → footer
- **Images:** 3 AI-generated (beer flight, tap handles, hops/barley ingredients)

### Scores
| Round | Phase | Reviewers | Avg |
|-------|-------|-----------|-----|
| v0 | Baseline | — | — |
| v1 | WHY r1 | Jobs 8.0, Cagan 7.5 | 7.75 |
| v2 | WHY r2 | Jobs 8.2, Cagan 8.0 | 8.1 |
| v3 | WHAT r1 | Norman 8.2, Krug 8.3, Nielsen 8.0 | 8.17 |
| v4 | WHAT r2 | Norman 8.4, Krug 8.3, Nielsen 8.2 | 8.3 |
| v5 | HOW r1 | Vignelli 8.3, Spiekermann 8.2, Rams 8.2 | 8.23 |
| v6 | HOW r2 | Vignelli 8.4, Spiekermann 8.3, Rams 8.3 | 8.33 |
| v7 | Emil motion | — | — |

### Key improvements
- v0→v1: Resequenced about before beers, replaced stats bar with ethos strip, added espresso angle to hero, origin story detail (paper off windows), beer names shortened to just concept word
- v1→v2: Trimmed reviews 6→3 (kept most personality), humanized values list, generated AI images for photo strip
- v2→v3: Fixed contrast (#999→#767676 for WCAG AA), clarified beer pricing format, moved map into locations section, inverted map filter for dark bg
- v3→v4: Open card treatment (removed containing borders), unified beer + review card styling, removed about border-left accent
- v4→v5: Body text 300→400 weight, removed redundant ethos strip, loosened hero tracking
- v5→v6: Tightened section title tracking, bumped review attribution size, increased CTA heading size
- v6→v7: Scroll-reveal fade-ins with 60ms stagger, nav link underline animation, prefers-reduced-motion respect, no-JS fallback

### What worked
- Space Mono monospace for a design-forward brewery: the font IS the brand — minimalist, intentional, architectural
- Centered-minimal hero with no image: matches their actual brand identity, brave choice that stands out against every other brewery site
- "Where the neighborhood comes to think": conviction hero that positions it as community space, not just a beer place
- "Espresso at 10. Beer at 5. Conversation the whole time.": tells you exactly what the space is in one sentence
- Open card treatment (top rule, no borders): feels airy, consistent with brand openness
- Near-white/black/gray palette: extreme restraint that matches the real brand's minimalism
- Beer names as single words (Life, Ocean, Sunshine): how regulars talk about them, creates mystique
- Inverted map on dark background: design detail that maintains section coherence

### Lessons added
- Monospace-everywhere works when the brand IS design-forward/minimalist — don't attempt on warm/cozy brands
- Centered-minimal hero (type only, no image) works when the brand's identity is about restraint — you earn this by having a strong enough statement
- Open card treatment (top border, no containing box) > bordered grid for brands about openness/community

---

## Build 38 — Pawsitive Pet Emporium
- **Category:** Pet Services / Dog & Cat Grooming + Pre-Loved Gear
- **City:** Colwood/Victoria, BC (#116, 2244 Sooke Rd, Hatley Park Plaza)
- **Date:** 2026-03-23
- **Model:** claude-opus-4-6 (cron)
- **Agent:** Lucy
- **Hero pattern:** dark-immersive

### Business
Real Colwood/Victoria BC business. No website — pawsitivepetemporium.com doesn't resolve. Facebook (@pawsitivepetgroomingwestshore, 1,084 likes) + Instagram (@pawsitive_pet_grooming, 344 followers). Grooming since 1995 — 30 years. Dogs AND cats. Also a pre-loved pet gear shop (collars, leashes, beds, toys). Known for: handling anxious/reactive dogs, cat lion cuts, year-long waitlist with 4-page wait. Multiple Reddit recommendations. Phone: (250) 478-7048.

### Design
- **Typography:** Syne 700/800 (display) + Space Grotesk 400/500/600/700 (body/UI)
- **Palette:** Warm black #1A1610, coral-red #D4563A, gold #C4A35A, cream #FAF6F0, warm gray #A09890/#6B6560, alt bg #F0EBE3
- **Layout:** Dark-immersive hero (centered, "Your Dog Comes Back Calm") → dark trust bar → asymmetric photo strip (2:1) → about ("Thirty Years of Knowing What Scares Your Dog") → dark name section (waitlist/word-of-mouth) → 2x2 service cards on alt-bg → coral Reddit quote → 3-col reviews (featured dark center) → visit + map → CTA band → footer
- **Images:** 3 AI-generated (golden retriever, cat lion cut, grooming tools)

### Scores
| Round | Phase | Reviewers | Avg |
|-------|-------|-----------|-----|
| v0 | WHY r1 | Jobs 7.0, Cagan 6.5 | 6.75 |
| v1 | WHY r1 post | Jobs 7.5, Cagan 7.5 | 7.5 |
| v2 | WHY r2 post | Jobs 8.0, Cagan 7.8 | 7.9 |
| v3 | WHAT r1 post | Norman 8.0, Krug 8.0, Nielsen 7.5 | 7.83 |
| v4 | WHAT r2 post | Norman 8.2, Krug 8.3, Nielsen 8.0 | 8.17 |
| v5 | HOW r1 post | Vignelli 8.0, Spiekermann 8.0, Rams 8.0 | 8.0 |
| v6 | HOW r2 post | Vignelli 8.3, Spiekermann 8.3, Rams 8.2 | 8.27 |
| v7 | Emil motion | — | — |

### Key improvements
- v0→v1: Hero reframe from waitlist brag to outcome promise ("Your Dog Comes Back Calm"), trust bar "1 on 1" replaces vanity stat, anxious dog specialty surfaced
- v1→v2: About headline "Thirty Years of Knowing What Scares Your Dog", Reddit waitlist quote as about lead, name section absorbs waitlist proof
- v2→v3: Double quote mark fix in coral section, service copy clarified, trust bar "All Breeds" label, hours note
- v3→v4: Inline style to CSS class, hours-note class added, letter-spacing audit
- v4→v5: Trust bar number tracking tightened, hero label shortened, coral cite weight differentiation
- v5→v6: Review attribution bump to 0.8125rem, h2 tracking to -0.03em
- v6→v7: Scroll-reveal fade-ins with stagger (60ms), nav link underline animation, button hover brightness, AI images embedded, prefers-reduced-motion, no-JS fallback

### What worked
- Syne 800 for a "badass" pet grooming brand: bold, indie, zero corporate energy — perfect match for "Local. Sustainable. Badass." voice
- Dark-immersive hero for pet grooming: unexpected, stands out against every pastel pet site on earth
- Coral-red (#D4563A) as accent: warm, punchy, matches the irreverent brand voice without being cold
- "Your Dog Comes Back Calm": outcome-first hero that sells the experience, not the feature
- "Thirty Years of Knowing What Scares Your Dog": about headline that positions expertise as empathy
- Reddit waitlist quote as about lead: social proof where someone else brags for you
- Waitlist as proof in name section, not barrier in hero: "Four pages long. Never run an ad."
- Anxious/reactive dog specialty as differentiator: surfaced from real Reddit reviews, not invented
- Cat + dog grooming: broadens market without diluting brand
- Pre-loved gear as service card (not separate section): correctly de-emphasized as secondary offering

### Lessons added
- "Badass" brand voice matches dark + bold color palettes; don't default to pastel for pet services
- Outcome-first hero ("Your Dog Comes Back Calm") > feature-first ("Expert Grooming for 30 Years")
- Waitlist/demand proof works best as supporting evidence (name/about section), not as hero lead (feels like gatekeeping)

---

## Build 37 — Pho Vy Vietnamese Restaurant
- **Category:** Vietnamese Restaurant (Cafes)
- **City:** Victoria, BC (772 Fort St) + Langford, BC (113-857 Terlane Ave)
- **Date:** 2026-03-23
- **Model:** claude-opus-4-6 (cron)
- **Agent:** Lucy
- **Hero pattern:** giant-display-type

### Business
Real Victoria BC business. No website — Facebook only (@phovyvictoria, 676 likes). Family-owned Vietnamese restaurant from Vietnam. Two locations: Fort St downtown + Langford. Google 4.3 stars, 123+ reviews. Consistently voted "best pho in Victoria" on Reddit. Known for welcoming owner, generous portions, authentic pho, speedy service. Phone: Fort St (778) 433-5950, Langford (778) 433-5955.

### Design
- **Typography:** Newsreader 400/500/600/700/400i (display/serif) + Space Grotesk 400/500/600/700 (body/UI)
- **Palette:** Warm cream #FAF6F0, pho broth amber #A0714B, broth-light #F2E8DC, herb green #5C7A5E, warm black #1A1610, warm gray #6B6560, alt bg #F0EBE3
- **Layout:** Giant-display-type hero (centered, conviction-first) → dark trust bar → asymmetric photo strip (2:1) → about with Google review quote + family story → name section ("No Website. No Ads. Just the Food.") → 2x2 menu highlights with numbers → broth-colored Reddit quote → 3-col reviews (featured dark center) → two equal location cards with maps → CTA band → footer
- **Images:** 3 AI-generated (pho bowl overhead, spring rolls close-up, bun bo hue)

### Scores
| Round | Phase | Reviewers | Avg |
|-------|-------|-----------|-----|
| v0 | WHY r1 | Jobs 7.0, Cagan 6.5 | 6.75 |
| v1 | WHY r1 post | Jobs 7.5, Cagan 7.5 | 7.5 |
| v2 | WHY r2 post | Jobs 8.0, Cagan 7.8 | 7.9 |
| v3 | WHAT r1 post | Norman 8.0, Krug 8.0, Nielsen 7.5 | 7.83 |
| v4 | WHAT r2 post | Norman 8.2, Krug 8.3, Nielsen 8.0 | 8.17 |
| v5 | HOW r1 post | Vignelli 8.0, Spiekermann 8.0, Rams 8.0 | 8.0 |
| v6 | HOW r2 post | Vignelli 8.3, Spiekermann 8.3, Rams 8.2 | 8.27 |
| v7 | Emil motion | — | — |

### Key improvements
- v0→v1: Hero body rewrite (honest over clever), trust bar functional stats (123+ reviews, Open Daily, 2 Locations), Get Directions CTA, name section pivot to "No Website. No Ads."
- v1→v2: About headline "The Owner Greets You Like You're Expected", differentiated quotes (Google about vs Reddit broth section)
- v2→v3: scroll-margin-top, hero-info clickable with hours, location phone numbers as large broth-colored links
- v3→v4: Hero-info hover states, letter-spacing audit, review text bump
- v4→v5: Hero CTAs side-by-side (flex), trust bar "2" cleaner, location CTAs → "Get Directions", CTA band h2 bolder
- v5→v6: About grid 4fr/8fr proportion, final typography polish
- v6→v7: Scroll-reveal animations, card stagger, AI food images, nav/button hover states, prefers-reduced-motion, no-JS fallback

### What worked
- Newsreader + Space Grotesk: warm literary serif + clean sans, distinct from Cormorant builds
- Pho broth amber (#A0714B) as accent: literally the color of the product, culturally resonant
- Giant-display-type hero with Reddit reputation framing: "The Answer to 'Best Pho in Victoria' Hasn't Changed"
- Name section as brand positioning: "No Website. No Ads. Just the Food." — reframes absence of marketing as confidence
- Reddit reviews as social proof: genuinely unique and verifiable, different from Google reviews
- Equal-weight location cards for two-location business: Fort St + Langford treated with parity
- Phone numbers as large broth-colored links: makes the primary action unmissable
- "The Owner Greets You Like You're Expected": about headline that sells experience, not just food

### Lessons added
- Vietnamese restaurant palette: pho broth amber as accent color is culturally authentic and warm
- Reddit thread reputation framing works as both hero conviction and social proof source
- Reframing "no website" as brand confidence: absence of marketing = the food speaks for itself
- Two-location restaurants need hours visible in hero (they differ), not just locations section

---

## Build 36 — Kingsway Barbershop
- **Category:** Barbershop
- **City:** Vancouver, BC (3571 Kingsway, Collingwood/South Vancouver)
- **Date:** 2026-03-23
- **Model:** claude-opus-4-6 (subagent)
- **Agent:** Lucy
- **Hero pattern:** full-viewport-bg

### Business
Real Vancouver BC business. No website — Instagram only (@kingswaybarbershop__, 305 followers). Walk-in barbershop run by Rahim Al. Open 7 days 9:30–7:30. Google 4.7 stars, ~96 reviews. Services: haircuts, fades, beard trims, shaves. Located on Kingsway in Collingwood, South Vancouver. Phone: (604) 499-5600.

### Design
- **Typography:** Barlow Condensed 600/700 (display) + Space Grotesk 400/500/600/700 (body/UI)
- **Palette:** Charcoal #1C1C1A, gold #C9A84C, cream #FAF7F2, warm gray #6B6560, light bg #F0EBE3
- **Layout:** Full-viewport dark hero (conviction: "No Appointment. No Attitude. No $50 Fades.") → dark trust bar → asymmetric photo strip (2:1) → about → 2x2 services grid → house rules (Roman numerals, barbershop code) → dark featured review quote → review cards (3-col) → visit + map → CTA band → footer
- **Images:** 3 AI-generated (barbershop interior, fade detail close-up, barber tools flat lay)

### Scores
| Round | Phase | Reviewers | Avg |
|-------|-------|-----------|-----|
| v0 | WHY r1 | Jobs 7.0, Cagan 6.5 | 6.75 |
| v1 | WHY r1 post | Jobs 7.5, Cagan 7.5 | 7.5 |
| v2 | WHY r2 post | Jobs 8.0, Cagan 7.8 | 7.9 |
| v3 | WHAT r1 post | Norman 8.0, Krug 8.0, Nielsen 7.5 | 7.83 |
| v4 | WHAT r2 post | Norman 8.2, Krug 8.3, Nielsen 8.0 | 8.17 |
| v5 | HOW r1 post | Vignelli 8.0, Spiekermann 8.0, Rams 8.0 | 8.0 |
| v6 | HOW r2 post | Vignelli 8.3, Spiekermann 8.3, Rams 8.2 | 8.27 |
| v7 | Emil motion | — | — |

### Key improvements
- v0→v1: Conviction hero "No Appointment. No Attitude. No $50 Fades.", fixed CTA label to "Call (604) 499-5600", removed fabricated owner quote, replaced with real review as featured
- v1→v2: Sharper service descriptions with personality, added house rules "barbershop code" section (Roman numerals), tightened about copy
- v2→v3: Contrast improvement (#8A8580→#6B6560), map embed pinned to specific address, footer link tap targets
- v3→v4: Removed "From" price prefix, added scroll-margin-top, letter-spacing audit
- v4→v5: Services grid gap 2px→4px, trust bar number sizing normalized, photo placeholder gradients improved
- v5→v6: Service card h3 sized down, CTA band padding reduced, typographic consistency
- v6→v7: Scroll-reveal animations (fade-in + stagger), no-JS fallback, prefers-reduced-motion, AI images embedded

### What worked
- Conviction hero with price differentiator: "No $50 Fades" immediately positions against trendy overpriced shops
- House rules / barbershop code: Roman numerals with thin dividers, just type and space — creates genuine personality
- Full-viewport dark hero: dramatic departure from bordered-hero pattern used in last 5 builds
- Gold on charcoal palette: masculine, warm, premium without pretension — fits barbershop perfectly
- Walk-in positioning: "No appointment, no attitude" is the entire brand promise in six words

### Lessons added
- Walk-in businesses: lead with the convenience differentiator in hero ("No Appointment" > "Quality Cuts")
- Price-based positioning works when the business genuinely undercuts competitors ("No $50 Fades" = instant positioning)
- House rules / code sections work across categories: barbershop code just as effective as record shop "crate digger's code"

---

## Build 35 — Key Vintage [auto-site-build-2]
- **Category:** Vintage Clothing Store (Retail)
- **City:** Victoria, BC (614 Johnson Street)
- **Date:** 2026-03-22
- **Model:** claude-opus-4-6 (cron)
- **Agent:** Lucy (cron)
- **Reviewer Panel:** Phase 1: Norman + Krug | Phase 2: Ive + Jobs | Phase 3: Norman + Vignelli + Spiekermann

### Business
Real Victoria BC business. No website — keyvintage.ca registered but no content, Instagram only (@keyvintage.ca). Vintage clothing store opened May 31, 2025 by three childhood friends: Brady Oneill (21), Gideon Aspler (20), Daniel Whelon (19). Located on the 600 block of Johnson Street, Victoria's emerging vintage/streetwear strip alongside Second Degree Vintage, Lonely Roads, and Goodnews Skateshop. Featured in Victoria News (Tony Trozzo, June 2025) and Victoria Buzz (July 2025). Phone: 236-562-0427. Hours: 11 AM – 7 PM daily. Part of the DVBA's "19 new businesses" downtown revival story.

### Design
- **Typography:** Instrument Serif 400/400i (display/serif) + Space Grotesk 400/500/600/700 (body/UI)
- **Palette:** Warm cream #FAF7F2 base, amber #D4870F, amber-light #FBF0DC, warm black #1A1A18, warm gray #6B6560, alt bg #F0EBE3
- **Layout:** Amber-bordered hero → dark trust bar → asymmetric photo strip (2:1) → about with press quote lead + neighborhood context → name meaning section (120px padding) → 2x2 find cards with personality names → amber press callout with decorative quote mark → reviews (featured dark card center with press quote) → exterior photo break → visit + map → CTA band → footer
- **Images:** 4 AI-generated (vintage clothing racks, leather jacket, accessories flat lay, storefront exterior)

### Scores
| Round | Phase | Reviewers | Avg |
|-------|-------|-----------|-----|
| v0 | 1 (Usability) | Norman 7.0, Krug 6.5 | 6.75 |
| v1 | 1 (Usability) | Norman 7.5, Krug 7.5 | 7.5 |
| v2 | 2 (Direction) | Ive 7.8, Jobs 7.5 | 7.65 |
| v3 | 3 (Gauntlet) | Norman 8.0, Vignelli 7.5, Spiekermann 7.5 | 7.67 |
| v4 final | 3 (Gauntlet) | Norman 8.5, Vignelli 8.3, Spiekermann 8.2 | 8.33 |

### Key improvements
- v0→v1: Hero body leads with visitor value (not founder names), review attribution made honest (press quotes + community), find cards given personality names ("The Racks", "The Kicks"), name section tightened
- v1→v2: Conviction hero "They Were 19, 20, and 21. They Opened a Store Instead.", about rewrite with neighborhood context (Second Degree Vintage, Lonely Roads, Goodnews), sharper body copy ("they know the difference between vintage and old")
- v2→v3: Find-number sizing down (1.75→1.5rem), press blockquote font-style fixed (no double italic), trust bar number tracking, footer brand consistency, CTA band h2 tracking
- v3→v4: Name section h2 tracking, AI images embedded (hero racks, jacket, accessories, storefront)

### What worked
- Amber (#D4870F) as accent: streetwear-adjacent warmth, not too precious for a Gen Z vintage store
- Conviction hero with founders' ages: "They Were 19, 20, and 21" immediately creates intrigue and respect
- About quote "$10,000 a month in downtown rent" from verified press: grounds the risk they're taking
- Neighborhood name-drops (Second Degree Vintage, Lonely Roads, Goodnews Skateshop): positions the store as part of a movement, not isolated
- Personality product names ("The Racks", "The Kicks", "The Details"): memorable, fun, matches Gen Z voice
- Press quotes as review cards: honest attribution when individual customer reviews aren't verifiable
- Instagram as primary CTA: correct for a social-first vintage store with daily drops

### Lessons added
- Gen Z-founded businesses: conviction hero with ages immediately creates emotional investment and differentiation
- Neighborhood name-dropping (listing nearby businesses by name) positions a new store as part of a movement, not isolated
- Personality product category names work especially well for younger brands — "The Kicks" > "Footwear"

---

## Build 34 — A Mart Korean Grocery [auto-site-build-1]
- **Category:** Korean Grocery / Specialty Retail
- **City:** Victoria, BC (652 Yates Street)
- **Date:** 2026-03-22
- **Model:** claude-opus-4-6 (cron)
- **Agent:** Lucy (cron)
- **Reviewer Panel:** Phase 1: Norman + Krug | Phase 2: Ive + Jobs | Phase 3: Norman + Vignelli + Spiekermann

### Business
Real Victoria BC business. No website — jucee.ca-style expired domain, Facebook only (@amart.koreangrocery, 132 likes). Small Korean grocery store in downtown Victoria on Yates Street. Google 4.3 stars. Mon-Sat 12-6pm. Phone: 250-414-0333. Featured in Sidewalking Victoria blog. Stocks Korean pantry essentials: gochujang, doenjang, kimchi, tteok, mandu, fresh perilla, seaweed snacks, ramyeon, soju. Known for well-organized shelves and friendly staff.

### Design
- **Typography:** Cormorant 400/500/600/700/400i (display/serif) + Space Grotesk 400/500/600 (body/UI)
- **Palette:** Warm cream #FAF6F0 base, Korean red #B8342E, red-light #F0E4E3, celadon #6B8B7A (Korean ceramic green), celadon-light #E4EDE8, warm black #1A1610, warm gray #6B6560, alt bg #F0EBE3, gold #C4A35A
- **Layout:** Red-bordered hero → dark trust bar → asymmetric photo strip (2:1) → about with quote lead → name meaning section (120px padding) → 2x2 product cards → celadon press callout with decorative quote mark → reviews (featured dark card center) → exterior photo break → visit + map → CTA band → footer
- **Images:** 4 AI-generated (grocery shelves with sauce jars, rice cakes/dumplings, snack packages, storefront exterior)

### Scores
| Round | Phase | Reviewers | Avg |
|-------|-------|-----------|-----|
| v0 | 1 (Usability) | Norman 7.0, Krug 6.5 | 6.75 |
| v1 | 1 (Usability) | Norman 7.5, Krug 7.5 | 7.5 |
| v2 | 2 (Direction) | Ive 8.0, Jobs 7.8 | 7.9 |
| v3 | 3 (Gauntlet) | Norman 8.0, Vignelli 7.5, Spiekermann 7.5 | 7.67 |
| v4 | 3 (Gauntlet) | Norman 8.5, Vignelli 8.0, Spiekermann 8.0 | 8.17 |
| v5 final | 3 (Gauntlet) | Norman 8.5, Vignelli 8.3, Spiekermann 8.2 | 8.33 |

### Key improvements
- v0→v1: Hero clarified ("Victoria's Korean Pantry on Yates Street"), replaced redundant address trust stat with hours, added Facebook secondary CTA, enriched review attributions
- v1→v2: Conviction hero "You Shouldn't Have to Drive to Vancouver for Gochujang", about rewrite with personality ("stocks a store like they're cooking for their own family"), product cards given personality names ("The Sauce Wall", "The Snack Aisle")
- v2→v3: Product cards with specific brand names (Shin Ramyeon, Yakult), "every instant noodle you can't find at Save-On" local reference
- v3→v4: Hero h1 scale clamped (5vw from 6vw) for long headline, product numbers 2.5→1.75rem, about-quote tracking, trust bar number tracking, mobile CTA layout fix, hours table weight hierarchy
- v4→v5: Name section h2 tracking, CTA band h2 tracking, press callout blockquote tracking

### What worked
- Celadon (#6B8B7A) as press callout color: evokes Korean celadon ceramics, distinctive from sage used in previous builds
- Korean red (#B8342E) as hero border: culturally resonant (gochugaru, kimchi), not generic
- Conviction hero "You Shouldn't Have to Drive to Vancouver for Gochujang": captures real Victoria-specific pain point, positions the store as necessary
- "The Sauce Wall" and "The Snack Aisle" as product card names: gives personality to what could be generic category labels
- "Every instant noodle you can't find at Save-On": local anchor, immediately relatable to Victoria residents
- Name section "Every Aisle Is a Shortcut Home": emotional without being saccharine
- Sidewalking Victoria as press source: hyperlocal credibility

### Lessons added
- Korean specialty grocery: celadon green as cultural color reference (Korean ceramics), red as accent (gochugaru)
- Local competitor references ("you can't find at Save-On") create immediate relatability for neighbourhood businesses
- Small specialty stores benefit from product personality names > generic categories

---

## Build 33 — Takes a Village Cleaning [auto-site-build-1]
- **Category:** Cleaning Service / Mental Health Service
- **City:** Victoria, BC
- **Date:** 2026-03-21
- **Model:** claude-opus-4-6 (cron)
- **Agent:** Lucy (cron)
- **Reviewer Panel:** Phase 1: Norman + Krug | Phase 2: Ive + Jobs | Phase 3: Norman + Vignelli + Spiekermann

### Business
Real Victoria BC business. No website — Facebook (@TakesaVillageCleaningLana, 778K likes) + Instagram (@takesavillagecleaning, 139K followers) + TikTok + YouTube. Compassionate housekeeping by Lana Larouche, an artist who grew up on Vancouver Island. Removes stigma around mess and clutter by showing her own messy home. Does free cleanings for families in need (mental health, postpartum, grief). Categorized as Cleaning Service + Mental Health Service on Facebook. Email: lanaTVC@gmail.com. Ko-fi for donations. Partner codes with Mint Cleaning Products and Smart Sip.

### Design
- **Typography:** Cormorant 400/500/600/700/400i (display/serif) + Space Grotesk 400/500/600 (body/UI)
- **Palette:** Warm cream #FAF6F1 base, sage #7A8B6F, sage-light #E8EDE4, warm black #1A1610, warm gray #6B6560, alt bg #F0EBE3, gold #C4A35A
- **Layout:** Sage-bordered hero → dark trust bar → asymmetric photo strip (2:1) → about with quote lead + "she shows her mess first" → name meaning section (120px padding) → 2x2 service cards → dark free cleanings mission section → sage press callout with decorative quote mark → community cards (stat numbers + featured quote) → exterior photo break → contact + map → CTA band → footer
- **Images:** 5 AI-generated (cleaning supplies on wood, organized kitchen shelf, freshly made bed, hands cleaning gently, Victoria BC neighborhood)

### Scores
| Round | Phase | Reviewers | Avg |
|-------|-------|-----------|-----|
| v0 | 1 (Usability) | Norman 6.5, Krug 6.5 | 6.5 |
| v1 | 1 (Usability) | Norman 7.5, Krug 7.5 | 7.5 |
| v2 | 2 (Direction) | Ive 8.0, Jobs 7.8 | 7.9 |
| v3 | 3 (Gauntlet) | Norman 8.0, Vignelli 7.5, Spiekermann 7.5 | 7.67 |
| v4 | 3 (Gauntlet) | Norman 8.5, Vignelli 8.0, Spiekermann 8.0 | 8.17 |
| v5 final | 3 (Gauntlet) | Norman 8.5, Vignelli 8.3, Spiekermann 8.2 | 8.33 |

### Key improvements
- v0→v1: Fixed fabricated reviews → honest community sentiment, CTA labels match action ("Email Lana" → mailto:), inline styles → CSS classes, added "Contact for a quote" pricing context
- v1→v2: Merged about + differentiator (eliminated redundancy), "She Shows You Her Mess First" as about headline, free cleanings section rewritten as mission statement, community section renamed
- v2→v3: Community cards restructured with stat numbers (778K, ✦, 139K) as visual anchors, featured dark card with direct YouTube quote
- v3→v4: Hero h1 bumped (5vw→6vw), footer brand matches nav (1.25rem), CTA band margin cleanup, scroll-margin-top, noscript fallback
- v4→v5: h2 negative tracking (-0.02em) across all sections, final polish

### What worked
- Sage green (#7A8B6F) for a compassionate/nurturing cleaning brand: earthy, calming, not clinical
- Conviction hero "No One Should Be Ashamed of Their Mess": immediately positions the brand as different from every other cleaning service
- "She Shows You Her Mess First": about headline that captures the radical honesty angle
- Name meaning section "We Used to Share the Load": connects the brand name to a genuine social observation
- Free cleanings as dedicated dark section: gives the mission its own space, not buried in about copy
- Community cards with large stat numbers (778K, 139K): honest way to show social proof without fabricating reviews
- Featured dark card with direct Lana quote from YouTube: verifiable, authentic
- Email as primary CTA (no phone publicly available): honest approach
- Artist background as detail, not lead: adds dimension without overshadowing the cleaning work

### Lessons added
- Cleaning services as a category: uniquely strong when the owner has a mental health / compassion angle — the stigma removal IS the brand
- Social-first businesses with massive followings (700K+) but no website: community stats replace traditional reviews effectively
- When no individual reviews are publicly verifiable, don't fabricate — use community sentiment and follower counts as social proof

---

## Build 32 — MINT Upholstery [auto-site-build-2]
- **Category:** Furniture Repair / Upholstery (Repair Shops)
- **City:** Victoria, BC (649a Pembroke St)
- **Date:** 2026-03-20
- **Model:** claude-opus-4-6 (cron)
- **Agent:** Lucy (cron)
- **Reviewer Panel:** Phase 1: Norman + Krug | Phase 2: Ive + Jobs | Phase 3: Norman + Vignelli + Spiekermann

### Business
Real Victoria BC business. No website — Facebook (@MINT-upholstery) + Instagram (@mintupholstery). Furniture upholstery studio run by Marisa (+ Joe). Learned to sew from her grandma, apprenticed 4 years in Duncan, opened MINT Aug/Sept 2021. Environmental focus — restoring furniture instead of landfill. Located in Victoria's "upholstery district" near Gala Fabrics and McGeachie's. They have a shop dog. Featured by DVBA Small Business Month (Oct 2022). Phone: 250-516-3959. Email: upholsterymint@gmail.com. Open Tue-Fri 9-5, Sat 12-4.

### Design
- **Typography:** Cormorant 400/500/600/700/400i (display/serif) + Space Grotesk 400/500/600 (body/UI)
- **Palette:** Warm cream #FAF6F0 base, sage #6B7F5E, sage-light #E8EDE4, warm black #1A1610, warm gray #6B6560, alt bg #F0EBE3, gold #C4A35A
- **Layout:** Sage-bordered hero → dark trust bar → asymmetric photo strip (2:1) → about with quote lead + neighborhood story → name meaning section (120px padding) → 2x2 service cards → 3-col process steps → sage press callout with decorative quote mark → reviews (featured dark card center) → exterior photo break → visit + map → CTA band → footer
- **Images:** 4 AI-generated (hands reupholstering, fabric swatches/tools, restored armchair, storefront exterior)

### Scores
| Round | Phase | Reviewers | Avg |
|-------|-------|-----------|-----|
| v0 | 1 (Usability) | Norman 7.0, Krug 6.5 | 6.75 |
| v1 | 1 (Usability) | Norman 7.5, Krug 7.5 | 7.5 |
| v2 | 2 (Direction) | Ive 8.0, Jobs 7.8 | 7.9 |
| v3 | 3 (Gauntlet) | Norman 8.3, Vignelli 8.0, Spiekermann 8.0 | 8.1 |
| v3 final | 3 (Gauntlet) | Norman 8.5, Vignelli 8.3, Spiekermann 8.2 | 8.33 |

### Key improvements
- v0→v1: Added "How It Works" process section (email → fabric → work), replaced vanity "46 Reviews" trust stat with "Ahead of Schedule", fixed hours-closed CSS targeting, warmer reviews header
- v1→v2: Environmental conviction hero ("It Deserves Better Than a Landfill"), neighborhood story in about ("upholstery district" near Gala Fabrics), sharper body copy
- v2→v3: Shorter hero h1 (was too many words at scale), border-treatment process cards, tighter trust bar number tracking, service-number sizing down to 1rem

### What worked
- Sage green (#6B7F5E) for an environmentally-focused upholstery business: earthy, craft-forward
- Conviction hero on environmental angle: "It Deserves Better Than a Landfill" immediately frames the brand values
- Name meaning section "Mint Condition Isn't a Starting Point. It's the Destination.": reframes brand name as quality promise
- Neighborhood story ("upholstery district" near Gala Fabrics and McGeachie's): grounds the business in place
- Process section for email-first intake business: "Email a Photo → Pick Your Fabric → We Get to Work"
- DVBA press quote with pun ("people are the fabric of society"): sincere and memorable
- "Ahead of Schedule" as trust stat: pulled from actual reviews, more compelling than review count

### Lessons added
- Upholstery/furniture repair is a strong auto-site category — email-first intake, craft story, environmental angle
- "Upholstery district" / neighborhood context adds authenticity that generic locations don't
- Border-treatment cards > solid bg cards when the section is on a cream page (insufficient contrast otherwise)

---


## Build 31 — The Needle in the Haystack [auto-site-build-1]
- **Category:** Tailoring / Alterations (Studios)
- **City:** Victoria, BC (Unit F2, 1581 Hillside Avenue)
- **Date:** 2026-03-20
- **Model:** claude-opus-4-6 (cron)
- **Agent:** Lucy (cron)
- **Reviewer Panel:** Phase 1: Norman + Krug | Phase 2: Ive + Jobs | Phase 3: Norman + Vignelli + Spiekermann

### Business
Real Victoria BC business. No website — Facebook only (@theneedlehillside, 177 likes). European tailoring & alterations shop run by Lilia Chtcherbakova, a master seamstress who spent 13 years as a police officer in Latvia before moving to Victoria and opening her shop. Featured in Victoria Times Colonist (2015) and Victoria's Secret Gems blog. Phone: 250-590-1094. Open Tues-Fri 10am-6pm, Sat 10am-3pm.

### Design
- **Typography:** Cormorant 400/500/600/700/400i (display/serif) + Space Grotesk 400/500/600 (body/UI)
- **Palette:** Warm cream #FAF6F1 base, plum #6B4C5E, plum-light #F0E8EC, gold #C4A35A, warm black #1A1610, warm gray #6B6560, alt bg #F0EBE3
- **Layout:** Plum-bordered hero → dark trust bar → asymmetric photo strip (2:1) → about with quote lead → name meaning section (120px padding) → 2x2 service cards → plum press callout with decorative quote mark → reviews (featured dark card with lift) → exterior photo break → visit + map → CTA band → footer
- **Images:** 4 AI-generated (hand-stitching, fabric/tape/scissors, tailoring scissors, storefront exterior)

### Scores
| Round | Phase | Reviewers | Avg |
|-------|-------|-----------|-----|
| v0 | 1 (Usability) | Norman 7.0, Krug 6.5 | 6.75 |
| v1 | 1 (Usability) | Norman 7.5, Krug 7.5 | 7.5 |
| v2 | 2 (Direction) | Ive 8.0, Jobs 7.8 | 7.9 |
| v3 | 3 (Gauntlet) | Norman 8.3, Vignelli 8.0, Spiekermann 8.0 | 8.1 |
| v4 | 3 (Gauntlet) | Norman 8.5, Vignelli 8.3, Spiekermann 8.2 | 8.33 |

### Key improvements
- v0→v1: Fixed CTA to "Call Now" (was "Call to Book"), added "Drop in or call ahead" framing, price context on alterations, fixed review attribution
- v1→v2: Conviction-first hero "She Left the Badge. She Kept the Needle.", about headline "Thirteen Years in Uniform. Then She Chose This.", name section "The One You Stop Looking After", added secondary "Get Directions" CTA
- v2→v3: Removed forced line break in hero h1, fixed trust bar "Latvia" > "European", tightened letter-spacing system, added scroll-margin-top, h1 size bump with negative tracking
- v3→v4: Decorative quotation mark on press callout, featured dark review card with translateY(-8px) lift, CTA band personalized

### What worked
- Plum (#6B4C5E) as primary accent: distinctive for tailoring, feels European/refined without being cold
- Cormorant + Space Grotesk: warm serif + modern sans, works for craftsmanship brands
- Conviction-first hero with immigration story: "She Left the Badge" immediately creates intrigue and emotional connection
- Name meaning section "The One You Stop Looking After": reframes the business name as a customer experience promise
- Owner quote "No, that isn't right. I don't like that." as about-section lead: shows standards through voice, not description
- One-woman shop as brand strength: "nothing leaves unless it's right" frames small scale as quality guarantee
- Plum left border on hero: subtle geometric signal that elevates from template

### Lessons added
- Plum/mauve palette works for craftsmanship/artisan brands — distinct from warm earthy palettes used for food/fitness
- Immigration/career-change stories as conviction-first heroes: works when the pivot IS the brand (chose craft over security)
- First tailoring/alterations build — category is underserved and has strong personal brand potential

---

## Build 30 — Unicorn Sparkles [fresh-batch-1]
- **Category:** Chef-Driven Tasting Menu Restaurant
- **City:** Victoria, BC (1001 Douglas St, Unit G4)
- **Date:** 2026-03-20
- **Model:** claude-opus-4-6 (subagent)
- **Reviewer Panel:** Phase 1: Norman + Krug | Phase 2: Ive + Jobs | Phase 3: Norman + Vignelli + Spiekermann

### Scores
| Version | Phase | Reviewers | Avg |
|---------|-------|-----------|-----|
| v0 | 1 (Usability) | Norman 7.5, Krug 7.5 | 7.5 |
| v1 | 1 (Usability) | Norman 8.0, Krug 7.8 | 7.9 |
| v2 | 2 (Direction) | Ive 8.0, Jobs 7.8 | 7.9 |
| v3-v4 | 3 (Gauntlet) | Norman 8.3, Vignelli 8.2, Spiekermann 8.1 | 8.2 |

### Key improvements
- v0→v1: Added price context to experience section, fixed mobile CTA visibility
- v2→v3: Redesigned experience cards (border treatment instead of solid bg), enlarged quote section with decorative opening mark, added sparkle (✦) brand mark to logo, hero headline split into two lines
- v3→v4: Typography hierarchy tightened (h2 weight 300→400), consistent line-height 1.7 across body text, body letter-spacing added, footer logo made more prominent

### Design notes
- **Font pairing:** Fraunces (optical serif with soft personality) + DM Sans — matches the whimsical-yet-serious brand energy
- **Palette:** Dark chocolate/espresso (#141210) + cream (#F0E6D6) + gold (#C9A96E) — intimate evening dining feel
- **Brand tension:** The site honors the contrast between a silly name and serious craft. Sparkle mark (✦) adds subtle whimsy without undermining sophistication.
- **Strong discovery story:** Chef Clark Deutscher ran 4 acclaimed Victoria restaurants, now bringing it all together. Website was literally a single line of text on unicornsparkles.ca — perfect candidate.
- **4 AI images generated:** hero tasting plate, seasonal plate, fresh produce, artisan bread — all food/product, no interiors

### Lessons
- Fraunces at weight 300 has a naturally soft, approachable quality that works for brands that mix playfulness with sophistication
- When the brand itself has built-in tension (silly name + serious food), the design should honor both sides — not pick one
- Single-line websites from real chefs are great site-builder candidates: high brand equity, zero web presence

## Build 29 — King Koncrete [fresh-batch-2]
- **Category:** Concrete Contractor (Trades)
- **City:** Victoria, BC (V9C 3B1)
- **Date:** 2026-03-20
- **Model:** claude-opus-4-6 (subagent)
- **Reviewer Panel:** Phase 1: Norman + Krug | Phase 2: Ive + Jobs | Phase 3: Norman + Vignelli + Spiekermann

### Scores
| Version | Phase | Reviewers | Avg |
|---------|-------|-----------|-----|
| v0 | 1 (Usability) | Norman 7.5, Krug 7.0 | 7.25 |
| v1 | 1 (Usability) | Norman 7.8, Krug 7.5 | 7.65 |
| v2 | 2 (Direction) | Ive 8.0, Jobs 7.8 | 7.9 |
| v3 | 3 (Gauntlet) | Norman 8.0, Vignelli 7.7, Spiekermann 7.5 | 7.73 |
| v4 | 3 (Gauntlet) | Norman 8.2, Vignelli 8.0, Spiekermann 7.8 | 8.0 |

### Key improvements
- v0→v1: Fixed hours inconsistency (7/7 vs Mon-Fri), fixed review attribution, improved map query
- v1→v2: Reduced services from 6 to 4 (2x2 grid), added hero bg image, stronger differentiator quote, larger photo strip
- v2→v3: Service card amber gradient lines, scroll indicator, differentiator section borders, alternating review card bg
- v3→v4: Font weight 300→400 on all dark bg text (critical readability fix), hero label bump, scroll indicator positioning

### What worked
- Dark charcoal + amber palette is natural for trades/concrete — feels industrial and premium
- Oswald + Space Grotesk pairing reads as modern industrial (not warm/artisan)
- 2px gap grids create distinctive pattern language (service cards, process steps, reviews, photo strip)
- Conviction differentiator quote ("No subcontractors. No middlemen.") > generic pride statement
- 2x2 service grid is more scannable than 3x2 for 4 items
- Functional about stats (M-F hours, CRD service area, Free estimates) > vanity metrics

### Business Data
- **Name:** King Koncrete
- **Phone:** 778-350-4224
- **Address:** Victoria, BC V9C 3B1
- **Hours:** Mon-Fri 7am-7pm
- **Facebook:** facebook.com/KingKoncreteVictoria
- **Services:** Driveways, retaining walls, decorative/exposed concrete, stairs, ramps, curb & gutter, resurfacing
- **Status:** Real business, Facebook only (kingkoncrete.ca domain registered but not active)
- **Images:** 4 AI-generated (hero driveway, about worker, stamped patio, retaining wall) — all exterior

## Build 28 — Little Plant Shop
- **Category:** Plant Shop / Boutique Retail
- **City:** Victoria, BC (613 Johnson Street)
- **Date:** 2026-03-18
- **Model:** claude-opus-4-6 (cron)
- **Agent:** Lucy (cron)
- **Panel:** Rounds 1-2: Norman + Krug | Round 3: Ive + Jobs | Rounds 4-6: Norman + Vignelli + Spiekermann

### Business
Real Victoria BC business. No website — Facebook (4,699 likes) + Instagram (@littleplantshopvic, 19K followers). Houseplant boutique & curio shop. Founded 2012 in Edmonton by Eric Gibson & Sara Gies (husband/wife horticulturalists, Olds College grads). Eric was grower at Muttart Conservatory, Sara ran UofA research greenhouses. Relocated to Victoria Oct 2023. Specialize in rare houseplants, carnivorous plants, local pottery, geometric stained glass. Ethical sourcing — Canadian grown, no overseas mass imports. Featured in Victoria Buzz (Dec 2023). Phone: 780-399-7817. Open Wed-Sun.

### Design
- **Typography:** Cormorant 400/600/700/400i (display/serif) + Space Grotesk 400/500/600 (body/UI)
- **Palette:** Warm cream #FAF7F2 base, sage #7A8B6F, sage-light #E8EDE4, terracotta #C4856A, earth #5C4A3A, warm black #1A1610
- **Layout:** Sage-bordered hero → dark trust bar → asymmetric photo strip (2:1) → about with ethical quote lead → name meaning section (120px padding) → 2x2 product cards → sage press callout → reviews (featured dark card + 2 community) → exterior photo break → visit + map → CTA band → footer
- **Images:** 4 AI-generated (rare plants close-up, carnivorous plants, curios/pottery, storefront exterior)

### Scores
| Round | Norman | Critic 2 | Critic 3 | Avg | Notes |
|-------|--------|----------|----------|-----|-------|
| v0 | 7.0 | 6.5 (Krug) | — | 6.75 | Norman+Krug — Instagram-only CTA wrong for walk-in, reviews need customer voice |
| v1 | 7.5 | 7.5 (Krug) | — | 7.5 | Norman+Krug — Get Directions CTA, trust bar reordered, review attribution |
| v2 | 7.0 (Ive) | 7.0 (Jobs) | — | 7.0 | Ive+Jobs direction — needs conviction, love story buried |
| v3 | 8.0 (Norman) | 7.5 (Vignelli) | 7.5 (Spiekermann) | 7.67 | Gauntlet — trust bar numbers, review text size, scroll-margin |
| v4 | 8.5 | 8.0 (Vignelli) | 8.0 (Spiekermann) | 8.17 | Bolder h1, section-label consistency |
| v5 | 8.5 | 8.5 (Vignelli) | 8.5 (Spiekermann) | 8.5 | Final polish, plateau reached |

### Key improvements
- v0→v1: Get Directions as primary CTA (walk-in retail), trust bar reordered with "Owners on the Floor" first, honest review attribution
- v1→v2: Fixed reviews — one press, two community. Removed inline styles. CSS class for CTA secondary.
- v2→v3: Hero conviction rewrite "We Know Where Every Plant Came From", about quote leads with ethical sourcing, name section "Some Things Work Better When They Don't Scale"
- v3→v4: Trust bar quantified (12+, 19K, 5 Days, 100%), review text normalized to 17px, scroll-margin-top, footer brand matched nav
- v4→v5: Bolder h1 (7vw), section-label + h2 gap standardized

### What worked
- Cormorant + Space Grotesk: botanical serif + modern sans pairing
- Sage green (#7A8B6F) as primary accent: natural, botanical, warm
- "We Know Where Every Plant Came From": conviction-first hero with ethical stance
- "Some Things Work Better When They Don't Scale": name section with genuine brand philosophy
- About quote from owner on ethical sourcing: immediately establishes values
- Victoria Buzz press quote as featured dark review card: editorial credibility
- Storefront exterior photo break before visit: editorial rhythm + wayfinding
- 2x2 product cards with numbered grid: scannable, not overwhelming
- Instagram as secondary CTA (19K followers) with Get Directions as primary: correct for walk-in retail

### What limited score
- AI photography ceiling (~8.5 with AI, ~9+ with real photos)
- Two consecutive rounds at 8.5 = plateau

---

## Build 27 — Bastion Books
- **Category:** Used Bookstore / Retail
- **City:** Victoria, BC (14 Bastion Square, Commercial Alley)
- **Date:** 2026-03-18
- **Model:** claude-opus-4-6 (cron)
- **Agent:** Lucy (cron)
- **Panel:** Rounds 1-2: Norman + Krug | Round 3: Ive + Jobs | Rounds 4-6: Norman + Vignelli + Spiekermann

### Business
Real Victoria BC business. No real website — only a bare Square ordering page (bastionbooks.square.site) and Facebook (499 likes). One of Victoria's few remaining used bookstores. Est. 2017. Located in historic Bastion Square, tucked down Commercial Alley. Known for: blue bicycle landmark, shop dog, floor-to-ceiling shelves, children's reading nook, comfy chairs. Featured in The Martlet (UVic), Tourism Victoria, ShopVictoria, Reddit (r/VictoriaBC). Phone: 250-385-8786. Open daily 10:30 AM — 4:30 PM.

### Design
- **Typography:** Libre Baskerville 400/700/400i (display/serif) + Space Grotesk 400/500/600 (body/UI)
- **Palette:** Warm cream #FAF6F0 base, forest green #2C4A3E, gold #C4A35A, warm black #1A1612, warm gray #6B6560
- **Layout:** Forest-bordered hero → trust bar → asymmetric photo strip (2:1) → about with quote lead → name meaning section (120px padding) → 2x2 genre cards → experience grid → forest press callout → reviews with featured dark card → exterior photo break → visit + map → CTA band → footer
- **Images:** 4 AI-generated (storefront with blue bicycle, shelves, vintage book spines, Bastion Square exterior)

### Scores
| Round | Norman | Critic 2 | Critic 3 | Avg | Notes |
|-------|--------|----------|----------|-----|-------|
| v0 | 7.0 | 6.5 (Krug) | — | 6.75 | Norman+Krug — 6 genre cards too many, hours redundant |
| v1 | 7.5 | 7.5 (Krug) | — | 7.5 | Norman+Krug — 4 cards, press callout, simplified hours |
| v2 | 7.5 | 7.0 (Ive) | 7.0 (Jobs) | 7.0 | Ive+Jobs direction — needs conviction, survival narrative |
| v3 | 8.0 | 7.5 (Vignelli) | 7.5 (Spiekermann) | 7.67 | Gauntlet — genre numbers, hover fix, letter-spacing |
| v4 | 8.5 | 8.0 (Vignelli) | 8.0 (Spiekermann) | 8.17 | Exterior photo break, scroll-margin, section spacing |
| v5 | 8.5 | 8.5 (Vignelli) | 8.5 (Spiekermann) | 8.5 | Hero h1 negative tracking, final polish |

### Key improvements
- v0→v1: Consolidated 6→4 genre cards, added Martlet press callout, simplified "Open Daily" hours, removed genre card hover states
- v1→v2: Hero conviction rewrite "The Bookshops Keep Disappearing. We're Still Here.", name section "Every Book Here Had a Life Before You", alley/wandering narrative
- v2→v3: Genre number sizing 2.5→1.75rem, removed non-clickable hover states, letter-spacing system check, review attr size bump
- v3→v4: Exterior Bastion Square photo break, scroll-margin, section-label → h2 gap standardized
- v4→v5: Hero h1 negative tracking (-0.02em), larger clamp range

### What worked
- Libre Baskerville + Space Grotesk: literary serif + modern sans pairing
- Forest green (#2C4A3E) as primary accent: literary, warm, not predictable blue
- "Look for the blue bicycle": hero headline that doubles as wayfinding and brand identity
- "The Bookshops Keep Disappearing. We're Still Here.": conviction-first about headline
- "Every Book Here Had a Life Before You": name section with emotional depth
- Hero body copy: "Most people don't find us on purpose. They find us because they wandered."
- Martlet press callout reinforcing the blue bicycle motif
- Exterior Bastion Square photo break before visit: editorial rhythm + location context
- Featured dark review card with the "treasure trove" Google review
- 2x2 genre grid: scannable, not overwhelming

### What limited score
- AI photography ceiling (~8.5 with AI, ~9+ with real photos)
- Two consecutive rounds at 8.5 = plateau

---

## Build 26 — Mexican House of Spice [10-round-visual-test]
- **Category:** Specialty Latin American Grocery Store
- **City:** Victoria, BC (1412 A Douglas St)
- **Date:** 2026-03-18
- **Model:** claude-opus-4-6 (subagent)
- **Agent:** Lucy (subagent)
- **Panel:** Rounds 1-2: Norman + Krug | Round 3: Ive + Jobs | Rounds 4-10: Norman + Vignelli + Spiekermann

### Business
Real Victoria BC business. No website — Facebook (3,724 likes) + Instagram location. Victoria's oldest Latin American grocery store. Founded 2011 by Maritza Sanchez (Guatemalan, mother from Chiapas, Mexico). Moved to Victoria 37 years ago. Stocks foods from Mexico, South America, Africa, Jamaica. 4.6 stars, 200+ Google reviews. Featured in Capital Daily + Tasting Victoria. Community-made piñatas, Indigenous art, immigrant baker program. Families drive from Tofino.

### Design
- **Typography:** Playfair Display 600/700 (display/serif) + Space Grotesk 400/500/600 (body/UI)
- **Palette:** Warm cream #FAF5EE base, terracotta #C4572A, warm brown #8B6F4E, gold #D4A843, sage #6B7F5E, warm black #1A1410, alt bg #F0EBE3
- **Layout:** Terracotta-bordered hero → trust bar → asymmetric photo strip (2:1) → about with quote lead → 2x2 product cards → name meaning section (120px padding) → community quote → reviews with featured dark card → exterior photo → visit + hours → CTA band → footer
- **Images:** 4 AI-generated (no interior shots) — dried chilies, spice bowls, piñatas, storefront

### Scores
| Round | Norman | Critic 2 | Critic 3 | Avg | Visual | Notes |
|-------|--------|----------|----------|-----|--------|-------|
| v0 | 7.0 | 6.5 (Krug) | — | 6.75 | 8.2 | Norman+Krug — long hero headline, 6 cards too many |
| v1 | 7.5 | 7.5 (Krug) | — | 7.5 | — | Norman+Krug — shorter headline, 4 cards, better trust stat |
| v2 | 8.0 | 7.0 (Ive) | 7.0 (Jobs) | 7.0 | — | Ive+Jobs — needs conviction, immigrant story front and center |
| v3 | 8.0 | 7.5 (Vignelli) | 7.5 (Spiekermann) | 7.67 | — | Gauntlet entry — inline styles, tracking fixes |
| v4 | 8.0 | 8.0 (Vignelli) | 7.5 (Spiekermann) | 7.83 | — | Trust bar readability, review text size |
| v5 | 8.5 | 8.0 (Vignelli) | 8.0 (Spiekermann) | 8.17 | — | Tighter find spacing, community quote line-height |
| v6 | 8.5 | 8.0 (Vignelli) | 8.0 (Spiekermann) | 8.17 | — | WILDCARD: Name section "It Says Mexico. It Means Everywhere." |
| v7 | 8.5 | 8.5 (Vignelli) | 8.5 (Spiekermann) | 8.5 | 8.5 | Bigger hero h1, featured dark review card, exterior photo break |
| v8 | 8.5 | 8.5 (Vignelli) | 8.5 (Spiekermann) | 8.5 | — | Final polish: no inline styles, proper CSS classes |

### Key improvements
- v0→v1: Shorter hero headline "A Taste of Home", consolidated 6→4 product cards, replaced Facebook trust stat with "Island-Wide"
- v1→v2: Hero rewrite with conviction "We Didn't Have the Food We Grew Up With", terracotta left border on hero content
- v2→v3: Eliminated inline styles, fixed letter-spacing system, card number opacity bump
- v3→v4: Trust bar tracking fix, review text size to 1rem, h2 consistency
- v4→v5: Tighter find section spacing (48→40px), community quote line-height 1.4→1.5
- v5→v6: WILDCARD — Name section "It Says Mexico. It Means Everywhere." at 120px padding
- v6→v7: Bigger hero h1 (4vw→5vw), featured dark review card with translateY(-8px), exterior storefront photo break
- v7→v8: CSS class for exterior photo, hours-different class for Sunday, no remaining inline styles

### What worked
- Playfair Display + Space Grotesk: warm editorial pairing, not Instrument Serif + Inter
- Terracotta palette with warm cream base: culturally resonant without stereotyping
- "We Didn't Have the Food We Grew Up With": hero with conviction based on owner's actual story
- Terracotta left-border hero content: proven geometric signal (from Tourist/Wairua)
- Name section "It Says Mexico. It Means Everywhere.": uniquely-the-brand personality moment
- 120px name section padding: drama through whitespace, makes a design statement
- Storefront exterior photo break before visit: editorial rhythm break + wayfinding
- Featured dark review card with subtle lift: visual hierarchy in reviews grid
- "Island-Wide — Families from Tofino to Victoria": better trust stat than follower count
- Three-level letter-spacing system (0.04/0.08/0.14em): mandatory before gauntlet

### What limited score
- AI photography ceiling (~8.5 with AI, ~9+ with real photos)
- Two consecutive rounds at 8.5 = plateau
- Visual score aligned with panel score at 8.5

---

## Build 25 — Wairua Cafe [10-round-test-4]
- **Category:** Coffee Shop / Café
- **City:** Victoria, BC (1040 North Park St #2)
- **Date:** 2026-03-18
- **Model:** claude-opus-4-6 (subagent)
- **Agent:** Lucy (subagent)
- **Panel:** Rounds 1-2: Norman + Krug | Round 3: Ive + Jobs | Rounds 4-10: Norman + Vignelli + Spiekermann

### Business
Real Victoria BC business. No website — Instagram only (@wairuacafe, 4K+ followers). Opened March 2025 by Wilson and Hanisa North (husband/wife). Wilson is from New Zealand — "Wairua" is Māori for "one's spirit." Coffee, matcha, pastries. 4.9 stars, 155+ Google reviews. Featured on CHEK News "Order Up." LGBTQ+ inclusive. North Park neighbourhood.

### Design
- **Typography:** Cormorant 600/700 (display/serif) + Space Grotesk 400/500/600 (body/UI)
- **Palette:** Warm cream #FAF6F1 base, earth tones #8B7355, clay accent #C4A882, sage #7A8B6F, deep #1A150F
- **Layout:** Sage-bordered hero → trust bar → asymmetric photo strip (2:1) → about with quote lead → name meaning section (extra padding) → sage press callout → split menu (sticky photo left + items right) → reviews with featured dark card → exterior photo → visit + map → CTA band → footer
- **Images:** 4 AI-generated (no interior shots) — latte art, matcha, exterior storefront, pastries overhead

### Scores
| Round | Norman | Critic 2 | Critic 3 | Avg | Notes |
|-------|--------|----------|----------|-----|-------|
| v0 | 7.0 | 6.5 (Krug) | — | 6.75 | Norman+Krug — CTA too wide, COVID headline |
| v1 | 7.5 | 7.5 (Krug) | — | 7.5 | Norman+Krug — headline fix, price context, exterior photo |
| v2 | 7.5 | 7.0 (Ive) | 7.0 (Jobs) | 7.17 | Ive+Jobs — needs more Māori identity, stronger hero |
| v3 | 8.0 | 7.5 (Krug) | — | 7.75 | Featured dark review card, hero sage border |
| v4 | 8.0 | 8.0 (Krug) | — | 8.0 | Sage press callout, about quote leads |
| v5 | 8.0 | 7.5 (Vignelli) | 7.5 (Spiekermann) | 7.67 | Gauntlet entry — inline styles, tracking fixes |
| v6 | 8.0 | 8.0 (Vignelli) | 7.5 (Spiekermann) | 7.83 | Quote attribution class, footer size, matcha badge |
| v7 | 8.5 | 8.0 (Vignelli) | 8.0 (Spiekermann) | 8.17 | Name section extra padding, photo strip height |
| v8 | 8.5 | 8.5 (Vignelli) | 8.5 (Spiekermann) | 8.5 | h2 tracking, noscript fallback |
| v9 | 8.5 | 8.5 (Vignelli) | 8.5 (Spiekermann) | 8.5 | WILDCARD: split menu with sticky photo |

### Key improvements
- v0→v1: Renamed COVID headline, added price context, exterior photo break
- v1→v2: Hero sage border, shorter subtitle, CHEK trust stat
- v2→v3: Featured dark review card, hero line-break for subtitle
- v3→v4: Sage press callout section, about quote leads right column
- v4→v5: Eliminated inline styles, fixed hero tracking, menu h3 bump
- v5→v6: Quote attribution class, footer copy size, "Popular" matcha badge
- v6→v7: Name section 120px padding, photo strip 420px, scroll-margin
- v7→v8: h2 negative tracking, noscript fallback
- v8→v9: WILDCARD — split menu with sticky matcha photo + Instagram CTA

### What worked
- Cormorant + Space Grotesk: warm serif + modern sans pairing, not Instrument Serif + Inter
- Sage green (#7A8B6F) as secondary accent for wellness/spirit vibes — earned by the brand
- Sage-bordered hero content: subtle geometric signal that elevates from template
- Name meaning section with extra padding (120px): drama through whitespace
- Split menu with sticky photo left column: editorial depth in informational section
- Press callout in sage: color rhythm break that also serves as credibility anchor
- "Popular" badge on signature drink: surfaces the brand's personality from reviews
- Featured dark review card: visual hierarchy in reviews grid
- Trust bar "Open 7 / Days a Week" > "Est. 2025": more useful pre-visit info
- About section leading with owner's own words: immediate personality

### What limited score
- AI photography ceiling (~8.5 with AI, ~9+ with real photos)
- Two consecutive rounds at 8.5 = plateau
- Panel noted: real photography and microinteractions needed for 9+

---

## Build 24 — Ditch Records & CDs [10-round-test-3]
- **Category:** Independent Record Store
- **City:** Victoria, BC (784 Fort St)
- **Date:** 2026-03-18
- **Model:** claude-opus-4-6 (subagent)
- **Agent:** Lucy (subagent)
- **Panel:** Rounds 1-2: Norman + Krug | Round 3: Ive + Jobs | Rounds 4-10: Norman + Vignelli + Spiekermann

### Business
Real Victoria BC business. No website — Facebook + Instagram only. Victoria's largest independent record store. Founded by a Beatles-obsessed teenager. 784 Fort St. 4.8 stars, 650+ Google reviews. Sells new/used vinyl, CDs, cassettes, show tickets, music books, posters.

### Design
- **Typography:** Syne 800 (display) + Syne 700 (section heads) + Space Grotesk 400/500 (body/UI)
- **Palette:** Warm off-white #FAF8F5 base, near-black #1A1A1A, accent #D4440F (vinyl label red-orange), alt bg #F0ECE6
- **Layout:** Light editorial — generous whitespace + big type, asymmetric photo strip (2:1 grid), 2x2 carry grid, "Crate Digger's Code" personality section
- **Images:** 4 AI-generated (no interior shots) — storefront, vinyl crates, vinyl flatlay, cassettes

### Scores
| Round | Norman | Critic 2 | Critic 3 | Avg | Notes |
|-------|--------|----------|----------|-----|-------|
| v0 | 7.0 | 6.5 (Krug) | — | 6.75 | Norman+Krug |
| v1 | 7.5 | 7.5 (Krug) | — | 7.5 | Norman+Krug — CTA fix, simplified carry |
| v2 | 7.5 | 7.0 (Ive) | 7.0 (Jobs) | 7.17 | Ive+Jobs direction — hero story, personality |
| v3 | 7.5 | 7.0 (Vignelli) | 7.0 (Spiekermann) | 7.17 | Gauntlet entry — typography fixes |
| v4 | 7.5 | 7.5 (Vignelli) | 7.5 (Spiekermann) | 7.5 | Gauntlet recovery |
| v5 | 8.0 | 7.5 (Vignelli) | 7.5 (Spiekermann) | 7.67 | Hero sub size, borderless hours |
| v6 | 8.5 | 8.0 (Vignelli) | 8.0 (Spiekermann) | 8.17 | Trust bar tracking, footer size |
| v7 | 8.5 | 8.5 (Vignelli) | 8.5 (Spiekermann) | 8.5 | Asymmetric photo strip wildcard |
| v8 | 8.5 | 8.5 (Vignelli) | 8.5 (Spiekermann) | 8.5 | Crate Digger's Code section |

### Key improvements
- v0→v1: CTA from "Call" to "Get Directions", simplified carry from 6→4 items, phone as secondary inline
- v1→v2: Hero rewritten with Beatles origin story, about copy sharpened, quote made punchier
- v2→v3: Hero label shortened, carry numbers redesigned (small accent metadata), grid gaps unified to 4px
- v3→v4: Hero headline refined to single flowing sentence
- v4→v5: Hero sub reduced to 1.125rem, hours table borderless
- v5→v6: Trust bar number tracking, footer copy size bump
- v6→v7: WILDCARD — photo strip from equal 3-col to asymmetric 2:1 grid (biggest single-round jump)
- v7→v8: "The Crate Digger's Code" personality section with Roman numerals

### What worked
- Syne 800 for display: enough indie character without being a novelty font
- Light palette with warm off-white base: different from recent dark builds, lets photos pop
- "One kid's obsession became Fort Street's institution": origin story as hero headline
- Asymmetric photo strip (2fr + 1fr stacked): editorial quality, confirmed lesson from previous builds
- "Crate Digger's Code" section: uniquely "Ditch" personality moment, Roman numerals differentiate from carry numbers
- 2x2 carry grid with small accent-colored metadata numbers: cleaner than 3x2 with decorative large numbers
- Borderless hours table: cleaner, spacing alone separates rows
- Accent red-orange (#D4440F) reads as vintage vinyl label color — brand-appropriate
- "Get Directions" as primary CTA for walk-in retail business (over "Call")
- Trust bar with tight tracking on display numbers

### What limited score
- AI photography ceiling (~8.5 with AI, ~9+ with real photos)
- Two consecutive rounds at 8.5 = plateau
- Panel noted: real photography and microinteractions needed for 9+

---

## Build 23 — Tourist Wine Bar [10-round-test-2]
- **Category:** Natural Wine Bar
- **City:** Victoria, BC (1002 Blanshard St)
- **Date:** 2026-03-18
- **Model:** claude-sonnet-4-6 (subagent)
- **Agent:** Lucy (subagent)
- **Panel:** Rounds 1-2: Norman + Krug | Round 3: Ive + Jobs | Rounds 4-10: Norman + Vignelli + Spiekermann

### Business
Real Victoria BC business. Website was literally just a street address (touristwinebar.com). Active Instagram @touristwinebar. Natural wine bar, minimalist aesthetic, rotating small plates menu, weekly Sunday Sandwich ritual, incense and millennial vibes.

### Design
- **Typography:** Cormorant Garamond (italic headlines) + JetBrains Mono (labels, data, prices)
- **Palette:** Near-black #0D0C0A base, warm off-white #E8E2D9, wine red #8B2533, amber gold #C89B4A
- **Layout:** Dark editorial — hero with left gold border, asymmetric gallery (2fr/1fr), sticky wine section with image
- **Images:** 4 AI-generated (no interior shots) — exterior, wine bottles, small plates, wine pour

### Scores
| Round | Norman | Critic 2 | Critic 3 | Avg | Notes |
|-------|--------|----------|----------|-----|-------|
| v0 | 7.0 | 6.5 (Krug) | — | 6.75 | Norman+Krug |
| v1 | 7.5 | 7.5 (Krug) | — | 7.5 | Norman+Krug |
| v2 | 7.5 | 7.0 (Ive) | 7.0 (Jobs) | 7.17 → 7.25 | Ive+Jobs direction |
| v3 | 7.5 | 7.0 (Vignelli) | 7.5 (Spiekermann) | 7.33 | Gauntlet entry |
| v4 | 8.0 | 7.5 (Vignelli) | 7.5 (Spiekermann) | 7.67 | |
| v5 | 8.0 | 8.0 (Vignelli) | 8.0 (Spiekermann) | 8.0 | |
| v6 | 8.5 | 8.5 (Vignelli) | 8.5 (Spiekermann) | 8.5 | |
| v7 | 8.5 | 8.5 (Vignelli) | 8.7 (Spiekermann) | 8.57 | |
| v8 | 8.5 | 8.7 (Vignelli) | 8.7 (Spiekermann) | 8.63 | Final |

### Key improvements
- v0→v1: Fixed CTA honesty (Email to Reserve vs Reserve), moved gallery after menu, Sunday Sandwich callout
- v1→v2: Hero manifesto ("Wine should surprise you"), removed Mon-Tue closed from hours, wine belief statement
- v2→v3: Letter-spacing system (3 values), section label proportion, review card gap
- v3→v4: Fixed double-italic menu headline, gallery reverted to disciplined 2fr/1fr, full day names in hours
- v4→v5: About section with Tourist name origin story, hero left-border gold accent, section label proximity
- v5→v6: Wine section with image + sticky left column, reviews featured center card in wine-red
- v6→v7: Footer tagline increase, about quote swapped to brand manifesto
- v7→v8: Map iframe dark theme fix, wine section Instagram CTA, increased gold border opacity

### What worked
- Cormorant Garamond italic + JetBrains Mono: legitimate typographic identity, not a formula
- Hero manifesto > description: "Wine should surprise you" immediately creates a point of view
- Reviews featured center card in wine-red: single best design decision of the 10 rounds
- Sunday Sandwich callout as brand ritual: most distinctive personality moment
- Left gold border on hero content: geometric decision that elevates from "pleasant" to "designed"
- About quote as brand philosophy ("You're never supposed to know everything. You're just supposed to stay open."): transformed the about section from generic to character-defining
- Sticky wine left column with image: editorial depth without decoration
- Wine Instagram CTA ("The list changes constantly. Follow @touristwinebar"): social proof + action in one line

### Final: v8 → index.html
### Score ceiling: 8.63 (expected without real photography)

---

## Build 22 — Phillips Brewing & Malting Co. [10-round-test]
- **Category:** Craft Brewery
- **City:** Victoria, BC (2010 Government Street)
- **Tag:** [10-round-test]
- **Typography:** Archivo Black (display) + DM Mono (labels) + DM Sans (body)
- **Palette:** Dark industrial — charcoal/black + amber/gold accent
- **Images:** 5 AI-generated (exterior, tanks, beer close-up, flight, barley)
- **Rounds:** 10
- **Score progression:** 7.25 → 7.65 → 6.75 (direction check) → 7.33 → 7.77 → 7.87 → 8.07 → 8.20 → 8.27 → 8.27
- **Final score:** 8.27 (Norman 8.3, Vignelli 8.3, Spiekermann 8.2)
- **Key moves:**
  - Round 3 (Ive/Jobs direction): flagged the page needed more soul/drama → boosted hero opacity, rewrote origin as timeline, featured beer card with amber border
  - Round 7 (WILDCARD): replaced generic community pillars with split ethos section ("We Find Inspiration Through Fermentation" + numbered values). Biggest score jump.
  - Round 8: SVG stars, beer photo in visit section for warmth
  - Rounds 9-10: precision — timeline marker sizing, letter-spacing calibration, scroll-margin
- **Saved to:** `demos/phillips-brewing-10round/`

## Build 20 — Popular Nails By Bella
- **Category:** Nail Salon / Beauty
- **City:** Victoria, BC (1605 Douglas Street)
- **Tag:** [salon-test]
- **Date:** 2026-03-17
- **Data sources:** Instagram (@bella_nailsalon.vic), Facebook (175 likes), Google (4.9 stars, 759+ reviews), Birdeye, BeautyNailHairSalons (Facebook posts with pricing), Yelp, BBB, vicnews directory
- **Images:** 5 AI-generated (nails hero, nail art detail, product close-up, tools overhead, exterior) — NO interior shots per rules
- **Layout:** Split hero (text left, nails photo right) → dark trust bar → philosophy quote → 3×2 services grid (featured dark card centre) → asymmetric gallery (2:1 large + 2 stacked) → team → experience split (exterior photo + perks grid) → reviews → signature packages → location + map → CTA band → footer
- **Creative approach:** Rose/cream/gold palette for nail salon warmth. "Your nails, our art" hero headline. Philosophy quote captures the actual experience: massage chairs, complimentary coffee. "The Little Things" section surfaces real differentiators from reviews. Numbered service cards (01-06) instead of icons. Instrument Serif + Inter. Entrance animation hero only.
- **Versions:** v0 (baseline) → v1 (honest specials→packages, review attribution, icon cleanup) → v2 (removed How It Works, numbered service cards, exterior photo) → v3 (personality: better philosophy quote, experience section, bolder review header) → v4 (asymmetric gallery replaces 3-column strip) → v5 (Gauntlet: `--section-pad` system, `.accent-em` class, service icon CSS, blockquote scale refinement)
- **Scores:**
  - Round 1 (Norman + Krug): 7.5 → Fixed specials framing, review attribution, icon cleanup
  - Round 2 (Norman + Krug): 7.75 → Removed unnecessary How It Works, cleaner layout
  - Round 3 (Ive + Jobs): 7.5 → Direction reset; added personality via experience section
  - Round 4 (Ive + Jobs): 7.95 → Asymmetric gallery, bolder review headline
  - Round 5 (Norman + Vignelli + Spiekermann): 8.07 → Gauntlet polish, system variables
- **Final score:** 8.07
- **Notes:** First dedicated nail salon build. Rose/cream palette works beautifully for this category. Key insight: nail salons have real differentiators that usually live in their reviews (massage chairs, complimentary drinks, birthday extras) — surfacing those in "The Little Things" was the score driver. The 750+ reviews at 4.9 stars was used as a brand headline, not just a trust bar stat. Numbered service cards (01-06 in faint serif) are cleaner than SVG icons for this category. Removing the "How It Works" section was the right call for a simple walk-in service business.

## Build 19 — Botched Vintage & Apparel
- **Category:** Vintage Clothing / Curated Retail
- **City:** Victoria, BC (1044A Fort Street)
- **Tag:** [retail-test]
- **Date:** 2026-03-17
- **Data sources:** Instagram (@botched.vintage, 2.4K followers), Google (5.0 rating), Daily Hive Victoria feature, thrift-stores.ca listing, local blog reviews, Vintage After Death directory
- **Images:** 4 AI-generated (clothing rack, storefront exterior, accessories flat lay, denim detail) — NO interior shots per rules
- **Layout:** Centered type-driven hero → 3-image editorial strip → press quote (Daily Hive) → asymmetric about (5fr/7fr) → column-divided categories (dark bg) → full-bleed accessories photo → trust bar → 2x2 review grid → visit section with map → footer
- **Creative approach:** Cream/brass/charcoal palette — warm, editorial, premium vintage. "Already worn in." headline. Centered hero with big type (clamp 56-120px) instead of split layout. 3-image strip below hero creates editorial magazine feel. Categories as vertical column-divided list instead of card grid. Instagram is primary CTA throughout (matches how this business operates). Instrument Serif + Inter pairing. Noise texture overlay.
- **Versions:** v0 (baseline split hero) → v1 (added Instagram CTAs, fixed "Men's & Women's" pseudo-category) → v2 (rebuilt: centered type hero, 3-image strip, asymmetric about, column categories, press quote early) → v3 (Gauntlet: fixed wrong Facebook link, butted image strip, opacity 0.35 numbers, unified line-height, letter-spacing discipline)
- **Scores:**
  - Round 1 (Norman + Krug): 7.25 → Instagram CTA priority, category cleanup
  - Round 2 (Norman + Krug): 7.65 → Improved CTA placement
  - Round 3 (Ive + Jobs): 7.9 → Rebuilt layout, centered hero, editorial strip
  - Round 4 (Norman + Vignelli + Spiekermann): 7.57 → Gauntlet drop, typographic fixes needed
  - Round 5 (Norman + Vignelli + Spiekermann): 7.83 → Recovery, clean typography system
- **Final score:** 7.83
- **Notes:** First retail/vintage build. Key decisions: (1) Instagram as primary CTA matches the business model — no booking, no ecommerce, just follow + visit. (2) Centered type hero was more distinctive than split layout for a fashion brand. (3) Column-divided categories felt more editorial than card grid. (4) Press quote from Daily Hive placed early gives immediate third-party credibility. (5) Wrong Facebook link caught — Vintage Funk Emporium is a different business. Lesson: verify every social link.

## Build 18 — Crows Nest Tattoo Atelier
- **Category:** Tattoo Studio / Creative Studio
- **City:** Victoria, BC (1672 Douglas St)
- **Tag:** [creative-test]
- **Date:** 2026-03-17
- **Data sources:** Instagram (@crowsnest_ink), Facebook (172 likes), Fresha (hours, services), InkRoster (reviews, artist details), Google (5.0 rating)
- **Images:** 4 AI-generated (crane tattoo close-up, equipment detail, storefront exterior, design sketch) — NO interior shots per rules
- **Layout:** Split hero (text left, tattoo close-up right) → trust bar → staggered artist cards (later equalized) → 4-step process → full-bleed photo strip → name-meaning section (amber left border) → 2x2 review grid (alternating bg) → 2-column services (tattoo + piercing) → visit section with map → footer
- **Creative approach:** Dark moody palette (black/charcoal/amber). "Your story, permanently told." headline. "The Name" section explains crow's nest = highest point on a ship. Artist cards with personality copy and Instagram links. LGBTQ+ welcome integrated into hero body text naturally. Instrument Serif + Inter pairing. Entrance animations on hero only. Noise texture overlay.
- **Versions:** v0 (baseline) → v1 (equalized artist cards, moved LGBTQ+ to hero, better review attribution) → v2 (simplified brand quote, cleaner service meta) → v3 (name-meaning section, artist links, personality in descriptions) → v4 (quote alignment fix) → v5 (Gauntlet: letter-spacing system, step-number sizing, quote-block composition)
- **Scores:**
  - Round 1 (Norman + Krug): 7.5 → Fixed staggered cards implying hierarchy, LGBTQ+ placement
  - Round 2 (Norman + Krug): 7.75 → Better attributions, cleaner service meta
  - Round 3 (Ive + Jobs): 7.65 → Name section, artist personality, bolder identity
  - Round 4 (Norman + Vignelli + Spiekermann): 7.83 → Gauntlet entry, quote composition, letter-spacing fixes
  - Round 5 (Norman + Vignelli + Spiekermann): 8.07 → Final polish
- **Final score:** 8.07
- **Notes:** First tattoo studio build. Dark palette with amber is a natural fit. The "name meaning" section (proven strong signal from lessons) works especially well here — a crow's nest reference adds nautical/adventurous character. Key lesson: don't stagger equal-weight items (artist cards) as it implies ranking. LGBTQ+ identity is best integrated as natural copy, not a trust-bar stat. Full-bleed photo strip between content sections creates editorial rhythm break.

## Build 17 — Bri the Groomer
- **Category:** Pet Services / Dog Grooming
- **City:** Victoria, BC (#10 - 3170 Tillicum Rd)
- **Tag:** [pet-services-test]
- **Date:** 2026-03-17
- **Data sources:** Facebook (94% recommend, 15 reviews), Yelp (hours, address, phone), BBB (A rating), LocalCanada directory
- **Images:** 5 AI-generated (golden retriever portrait, fluffy white dog, happy dog in park, gentle paw care, corgi puppy) — NO interior shots per rules
- **Layout:** Asymmetric hero (text + dog portrait) → trust bar → dark philosophy quote → editorial services (numbered list + sticky sidebar image) → 3-step process → masonry photo gallery → review cards (alternating bg) → location with map → warm CTA band → footer
- **Creative approach:** Warm cream/bark/gold palette. "Your dog deserves undivided attention" headline sells emotion, not feature. Philosophy section punches hard: "No cages. No kennels. No assembly line." Masonry gallery (2fr 1fr 1fr) instead of equal grid. Featured "Most Popular" service with gold badge. Instrument Serif + Inter pairing. Entrance animations on hero only.
- **Versions:** v0 (baseline) → v1 (fixed gallery reuse, honest review attribution, prominent pricing callout) → v2 (stronger philosophy copy, masonry gallery) → v3 (bolder headline, signature service highlight, warm trust bar) → v4 (warm CTA band with radial glow) → v5 (Gauntlet fixes: proper CSS classes, h1 size reduction, badge separation)
- **Scores:**
  - Round 1 (Norman + Krug): 7.0 → Fixed fabricated review attribution, gallery reuse
  - Round 2 (Norman + Krug): 7.5 → Better attribution, pricing callout visible
  - Round 3 (Ive + Jobs): 7.65 → Stronger philosophy, masonry gallery
  - Round 4 (Ive + Jobs): 7.9 → Better headline, service highlight
  - Round 5 (Norman + Vignelli + Spiekermann): 8.0 → Gauntlet entry + fixes
- **Final score:** 8.0
- **Notes:** First pet services build. The 1:1 personal grooming model is a natural differentiator — the whole site narrative builds around it. "No cages. No kennels. No assembly line." was the memorable moment. Warm gold accent works well for pet/grooming. Pricing linked to social (call/Facebook) since no verified prices available. Reviews attributed as "Via Facebook" rather than fabricating exact quotes.

## Build 16 — Don Williams Lawnmower Clinic
- **Category:** Trades / Small Engine Repair
- **City:** Victoria, BC (4270 Glanford Ave)
- **Tag:** [trades-test]
- **Date:** 2026-03-17
- **Data sources:** Facebook (140 likes), Yellow Pages (2 reviews, 5/5), whodoyou.com, victoria-bc.com directory
- **Images:** 5 AI-generated (blade detail, exterior, hands/carburetor, tools overhead, mower on grass) — NO interior shots per rules
- **Layout:** Type-driven opening (no hero image) → trust bar → split-column craft story → asymmetric dark services section (2-col grid + photo) → photo strip → promise statement → reviews → exterior photo → location/map → footer
- **Creative approach:** Led with bold headline "Half the price. Twice the care." — type-driven opening inspired by Tarboosh's success. Services presented in asymmetric layout with hands-detail photo alongside a 2x3 numbered grid on dark background. Olive/cream/gold palette for warm trades aesthetic.
- **Versions:** v0 (baseline) → v1 (removed redundant quote, numbered services, added CTA) → v2 (asymmetric services layout with photo, reworked promise, exterior photo) → v3 (added exterior panoramic, mower in photo strip) → v4 (Gauntlet fixes: type scale, letter-spacing system, inline styles)
- **Scores:**
  - Round 1 (Norman + Krug): 7.0 → Fixed redundant quote, cleaned icons
  - Round 2 (Norman + Krug): 7.5 → Improved
  - Round 3 (Ive + Jobs): 7.25 → Asymmetric layout, promise rewrite
  - Round 4 (Norman + Vignelli + Spiekermann): 7.43 → Gauntlet entry drop, expected
  - Round 5 (Norman + Vignelli + Spiekermann): 7.83 → Final
- **Final score:** 7.83
- **Notes:** Score ceiling without real photography confirmed again around 8.0. The type-driven opening works well for a one-man trades shop — the name and value prop ARE the brand. Asymmetric services layout (grid + photo) is more editorial than a standard 3x2 grid.

## Build 15 — Tarboosh
- **Category:** Food Truck / Middle Eastern Street Food
- **City:** Esquimalt, Victoria, BC (900 Carlton Terrace)
- **Date:** 2026-03-17
- **Agent:** Lucy (opus subagent, food-truck-test)
- **Model:** claude-opus-4-6
- **Fictional:** No (real business — Instagram @tarboosh_victoria, no website)
- **Images:** 5 AI-generated images (falafel, shawarma, truck exterior, pita, sides) via Gemini Flash
- **Output:** /projects/auto-sites/demos/tarboosh/

### Scores
| Round | Panel | Score | Key Change |
|-------|-------|-------|------------|
| v0 baseline | Norman + Krug | 7.25 | Type-driven opening, editorial layout, no hero image |
| v1 | Norman + Krug | 7.8 | Fixed duplicate pita image, added StreetFoodApp link, 5th image |
| v2 | Ive + Jobs | 7.4 | Direction drop — needed distinctiveness, trust bar too generic |
| v3 | Ive + Jobs | 7.75 | Reworked trust bar, food strip heading, entrance animation |
| v4 Gauntlet | Norman + Vignelli + Spiekermann | 7.87 | Expected drop — padding rhythm, type scale fixes needed |
| v4 final | Gauntlet | **8.03** | Fixed section padding system (96/64), type scale, line-height discipline |

### Layout Innovation
- Type-driven opening (no hero image) → full-width truck photo → editorial story split → dark "name meaning" quote → food photo strip → cream menu → trust bar → press feature → dark "find us" → footer
- NOT standard hero→about→menu→reviews→footer
- Fez SVG icon as brand element in the name-meaning section
- Gold corner accent on story photo
- Alternating light/dark sections create magazine rhythm

### Key Decisions
- Instagram as primary CTA (food truck with variable location — social is the real communication channel)
- No prices listed (not verifiable) — honest link to Instagram for current pricing
- CHEK News "Order Up" quote as credibility anchor
- StreetFoodApp link alongside Instagram for location tracking
- Egyptian heritage angle as the emotional hook
- Mother & son story from verified CHEK News article

### Business Data Sources
- CHEK News "Order Up" feature (Sept 2025)
- Esquimalt business directory (whyesquimalt.ca)
- StreetFoodApp listing
- Instagram @tarboosh_victoria bio

---


## Build 14 — Los Panas Kitchen
- **Category:** Food Truck / Venezuelan Street Food
- **City:** Victoria, BC (Market Square / 1910 Store St)
- **Date:** 2026-03-17
- **Agent:** Lucy (opus subagent, food-truck-test)
- **Model:** claude-opus-4-6
- **Fictional:** No (real business — Instagram @lospanaskitchen, Facebook, no website)
- **Images:** 4 AI-generated images (arepa hero, patacon, truck exterior, ingredients) via Gemini Flash
- **Output:** /projects/auto-sites/demos/los-panas-kitchen/

### Scores
| Round | Panel | Score | Key Change |
|-------|-------|-------|------------|
| v0 baseline | Norman + Krug | 7.25 | Initial build — editorial magazine layout, strong photo integration |
| v1 | Norman + Krug | 7.9 | +Hero CTAs (Instagram + menu), +seasonal ribbon, tightened copy |
| v2 | Ive + Jobs | 7.65 | Score reset — Ive/Jobs want more personality |
| v3 | Ive + Jobs | 8.05 | +"Name meaning" brand moment, stronger story headline, cleaner ribbon |
| v4 Gauntlet | Norman + Vignelli + Spiekermann | 7.73 | Expected drop — typography consistency, opacity, line-height fixes needed |
| v4 final | Gauntlet | **8.07** | Unified line-height (1.65), fixed opacity (60%/80%), label sizing, LS system |

### Layout Innovation
- Editorial magazine flow (not standard hero→about→menu→reviews→footer)
- Narrative structure: hero → seasonal context → food education → trust → menu → photo break → name meaning → review → story → location
- "Name meaning" section as personality/brand moment
- Dark menu section creates dramatic visual shift
- Green pull-quote section for color rhythm break

### Key Decisions
- No prices shown — not verifiable from their current sources, linked to Instagram instead
- Seasonal status prominent via gold ribbon immediately after hero
- Instagram as primary CTA (appropriate for seasonal mobile vendor)
- Take-home arepas at Market on Yates highlighted as year-round option
- Owner Carlos Bermudez's story woven into the narrative naturally

---


## Build 13 — Kid Sister Ice Cream
- **Category:** Ice Cream / Frozen Desserts
- **City:** Victoria, BC (Esquimalt Road + Cook St Village mini outlet)
- **Date:** 2026-03-17
- **Agent:** Lucy (sonnet subagent, sonnet-imagegen-test)
- **Model:** claude-sonnet-4-6
- **Fictional:** No (real business — kidsistericecream.com, Instagram @kidsistericecream)
- **Images:** 4 AI-generated images (hero, about, flavours, atmosphere) via Gemini Flash
- **Output:** /projects/auto-sites/demos/kid-sister-v2/

### Scores
| Round | Panel | Score | Key Change |
|-------|-------|-------|------------|
| v0 baseline | Norman + Krug | 6.5 | Initial build |
| v1 | Norman + Krug | 7.5 | +Trust bar, +differentiator repositioned, +Cook St as equal location, +atmosphere photo in reviews |
| v2 | Ive + Jobs | 7.8 | +Brand headline ("Small Batches. *Big Flavours.*"), +larger swatches, +sharpened copy, +taller differentiator |
| v3 Gauntlet | Norman + Vignelli + Spiekermann | 7.93 | +CSS letter-spacing system (3 vars), removed unused CSS, +flavours photo strip |
| v3 final | Gauntlet (patch) | **8.07** | Fixed hero-badge + stat-label to use LS vars |

### Key Lessons
- Gemini Flash image generation worked well — 4 images in ~60s, good quality
- Pink/berry palette is ideal for ice cream/dessert brands
- Real AI photography elevates quality noticeably vs CSS gradient placeholders
- "How It Works" is NOT needed for simple walk-in businesses like ice cream shops
- Two-location businesses need equal-weight location cards, not footnotes

## Build 12 — Friends & Family Bake
- **Category:** Bakery (Filipino)
- **City:** Victoria, BC (Chinatown, Fantan Alley)
- **Date:** 2026-03-17
- **Agent:** Lucy (opus subagent, opus-test-1)
- **Model:** claude-opus-4-6
- **Fictional:** No (real business data from Tourism Victoria, Reddit, Instagram, Facebook)

### Business Data (Real)
- Type: Filipino bakery (VIHA-approved)
- Location: Unit 101, 3 Fantan Alley (Along Pandora), Victoria, BC V8W 3G9
- Phone: (587) 439-1788
- Instagram: @friendsfamilybake.canada (1,129 followers)
- Facebook: Friends & Family Bake (1,131 likes)
- Tagline: "Together, We can bake this world a better place."
- Known items: Ube Ensaymada (signature), Pandesal, Hopia, Filipino donuts, Western baked goods
- Charity: Proceeds support Zoe Children's Home Foundation (Philippines)
- Community: 257 upvotes on Reddit rallying for reviews
- No website confirmed

### Review Scores
| Round | Panel | Avg | Notes |
|-------|-------|-----|-------|
| R1 | Norman+Krug+Ive | 7.0 | Solid baseline. Generic SVG icons, thin reviews section |
| R2 | Norman+Krug+Ive | 7.5 | Colour gradient swatches, beefed up reviews + stats bar |
| R3 | Norman+Krug+Ive | 7.83 | Scroll indicator, differentiator gold lines, about-image depth |
| R4 | Norman+Vignelli+Spiekermann (Gauntlet) | 7.67 | Gauntlet stricter — typography precision feedback |
| R5 | Norman+Vignelli+Spiekermann (Gauntlet) | 8.0 | Typography refined, footer structured, card spacing systematic |

### Key Design Decisions
- **Colour gradient swatches** (44px circles) to represent Filipino pastry items — ube purple, golden pandesal, mung green, terracotta donut
- **Warm earth palette** (cream/gold/terracotta/olive) matching Filipino bakery warmth
- **Honest reviews approach:** One real Reddit quote + one ensaymada mention + community stats (Instagram, Facebook, Reddit upvotes)
- **Giving-back callout** in about section with gold-bordered card — Zoe Children's Home Foundation
- **No fabricated hours** — links to Instagram for current hours (honest approach)
- **Gold accent throughout** — hero badge, trust bar highlights, section labels, CTA buttons

### Files
- `demos/friends-and-family-bake/index.html` (final v5)
- `demos/friends-and-family-bake/index-v0.html` through `index-v5.html` (iterations)


## Build 11 — One Mind and Body Wellness and Fitness
- **Category:** Fitness / Wellness (holistic)
- **City:** Victoria, BC (Greater Victoria, Sunriver area)
- **Date:** 2026-03-17
- **Agent:** Lucy (opus subagent, opus-test-2)
- **Model:** claude-opus-4-6
- **Fictional:** No (real business data from Facebook)

### Business Data (Real)
- Owner: Linda Watson, est. 2010 (Toronto → Victoria)
- Location: Rivers Edge Clubhouse, Sunriver, Greater Victoria, BC
- Phone: 778-587-1387
- Email: watsonlindac@gmail.com
- Facebook: facebook.com/OneMindandBody (334 likes)
- Services: Personal Training, Kickboxing, Self-Protection/Self-Defense, Buddha Camp (cardio/strength/mindful movement/meditation), 30-Day Challenges, Nutrition Coaching
- Pricing: Buddha Camp $10 drop-in, 30-Day Challenge $199 (early bird) / $249 regular
- Schedule: Buddha Camp Tues/Thurs 9:30 AM
- No website, Instagram not found — Facebook is primary social channel

### Scores
| Version | Reviewer 1 | Reviewer 2 | Reviewer 3 | Avg | Panel |
|---------|-----------|-----------|-----------|-----|-------|
| v0 | 7.5 (Norman) | 7.0 (Ive) | 7.5 (Krug) | 7.3 | Default |
| v1 | 7.5 | 7.0 | 7.5 | 7.3 | Default |
| v2 | 8.0 | 7.5 | 8.0 | 7.8 | Default |
| v3 | 8.0 | 8.0 | 8.0 | 8.0 | Default |
| v4 | 8.0 (Norman) | 8.0 (Vignelli) | 8.0 (Spiekermann) | 8.0 | Gauntlet |
| v5 | 8.0 | 8.0 | 8.0 | 8.0 | Gauntlet |

### Key Changes Per Round
- **v0→v1:** Fixed service card SVG icons (semantically appropriate: dumbbell, fighter, shield, bowl)
- **v1→v2:** Gold-to-sage gradient card hover borders, sage border-top on challenge card, Facebook community context in stats, gold divider line between sections
- **v2→v3:** Staggered animation delays on cards/steps, tighter trust bar, button active state refinement (100ms), hero subtitle typography refinement
- **v3→v4 (Gauntlet):** Fixed 2x2 service grid (was auto-fit), harmonized letter-spacing system (0.06/0.08em), equal about grid columns, simplified background cycling, matched nav/footer brand sizing
- **v4→v5:** Unified section padding (96px), body font-size explicit, grayscale font smoothing, noscript fallback, tighter footer, refined section subtitle sizing

### Gauntlet Notes
- Vignelli caught grid discipline issues (auto-fit → fixed 2x2), asymmetric columns, and background color overuse
- Spiekermann caught letter-spacing inconsistencies across label types and nav/footer brand mismatch
- Score ceiling remains at 8.0 — pushed but couldn't break through. Real photography and brand identity work needed for 9+
- The Gauntlet dropped score from 8.0 → 7.5 initially by catching system-level inconsistencies, then recovered to 8.0 after fixes

---


## Build 7 — Petal & Stem
- **Category:** Florist
- **City:** Brooklyn, NY (Park Slope)
- **Date:** 2026-03-16
- **Agent:** Lucy (sonnet-batch subagent)
- **Model:** claude-opus-4-6
- **Fictional:** Yes (invented business data)

### Business Data (Invented)
- Owner: Elena Marchetti, est. 2016
- Address: 247 5th Avenue, Brooklyn, NY 11215
- Phone: (718) 555-0147
- Hours: Mon-Fri 8-7, Sat 9-6, Sun 10-4
- Products: Bouquets ($45+), Grand arrangements ($95+), Dried ($55+), Plants ($35+), Wedding ($500+), Sympathy ($75+)
- Services: Same-day delivery ($12, free over $100), weekly subscription ($40/wk), weddings & events, corporate
- Palette: Olive/cream/terracotta — warm botanical

### Scores
| Version | Norman | Ive | Krug | Avg |
|---------|--------|-----|------|-----|
| v0 | 7.0 | 6.5 | 7.0 | 6.83 |
| v1 | 7.5 | 7.0 | 7.5 | 7.33 |
| v2 | 8.0 | 7.5 | 8.0 | 7.83 |
| v3 | 8.0 | 8.0 | 8.0 | 8.00 |

### Key Changes Per Round
- **v0→v1:** Reduced arrangements 6→4, added differentiator section, varied card gradients, noise texture, separated services from arrangements, service meta labels
- **v1→v2:** Fixed fade-in for screenshots (js-ready class), added olive left-border to service cards, Instagram CTA in about section
- **v2→v3:** Changed How It Works bg to sage green for visual rhythm, enriched about image placeholder, adjusted step text colors

### Exit: Round 4 — all 3 reviewers scored 8+

---

## Build 6 — Kid Sister Ice Cream
- **Category:** Ice Cream Shop
- **City:** Victoria, BC
- **Model:** claude-opus-4-6 (sonnet-kid-sister tag)
- **Date:** 2026-03-16
- **Versions:** v0 → v4 (5 versions, 5 review rounds)
- **Panel:** Don Norman / Jony Ive / Steve Krug

| Round | Version | Norman | Ive | Krug | Avg |
|-------|---------|--------|-----|------|-----|
| 1 | v0 | 6.5 | 6.5 | 7.0 | 6.67 |
| 2 | v1 | 7.5 | 7.0 | 7.5 | 7.33 |
| 3 | v2 | 7.5 | 7.5 | 7.5 | 7.50 |
| 4 | v3 | 8.0 | 7.5 | 8.0 | 7.83 |
| 5 | v4 | 8.0 | 8.0 | 8.0 | 8.00 |

**Early exit:** All 3 reviewers scored 8+ at round 5.

**Key changes per round:**
- v0→v1: Removed emoji icons (colour swatches), removed How It Works (unnecessary for ice cream), replaced fabricated review with stats card, added differentiator quote section
- v1→v2: Better SVG icons for treats (popsicle/scoop/container), wavy section divider, playful italic rotation on hero heading
- v2→v3: Cook St Village outlet mention, wholesale/events contact, gift cards CTA, polished about image badge
- v3→v4: Noise texture on hero, improved gift cards button visibility, flavour swatch hover scale animation

**What worked:** Pink/berry/cream palette perfect for ice cream. Colour swatches replacing emoji was immediate improvement. Stats card for social proof when limited reviews. Differentiator quote section (Mexican paleta culture inspiration) added real personality. Wavy divider felt on-brand for a playful food business.

**Palette:** Cream #FFF8F0, Berry #9B3E6F, Pink #E8A0BF, Peach #FDDCBF, Mint #B8E0D2, Dark #2E1A12
**Fonts:** DM Serif Display + DM Sans

## Build 5 — First Light Coffee
- **Category:** Coffee Roaster (cafe/artisan)
- **City:** Vancouver, BC
- **Fictional:** Yes (invented business details)
- **Date:** 2026-03-16
- **Model:** claude-opus-4-6 [sonnet-batch]
- **Rounds:** 3 (early exit — all 3 reviewers scored 8+)
- **Versions:** v0, v1, v2 (best)

### Scores
| Round | Norman | Ive | Krug | Avg |
|-------|--------|-----|------|-----|
| v0    | 7.0    | 7.5 | 7.0  | 7.17 |
| v1    | 7.5    | 7.5 | 7.5  | 7.5  |
| v2    | 8.0    | 8.0 | 8.0  | 8.0  |

### Key Improvements by Round
- **v0 → v1:** Added roast level bars to bean cards, differentiator quote section, alternating review card backgrounds, gold gradient hover on bean cards
- **v1 → v2:** 2x2 bean grid (no orphan card), brew method tags, process step card backgrounds, SVG noise texture on hero

### Lessons
- Roast level indicator bars (small data viz) on product cards add sophistication and utility — users can quickly scan for their preference
- Brew method tags as small pill badges give actionable guidance without cluttering the card
- 2x2 grid > auto-fit for exactly 4 items — avoids orphan card problem
- Differentiator quote sections with attribution work well between content-heavy sections — provides breathing room and brand voice
- Process step cards with subtle backgrounds (rgba + border) read better than bare text on dark backgrounds
- For fictional businesses, inventing believable details (specific farm names, roaster model, resting period) creates authentic copy

## Build 1 — Kreative Ink
- **Category:** Tattoo Studio (studios)
- **City:** Victoria, BC
- **Baseline score:** 6.67
- **Final score:** 7.5
- **Rounds:** 5 (2 architecture, 3 polish)
- **Key lessons added:** Appointment-only hours handling, process section for service businesses, Instagram-as-portfolio strategy, pricing guidance for custom work, single accent border on review cards
- **Date:** 2026-03-14

## Build 2 — Barry and Busters Pet Grooming
- **Category:** Pet Services (pet services)
- **City:** Victoria (Esquimalt + Sidney), BC
- **Baseline score:** 6.67
- **Final score:** 7.5
- **Rounds:** 4 (2 architecture, 2 polish — plateau reached at round 4, skipped round 5)
- **Key lessons added:** Multi-location parity, honest review layouts, don't fabricate prices, pet service process sections
- **Date:** 2026-03-14

## Build 3 — Puerto Vallarta Amigos
- **Category:** Food Truck / Restaurant (cafes/food trucks)
- **City:** Victoria, BC (Fisherman's Wharf + Uptown Centre)
- **Baseline score:** 6.83
- **Final score:** 7.5
- **Rounds:** 5 (2 architecture, 3 polish)
- **Key lessons added:** Multi-location trust bar hours, Google Maps embed without API key, cultural events sections, gold accents for food businesses, gold hero badges, unverified price handling with social links
- **Date:** 2026-03-15

## Build 4 — Brothers Barbershop
- **Category:** Salon / Barber (salons)
- **City:** Victoria, BC (Downtown + Langford)
- **Baseline score:** 6.83
- **Final score:** 7.67
- **Rounds:** 5 (2 architecture, 3 polish — plateau at round 3, marginal gains rounds 4-5)
- **Key lessons added:** Walk-in process sections, conflicting hours handling, named staff authenticity, numbered step cards, gold gradient hero dividers
- **Date:** 2026-03-15

## Build 5 — Focus Strength Performance
- **Category:** Fitness / Personal Training (fitness)
- **City:** Victoria, BC
- **Baseline score:** 6.83
- **Final score:** 7.5
- **Rounds:** 5 (2 architecture, 3 polish)
- **Key lessons added:** Dead website domain as demo signal, service meta labels for format clarity, scroll fade-in animations via IntersectionObserver
- **Date:** 2026-03-16

## Build 5 — Deep Cuts Vinyl
- **Category:** Record Shop (retail)
- **City:** Austin, TX
- **Date:** 2026-03-16
- **Model:** claude-opus-4-6 (sonnet-batch task)
- **Agent:** Lucy (subagent)
- **Panel:** Don Norman, Jony Ive, Steve Krug

### Scores
| Round | Norman | Ive | Krug | Avg |
|-------|--------|-----|------|-----|
| v0    | 7.0    | 7.0 | 7.0  | 7.0 |
| v1    | 7.5    | 7.5 | 7.5  | 7.5 |
| v2    | 7.5    | 8.0 | 7.5  | 7.67|
| v3    | 8.0    | 8.0 | 8.0  | 8.0 |

### Key improvements
- v0→v1: Added How It Works (Buy/Sell/Trade) with pricing, fixed hero CTA mismatch, improved footer
- v1→v2: Featured "Local Pressings" genre card (dark + gold), noise texture on about placeholder
- v2→v3: Noise on hero, scroll indicator animation, alternating review card backgrounds

### Early exit: All 3 at 8+ after round 4 (v3). 4 rounds total.

### What worked
- How It Works section with pricing context was the single biggest score driver
- Dark featured card in a light grid creates a focal point that reviewers loved
- Noise texture on dark backgrounds adds perceived quality at zero cost
- The buy/sell/trade framing was more effective than a generic "differentiator" section
- Gold accent lines (gradient with transparency) for elegant section separation

## Build 6 — Stillwater Yoga
- **Category:** Yoga Studio (fitness/wellness)
- **City:** Portland, OR (fictional)
- **Date:** 2026-03-16
- **Model:** claude-opus-4-6 (sonnet-batch task)
- **Reviewer Panel:** Don Norman, Jony Ive, Steve Krug

### Scores
| Version | Norman | Ive | Krug | Avg |
|---------|--------|-----|------|-----|
| v0      | 7.0    | 7.0 | 7.0  | 7.0 |
| v1      | 7.5    | 7.5 | 7.5  | 7.5 |
| v2      | 7.5    | 8.0 | 7.5  | 7.67|
| v3      | 8.0    | 8.0 | 8.0  | 8.0 |

### Summary
- **Rounds:** 4 (early exit — all 3 scored 8+)
- **Best version:** v3 → copied to index.html
- **Key improvements:** CTA label honesty (Book → Call to Book), hero value prop (first class free), noise texture overlay, about image shadow, review card differentiation, section dividers
- **Palette:** Sage green (#7A8B6F) + cream (#FAF7F2) + warm neutrals
- **Typography:** Instrument Serif + Inter
- **Business data:** Fully invented (fictional studio). 6 class types, 3 instructors, 4 pricing tiers, 3 reviews, weekly schedule, How It Works section
- **Notable:** First build to hit 8.0 across all 3 reviewers in 4 rounds. Sage palette works well for wellness/yoga category. "First class free" as hero copy is high-impact for service businesses.


### Scott Bell Portfolio v5 — Personal Portfolio
- **Date:** 2026-03-25
- **Hero pattern:** split-image-right
- **Typography:** Cormorant Garamond + DM Mono
- **Review layout:** Side-by-side equal cards, same treatment (no checkerboard)
- **Stats bar style:** dark-bar
- **Score:** 7.5 (v0) → 8.3 (v5 estimated)
- **Key decisions:** Warm paper (#F5F0E8) + deep ink + copper accent — entirely new palette direction. Classical serif paired with monospace creates tension matching Scott's thesis: craft + code. "Not theorizing about AI. Living inside it." hero line pulled directly from his LinkedIn voice. AI products framed as "the last year wasn't a gap, it was deliberate" handles career-pivot narrative proactively. On-load hero line stagger + scroll-reveal throughout.
