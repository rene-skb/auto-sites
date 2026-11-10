# Source map

Scope: approved complete frontend v0. Sources are local owner-approved documents, not inferred from older demos or Onggi.

## Visible copy

- Kid Sister / Pantry, jellies and vinegars, five product names, categories, 250 mL, $13 CAD jellies / $22 CAD vinegars: `../storefront-build-brief.md`, §§4–6.
- Main-site navigation destinations: current live routes on `https://www.kidsistericecream.com/`, `/about`, `/stockists` and `/events`, verified November 9, 2026. The Pantry route stays local to this storefront.
- “Small batch handmade in Esquimalt BC”: shared line, `../brand-assets/label-asset-audit-2026-11-09.md`.
- Ingredient copy on product pages: corresponding verified product entry in that audit. No additional taste, health, sourcing or process claims.
- Refrigeration and best-enjoyed periods: audit, jelly = 1 year / vinegar = 6 months. Punctuation normalized only.
- Pickup only, 1320 Esquimalt Road, Thu–Fri 3–8 PM / Sat–Sun 1–8 PM / Closed Mon–Wed: brief §6H. Hours are editable in `src/lib/products.ts`.
- “On the shelf”, “Shop the pantry”, empty bag, pickup form and preview boundary text: functional UI labels, not product claims.
- Loading, sold-out, low-stock, stale-price and server-error states are development fixtures only. No live inventory, payment, order or confirmation state is inferred.
- Google Maps URL: owner-approved direct listing link preserved in `../storefront-build-brief.md`, §6H. The site does not derive hours from the listing.

## Asset map

Originals: `../incoming/product-photos/originals/`. Files are unchanged. Reproducible WebP derivatives and original dimensions/byte counts are recorded in `review/asset-manifest.json`. Next/Image handles serving at responsive widths in server mode; the static review export serves the prepared local WebP files without a remote image optimizer.

| Slot | Original | Treatment |
| --- | --- | --- |
| Hero / OG | Pantry Items 20206_1.jpg | Full 3:2 composition; no copy overlay |
| Concord Grape Jelly | Jellies 2026_9.jpg | Group image; focal metadata in product data |
| Rhubarb Jelly | Jellies 2026_4.jpg | Different group frame |
| Quince Jelly | Jellies 2026_2.jpg | Different group frame |
| Plum Vinegar | Plum Vinegar_9.jpg | Bottle group |
| Orchard Vinegar | Orchard Vinegar_6.jpg | Bottle group |

Product pages and the bag reuse the selected product image as a commerce context, not additional editorial photo slots.

Official wordmark: byte-for-byte copy of `../incoming/labels/source-2026-11-09/KID SISTER logo.svg` to `public/brand/kid-sister.svg`. It is used in the shared-site header. Five original label strips are preserved as local reference copies under `review/label-references/`; they are evidence, not UI templates.

Product colors from SVG audit: Concord #79BF6A, Rhubarb #CC6891, Quince #E1D66E, Plum #F2AF4F, Orchard #FF7B74. Near-black #242720 supplies structure and text; Orchard coral #FF7B74 is reserved for shopping actions and the active bag count.

Albert Sans: locally supplied Google Fonts variable TTF from `../../../artifacts/dq40-albert-sans/fonts/`, OFL license copied alongside. Served locally using next/font, no runtime font request to Google.

## Editorial placeholders and deferred items

No unverified marketing copy. Empty placeholder list in product data. Share metadata uses the approved public demo URL, not the production Kid Sister domain. Two unfinished vinegars and the unverified two-for-$40 offer are omitted. Final wordmark clear-space rules, packaging finality, hours exceptions and Square item spelling remain later launch checks. The Square handoff explicitly states that checkout is not connected and does not imitate payment, receipt or order creation.

## Critic experiment additions
- Vinegar serving paragraph: exact shared serving text from the Plum and Orchard labels in `../brand-assets/label-asset-audit-2026-11-09.md`.
- Jelly group-photo caption: actual photography, verified green/pink/yellow label colors, and single 250 mL unit pricing from the same audit and owner-approved brief.
- Pickup-only hero note: existing local-pickup-first brief; no shipping added.
