# Naturally Restful — Growth Playbook (owner's principles, Oct 12 2026)
*Read before any growth/SEO work. Companion to docs/design-system.md.*

## The owner's principles (verbatim intent)

1. **Viral loops / product-led growth:** virality built into the product so real user actions invite real users (Loom pattern); **embeddable virality** — let others embed our tools on their sites (Tally Forms: $0→$4m via embedded forms).
2. **UGC & community:** showcases of user work (Miroverse pattern) attract new users; incentivized real reviews/testimonials drive organic shares.
3. **Ethical content strategy:** NEVER black-hat (cloaking, link farms, spammy backlinks — ban risk, especially fatal for a YMYL health domain). **Programmatic SEO is legitimate ONLY with unique value per page** (Zapier pattern; thin duplicates get penalized). **Trend-jacking:** use social listening to hit micro-trends first, with authentic/humanized voice.
4. **Viral-traffic readiness:** surge-proof infra and support BEFORE any push. A crashed site kills momentum instantly.

## Site-specific implementations (what these mean HERE)

### 1. Embeddable + loop mechanics (BUILD NEXT — priority)
- **Embeddable quiz widget:** an iframe/JS embed of the Sleep Supplement Finder ("What supplement fits you? — powered by Naturally Restful") that sleep blogs, newsletters, and coaches can drop into their own pages. Every embed = permanent contextual backlink + traffic loop. This is the Tally pattern applied to our strongest asset. Offer: "free tool for your readers, one line of code."
- **Shareable result cards:** quiz results render as a saveable/shareable image card ("Your match: Glycine — 97% community approval, 3g dose") carrying the site URL. Sharing a result IS the invitation (Loom pattern).
- Comparison buttons on result cards ("See how the other 11 scored") keep the loop internal.

### 2. UGC / community showcase
- **"Community Notes" section in each monthly Reality Index:** readers submit their own supplement outcomes (structured: supplement, dose, weeks, verdict); best get quoted in the next edition with first name + optional site. Contributors share their inclusion → their audience arrives. Miroverse pattern at data scale.
- Reader testimonials about the quiz/Index (incentivized honestly: featured placement, never paid fake reviews).

### 3. Programmatic SEO — unique value only (SECOND BUILD)
- **Pairwise comparison pages from the Index dataset:** "Glycine vs Melatonin for Sleep" style, generated per pair (~66 pages from 12 supplements). Each page is UNIQUE because it carries OUR data: approval deltas, volume, form consensus, top community quotes — plus curated verdict text. This is the Zapier pattern on a dataset nobody else has. RULE: no page ships without at least 3 data-unique elements; no templated filler sentences.
- **Trend-jacking protocol:** during each monthly harvest, also note spike topics in the 5 subreddits; when a sleep-supplement story trends (news, podcast, celebrity), publish the data-grounded take within 24h — our Reddit dataset is the natural "here's what the community actually says" angle nobody else can publish.

### 4. Surge readiness (ALREADY SATISFIED — verify before pushes)
- Static Astro on Cloudflare Pages: no server, no DB — the free tier absorbs traffic spikes (CF CDN). Quiz is client-side JS. Action: before any push, `npm run build && wrangler pages deploy` is our scaling. Optional pre-push check: confirm 200s on /, /data, quiz after deploy.
- Support scale: /contact page + FAQ + llms.txt already live; auto-answers via Reality Index FAQ schema.

## Non-negotiables (hard rules)
- White-hat only. No bought links beyond disclosed sponsored posts (see backlink vetting rules in handoff), no cloaking, no thin programmatic pages.
- Every growth mechanic must carry the honest-verdict brand voice — virality that sacrifices credibility is a loss, not a win.
- Pair with design-system.md rules: any new shareable/embed asset follows the rotation and brand DNA.
