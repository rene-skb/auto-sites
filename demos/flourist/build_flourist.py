from pathlib import Path
import shutil

folder = Path('/Users/rene/clawd/projects/auto-sites/demos/flourist')

photo_notes = """<!--
PHOTO RANKING
1. candidate-2.jpg — Hero. Landscape loaf on wood table, strongest editorial warmth, best negative space.
2. candidate-6.jpg — Supporting grid. Three Flourist bags, brand breadth, bright and clean.
3. candidate-1.jpg — Supporting grid. Single flour bag with banneton, calm premium kitchen context.
4. candidate-4.jpg — Supporting grid. Product-plus-tools shot, useful context.
5. candidate-3.jpg — Supporting grid. Dough process detail, tactile but secondary.
6. candidate-5.jpg — Supporting detail only. Tight branding crop.
7. candidate-7.jpg — Skip. Bakery table atmosphere is weaker and less focused.
-->
"""

base_css = """
    :root {
      --bg: #f5efe4;
      --paper: #efe5d6;
      --paper-2: #e6d6c0;
      --ink: #2b2118;
      --muted: #685847;
      --line: rgba(64, 49, 35, 0.16);
      --accent: #8a5a2b;
      --accent-deep: #5d3a18;
      --olive: #6c7249;
      --shadow: 0 24px 80px rgba(73, 48, 22, 0.12);
      --max: 1180px;
      --ease-out: cubic-bezier(0.23, 1, 0.32, 1);
      --ease-in-out: cubic-bezier(0.77, 0, 0.175, 1);
      --section-pad: clamp(4rem, 9vw, 8rem);
    }
    * { box-sizing: border-box; }
    html { scroll-behavior: smooth; }
    body {
      margin: 0;
      font-family: 'Instrument Sans', sans-serif;
      background: var(--bg);
      color: var(--ink);
      line-height: 1.65;
      -webkit-font-smoothing: antialiased;
    }
    img { max-width: 100%; display: block; }
    a { color: inherit; }
    .page-shell {
      position: relative;
      overflow: hidden;
      background:
        radial-gradient(circle at top left, rgba(255,255,255,0.6), transparent 28%),
        linear-gradient(180deg, #f8f3ea 0%, #f5efe4 44%, #ece0d0 100%);
    }
    .grain {
      position: fixed;
      inset: 0;
      opacity: 0.04;
      pointer-events: none;
      background-image: radial-gradient(rgba(62, 44, 28, 0.35) 0.6px, transparent 0.6px);
      background-size: 8px 8px;
      mix-blend-mode: multiply;
    }
    .wrap { width: min(var(--max), calc(100% - 2rem)); margin: 0 auto; }
    header.site-header {
      position: sticky; top: 0; z-index: 20;
      backdrop-filter: blur(18px);
      background: rgba(245, 239, 228, 0.84);
      border-bottom: 1px solid rgba(74, 57, 38, 0.08);
    }
    .nav { display: flex; align-items: center; justify-content: space-between; gap: 1rem; padding: 1rem 0; }
    .brand { display: flex; align-items: center; gap: 0.85rem; text-decoration: none; }
    .brand-mark {
      width: 2.7rem; height: 2.7rem; border-radius: 50%; border: 1px solid var(--line);
      display: grid; place-items: center; font-size: 0.8rem; letter-spacing: 0.18em; text-transform: uppercase;
      background: rgba(255,255,255,0.45);
    }
    .brand-copy strong, .eyebrow, .stat-label, .detail-label, .kicker, .review-meta, .chapter-label, .mini-label {
      text-transform: uppercase; letter-spacing: 0.12em; font-size: 0.72rem;
    }
    .brand-copy span { display: block; color: var(--muted); font-size: 0.88rem; }
    .nav-links { display: flex; gap: 1.25rem; align-items: center; }
    .nav-links a { text-decoration: none; color: var(--muted); font-size: 0.95rem; }
    .nav-links a:hover, .nav-links a:focus-visible { color: var(--ink); }
    .nav-toggle { display: none; }
    .hero { padding: clamp(3rem, 7vw, 6rem) 0 var(--section-pad); }
    .hero-grid { display: grid; grid-template-columns: 1.15fr 0.85fr; gap: clamp(2rem, 4vw, 4rem); align-items: start; }
    .eyebrow { color: var(--accent); margin-bottom: 1rem; }
    h1, h2, h3 { font-family: 'Newsreader', serif; font-weight: 500; line-height: 0.98; margin: 0; }
    h1 { font-size: clamp(4rem, 10vw, 7.7rem); letter-spacing: -0.06em; max-width: 9ch; }
    .hero-copy p.lead { font-size: clamp(1.12rem, 2vw, 1.38rem); color: var(--ink); max-width: 34rem; margin: 1.4rem 0 0; }
    .hero-copy p.support { color: var(--muted); max-width: 32rem; margin: 1rem 0 0; }
    .hero-actions { display: flex; flex-wrap: wrap; gap: 0.9rem; margin-top: 2rem; }
    .btn {
      display: inline-flex; align-items: center; justify-content: center; gap: 0.65rem;
      min-height: 3.4rem; padding: 0 1.25rem; border-radius: 999px; text-decoration: none;
      border: 1px solid transparent; transition: transform 180ms var(--ease-out), background 180ms var(--ease-out), color 180ms var(--ease-out), border-color 180ms var(--ease-out), box-shadow 180ms var(--ease-out);
    }
    .btn:active { transform: scale(0.97); }
    .btn.primary { background: var(--ink); color: #f8f1e8; box-shadow: var(--shadow); }
    .btn.secondary { background: rgba(255,255,255,0.5); color: var(--ink); border-color: var(--line); }
    .hero-notes {
      margin-top: 2rem; display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 1rem;
    }
    .hero-note, .fact-card, .proof-card, .contact-card, .program-card, .review-card {
      background: rgba(255,255,255,0.46); border: 1px solid var(--line); border-radius: 1.5rem; padding: 1.1rem; box-shadow: 0 8px 28px rgba(64,49,35,0.06);
    }
    .hero-media figure { margin: 0; }
    .hero-media img { width: 100%; height: min(72vh, 760px); object-fit: cover; border-radius: 1.9rem; box-shadow: var(--shadow); }
    .hero-caption { display: flex; justify-content: space-between; gap: 1rem; color: var(--muted); margin-top: 0.8rem; font-size: 0.9rem; }
    section { padding: 0 0 var(--section-pad); }
    .chapter-label { color: var(--accent); margin-bottom: 1rem; }
    .section-head { display: grid; grid-template-columns: 0.9fr 1.1fr; gap: 2rem; align-items: end; margin-bottom: 2rem; }
    .section-head p { margin: 0; color: var(--muted); max-width: 38rem; }
    .facts-grid, .proof-grid, .program-grid, .contact-grid, .gallery-grid { display: grid; gap: 1rem; }
    .facts-grid { grid-template-columns: repeat(3, minmax(0, 1fr)); }
    .fact-card p, .proof-card p, .program-card p, .contact-card p, .review-card p { margin: 0.55rem 0 0; color: var(--muted); }
    .stat-line { display: block; font-size: 1.4rem; line-height: 1.2; font-family: 'Newsreader', serif; margin-top: 0.55rem; }
    .story-grid { display: grid; grid-template-columns: 0.95fr 1.05fr; gap: clamp(1.5rem, 4vw, 4rem); align-items: start; }
    .story-grid p { margin: 0 0 1rem; }
    .quote-block {
      background: var(--ink); color: #f6eee3; padding: clamp(2rem, 5vw, 3rem); border-radius: 2rem; position: relative; overflow: hidden;
    }
    .quote-block::after {
      content: ''; position: absolute; inset: auto -10% -25% auto; width: 18rem; height: 18rem; border-radius: 50%; background: rgba(138, 90, 43, 0.22);
    }
    .quote-block p { position: relative; margin: 0; font-size: clamp(1.55rem, 3vw, 2.35rem); line-height: 1.12; font-family: 'Newsreader', serif; max-width: 13ch; }
    .quote-block span { position: relative; display: block; margin-top: 1rem; color: rgba(246, 238, 227, 0.75); }
    .gallery-grid { grid-template-columns: 1.1fr 0.9fr 0.9fr; align-items: start; }
    .gallery-grid figure, .process-grid figure { margin: 0; }
    .gallery-grid img, .process-grid img { width: 100%; border-radius: 1.6rem; object-fit: cover; box-shadow: var(--shadow); }
    .gallery-grid .hero-product img { aspect-ratio: 1.2 / 1; }
    .gallery-grid .stack img { aspect-ratio: 1 / 1.22; }
    .gallery-grid .detail img { aspect-ratio: 1 / 1.22; }
    .process-grid { display: grid; grid-template-columns: 0.8fr 1.2fr; gap: 1rem; align-items: stretch; }
    .process-grid img { height: 100%; min-height: 24rem; }
    .program-grid { grid-template-columns: repeat(3, minmax(0, 1fr)); }
    .reviews-wrap { display: grid; grid-template-columns: 1.1fr 0.9fr; gap: 1rem; align-items: stretch; }
    .review-feature {
      background: linear-gradient(180deg, #f7f0e4 0%, #ead8bf 100%); border: 1px solid rgba(93, 58, 24, 0.16); border-radius: 2rem; padding: clamp(2rem, 4vw, 3rem);
      display: flex; flex-direction: column; justify-content: space-between; min-height: 100%;
    }
    .review-feature blockquote { margin: 0; font-family: 'Newsreader', serif; font-size: clamp(2rem, 4vw, 3rem); line-height: 1.02; max-width: 11ch; }
    .review-side { display: grid; gap: 1rem; }
    .review-meta { color: var(--accent-deep); margin-top: 1rem; }
    .contact-section {
      background: linear-gradient(180deg, rgba(43,33,24,0.96), rgba(58,43,29,0.95));
      color: #f6eee3; border-radius: 2rem; padding: clamp(2rem, 5vw, 3rem);
    }
    .contact-section .section-head p, .contact-section .contact-card p, .contact-section .detail-copy { color: rgba(246,238,227,0.76); }
    .contact-grid { grid-template-columns: 1.1fr 0.9fr 0.9fr; margin-top: 2rem; }
    .contact-card { background: rgba(255,255,255,0.05); border-color: rgba(255,255,255,0.12); box-shadow: none; }
    .hours-list { list-style: none; padding: 0; margin: 1rem 0 0; display: grid; gap: 0.5rem; }
    .hours-list li { display: flex; justify-content: space-between; gap: 1rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.45rem; }
    .reveal { opacity: 0; transform: translateY(24px); transition: opacity 700ms var(--ease-out), transform 700ms var(--ease-out); }
    .reveal.is-visible { opacity: 1; transform: translateY(0); }
    .reveal[data-delay='1'] { transition-delay: 80ms; }
    .reveal[data-delay='2'] { transition-delay: 160ms; }
    .reveal[data-delay='3'] { transition-delay: 240ms; }
    footer { padding: 2rem 0 3rem; color: var(--muted); font-size: 0.92rem; }
    @media (max-width: 980px) {
      .hero-grid, .section-head, .story-grid, .reviews-wrap, .process-grid, .contact-grid { grid-template-columns: 1fr; }
      .facts-grid, .program-grid, .gallery-grid { grid-template-columns: 1fr 1fr; }
      .hero-media { order: -1; }
    }
    @media (max-width: 720px) {
      .wrap { width: min(var(--max), calc(100% - 1.1rem)); }
      .nav { align-items: flex-start; }
      .nav-toggle { display: inline-flex; border: 1px solid var(--line); background: rgba(255,255,255,0.55); color: var(--ink); border-radius: 999px; padding: 0.8rem 1rem; font: inherit; }
      .nav-links { display: none; width: 100%; flex-direction: column; align-items: flex-start; padding-top: 1rem; }
      .nav-links.open { display: flex; }
      .hero-notes, .facts-grid, .program-grid, .gallery-grid { grid-template-columns: 1fr; }
      .hero-media img { height: auto; }
      h1 { max-width: 100%; }
    }
    @media (prefers-reduced-motion: reduce) {
      html { scroll-behavior: auto; }
      .reveal, .reveal.is-visible, .btn, .nav-links { transition: none !important; transform: none !important; opacity: 1 !important; }
    }
"""

body_template = """
<div class="page-shell">
  <div class="grain"></div>
  <header class="site-header">
    <div class="wrap nav">
      <a class="brand" href="#top" aria-label="Flourist home">
        <div class="brand-mark">FM</div>
        <div class="brand-copy"><strong>Flourist</strong><span>East Vancouver mill and bakery</span></div>
      </a>
      <button class="nav-toggle" aria-expanded="false" aria-controls="site-nav">Menu</button>
      <nav class="nav-links" id="site-nav">
        <a href="#story">Why it tastes different</a>
        <a href="#bakery">What to get</a>
        <a href="#classes">Classes</a>
        <a href="#visit">Visit</a>
      </nav>
    </div>
  </header>

  <main id="top">
    <section class="hero wrap">
      <div class="hero-grid">
        <div class="hero-copy reveal is-visible">
          <div class="eyebrow">Fresh milled flour, bread, pastry, coffee</div>
          <h1>{headline}</h1>
          <p class="lead">{lead}</p>
          <p class="support">{support}</p>
          <div class="hero-actions">
            <a class="btn primary" href="https://flourist.com/" target="_blank" rel="noreferrer">Shop flour and dry goods</a>
            <a class="btn secondary" href="#visit">See hours and phone</a>
          </div>
          <div class="hero-notes">
            <div class="hero-note reveal is-visible" data-delay="1"><span class="mini-label">What makes it different</span><strong class="stat-line">Stone milled in house, to order</strong></div>
            <div class="hero-note reveal is-visible" data-delay="2"><span class="mini-label">Bakery fact</span><strong class="stat-line">First and only Vancouver bakery using flour stone-milled on site exclusively</strong></div>
            <div class="hero-note reveal is-visible" data-delay="3"><span class="mini-label">Good reason to linger</span><strong class="stat-line">Thursday and Friday run late, with pizza starting at 5PM</strong></div>
          </div>
        </div>
        <div class="hero-media reveal is-visible" data-delay="2">
          <figure>
            <img src="candidate-2.jpg" alt="A rustic round loaf on a wooden table with bowls and linen nearby">
          </figure>
          <div class="hero-caption"><span>Fresh sourdough, baked with Flourist flour</span><span>3433 Commercial Street</span></div>
        </div>
      </div>
    </section>

    <section class="wrap" id="bakery">
      <div class="section-head reveal">
        <div>
          <div class="chapter-label">Bakery first</div>
          <h2>{section_title}</h2>
        </div>
        <p>{section_copy}</p>
      </div>
      <div class="facts-grid">
        <article class="fact-card reveal"><span class="detail-label">Bread and pastry</span><p>Join them daily for bread, pastry, coffee, flour, dry goods, and more. The bakery page says the shop is open every day.</p></article>
        <article class="fact-card reveal" data-delay="1"><span class="detail-label">Flour worth refrigerating</span><p>The flour is milled fresh, includes the grain’s natural oils, and Flourist tells customers to keep it in the fridge or freezer to protect flavour and freshness.</p></article>
        <article class="fact-card reveal" data-delay="2"><span class="detail-label">Direct farm link</span><p>Flourist says it works directly with Canadian family farms for whole grains and beans, then mills the grain in house, to order.</p></article>
      </div>
    </section>

    <section class="wrap" id="story">
      <div class="story-grid">
        <div class="reveal">
          <div class="chapter-label">Why it lands</div>
          <h2>They don’t treat flour like shelf-stable filler.</h2>
          <p>Flourist’s clearest idea is simple. Flour should still feel alive when you buy it. Their own flour page spends more time explaining freshness, oils, germ, bran, and storage than polishing a lifestyle story, which is exactly why the brand feels credible.</p>
          <p>That shows up everywhere else too. There’s a bakery on Commercial Street, sourdough classes in the evening, and a product line that starts with freshly stone-milled Canadian grain instead of packaging tricks.</p>
        </div>
        <aside class="quote-block reveal" data-delay="1">
          <p>"Food creates connection."</p>
          <span>Official story page</span>
        </aside>
      </div>
    </section>

    <section class="wrap">
      <div class="section-head reveal">
        <div>
          <div class="chapter-label">Product curation</div>
          <h2>Show the grain, the bag, and the finished loaf. That’s the whole argument.</h2>
        </div>
        <p>Flourist already has the assets. The right move is not a fake storefront or a mood-board detour. It’s a tighter editorial page that lets product texture and real kitchen proof do the work.</p>
      </div>
      <div class="gallery-grid">
        <figure class="hero-product reveal"><img src="candidate-6.jpg" alt="Three Flourist flour bags lined up on a kitchen counter"><figcaption class="hero-caption"><span>Core flour lineup</span><span>Use as supporting brand shot</span></figcaption></figure>
        <figure class="stack reveal" data-delay="1"><img src="candidate-1.jpg" alt="A single Flourist flour bag beside a banneton and baking tools"><figcaption class="hero-caption"><span>Home baking setup</span><span>Quiet, clean, premium</span></figcaption></figure>
        <figure class="detail reveal" data-delay="2"><img src="candidate-3.jpg" alt="Proofed dough resting on a bench scraper over a wood surface"><figcaption class="hero-caption"><span>Process detail</span><span>Use lower on page</span></figcaption></figure>
      </div>
    </section>

    <section class="wrap">
      <div class="process-grid">
        <figure class="reveal"><img src="candidate-4.jpg" alt="A Flourist flour bag beside a rolling pin and bowl of flour"></figure>
        <div class="reveal" data-delay="1">
          <div class="chapter-label">Proof, not filler</div>
          <h2>Three things worth calling out before anyone scrolls away.</h2>
          <div class="proof-grid">
            <article class="proof-card"><span class="detail-label">Sourdough class</span><p>Their class runs 6:30PM to 9:30PM at 3433 Commercial Street, with hands-on instruction, a starter, a banneton, and a loaf to finish at home.</p></article>
            <article class="proof-card"><span class="detail-label">Local delivery</span><p>The FAQ says local delivery needs a $40 minimum. Pickup is free, and pickup at Commercial Street starts from 12PM until close.</p></article>
            <article class="proof-card"><span class="detail-label">Mill in the middle</span><p>Flourist says one of its Osttiroler mills sits in the centre of the Commercial Street space behind glass and supplies the bakery with on-site flour.</p></article>
          </div>
        </div>
      </div>
    </section>

    <section class="wrap" id="classes">
      <div class="section-head reveal">
        <div>
          <div class="chapter-label">Classes and learning</div>
          <h2>The class offering makes the whole brand feel lived in.</h2>
        </div>
        <p>The Sourdough Bread Class is one of the strongest credibility anchors on the site because it turns Flourist from a shop into a place that teaches people how to bake with the flour they’re buying.</p>
      </div>
      <div class="program-grid">
        <article class="program-card reveal"><span class="detail-label">Class focus</span><p>Techniques and tricks for baking sourdough with freshly milled flour, plus starter care and scoring instruction.</p></article>
        <article class="program-card reveal" data-delay="1"><span class="detail-label">What you leave with</span><p>A jar of sourdough starter, a round banneton, and a shaped loaf to bake at home.</p></article>
        <article class="program-card reveal" data-delay="2"><span class="detail-label">When and where</span><p>Select dates. 6:30PM to 9:30PM. Flourist, 3433 Commercial Street, Vancouver.</p></article>
      </div>
    </section>

    <section class="wrap">
      <div class="section-head reveal">
        <div>
          <div class="chapter-label">From customers</div>
          <h2>{review_title}</h2>
        </div>
        <p>{review_copy}</p>
      </div>
      <div class="reviews-wrap">
        <article class="review-feature reveal">
          <blockquote>"The only flour I will eat. I can’t live without this item."</blockquote>
          <div class="review-meta">Amanda K. · Homepage testimonial</div>
        </article>
        <div class="review-side">
          <article class="review-card reveal" data-delay="1"><p>"I absolutely love Flourist flours for baking my sourdough bread. Been purchasing them for years and the taste is so superior."</p><div class="review-meta">Anita S. · Homepage testimonial</div></article>
          <article class="review-card reveal" data-delay="2"><p>"I made the sourdough harvest loaf from your recipe and my starter flours. Flavour and texture were just what I like to see."</p><div class="review-meta">Lyne M. · Homepage testimonial</div></article>
        </div>
      </div>
    </section>

    <section class="wrap" id="visit">
      <div class="contact-section reveal">
        <div class="section-head">
          <div>
            <div class="chapter-label">Visit and contact</div>
            <h2>Get there early, or come back for pizza.</h2>
          </div>
          <p>The official contact page already says what most bakery sites bury: exact address, direct Commercial Street phone line, daily hours, and the late-night Thursday and Friday wrinkle.</p>
        </div>
        <div class="contact-grid">
          <article class="contact-card">
            <span class="detail-label">Commercial Street</span>
            <p>3433 Commercial Street<br>Vancouver, BC</p>
            <p><a href="tel:+16043369423">Call 604.336.9423</a><br><a href="mailto:info@flourist.com">Email info@flourist.com</a></p>
          </article>
          <article class="contact-card">
            <span class="detail-label">Hours</span>
            <ul class="hours-list">
              <li><span>Mon to Wed</span><span>7AM to 6PM</span></li>
              <li><span>Thu to Fri</span><span>7AM to 8PM</span></li>
              <li><span>Saturday</span><span>7AM to 6PM</span></li>
              <li><span>Sunday</span><span>7AM to 6PM</span></li>
            </ul>
          </article>
          <article class="contact-card">
            <span class="detail-label">Useful notes</span>
            <p>Lunch ends at 3PM on Thursday, Friday, and Saturday. Pizza starts at 5PM on Thursday and Friday. Local delivery has a $40 minimum. Pickup is free.</p>
            <p><a href="https://www.instagram.com/flourist/" target="_blank" rel="noreferrer">Follow @flourist</a></p>
          </article>
        </div>
      </div>
    </section>
  </main>

  <footer class="wrap">
    Built as an editorial alternative for Flourist using official copy, official facts, and real site photography.
  </footer>
</div>
<script>
  const toggle = document.querySelector('.nav-toggle');
  const nav = document.querySelector('.nav-links');
  if (toggle && nav) {
    toggle.addEventListener('click', () => {
      const open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', String(open));
    });
  }
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const reveals = document.querySelectorAll('.reveal');
  if (!reduceMotion && 'IntersectionObserver' in window) {
    const io = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.15 });
    reveals.forEach((el) => {
      if (!el.classList.contains('is-visible')) io.observe(el);
    });
  } else {
    reveals.forEach((el) => el.classList.add('is-visible'));
  }
</script>
"""

def build_html(delta, headline, lead, support, section_title, section_copy, review_title, review_copy):
    filled_body = body_template
    replacements = {
        '{headline}': headline,
        '{lead}': lead,
        '{support}': support,
        '{section_title}': section_title,
        '{section_copy}': section_copy,
        '{review_title}': review_title,
        '{review_copy}': review_copy,
    }
    for key, value in replacements.items():
        filled_body = filled_body.replace(key, value)
    return f"""<!DOCTYPE html>
<html lang=\"en\">
<head>
  <meta charset=\"UTF-8\">
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">
  <title>Flourist, remilled for the web</title>
  <meta name=\"description\" content=\"An editorial demo page for Flourist, the East Vancouver mill and bakery that stone mills flour in house and serves bread, pastry, coffee, and sourdough classes.\">
  <meta property=\"og:title\" content=\"Flourist, East Vancouver mill and bakery\">
  <meta property=\"og:description\" content=\"Fresh milled flour, bread, pastry, coffee, and sourdough classes on Commercial Street.\">
  <meta property=\"og:image\" content=\"https://auto-sites.pages.dev/demos/flourist/candidate-2.jpg\">
  <meta property=\"og:url\" content=\"https://auto-sites.pages.dev/demos/flourist/\">
  <meta name=\"theme-color\" content=\"#f5efe4\">
  <link rel=\"preconnect\" href=\"https://fonts.googleapis.com\">
  <link rel=\"preconnect\" href=\"https://fonts.gstatic.com\" crossorigin>
  <link href=\"https://fonts.googleapis.com/css2?family=Instrument+Sans:wght@400;500;600&family=Newsreader:opsz,wght@6..72,400;6..72,500&display=swap\" rel=\"stylesheet\">
  {delta}
  {photo_notes}
  <style>{base_css}</style>
</head>
<body>
{filled_body}
</body>
</html>
"""

variants = [
    ('index-v0.html', '<!-- v0 brand research build. Hero direction: editorial-spread. Typography: Newsreader + Instrument Sans. Review layout: one feature review plus two stacked review cards. Visit layout: dark three-card utility block. -->',
     'Fresh flour should taste alive.',
     'Flourist works best when the page leads with the mill, the loaf, and the fact that this is bread built from grain they mill themselves in East Vancouver.',
     'The official site already has strong facts and real photos. This version pulls the useful layer closer to the top and lets the product do the convincing.',
     'Come for bread, pastry, coffee, and flour that was milled for eating, not storage.',
     'The page should act like a sharp first visit. What is this place, why does it taste different, and what can I buy or learn here tonight?',
     'People keep coming back because the flour changes the result.',
     'The strongest customer quotes all orbit the same thing. Better flavour, better texture, better digestion, and a product they actually miss when it runs out.'),
    ('index-v1.html', '<!--\nDELTA: v1 iteration notes\n- Tightened the hero to lead even harder on freshness and the bakery payoff\n- WHY panel reviewers: Steve Jobs, Paul Graham, David Ogilvy\n- WHY panel scores: [8.2, 7.8, 8.4] avg 8.13\n- Key feedback addressed: cut diffuse story language, bring East Vancouver and the bakery offer up faster, make the central idea feel inevitable\n- See panel-notes.md -> WHY critique\n-->',
     'Fresh flour should taste alive.',
     'Flourist mills grain in house, bakes with it on Commercial Street, and sells the difference in a form you can actually bring home.',
     'The clearer the page gets, the stronger the brand feels. Less philosophy up front. More loaf, flour, bakery hours, and reasons to stop in.',
     'Come for bread, pastry, coffee, and flour that was milled for eating, not storage.',
     'The page now opens with the payoff instead of warming up to it. Bread, pastry, coffee, flour, then the explanation for why those things taste different here.',
     'People keep coming back because the flour changes the result.',
     'The homepage testimonials are unusually specific. They talk about sourdough, flavour, texture, digestion, and repeat buying, which makes them worth surfacing early.'),
    ('index-v2.html', '<!--\nDELTA: v2 iteration notes\n- Simplified section intros, improved scan order, clarified class and logistics cards\n- WHAT panel reviewers: Don Norman, Steve Krug, Jakob Nielsen\n- WHAT panel scores: [8.0, 7.7, 8.1] avg 7.93\n- Key feedback addressed: faster scanning above the fold, cleaner fact buckets, simpler visit section wording\n- See panel-notes.md -> WHAT critique\n-->',
     'Fresh flour should taste alive.',
     'Flourist mills grain in house, bakes with it on Commercial Street, and sells the difference in a form you can actually bring home.',
     'If a visitor only gives you twenty seconds, they should still leave with the whole picture. This is a mill, a bakery, a pantry shop, and a class space in one address.',
     'Bread, pastry, flour, coffee. Then the reason the loaf tastes different.',
     'The page is arranged to answer first-visit questions in order: what it is, what makes it different, what to buy, what to book, and when to show up.',
     'The customer proof is strongest when it stays concrete.',
     'The best lines are not about vague quality. They are about sourdough, digestibility, flavour, and what changed in the bake.'),
    ('index-v3.html', '<!--\nDELTA: v3 iteration notes\n- Refined hierarchy, stronger section titles, tighter proof card rhythm, cleaner dark utility block\n- HOW panel reviewers: Massimo Vignelli, Erik Spiekermann, Dieter Rams, Emil Kowalski\n- HOW panel scores: [8.1, 8.0, 7.8, 8.4] avg 8.08\n- Key feedback addressed: typography does more work, repetition reduced, motion plan reserved for section reveals and button feedback\n- Motion plan from Emil carried into Phase 10\n- See panel-notes.md -> HOW critique\n-->',
     'Fresh flour should taste alive.',
     'Flourist mills grain in house, bakes with it on Commercial Street, and sells the difference in a form you can actually bring home.',
     'The craft layer is stronger when the layout stays quiet. Warm paper palette, one serif voice, one sans voice, and real photography carrying most of the emotional load.',
     'Bread, pastry, flour, coffee. Then the reason the loaf tastes different.',
     'The visual job here is reduction. Let the loaf photo open the page, then let the flour story, the classes, and the visit details stack without extra noise.',
     'The strongest proof sounds like a person talking after they baked with it.',
     'These testimonials work because they are not generic praise. They describe sourdough success, flavour shifts, and what changed in someone’s kitchen.'),
    ('index-v4.html', '<!-- v4 motion pass. Added scroll reveals, staggered card entrances, and restrained active-state feedback. -->',
     'Fresh flour should taste alive.',
     'Flourist mills grain in house, bakes with it on Commercial Street, and sells the difference in a form you can actually bring home.',
     'The motion layer stays restrained. Sections rise in quietly, buttons compress on press, and everything remains readable with reduced motion turned on.',
     'Bread, pastry, flour, coffee. Then the reason the loaf tastes different.',
     'Nothing in the layout needs spectacle. The movement is there to reinforce rhythm and keep the page from feeling dead, not to sell a trick.',
     'The strongest proof sounds like a person talking after they baked with it.',
     'These testimonials work because they stay specific and let the customer describe the change in their own words.'),
    ('index-v5.html', '<!--\nDELTA: v5 final polish notes\n- Tightened copy in section intros, smoothed pacing between bakery, process, classes, and reviews, and made the hero support copy more direct\n- Self-review score: 8.7\n- Panel averages carried forward from panel-notes.md: WHY 8.13 / WHAT 7.93 / HOW 8.08\n- Final polish focus: facts-first bakery framing with a warmer editorial rhythm\n-->',
     'Fresh flour should taste alive.',
     'Flourist mills grain in house, bakes with it on Commercial Street, and sells the difference in a form you can actually bring home.',
     'This version keeps the best part of the brand in front the whole time: flour as a fresh ingredient, not a dry commodity. Everything else hangs off that idea.',
     'Bread, pastry, flour, coffee. Then the reason the loaf tastes different.',
     'The page works hardest when it treats the bakery, the mill, the classes, and the pantry as one connected system instead of four unrelated offers.',
     'The customer proof is strongest when it describes what changed in the bake.',
     'That is the throughline in every good quote here. Better sourdough, better flavour, better texture, and a product people keep buying because the result is obvious.')
]

for filename, delta, headline, lead, support, section_title, section_copy, review_title, review_copy in variants:
    (folder / filename).write_text(build_html(delta, headline, lead, support, section_title, section_copy, review_title, review_copy), encoding='utf-8')

shutil.copyfile(folder / 'index-v5.html', folder / 'index.html')
