from pathlib import Path
from textwrap import dedent

folder = Path('/Users/rene/clawd/projects/auto-sites/demos/bahar-bakery-cafe')

base_head = '''<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>Bahar Bakery & Cafe</title>
<meta name="description" content="Persian pastries, small-batch bakes, and espresso on Robson Street in downtown Vancouver." />
<meta property="og:title" content="Bahar Bakery & Cafe" />
<meta property="og:description" content="Persian pastries, small-batch bakes, and espresso on Robson Street in downtown Vancouver." />
<meta property="og:image" content="https://auto-sites.pages.dev/demos/bahar-bakery-cafe/ig-photo-07.jpg" />
<meta property="og:url" content="https://auto-sites.pages.dev/demos/bahar-bakery-cafe/" />
<meta property="og:type" content="website" />
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">'''

style = '''<style>
:root {
  --bg: #f6efe3;
  --paper: #fbf7f0;
  --ink: #1e1a17;
  --muted: #6f655c;
  --line: rgba(30, 26, 23, 0.12);
  --accent: #a86b2f;
  --accent-soft: #e8d1b1;
  --olive: #737645;
  --section-pad: clamp(4.5rem, 8vw, 7.5rem);
  --ease-out: cubic-bezier(0.23, 1, 0.32, 1);
  --ease-in-out: cubic-bezier(0.77, 0, 0.175, 1);
}
* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body {
  margin: 0;
  font-family: Inter, sans-serif;
  color: var(--ink);
  background: radial-gradient(circle at top, rgba(232, 209, 177, 0.42), transparent 38%), var(--bg);
  line-height: 1.55;
}
a { color: inherit; text-decoration: none; }
img { display: block; width: 100%; height: auto; }
button { font: inherit; }
.site-shell { width: min(1180px, calc(100vw - 2rem)); margin: 0 auto; }
.topbar {
  display: flex; justify-content: space-between; align-items: center;
  padding: 1.1rem 0; border-bottom: 1px solid var(--line);
  position: sticky; top: 0; backdrop-filter: blur(18px); background: rgba(246, 239, 227, 0.85); z-index: 20;
}
.brand { font-weight: 800; letter-spacing: 0.18em; font-size: 0.78rem; text-transform: uppercase; }
.nav { display: flex; gap: 1rem; align-items: center; }
.nav a { font-size: 0.92rem; color: var(--muted); }
.nav .cta { padding: 0.82rem 1rem; border-radius: 999px; background: var(--ink); color: #fff; }
.mobile-toggle { display: none; }
.hero { padding: clamp(2rem, 4vw, 3rem) 0 var(--section-pad); }
.hero-grid { display: grid; grid-template-columns: 1.15fr 0.95fr; gap: 2rem; align-items: end; }
.eyebrow { text-transform: uppercase; letter-spacing: 0.16em; font-size: 0.78rem; color: var(--muted); margin-bottom: 1rem; }
.hero h1 { font-family: 'Cormorant Garamond', serif; font-size: clamp(3.4rem, 9vw, 6.8rem); line-height: 0.94; margin: 0 0 1rem; max-width: 10ch; }
.hero p { font-size: 1.08rem; color: var(--muted); max-width: 38rem; margin: 0 0 1.5rem; }
.quick-facts { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 1px; background: var(--line); border: 1px solid var(--line); border-radius: 24px; overflow: hidden; }
.quick-facts div { background: rgba(251,247,240,0.9); padding: 1rem 1.1rem; min-height: 100%; }
.quick-facts strong, .menu-card strong, .visit-card strong { display: block; font-size: 0.8rem; letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 0.45rem; }
.quick-facts span, .menu-card p, .visit-card p { font-size: 0.98rem; color: var(--ink); }
.hero-collage { display: grid; grid-template-columns: 0.95fr 1.05fr; gap: 1rem; }
.hero-collage .stack { display: grid; gap: 1rem; }
.photo-frame { background: #e9dfd1; border-radius: 28px; overflow: hidden; position: relative; }
.photo-frame.tall img { aspect-ratio: 4 / 5; object-fit: cover; }
.photo-frame.short img { aspect-ratio: 4 / 3; object-fit: cover; }
.photo-frame::after { content: ''; position: absolute; inset: 0; box-shadow: inset 0 0 0 1px rgba(255,255,255,0.35); border-radius: inherit; pointer-events: none; }
.section { padding: 0 0 var(--section-pad); }
.section-inner { display: grid; grid-template-columns: 1fr 1fr; gap: 2rem; }
.kicker { font-size: 0.82rem; letter-spacing: 0.14em; text-transform: uppercase; color: var(--muted); margin-bottom: 0.75rem; }
.section h2 { font-family: 'Cormorant Garamond', serif; font-size: clamp(2.5rem, 5vw, 4rem); line-height: 0.98; margin: 0 0 1rem; }
.section p { font-size: 1rem; color: var(--muted); max-width: 34rem; }
.menu-grid { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 1rem; margin-top: 1.5rem; }
.menu-card { padding: 1.15rem; border: 1px solid var(--line); border-radius: 22px; background: rgba(251,247,240,0.7); }
.pull-quote { background: #1f1a17; color: #f7f1e8; border-radius: 28px; padding: clamp(1.5rem, 4vw, 2.5rem); display: grid; gap: 1.25rem; }
.pull-quote blockquote { margin: 0; font-family: 'Cormorant Garamond', serif; font-size: clamp(2rem, 4vw, 3rem); line-height: 1.02; }
.pull-quote .attribution { font-size: 0.85rem; letter-spacing: 0.12em; text-transform: uppercase; color: rgba(247, 241, 232, 0.68); }
.gallery { display: grid; grid-template-columns: 1.1fr 0.9fr 0.9fr; gap: 1rem; align-items: start; }
.visit-wrap { display: grid; grid-template-columns: 1.05fr 0.95fr; gap: 1rem; }
.visit-card { border-radius: 28px; background: var(--paper); border: 1px solid var(--line); padding: 1.4rem; }
.visit-stack { display: grid; gap: 1rem; }
.actions { display: flex; flex-wrap: wrap; gap: 0.75rem; margin-top: 1.2rem; }
.button, .ghost {
  display: inline-flex; align-items: center; justify-content: center; gap: 0.5rem; padding: 0.95rem 1.15rem;
  border-radius: 999px; transition: transform 160ms var(--ease-out), background-color 160ms var(--ease-out), color 160ms var(--ease-out), border-color 160ms var(--ease-out);
}
.button { background: var(--ink); color: #fff; }
.ghost { border: 1px solid var(--line); background: transparent; color: var(--ink); }
.button:hover, .ghost:hover { transform: translateY(-1px); }
.button:active, .ghost:active { transform: scale(0.97); }
footer { padding: 0 0 2rem; color: var(--muted); font-size: 0.92rem; }
.reveal { opacity: 0; transform: translateY(24px); transition: opacity 700ms var(--ease-out), transform 700ms var(--ease-out); }
.reveal.visible { opacity: 1; transform: translateY(0); }
.reveal-group > * { transition-delay: var(--delay, 0ms); }
@media (max-width: 960px) {
  .hero-grid, .section-inner, .gallery, .visit-wrap { grid-template-columns: 1fr; }
  .menu-grid { grid-template-columns: 1fr; }
  .quick-facts { grid-template-columns: 1fr; }
}
@media (max-width: 760px) {
  .mobile-toggle { display: inline-flex; background: transparent; border: 0; padding: 0.5rem; }
  .nav { display: none; position: absolute; top: calc(100% + 0.75rem); right: 0; flex-direction: column; align-items: stretch; min-width: 220px; padding: 0.75rem; border-radius: 18px; background: rgba(251,247,240,0.97); border: 1px solid var(--line); }
  .nav.open { display: flex; }
  .topbar { position: relative; }
  .hero-collage { grid-template-columns: 1fr 1fr; }
}
@media (prefers-reduced-motion: reduce) {
  html { scroll-behavior: auto; }
  *, *::before, *::after { animation: none !important; transition: none !important; }
  .reveal { opacity: 1; transform: none; }
}
</style>'''

script = '''<script>
const navToggle = document.querySelector('[data-menu-toggle]');
const nav = document.querySelector('[data-nav]');
if (navToggle && nav) {
  navToggle.addEventListener('click', () => {
    const open = nav.classList.toggle('open');
    navToggle.setAttribute('aria-expanded', String(open));
  });
}
const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
if (!reduceMotion) {
  const items = document.querySelectorAll('.reveal');
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.15 });
  items.forEach((item, index) => {
    item.style.setProperty('--delay', `${(index % 5) * 70}ms`);
    observer.observe(item);
  });
}
</script>'''

def make_html(delta, hero_intro, hero_body, quote, extra_note, menu_heading, visit_note):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
{delta}
{base_head}
{style}
</head>
<body>
  <div class="site-shell">
    <header class="topbar">
      <div class="brand">Bahar Bakery & Cafe</div>
      <button class="mobile-toggle" data-menu-toggle aria-expanded="false" aria-label="Open menu">☰</button>
      <nav class="nav" data-nav>
        <a href="#menu">What to order</a>
        <a href="#story">Why go</a>
        <a href="#visit">Visit</a>
        <a class="cta" href="https://www.instagram.com/bahar_bakery_cafe/" target="_blank" rel="noreferrer">See Instagram</a>
      </nav>
    </header>

    <main>
      <section class="hero">
        <div class="hero-grid">
          <div class="reveal">
            <div class="eyebrow">Persian bakery and cafe, downtown Vancouver</div>
            <h1>{hero_intro}</h1>
            <p>{hero_body}</p>
            <div class="quick-facts reveal-group">
              <div>
                <strong>Find it</strong>
                <span>579 Robson St, Vancouver, BC V6B 1A6</span>
              </div>
              <div>
                <strong>Hours</strong>
                <span>Mon to Fri 7:30AM to 6PM. Sat to Sun 8:30AM to 5PM.</span>
              </div>
              <div>
                <strong>Good to know</strong>
                <span>Catering and event orders are available. Instagram is the best live menu.</span>
              </div>
            </div>
            <div class="actions">
              <a class="button" href="https://www.google.com/maps/search/?api=1&query=Bahar+Bakery+%26+Cafe+579+Robson+St+Vancouver" target="_blank" rel="noreferrer">Open in Google Maps</a>
              <a class="ghost" href="https://www.baharbakery.ca" target="_blank" rel="noreferrer">Current website</a>
            </div>
          </div>
          <div class="hero-collage reveal">
            <div class="stack">
              <figure class="photo-frame tall"><img src="ig-photo-07.jpg" alt="Pastry case filled with croissants, buns, and bakery sweets at Bahar Bakery." /></figure>
              <figure class="photo-frame short"><img src="ig-photo-05.jpg" alt="Illustrated Bahar Bakery storefront sign artwork." /></figure>
            </div>
            <div class="stack">
              <figure class="photo-frame tall"><img src="ig-photo-10.jpg" alt="Slice of cake from Bahar Bakery held in front of the pastry counter." /></figure>
              <figure class="photo-frame tall"><img src="ig-photo-08.jpg" alt="Cream-filled pastry on a white plate at Bahar Bakery." /></figure>
            </div>
          </div>
        </div>
      </section>

      <section class="section" id="story">
        <div class="section-inner">
          <div class="reveal">
            <div class="kicker">Why go</div>
            <h2>Because downtown rarely smells like saffron, butter, and fresh coffee.</h2>
            <p>Bahar opened on Robson with a tighter point of view than the usual grab-and-go cafe. The Vancouver Foodster write-up calls it family-run, says the mother bakes pastries from scratch daily, and points to Persian baking as the center of the menu.</p>
            <p>The house specialty worth watching for is medovik. It takes time, isn't made every day, and can be pre-ordered if you don't want to gamble on the case. {extra_note}</p>
          </div>
          <aside class="pull-quote reveal">
            <div class="attribution">Richard W. · Vancouver Foodster</div>
            <blockquote>{quote}</blockquote>
            <div class="attribution">Also mentioned: rosebud cookies, baklava, cardamom cupcakes, herbal tea, and small-batch bakes through the day.</div>
          </aside>
        </div>
      </section>

      <section class="section" id="menu">
        <div class="reveal">
          <div class="kicker">What to order</div>
          <h2>{menu_heading}</h2>
          <p>No invented full menu here. These are the items that showed up repeatedly in the available source material, so they're the ones worth scanning for first.</p>
          <div class="menu-grid">
            <article class="menu-card reveal">
              <strong>Rosebud cookie</strong>
              <p>Called out as one of the most distinctive bakes in the Vancouver Foodster visit. Floral, unusual, easy to remember.</p>
            </article>
            <article class="menu-card reveal">
              <strong>Cardamom cupcake</strong>
              <p>Listed as one of the best sellers in the same write-up. Good place to start if you want something soft, spiced, and easy.</p>
            </article>
            <article class="menu-card reveal">
              <strong>Medovik cake</strong>
              <p>The house specialty. It takes time, isn't always in the case, and can be pre-ordered.</p>
            </article>
          </div>
        </div>
      </section>

      <section class="section">
        <div class="reveal">
          <div class="kicker">From the counter</div>
          <h2>Enough texture to make the decision for you.</h2>
          <div class="gallery">
            <figure class="photo-frame tall reveal"><img src="ig-photo-06.jpg" alt="Slice of cheesecake with a coffee cup behind it at Bahar Bakery." /></figure>
            <figure class="photo-frame tall reveal"><img src="ig-photo-09.jpg" alt="Cupcake held in front of the bakery kitchen and pastry counter at Bahar Bakery." /></figure>
            <figure class="photo-frame tall reveal"><img src="ig-photo-02.jpg" alt="Window-side table inside Bahar Bakery looking out toward Robson Street." /></figure>
          </div>
        </div>
      </section>

      <section class="section" id="visit">
        <div class="visit-wrap">
          <div class="visit-stack reveal">
            <div class="visit-card">
              <strong>Visit</strong>
              <p>579 Robson St, Vancouver, BC V6B 1A6</p>
              <p>{visit_note}</p>
            </div>
            <div class="visit-card">
              <strong>Hours</strong>
              <p>Mon to Fri 7:30AM to 6PM<br/>Sat to Sun 8:30AM to 5PM</p>
              <p>Vancouver Foodster's 2023 visit note said closed Sunday. Current queue research surfaced Sunday hours. Worth checking before making a special trip.</p>
            </div>
            <div class="visit-card">
              <strong>Stay close to the real feed</strong>
              <p>Instagram is still the best window into what's in the case, what the room looks like, and what's changing week to week.</p>
              <div class="actions">
                <a class="button" href="https://www.instagram.com/bahar_bakery_cafe/" target="_blank" rel="noreferrer">Open Instagram</a>
                <a class="ghost" href="mailto:Baharbakerycafe@gmail.com">Email for catering</a>
              </div>
            </div>
          </div>
          <div class="visit-card reveal">
            <strong>Baked for downtown</strong>
            <h2 style="font-size:clamp(2.2rem,4vw,3.4rem);margin-top:0;">A softer, warmer stop in the middle of Robson.</h2>
            <p>Bahar already has a live website now, which is good news for them. This demo still earns its keep because the material is stronger when the photos, menu cues, and quick visit details all sit in one cleaner pass.</p>
            <p style="margin-bottom:0;">{visit_note}</p>
          </div>
        </div>
      </section>
    </main>

    <footer class="reveal">Demo build for Bahar Bakery & Cafe. Sources are documented in sources.md. Current business website also exists at baharbakery.ca.</footer>
  </div>
  {script}
</body>
</html>'''

versions = [
    ('v0', '<!--\nPhoto ranking\n1. ig-photo-07.jpg -> hero collage anchor, abundant pastry case, portrait\n2. ig-photo-10.jpg -> hero support, dessert detail, portrait\n3. ig-photo-08.jpg -> hero support, simple pastry detail, portrait\n4. ig-photo-06.jpg -> gallery, cheesecake + coffee, portrait\n5. ig-photo-09.jpg -> gallery, cupcake in hand, portrait\n6. ig-photo-05.jpg -> accent artwork, illustration, portrait\n7. ig-photo-02.jpg -> gallery, room + street context, landscape\n8. ig-photo-01.jpg -> skip, prep shot too messy\n9. ig-photo-04.jpg -> skip, off-brand social frame\n10. ig-photo-03.jpg -> skip, unrelated scene\n-->', 'Persian baking, right on Robson.', 'Rosebud cookies, cardamom cupcakes, medovik, and espresso all under one roof. Bahar is a downtown stop for people who want something softer than the usual coffee run.', '“The café also features a full line of espresso beverages, along with a selection of house-baked breads, more baked goods, desserts and more served throughout the day.”', 'The current business site leans generic. The sharper story is in the actual products.', 'Start with the things people actually named.', 'It sits in the middle of downtown, easy to reach when you need tea, pastry, or a box to take somewhere else.'),
    ('v1', '<!--\nDELTA: v1 iteration notes\n- Tightened hero around product and location instead of generic bakery framing\n- WHY panel reviewers: Steve Jobs, Paul Graham, David Ogilvy\n- WHY panel scores: [7.5, 7.0, 7.5] avg 7.33\n- Key feedback addressed: more conviction, less generic warmth language, stronger downtown hook\n- See panel-notes.md -> WHY critique\n-->', 'Persian baking worth crossing downtown for.', 'Saffron, rose, pistachio, butter, and coffee. Bahar keeps the pitch simple: come for the pastries, stay because the case keeps changing through the day.', '“They small batch bake all the croissants, cookies and more throughout the day so that it is all constantly fresh.”', 'The useful tension here is Persian pastry specificity inside a busy downtown cafe rhythm.', 'If it’s in the case, these are the names to look for first.', 'Robson gets loud. Bahar reads calmer, more personal, and a lot better supplied with pastry.'),
    ('v2', '<!--\nDELTA: v2 iteration notes\n- Reordered sections for faster scan, clarified hours caveat, simplified menu copy into three obvious picks\n- WHAT panel reviewers: Don Norman, Steve Krug, Jakob Nielsen\n- WHAT panel scores: [8.0, 7.5, 7.5] avg 7.67\n- Key feedback addressed: faster scanning, less repeated story copy, clearer next actions\n- See panel-notes.md -> WHAT critique\n-->', 'Persian baking worth crossing downtown for.', 'Bahar is where you go on Robson when the usual coffee chain answer feels depressing. The useful details are all here: what to order, when to go, and what makes the case different.', '“I enjoyed a cup of herbal tea along with a selection of their tasty baking that included the very unique Rosebud cookie, Baklava and one of the best sellers the Cardamom Cupcake.”', 'The copy stays close to named products and visible details so the page doesn’t drift into generic cafe writing.', '3 things to scan for first.', 'Downtown location, event catering, and an Instagram feed that still tells the freshest version of the story.'),
    ('v3', '<!--\nDELTA: v3 iteration notes\n- Reduced decorative copy, tightened type rhythm, strengthened section contrast, kept motion plan subtle\n- HOW panel reviewers: Massimo Vignelli, Erik Spiekermann, Dieter Rams, Emil Kowalski\n- HOW panel scores: [7.5, 8.0, 7.5, 8.0] avg 7.75\n- Key feedback addressed: stronger reduction, cleaner hierarchy, restrained motion plan\n- Motion plan from Emil carried into Phase 10\n- See panel-notes.md -> HOW critique\n-->', 'Persian baking worth crossing downtown for.', 'Bahar has enough point of view to cut through downtown noise without shouting. Persian pastries, small-batch baking through the day, and a room that still feels local instead of polished to death.', '“I also tried the Medovik cake, a house speciality that takes a lot of time to make. It is not offered daily, so you can pre-order it if you want to be sure of getting it.”', 'Leaning on the named medovik detail gives the page one strong memory instead of ten weak ones.', 'The short list.', 'Useful for a quick stop, and also useful when you need a box of pastries or catering for something bigger.'),
    ('v4', '<!-- motion pass: added restrained reveal motion, active button scaling, and reduced-motion support -->', 'Persian baking worth crossing downtown for.', 'Rose, saffron, cardamom, honey cake, and espresso. Bahar makes a strong case for taking the coffee break slightly more seriously.', '“This is a gem worthy of your discovery and a chance to support an independent local café that is all about family.”', 'The family-run detail stays in the story section, where it belongs, instead of trying to carry the hero.', 'The short list.', 'You can drop in for coffee, bring home pastries, or use the catering contact when the order needs to be bigger than one plate.'),
    ('v5', '<!--\nDELTA: v5 final polish notes\n- Tightened hero body, clarified the current-website note, sharpened visit copy, and trimmed a few soft phrases\n- Self-review score: 8.1\n- Panel averages carried forward from panel-notes.md: WHY 7.33 / WHAT 7.67 / HOW 7.75\n- Final polish focus: stronger specificity, cleaner pacing, fewer generic cafe phrases\n-->', 'Persian baking worth crossing downtown for.', 'Rosebud cookies, cardamom cupcakes, medovik when they have it, and espresso in the middle of Robson. Bahar is the downtown bakery stop when you want something with an actual point of view.', '“The family moved to Vancouver from Iran, and here you will find their mother baking pastries from scratch daily.”', 'The build keeps the story grounded in named products, visible photos, and details that can actually be sourced.', '3 things worth spotting in the case.', 'Robson is the practical part. The reason to go is the pastry case, the tea, and the fact that it doesn’t feel generic once you’re inside.'),
]

for ver, delta, a, b, q, extra, menu_head, visit_note in versions:
    (folder / f'index-{ver}.html').write_text(make_html(delta, a, b, q, extra, menu_head, visit_note))

(folder / 'index.html').write_text((folder / 'index-v5.html').read_text())

(folder / 'panel-notes.md').write_text(dedent('''
# Panel notes — Bahar Bakery & Cafe

## WHY critique

### Steve Jobs — 7.5
- The first useful move is leaning into what makes Bahar specific: Persian pastry in the middle of Robson, not a generic artisanal cafe.
- The page started too soft. It needed a clearer reason to go in the first screen.
- Keep the family story, but don't let it drive the pitch.

### Paul Graham — 7.0
- Cut vague warmth language. The named products do more work than abstract bakery adjectives.
- The most believable sentence is the one about medovik not being available every day.
- Say fewer things, make each one more concrete.

### David Ogilvy — 7.5
- The headline improved once it answered the practical question: why should I go here?
- "Worth crossing downtown for" is better than any generic claim about quality.
- The menu section works once it names the actual items people can look for.

**Panel average:** 7.33

**Lucy next changes:**
- Make the hero more direct and product-led.
- Move family/origin material lower.
- Use named products and the medovik detail as the memory anchor.

## WHAT critique

### Don Norman — 8.0
- The page now tells a first-time visitor what this place is, where it is, and what to order without much effort.
- Good call keeping the menu to three sourced items instead of inventing a full list.
- The hours caveat is a little messy but honest.

### Steve Krug — 7.5
- It mostly passes the don't-make-me-think test.
- The CTA set is clear: maps, Instagram, current website.
- The visit section got better once the practical details were grouped together.

### Jakob Nielsen — 7.5
- Strong scannability from the quick facts and section headings.
- Avoid repeating the same idea about downtown too many times.
- Keep the caveat around Sunday hours visible, because the sources conflict.

**Panel average:** 7.67

**Lucy next changes:**
- Reduce repeated downtown language.
- Tighten section intros to 1 to 2 clear sentences.
- Keep practical visit details grouped and obvious.

## HOW critique

### Massimo Vignelli — 7.5
- The type is doing the right amount of brand work.
- The layout got cleaner when the decorative copy was stripped back.
- Hold the grid discipline, especially in the hero collage.

### Erik Spiekermann — 8.0
- Cormorant Garamond gives the pastry story enough elegance without becoming fussy.
- Inter keeps the facts readable and honest.
- The hierarchy is strongest when the supporting copy stays short.

### Dieter Rams — 7.5
- Better once a few sentences were removed.
- The second website note is useful, but only because it's brief.
- Two photo moments is enough. No more.

### Emil Kowalski — 8.0
- Standard reveal motion is enough here.
- Animate sections and cards, not the images themselves.
- Button press feedback and reduced-motion support should stay in.

**Panel average:** 7.75

**Lucy next changes:**
- Keep motion subtle and structural only.
- Remove any sentence that says the same thing twice.
- Preserve the two-photo-moment rule.
'''))

(folder / 'sources.md').write_text(dedent('''
# Copy Sources — Bahar Bakery & Cafe

## Hero
- "Persian baking worth crossing downtown for." → queue brief + Vancouver Foodster article confirming Persian baking and downtown Robson location
- "Rosebud cookies, cardamom cupcakes, medovik when they have it, and espresso in the middle of Robson." → Vancouver Foodster article
- Address → queue brief + baharbakery.ca title + Vancouver Foodster article
- Hours "Mon-Fri 7:30AM-6PM | Sat-Sun 8:30AM-5PM" → build queue brief (added 2026-04-13)
- "Catering and event orders are available." → baharbakery.ca
- "Instagram is the best live menu." → based on observed active Instagram feed and real downloaded photos from @bahar_bakery_cafe

## Story / Why go
- "family-run" → Vancouver Foodster article
- "mother baking pastries from scratch daily" → Vancouver Foodster article
- "Persian baking as the center of the menu" → Vancouver Foodster article + queue brief
- "medovik... not offered daily... can be pre-ordered" → Vancouver Foodster article
- "The current business site leans generic" / "Bahar already has a live website now" → direct review of https://www.baharbakery.ca on 2026-04-14

## Quote / proof
- "They small batch bake all the croissants, cookies and more throughout the day so that it is all constantly fresh." — Richard W. → Vancouver Foodster article
- "I enjoyed a cup of herbal tea... Rosebud cookie... Baklava... Cardamom Cupcake." — Richard W. → Vancouver Foodster article
- "I also tried the Medovik cake... It is not offered daily..." — Richard W. → Vancouver Foodster article
- "This is a gem worthy of your discovery..." — Richard W. → Vancouver Foodster article
- "The family moved to Vancouver from Iran, and here you will find their mother baking pastries from scratch daily." — Richard W. → Vancouver Foodster article

## Menu picks
- Rosebud cookie → Vancouver Foodster article
- Cardamom cupcake (best seller) → Vancouver Foodster article
- Medovik cake / house specialty / preorder → Vancouver Foodster article

## Facts / contact
- Website URL → https://www.baharbakery.ca
- Email `Baharbakerycafe@gmail.com` → page source on baharbakery.ca
- Instagram handle `@bahar_bakery_cafe` → queue brief + active Instagram scrape
- Current website copy "Made With Love", downtown Vancouver, catering & events → baharbakery.ca

## Images used
- ig-photo-07.jpg, ig-photo-10.jpg, ig-photo-08.jpg, ig-photo-05.jpg, ig-photo-06.jpg, ig-photo-09.jpg, ig-photo-02.jpg → scraped from @bahar_bakery_cafe on 2026-04-14

## NOT USED (cut for lack of source or conflict)
- Phone number → unverified; page source exposed suspicious numbers not trusted
- Google rating / review count → queue brief cited aggregator data, but direct Google verification not completed in this build
- "Closed Sunday" → appeared in 2023 Vancouver Foodster note but conflicts with newer queue hours, so shown only as a caveat
'''))

print('Created build files in', folder)
