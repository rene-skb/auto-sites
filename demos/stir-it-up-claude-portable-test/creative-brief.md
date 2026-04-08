# Creative Brief — Stir It Up

## The Business
Caribbean Soul Food. 760A Yates St, Victoria, BC. Down an alley. Hidden gem. Owner-operated, tiny kitchen, massive portions. 4.5★ on Google, 188+ reviews. Cash only. Open Tue-Sat 11am-7pm. Instagram: @stiritup.yyj.

## The Feeling
This site should feel like walking into the restaurant on a warm evening. Smoky, golden, intimate. You smell the jerk chicken before you see the menu. The space is small but the presence is big. Heritage, pride, and craft in every plate.

## Palette
Dark and warm. Pull directly from the actual photos.

| Role | Color | Source |
|------|-------|--------|
| Background (dominant) | `#1a1210` | Charred jerk chicken, dark wood from spice photo |
| Background (alt sections) | `#1B4D4D` | Deep teal from the storefront sign |
| Primary text | `#FAF5EE` | Warm cream, not pure white |
| Accent | `#E5B94E` | Curry gold, scotch bonnet yellow, glaze on the chicken |
| Secondary accent | `#C4472A` | Scotch bonnet red, hot sauce |
| Muted text | `#A89585` | Weathered wood, burlap, warm brown-grey |

Dark should dominate. 70%+ of the page should be dark backgrounds. Cream sections can break it up but should feel like pauses, not the default.

## Typography
- **Headlines:** Bitter (serif). Bold, warm, grounded. Feels like hand-painted signage.
- **Body:** Inter. Clean, readable, stays out of the way.
- Headline sizes: Hero 56-64px, section titles 36-40px, body 17-18px.
- Line height: 1.6-1.8 for body. Generous.

## Hero Section
- Layout: Full-width dark background. Owner portrait on the right (ig-photo-owner.jpg). Headline and subhead on the left.
- Headline: **"Down the alley off Yates."** (from their Instagram bio / customer language)
- Subhead: **"Worth finding."**
- Single CTA: "See the menu" → scrolls to menu section
- Below the hero: a thin warm strip with address, hours, and phone. Gold accent text on dark background. No cards, just an inline info strip.

## Section Flow (top to bottom)

### 1. Hero (dark background #1a1210)
As described above.

### 2. Info Strip (dark teal #1B4D4D)
Address • Hours • Phone • Instagram. One line, centered, gold accent for key info. Compact.

### 3. The Food (dark background #1a1210)
- Small label: "The Food"
- Headline: "Small kitchen. Big flavors."
- One paragraph of copy: "Authentic Caribbean recipes, real ingredients, everything made fresh in a tiny kitchen down the alley off Yates."
- Pair with the jerk chicken hero image (hero-jerk-chicken.png). Let the image take up generous space. Editorial layout — text on one side, image on the other.

### 4. The Menu (dark teal #1B4D4D)
- Label: "What's Cooking"
- Simple list layout. NOT cards. Just item name, price, one-line description.
- Items from brief: Curry Chicken Roti $16, Jerk Chicken $18, Oxtail Stew $22 (with "Saturdays only" note in gold), Beef Patty $5, Fried Plantains $6.
- Keep it clean and scannable. Gold for prices. Cream for names. Muted for descriptions.

### 5. Photo Grid (dark background #1a1210)
- 2x2 or 3-across grid of food photos from Instagram.
- Use: ig-photo-01.jpg through ig-photo-06.jpg (pick the 4 most appetizing).
- No captions needed. Let the food speak. Subtle rounded corners (4-8px). Small gap between images.

### 6. Reviews (cream background #FAF5EE for contrast break)
- Label: "Word on the Street"
- 3 review cards on the cream background. Dark text.
- Reviews from brief:
  - Marcus T., Feb 2026: "Best oxtail I've had outside of Jamaica. The portions are massive and the flavors are authentic."
  - Jenny L., Jan 2026: "Hidden gem! The curry chicken roti is incredible. Cash only but worth the trip to the ATM."
  - David R., Mar 2026: "Finally, real Caribbean food in Victoria. The jerk chicken has actual heat. Thank you."
- Format: quote text, then name + stars + date below. First name + last initial. All 5 stars.

### 7. Find Us (dark background #1a1210)
- Headline: "Down the alley off Yates"
- Address, hours, phone. Clean layout.
- Single gold CTA button: "Get Directions" → Google Maps link
- No map embed.

### 8. Footer (darkest, #120e0c)
- Tiny footer. Business name + address + "Caribbean Soul Food." in muted text. That's it.

## Animation
- Subtle scroll-reveal: elements fade in + translate up 20px on enter. Use IntersectionObserver.
- Easing: `cubic-bezier(0.23, 1, 0.32, 1)` (custom ease-out)
- Duration: 600ms, stagger child elements by 100ms
- Buttons: `scale(0.97)` on `:active`, 100ms transition
- `prefers-reduced-motion`: respect it, disable all animations
- Do NOT use scroll-triggered class toggling that breaks screenshots. All elements should have a visible default state.

## Photo Usage
Photos are in the build folder. Use these specific files:
- `ig-photo-owner.jpg` — hero, owner portrait
- `hero-jerk-chicken.png` — food feature section
- `ig-photo-01.jpg` through `ig-photo-06.jpg` — photo grid (pick best 4)
- `roti-making.png` — optional, could work in food section
- `spices.png` — optional, could work as texture/atmosphere

## What This Site Is NOT
- Not a SaaS dashboard
- Not a template with interchangeable content
- Not cold, corporate, or blue
- Not over-organized into card grids
- Not a design portfolio piece that talks about itself
- Copy should never sound like a designer explaining their choices

## Copy Rules
- Every visible sentence should sound like the business talking, a customer talking, or a factual visitor guide
- No meta-language, no process language, no panel/review terminology
- Source all copy from the brief, reviews, and Instagram
- If a line wouldn't make sense on a printed menu or a sandwich board outside the shop, cut it
