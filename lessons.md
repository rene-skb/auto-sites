# Auto-Sites Lessons

*Tiered learning system. Lessons get promoted as they prove themselves across builds.*

---

## Tier 1 — Recent Observations
*New patterns from 1-2 builds. Watch for repetition.*

### [COPY] Facts-first copy with editorial voice outscores generic food descriptions.
"If you get there late, the oxtail is probably gone" and "That's the kind of place this is" — specific, honest lines that all three WHY reviewers praised. Graham 8, Ogilvy 7. Don't describe food with adjectives. Tell the truth about what happens there. — Stir It Up Lucy b110

### [STRUCTURE] Interior photo breaks get cut when they don't advance user decisions.
Rams flagged the atmospheric interior photo as "decoration without function" (score 7). It interrupted reading flow without earning its space. Removing it tightened the page. If you keep a photo break, overlay actionable content (address, hours). — Stir It Up Lucy b110

### [LAYOUT] dark-immersive hero with centered product photo creates jewel-box intimacy.
When the brand is precious/handmade, centering a single product photo against a near-black background with restrained type creates a luxury feel. The photo floats in darkness like something precious revealed. Works well with portrait product shots. WHAT panel scored it low initially (4.33) due to contrast issues — body text must be bright enough. — Sow Song Lucy 3 b109

### [WHAT] Text contrast on dark backgrounds: body text needs 0.9+ opacity minimum.
Three panels independently flagged insufficient contrast. rgba(219,213,198,0.7) fails. rgba(237,232,221,0.9) passes. Don't sacrifice readability for moodiness. — Sow Song Lucy 3 b109

### [LAYOUT] giant-display-type hero pattern works well for intimate brands with strong brand copy.
When the business has genuinely poetic language (Tia's "Traces of history, marks of moments"), leading with giant typography on cream creates a distinctive first impression. No competing photo needed. Works especially well when all available photos are portrait format and don't fit a landscape hero slot. — Sow Song Lucy 2 b108

### [WHAT] Numbered service items (01/02/03) create false affordance — visitors expect them to be clickable.
Norman scored 7, flagged this twice across two iterations. Removing numbers and using clean border-top treatment makes it clear these are informational, not navigation. Norman still scored 7 — the content structure matters more than the numbering. — Sow Song Lucy 2 b108

### [WHAT] WHAT panel scannability (Krug) scores below 7 when emotional storytelling sections lack scannable entry points.
Story sections with large italic serif blocks and no bold text, no subheads, no visual hierarchy within the block = Krug scores 6. Even one bolded phrase or a clear pull-quote visual treatment would help. Consider adding a border-left accent to major quotes (as done in v5 story-quote) to create visual anchoring. — Sow Song Lucy 2 b108

### [COPY] Moving the emotional story near the top of the page moved WHY from 5.5 → 6.83.
Story buried at bottom: WHY 5.5. Story as second section after hero: WHY 6.83. The Grandpa Soby narrative is the brand's heart — it earned a prominent position. — Sow Song Lucy 2 b108

### [CRAFT] Fraunces italic loses impact when used across 4+ section types on one page.
Spiekermann scored 8 but flagged that Fraunces italic used for hero h1, section titles, pull quotes, AND contact headline dilutes its specialness. Reserve italic for the 2 most important moments. Non-italic Fraunces or Inter can carry other headings. — Sow Song Lucy 2 b108

### [CRAFT] Body text readability is the first HOW failure point.
Spiekermann flags small/low-contrast body text every time. 18px minimum, rgba(255,255,255,0.85) minimum on dark backgrounds. This failed the HOW panel (6.0) before fixing. — Kreative Ink v3

### [CRAFT] Single CTA > dual CTAs for focus.
"See the Work" + "How Booking Works" created decision friction. Single primary CTA in hero scores higher on Rams' reduction principle. — Kreative Ink v3

### [CRAFT] Section spacing consistency matters for grid discipline.
Vignelli flags inconsistent vertical rhythm between sections. Use a single --section-pad variable everywhere. — Kreative Ink v3, MacLeod's Books b102

### [COPY] Plural pronouns in headlines create subtle disconnects for solo makers.
"Alchemists of our innermost feelings" (plural) when Tia is one maker created a tonal mismatch. Self-review caught it. Simplified to "Where feelings become gold" (no pronoun). For single-maker brands, watch headline pronouns. — Sow Song v2

### [LAYOUT] Numbered process steps can feel templated in intimate brands.
Jobs scored 8/10 but flagged that "How It Works" 01/02/03 section "breaks the spell" of intimacy. Removed it entirely, wove process into About prose. Numbered steps have SaaS/tech energy; intimate brands need conversational process descriptions. — Sow Song v2

### [CRAFT] Page length reduction per Rams often loses nothing.
Removed atmospheric image section, cut page by 40%. HOW panel confirmed "loses nothing of meaning." When Rams says cut, trust Rams. — Sow Song v2

### [LAYOUT] Merging Story + Maker into one section reduces redundancy without losing emotional depth.
Two separate dark-background sections (Story, then Maker) each fighting for attention. Merging them on a single burgundy canvas — portrait left, text right with story+attribution+grandpa inset+divider+maker copy — scored better with Rams (less decoration, more purpose) and reduced scroll fatigue. When a brand's story IS the maker, these should be one section. — Sow Song Lucy b107

### [WHAT] Nielsen's portfolio depth critique is a structural limitation of single-page HTML.
Repeatedly scored 6 for not having "dedicated category pages" and "multiple images per piece." This is a known ceiling for our format. Best mitigation: enriched work grid (4 columns, clear labels), process section as prose, and explicit invitation to email. Accept the limitation, don't fight it. — Sow Song Lucy b107

### [COPY] When process steps feel templated, reframe as conversational prose.
01/02/03 numbered steps feel like SaaS onboarding for intimate brands (Jobs flagged this). But removing process info entirely scored 6 with Nielsen. Solution: keep the process info, write it as natural prose in two-column layout. Gets the information clarity without the template feel. — Sow Song Lucy b107

### [COPY] "No website until X" is powerful self-aware copy for zero-digital-presence businesses.
"1,103 Google reviews. No website until tonight." is the strongest constraint-as-brand line in any build. Earned trust immediately because it sounds like a person who doesn't care about marketing. Works best when the business has genuine longevity or reputation that precedes the site. — MacLeod's Books b102

### [LAYOUT] Grid card components feel mismatched when the surrounding page has strong typographic personality.
Used a 3×2 box-card grid for categories; WHY and self-review flagged it as tonal mismatch. Replacing with a typographic list (row with dividers) resolved it in v5. Moral: card grids have SaaS/tech energy. For heritage/artisan businesses, line-separated typographic lists feel more authentic. — MacLeod's Books b102

### [COPY] Third-party endorsements as hero headlines outperform any self-written line.
Using the Maclean's Magazine "Canada's last great used bookstore" quote as the actual H1 was more convincing than any constructed headline. WHY panel scored it higher than self-promotion. Lesson: when you have an authoritative external endorsement, feature it — don't try to top it. — MacLeod's Books b102

---

## Tier 2 — Emerging Patterns
*Seen in 3-4 builds. Gaining confidence.*

*(Empty — patterns promote here after 3+ builds confirm them)*

---

## Tier 3 — Reliable Patterns
*Seen in 5+ builds. Ready for DESIGN-KNOWLEDGE.md graduation.*

*(Empty — patterns graduate to DESIGN-KNOWLEDGE.md after 5+ builds)*

---

## Graduated
*Moved to DESIGN-KNOWLEDGE.md "Things We've Learned" section.*

*(List graduated lessons here for reference)*
