# Auto-Sites Overnight Build Plan

*Draft — March 13, 2026*

## 1. Overnight Build Schedule

### Structure
- **2 sites per night**, each as a separate sub-agent (token-efficient, clean context)
- Each agent reads: `skills/auto-site-builder/SKILL.md` + `skills/auto-site-builder/lessons.md`
- Each agent: discovers business → builds from scratch → runs staggered review loop → updates lessons.md
- Stagger the agents (don't run simultaneously to avoid rate limits)

### Overnight cron setup
- **Agent 1:** Fires at 2:00 AM — builds site 1
- **Agent 2:** Fires at 3:30 AM — builds site 2 (gives agent 1 time to finish and write lessons)
- Agent 2 benefits from any lessons agent 1 just added (compounding within a single night)

### Business discovery
- Start with Victoria BC (familiar, fun to recognize businesses)
- Expand to other cities once the process is proven
- Categories to rotate through: cafes, salons, trades, retail, fitness, food trucks, pet services, studios, repair shops
- Target: businesses with Facebook/Instagram presence but no website
- Avoid: businesses that already have a website, chains, franchises

### Tracking
- Each completed site logged in `projects/auto-sites/build-log.md`:
  - Business name, category, city
  - Baseline score → final score
  - Key lessons added
  - Date built

### Compute budget
- Each site uses ~15% of a 5-hour block
- 2 sites = ~30% of the overnight block
- Leaves headroom for other overnight tasks if needed
- If we hit limits, drop to 1 site per night

---

## 2. The Full Autonomous Pipeline (Future Vision)

### Discovery
- **Outscraper** (free tier: 500 businesses, then $3/1K) — scrape Google Maps by category + city
- Filter: has Facebook/Instagram, no website detected
- Output: CSV of prospects with name, address, phone, social links, category

### Build
- Auto-site-builder skill handles this end-to-end
- Each site saved to `projects/auto-sites/demos/{business-name}/`

### Outreach
- **Cold email template** already exists at `projects/auto-sites/cold-email-template.md`
- Personalized per business (mention their specific reviews, location, services)
- Include a live link to their demo site (hosted temporarily)
- Email via: Cloudflare email routing or a dedicated outreach email

### Sell
- Prospect clicks the link, sees their business already has a site
- CTA: "Want this live? $X one-time setup."
- If yes: we buy their domain, deploy to Vercel/Netlify, hand over credentials

### Conversion math (realistic, not optimistic)
- 50 sites built → 50 cold emails sent
- **5% response rate** = 2-3 responses (cold email baseline)
- **50% of responses convert** = 1-2 sales
- At $500/site: $500-$1,000
- At $1,000/site: $1,000-$2,000
- At $1,500/site: $1,500-$3,000

**Note:** These are conservative estimates. The "here's your site already built" approach is unusual and might perform better than typical cold email because there's something tangible to look at. Or it might creep people out. We won't know until we test.

### Scale math
- 2 sites/night × 30 nights = 60 sites/month
- Even at 2% conversion and $500/site = $600/month passive
- At 5% and $1,000/site = $3,000/month
- The marginal cost per site is near-zero (just compute time)

---

## 3. Hosting + Pricing Options (Suggestions)

### Pricing tiers to consider

**Option A: One-time sale ($500-$1,500)**
- Build + deploy. They own it. Done.
- Pros: Simple, easy sell, no ongoing obligation
- Cons: No recurring revenue, no relationship

**Option B: Setup + annual hosting ($500 setup + $100/year)**
- We host on Vercel/Netlify under our account
- First year included in setup fee
- They pay $100/year to keep it live
- Pros: Recurring revenue, ongoing relationship, can upsell changes
- Cons: We're responsible for uptime

**Option C: Monthly retainer ($500 setup + $50/month)**
- Includes hosting + one content update per month
- Pros: Steady income, reason to stay in touch, can upsell
- Cons: Higher commitment from us, harder sell for small businesses

### Hosting logistics

**Vercel (recommended for now):**
- Free tier: 100 deployments/day, 100GB bandwidth
- Each site is a separate project
- Custom domain: business buys their domain (~$12/year), we point DNS to Vercel
- We control the Vercel account, hand over if they want to leave

**Netlify (alternative):**
- Similar free tier
- Slightly simpler for static sites

**Domain handling:**
- Option 1: We buy the domain for them, include in price, transfer ownership
- Option 2: They buy their own domain, we configure DNS
- Option 3: We register under our account, they "lease" it (sketchy, don't recommend)

**Recommendation:** Option B ($500 + $100/year) on Vercel. Simple enough to sell, recurring enough to build income, and Vercel's free tier means our actual hosting cost is $0. The $100/year is pure margin. Business buys their own domain, we configure it.

### What we'd need to set up
1. Dedicated outreach email (support@nakamotodesign.co or similar)
2. Stripe payment link for each tier
3. Simple onboarding doc for new clients (DNS instructions, what's included)
4. A way to show demo sites publicly (currently on local network only)

### Public demo hosting
- Deploy demo sites to Vercel on throwaway subdomains (e.g., brothers-barbershop.nakamotodesign.co)
- Or use a single showcase page: nakamotodesign.co/demos
- Prospect sees their actual site, not a screenshot

---

## Open Questions
- Do we need Scott's direct involvement for sales conversations, or can the outreach be fully automated?
- Should we start with Victoria only (local advantage, can visit in person) or go wider immediately?
- Is $500 too high for a small business with no current website? Some of these businesses might only have $200 budget.
- How do we handle requests for changes after purchase? Scope creep is real.
- Should the outreach mention AI at all, or just present as "Nakamoto Design Corp, web design for local businesses"?

---

*This is a plan, not a commitment. Next step: pick a pricing model, host a few demos publicly, send 5 test emails, see what happens.*
