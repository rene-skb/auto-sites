# Panel Notes — Scott Bell Sonnet Panelproof

---

## WHY critique

**Input:** index-v0.html
**Panel:** Steve Jobs · Paul Graham · David Ogilvy
**Question:** Does it land? Does it feel inevitable? Is there conviction?

---

### Steve Jobs — Taste & Conviction

**Score: 7.5 / 10**

**Strengths:**
1. "14 years. 24 products. Six shipped this year." — three punches, lands hard. The rhythm is right. This is conviction without self-congratulation.
2. Green accent (#1A8C5F) is unexpected in portfolio design. It reads active, alive, present-tense. Right for someone building right now.
3. Showing real case study screenshots immediately in the hero right column is honest. No stock photos, no abstractions — just work.

**Weaknesses:**
1. The proof strip is a stats bar in disguise. Five numbers in a row after the hero is redundant. The hero headline already said "14 years / 24 products / 6 this year." Cut it — it makes the page feel like it doesn't trust its own opening.
2. The Now section lists 6 cards in a 3-column grid. Six equal items reads like a feature spec, not a portfolio statement. The reader doesn't know what to prioritize. Creative momentum needs curation, not enumeration.
3. The contact section headline "Let's talk." is safe. It's the right sentiment but it doesn't land with the same force as the hero. The page opens with a punch and ends with a shrug.

**Highest-leverage fix:** Kill the proof strip entirely. The hero headline already carries those numbers. The strip is redundant noise.

---

### Paul Graham — Clarity & Signal

**Score: 7.0 / 10**

**Strengths:**
1. Outcome-first case study headlines — "The market cap went 100×. The design system held." — are specific enough to be real. These read like things a person who was there would say, not resume language.
2. About section opens with microbiology. That's the most interesting thing on the page — don't bury it. The instinct to "go one layer deeper" is a real differentiator that the rest of the page proves.
3. No fluff in the hero body. "Designer who builds" is the thesis, and the three sentences that follow support it with facts.

**Weaknesses:**
1. The Now grid is 6 cards of equal weight. Six equals no priority. The reader finishes it and thinks "ok, lots of things" rather than "that's impressive." A reader who can't tell what matters will move on.
2. "Agent UX" card ends on an unsubstantiated claim — "the design layer that most AI teams are skipping." Strong, but needs one specific observation to earn it. Claims require evidence.
3. Proof strip duplicates the hero headline numbers. Repetition without new information kills momentum.

**Highest-leverage fix:** Cut the Now grid from 6 to 3. Choose the 3 that are most credible and specific. Removing 3 cards makes the remaining 3 more important, not less.

---

### David Ogilvy — Headline Craft & Persuasion

**Score: 7.0 / 10**

**Strengths:**
1. "Six shipped this year" is the most differentiated claim on the page. Most senior designers can say 14 years. Nobody says six released this calendar year. This should be the page's hero claim.
2. KOHO case study structure: "Employee #1. Zero users. Now it's worth $800M." is near-perfect Ogilvy — three beats, a complete story in 12 words. Keep this structure everywhere.
3. The hero body is offer-forward. It leads with what Scott does and provides, not with what he wants. Good instinct — maintained through most of the page.

**Weaknesses:**
1. The hero label "Product Designer · Victoria, BC" above the headline is dead space. Those words don't earn the position above the most important line on the page. Either remove or replace with something that actually qualifies ("Lead Designer, 14 years building products from zero").
2. Contact section body copy: "Looking for staff-level product design roles in AI. Especially interested in agent design..." — this is what Scott wants, not what he offers. Recruiters care about what they get. Flip the frame: what does he bring to an AI team that nobody else does?
3. Nakamoto Design card buries its strongest fact: "80+ demos built." That number is in the body copy, not the headline. The headline should earn the click/read, not the body.

**Highest-leverage fix:** Rewrite the contact body from "what I'm looking for" to "what you get" — offer-first, not want-first.

---

**WHY panel averages:**
| Reviewer | Score |
|----------|-------|
| Steve Jobs | 7.5 |
| Paul Graham | 7.0 |
| David Ogilvy | 7.0 |
| **WHY average** | **7.17** |

**Concrete changes for v1:**
1. **Remove proof strip** — numbers already live in hero headline; strip is redundant
2. **Cut Now grid from 6 → 3 cards** — Nakamoto, LoopIn, Browser Bridge (most credible, most specific)
3. **Rewrite contact body** — offer-first, not want-first
4. **Move "80+ demos" into Nakamoto card headline** — strongest fact belongs in the lead
5. **Remove or replace hero label** — "Product Designer · Victoria, BC" earns nothing above the headline

---

## WHAT critique

**Input:** index-v1.html
**Panel:** Don Norman · Steve Krug · Jakob Nielsen
**Question:** Can a first-time visitor understand this? Is hierarchy obvious? Any friction?

---

### Don Norman — Mental Model & Affordance

**Score: 7.0 / 10**

**Strengths:**
1. The page communicates credibility immediately. Real screenshots in the hero signal "this is actual work" fast.
2. Section order mostly follows a sensible mental model: proof first, current work second, background third, contact last.
3. The primary CTA is visible in the hero and the top nav is restrained enough that it doesn't distract.

**Weaknesses:**
1. The hero headline is memorable, but not fully self-explanatory. A first-time visitor gets the numbers before they get the offer. What exactly does Scott do for a team right now?
2. The right-side screenshot stack in the hero is visually dominant. It attracts attention, but doesn't help the visitor understand where to look next or what action to take.
3. "Now" in the nav and section label is abstract. For a portfolio visitor, "Current Work" maps better to expectation than "Now."

**Highest-leverage fix:** Add a single explicit value-proposition line under the hero headline, then rename "Now" to "Current Work" everywhere.

---

### Steve Krug — Clarity & Scanability

**Score: 6.5 / 10**

**Strengths:**
1. Case study headlines are highly scannable. Each one tells a compact story before the body copy starts.
2. Repetition in the case study structure helps. Once you understand one case, the rest follow the same pattern.
3. The page is text-led without drifting into bloated paragraphs. Copy is mostly disciplined.

**Weaknesses:**
1. The hero still feels crowded: giant headline, explanatory paragraph, CTA, and two large screenshots all compete on first view.
2. The left-column case metadata is too small and visually weak. Company name and role should help scanning, but right now they disappear.
3. Each case study carries headline, paragraph, pills, and two screenshots. Repeated four times, it becomes visually heavy. The reader has to work to separate chapters.

**Highest-leverage fix:** Reduce each case study to one image, strengthen the metadata column, and create clearer spacing between case study elements.

---

### Jakob Nielsen — Heuristic Risk Audit

**Score: 6.5 / 10**

**Strengths:**
1. Navigation is consistent and persistent. The page never hides basic orientation or top-level actions.
2. The contact CTA is clear and conventional. No mystery interaction, no cleverness tax.
3. The visual language is consistent across sections. Nothing feels random or systemless.

**Weaknesses:**
1. Recognition over recall: users must infer what "six shipped this year" actually refers to. Is it products? experiments? client work? Clarify.
2. Information density is still high. Four large case studies plus a three-card current-work section is a lot of homepage real estate before the user reaches contact.
3. Mid-page conversion is missing. If a recruiter is already convinced after Strike or AIOZ, there's no secondary CTA nearby.

**Highest-leverage fix:** Clarify "six shipped this year" in the hero copy and add a lightweight inline CTA after the case studies.

---

**WHAT panel averages:**
| Reviewer | Score |
|----------|-------|
| Don Norman | 7.0 |
| Steve Krug | 6.5 |
| Jakob Nielsen | 6.5 |
| **WHAT average** | **6.67** |

**Concrete changes for v2:**
1. Add a more explicit value line in the hero: what Scott does now, not just the numbers
2. Rename **Now** to **Current Work** in nav and section label
3. Reduce hero visual weight on the right so the CTA and copy lead more clearly
4. Use **one image per case study** instead of two, and strengthen case metadata typography
5. Add a small inline CTA after the case studies for visitors ready before the footer


---

## HOW critique

**Input:** index-v2.html
**Panel:** Massimo Vignelli · Erik Spiekermann · Dieter Rams · Emil Kowalski
**Question:** Is the visual system coherent? Is typography doing heavy lifting? What can be removed?

---

### Massimo Vignelli — Grid & System Coherence

**Score: 7.5 / 10**

**Strengths:**
1. The page has a clear editorial backbone: left rail, main content column, repeated section dividers, disciplined whitespace.
2. Case study structure is consistent enough that the page feels authored, not assembled.
3. Palette restraint helps the grid read clearly. Nothing competes with the structure.

**Weaknesses:**
1. The system shifts too much between sections: split hero, case-study grid, then three-up Current Work cards. Good pieces, but not one tight system.
2. Internal alignment loosens inside modules, especially between metadata, pills, and images. The baseline rhythm isn't strict enough.
3. Current Work cards introduce a second layout language right when the page should feel most unified.

**Highest-leverage fix:** Convert Current Work from cards into the same editorial grid language as the rest of the page.

---

### Erik Spiekermann — Typography & Readability

**Score: 7.0 / 10**

**Strengths:**
1. Libre Baskerville gives the page real voice. It feels human and deliberate without becoming retro.
2. Headline hierarchy is clear. Large serif display, restrained sans metadata, muted body — the roles are legible.
3. The green accent is disciplined and doesn't cheapen the type.

**Weaknesses:**
1. Body copy is a little too soft relative to the page scale. It looks elegant, but quick scanning suffers.
2. Labels, roles, and metric pills each behave like slightly different typographic systems. They're close, but not snapped together.
3. The hero line breaks are dramatic, but the subhead/body stack could feel tighter and more intentional.

**Highest-leverage fix:** Tighten the type scale and darken body copy slightly so the serif drama is balanced by stronger reading performance.

---

### Dieter Rams — Reduction & Necessity

**Score: 7.5 / 10**

**Strengths:**
1. The page is mostly disciplined. No decorative junk, no gradients, no fake complexity.
2. Reducing case studies to one image each was the right move. It made the page calmer immediately.
3. The strongest facts are now leading the sections instead of being buried.

**Weaknesses:**
1. Some metric pills are still doing work the headlines and body copy already did. Not all of them earn their space.
2. Current Work still explains too much in parallel. Three modules is better than six, but the section can be leaner.
3. The footer CTA is effective, but the page doesn't need both a heavy dark block and a separate inline CTA unless each has a distinct job.

**Highest-leverage fix:** Trim metric pills and simplify Current Work copy so fewer elements say more.

---

### Emil Kowalski — Modern Web Craft & Polish

**Score: 7.5 / 10**

**Strengths:**
1. The page feels current. The spacing, restrained color, and screenshot framing are clean and modern.
2. Negative space is doing real work. The site breathes instead of crowding itself.
3. The inline CTA improved pacing. It gives the scroll a useful release valve before the footer.

**Weaknesses:**
1. Media framing could feel more premium. Screenshots are clean, but not fully art-directed.
2. Spacing rhythm is close but not fully consistent. Some section internals feel laid out, not tuned.
3. The page is static right now. It wants restrained reveal motion and better interaction states to feel fully finished.

**Highest-leverage fix:** Standardize media framing and spacing, then add restrained motion in the next pass.

---

**HOW panel averages:**
| Reviewer | Score |
|----------|-------|
| Massimo Vignelli | 7.5 |
| Erik Spiekermann | 7.0 |
| Dieter Rams | 7.5 |
| Emil Kowalski | 7.5 |
| **HOW average** | **7.38** |

**Concrete changes for v3:**
1. Convert **Current Work** from cards into a more editorial row/list system to unify the page grid
2. Darken body copy slightly and tighten type roles for labels, metadata, and pills
3. Trim metric pills to the 2 to 3 that matter most in each case study
4. Use more deliberate screenshot framing so media feels less dropped in
5. Prepare a restrained motion plan for the next pass, not decorative animation
