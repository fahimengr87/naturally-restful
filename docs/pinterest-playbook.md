# Pinterest Playbook — Naturally Restful

Pin images: `Desktop/pinterest-pins/` (6 ready). Format 1000×1500 — Pinterest's ideal.

## One-time setup (10 minutes, Firefox)

1. **Profile:** name "Naturally Restful" · bio: "Honest, research-cited guides to sleep & stress supplements. No hype, no miracle claims." · website: `https://naturallyrestful.xyz`
2. **Claim the website:** Settings → Claimed accounts → Claim a website → choose **HTML tag** method → copy the `pinterest-xxxx` meta tag → **paste it to ZCode** (I add it to the site in 2 minutes) → click Verify. Claimed sites get analytics + Rich Pins (pin titles/descriptions auto-sync from the page).
3. **Create 3 boards:**
   - **Sleep Supplements** (description: "What the research actually says about magnesium, melatonin, glycine and more")
   - **Stress & Adaptogens** ("Ashwagandha, rhodiola and L-theanine — honest reviews and comparisons")
   - **Better Sleep Tips** ("Free, evidence-based ways to sleep better before touching a bottle")

## The 6 launch pins (upload: Create Pin → image → title/description/link → board)

| Image | Title | Link | Board |
|---|---|---|---|
| pin-01-brand | Sleep Supplements, Honestly Reviewed — Naturally Restful | https://naturallyrestful.xyz | all 3 |
| pin-02-best-comparison | The 5 Best Sleep Supplements, Honestly Compared (2026) | https://naturallyrestful.xyz/best-sleep-supplements/ | Sleep Supplements |
| pin-03-magnesium | Magnesium for Sleep: Real Doses, Real Timeline (2 vs 4 Weeks) | https://naturallyrestful.xyz/articles/magnesium-before-bed-timing-and-dosage/ | Sleep Supplements |
| pin-04-ashwagandha | Ashwagandha for Stress: What the Trials Actually Show | https://naturallyrestful.xyz/articles/ashwagandha-for-stress-what-the-research-says/ | Stress & Adaptogens |
| pin-05-melatonin | You're Probably Taking 5–10× Too Much Melatonin | https://naturallyrestful.xyz/articles/melatonin-most-people-take-too-much/ | Sleep Supplements |
| pin-06-3am-wakeups | The 3 A.M. Wake-Up: Why It Happens + What Actually Helps | https://naturallyrestful.xyz/articles/sleep-anxiety-3am-wake-ups/ | Better Sleep Tips |

**Pin descriptions (paste into the description field, 2–3 sentences with keywords):**
- 01: "Evidence-based sleep supplement guides — what works, what doesn't, and who shouldn't take it. US/UK readers: start with the full comparison."
- 02: "Magnesium glycinate vs ashwagandha vs theanine vs melatonin vs glycine — ranked by evidence with one clear top pick. Honest 2026 comparison."
- 03: "How much magnesium for sleep, when to take it, and what to expect at week 2 vs week 4. Glycinate dosing protocol from actual trials."
- 04: "KSM-66 ashwagandha cut cortisol ~28% in trials. The honest evidence, real doses, and who must avoid it."
- 05: "The effective melatonin dose in research is 0.5–1 mg. Your bottle says 10. Why less is more for jet lag and sleep timing."
- 06: "Falling asleep fine, then wide awake at 3 a.m.? The common causes — and the supplements that actually target middle-of-the-night wake-ups."

## Cadence (the part that compounds)
- 2–3 pins/week (never 6 in a day after launch day)
- Re-pin others' content occasionally — accounts that only self-promote get throttled
- Each new article = 1–2 new pins (ask ZCode to generate them)
- Check Pinterest Analytics monthly: which pins get saves → make more like those

---

## SEP 22, 2026 — DISTRIBUTION FIX (critical)

**Diagnosis (verified in-account):**
1. **Zero distribution:** all 16 pins had 0-2 impressions, 9 monthly views. No policy strikes, no bans.
2. **Root cause found: the domain naturallyrestful.xyz is spam-flagged by Pinterest.** Any naturallyrestful.xyz URL added to a new pin shows "Sorry! We blocked this link because it may lead to spam." Control URL (example.com) passes. This flag almost certainly also explains the zero impressions.
3. **Probable trigger:** 16 template-identical pins, all linking the same external domain, published in batches from a brand-new account that followed nobody and never repinned.

**Actions taken Sep 22:**
- Warm-up started: followed 6 sleep-wellness creators, repinned 3 pins to Sleep Supplements board
- Pin 27 ("12 Sleep Supplements, Ranked by 1,673 Reddit Threads") published WITHOUT a link (linkless pins still distribute; description carries the domain as text)
- **Appeal filed** via help.pinterest.com/contact → Appeals → "Pinterest blocked my site" → "A Pin from my website is blocked for Spam" (confirmation received; watch fahim.mahmood6@gmail.com + Pinterest notifications for the reply)

**The recovery protocol (until the domain unblocks):**
- Max 1 new pin per day, varied visual templates (don't reuse one layout 16 times)
- Publish linkless pins or pins linking to non-flagged destinations (e.g., Medium articles) while the flag is active — test the domain weekly by pasting a site URL into the pin builder link field
- 2-3 repins of others' content and 1-2 new follows per week (keep the account human)
- When the domain unblocks: add links to new pins again, but keep ≤2/day cadence permanently
- Do NOT edit the 16 existing pins in bulk — leave them; once the domain is clean they should regain eligibility

**Why this happened (so it never repeats):** Pinterest's spam classifier weighs (identical templates × same-domain links × new account × batch cadence). Any two of those are fine; all four together trip it.
