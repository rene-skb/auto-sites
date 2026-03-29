# Nakamoto Design Co — Landing Page Brief

## What This Is
A landing page for nakamotodesign.co. This is Scott Bell's design studio. It needs to look like a credible, confident small studio that builds beautiful websites for local businesses.

## Why It Exists
When Scott sends a cold email from scott@nakamotodesign.co offering to build a website, the recipient will Google the domain. This page needs to make them think "oh, these people are legit" within 3 seconds.

## Tone
Confident, minimal, professional. Not corporate. Not startup-y. A small studio that does excellent work and doesn't need to shout about it. Think: the kind of designer's website that other designers respect.

## DO NOT MENTION
- AI, agents, automation, pipelines, machine learning, or any technology behind the work
- How the sites are built
- Pricing (that comes in the email conversation)

## Content

### Hero
- Studio name: Nakamoto Design Co.
- Location: Victoria, BC
- Tagline: Something about building websites for businesses that deserve better than a template. Keep it short, human, not slogany.

### What We Do (1-2 sentences max)
We design and build websites for local businesses. Custom, fast, built to convert foot traffic.

### Work (THIS IS THE MOST IMPORTANT SECTION)
Show 4-6 of the best demo sites as portfolio pieces. Use real screenshots. Link each to its live subdomain URL.

Suggested sites to feature (pick based on visual quality):
- 33 Acres Brewing (scored 8.33)
- Farine & Vanille (bakery, beautiful photography)
- Kid Sister Ice Cream (real photos, warm)
- Crust Bakery or Goodside Pastry House
- One that's NOT food (barbershop, tattoo, vintage shop — show range)
- One more that looks great

For each: screenshot, business name, city, one-line description, link to live demo.

### About (brief)
- Founded by Scott Bell
- 14 years product design experience
- Built products used by millions (Strike, KOHO)
- Now focused on helping local businesses get online
- Based in Victoria, BC
- No photo needed (keep it mysterious/minimal)

### Contact
- Email: scott@nakamotodesign.co
- Keep it simple. No contact form needed.

## Design Direction
- Dark theme, warm tones (consistent with our portfolio aesthetic)
- Minimal. Let the work speak.
- The work section should be the hero of the page — big screenshots, clean grid
- This page itself is proof of quality. If it looks mediocre, the whole pitch falls apart.
- Include OG meta tags (og:title, og:description, og:image, og:url)

## Technical
- Single index.html with inline CSS
- Google Fonts only
- Responsive
- Save to: projects/auto-sites/demos/nakamoto-design/

## Screenshots
To get screenshots of the demo sites for the portfolio section, use the screenshot tool:
```bash
cd /Users/rene/clawd/projects/auto-sites/demos/{site-name}
python3 -m http.server 8891 &
node /Users/rene/clawd/skills/auto-site-builder/screenshot.js http://localhost:8891/index.html /tmp/{site-name}-preview.png
```
Or just reference the live URLs directly as images won't work inline — use placeholder colored blocks with the business name if screenshots are too complex.
