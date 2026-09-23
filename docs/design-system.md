# Naturally Restful — Design System & Variation Rules
*Codified from the owner's design direction (Sep 23, 2026). Every pin, card, and image this project generates MUST follow this document. Automations read this before generating any visual.*

## The owner's principles (verbatim intent)

1. **Design must speak for itself.** Expressive, self-explanatory visuals — the image communicates the finding before anyone reads the description.
2. **A touch of light sensation attracts.** Airy, light, soft-glow compositions pull viewers in — use them alongside the dark night theme, not instead of it.
3. **Consistency lives in brand DNA, not in layout repetition.** Repeating the same layout continuously bores viewers and hurts the business.
4. **Never afford a reach penalty to sameness.** Identical-template batches are believed to have triggered the Pinterest spam flag (Sep 2026). No two consecutive pins may share a style.

## Brand DNA — the consistency layer (ALWAYS present)

- The **crescent moon mark** (or its light-mood counterpart, the soft glowing disc)
- **naturallyrestful.xyz** footer + context line
- Palette family anchored in **navy night + cream**, with per-style accents
- **Data-forward content**: every pin leads with a number, a chart, or a verdict

## Style rotation — the variety layer

Five approved visual languages. Rotate; never publish the same style twice in a row.

| Style | Mood | Palette | Use for |
|---|---|---|---|
| **Aura** | Dark, dreamy, premium | indigo→violet→teal gradient, glow, grain, serif display | flagship findings, article pins |
| **Editorial** | Print, serious, data-product | cream paper, huge black type, one hot accent | Reality Index reports, controversy stories |
| **Sticker** | Playful, Gen-Z collage | navy + yellow stickers, outline type, doodles | lighter topics, myths, "hot takes" |
| **Chrome** | Techy Y2K-lite | near-black, chrome type, cyan/magenta glow | biohacker/stack content, sparingly |
| **Dawn** | Light, airy, calm (the "light sensation") | cream→blush→lavender sky, soft glow disc, deep navy type | wellness-adjacent, gentle truths, morning content |

## Composition variety (within a style)

Vary the hero element across consecutive pins even in the same style:
- **stat-hero** — one giant number dominates
- **headline-hero** — big type stack carries it
- **chart-hero** — the bars/ranking are the visual
- **split** — top half statement, bottom half evidence

Accents may rotate within a style's palette (gold ↔ teal in Aura; coral ↔ rust in Editorial).

## Hard rules

1. No two consecutive published pins share style + hero type.
2. A batch of pins for one campaign (e.g., a monthly report) MUST span ≥3 styles.
3. Light-mood (Dawn) pins appear at least 1 in 5 — the feed must breathe.
4. Before generating, read this file; pick the style by rotating from the last used (tracked in docs/design-log.md).
5. Text hierarchy: one hero element only; everything else supports it.
6. Charts are content, not decoration — real numbers, labeled, honest.

## Canva hand-tune spec (if editing manually)

- Pin 1000×1500 · Idea Pin 1080×1920
- Aura: #1A1440→#4A2F7A→#1A4E5C, display Georgia/Playfair Display
- Editorial: bg #F5EFE4, ink #121212, accent #E4572E, display Anton/Bebas Neue
- Sticker: bg #161E32, sticker #FFD60A, teal #78C8BE, display Anton with stroke
- Chrome: bg #0A0C18, glows #5AC8FF/#FF5AC8, display Anton
- Dawn: bg #FDF6EC→#F9E3E0→#EFE6F7, type #232A4D, display Playfair Display
