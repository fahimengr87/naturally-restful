# Naturally Restful — Autonomous Reach Engine
*The complete system that grows the site's reach without human prompts. Arm once, runs forever.*

## How to arm (one time)

Open a NEW ZCode chat and paste:

> Read C:/Users/Fahim/ZCodeProject/naturallyrestful/docs/reach-engine.md and register ALL its automations with CronCreate exactly as specified.

---

## AUTOMATION 1: Weekly Content Engine
**Cron:** `0 10 * * 0` (every Sunday 10:00 AM) | **recurring: true**

**Prompt for each run:**

1. **PICK** the first unchecked topic in `docs/article-queue-extended.md` (or `docs/content-calendar.md` if that's exhausted). If all done, refresh the comparison page's "Updated" date.

2. **WRITE** `src/content/articles/<slug>.md` in the site's CONFIDENT HUMAN voice:
   - Varied sentence rhythm, direct address, personal observations, actual opinions
   - Zero hedging — every recommendation is a verdict
   - Human trials only, structure/function claims only, who-should-skip section
   - Key studies block with named citations
   - 2-4 interlinks to existing articles + /best-sleep-supplements
   - 600-900 words

3. **TICK** the checkbox in the queue file.

4. **BUILD + DEPLOY:**
   ```
   cd /c/Users/Fahim/ZCodeProject/naturallyrestful
   npm run build
   CI=true npx wrangler pages deploy dist --project-name naturally-restful --branch main
   ```

5. **PIN:** Generate a 1000×1500 branded pin with PIL (navy gradient, cream crescent moon, stars, bold white title, kicker label, naturallyrestful.xyz footer — copy the pattern from existing pins in C:/Users/Fahim/ZCodeProject/pinterest-pins/). Save as pin-NNN-<slug>.png. Publish via Playwright browser to https://www.pinterest.com/pin-creation-tool/ (session logged in as Naturally Restful). Steps: upload image → fill Title (article title), 2-sentence Description, article Link → select board (Sleep Supplements or Stress & Adaptogens) → Publish with Escape+force-click. If browser session expired, skip and note it.

6. **INDEXNOW PING:**
   ```bash
   KEY=$(cat scripts/.indexnow-key)
   curl -s -X POST "https://www.bing.com/indexnow" -H "Content-Type: application/json" -d '{"host":"naturallyrestful.xyz","key":"'$KEY'","urlList":["<new article URL>"]}'
   ```

7. **SYNC:** git add/commit/push to origin main.

8. **REPORT (<150 words):** Article title, live URL (verify HTTP 200), pin status, IndexNow status, total article count.

---

## AUTOMATION 2: Daily Quora Engine
**Cron:** `0 9 * * 1-5` (weekdays 9:00 AM) | **recurring: true**

**Prompt for each run:**

1. Check if there are remaining pre-written answers in `docs/quora-answer-kit.md`. If yes, post the next one.
2. If all pre-written answers are used, search Quora for a new sleep/stress supplement question with <20 answers.
3. Write a confident, helpful, zero-link answer (150-250 words) in the site's voice.
4. Post via the Playwright browser (navigate to question → click Answer → type in editor → Post).
5. If browser session expired, skip and note "Quora session needs refresh."
6. After ~10 total answers (2 weeks), begin adding contextual links where the article genuinely answers the question.

---

## AUTOMATION 3: Monthly Analytics Review
**Cron:** `0 10 1 * *` (1st of each month 10:00 AM) | **recurring: true**

**Prompt for each run:**

1. Pull Cloudflare analytics (GraphQL API, zone 54d194a7a28ed96059738d9d8c569c6b):
   - 30-day traffic by day (requests, page views, uniques)
   - Top countries (check EU percentage)
   - Compare to previous month

2. Check Pinterest: navigate to pinterest.com/naturallyrestful/ in Playwright, count pins, check for "monthly views" metric.

3. Check site health: curl homepage, /articles, /best-sleep-supplements — verify all HTTP 200.

4. **REPORT (under 300 words):**
   - Traffic trend (up/flat/down vs last month)
   - Top countries
   - Pinterest: pin count, monthly views
   - Site health: all pages 200?
   - Top-performing article (if identifiable)
   - One strategic recommendation for next month

5. **Save report** to `docs/analytics/YYYY-MM.md`

---

## AUTOMATION 4: Search Console Check (weekly)
**Cron:** `0 14 * * 3` (every Wednesday 2:00 PM) | **recurring: true**

**Prompt for each run:**

1. Open Search Console performance report via browser (or use Cloudflare analytics as proxy if SC session unavailable)
2. Look for: impressions > 0, clicks > 0, average position changes
3. If impressions are appearing, identify which queries and pages are getting visibility
4. Report findings (under 200 words) — especially:
   - Any queries where the site appears (even position 50+)
   - Which articles are getting impressions
   - Any Manual Actions or Security Issues notifications
5. If impressions are still 0, simply note "Still in sandbox — normal for <90 day domains"

---

## Summary of what runs autonomously:

| Automation | Schedule | What it does |
|---|---|---|
| Content Engine | Sunday 10 AM | Write article, deploy, pin, ping IndexNow, sync |
| Quora Engine | Weekdays 9 AM | Post one answer daily (karma → eventual backlinks) |
| Analytics Review | 1st of month | Pull traffic data, report trends, strategic advice |
| Search Console | Wednesday 2 PM | Check for first impressions, index status |

**Combined output:** ~4 articles/month, ~20 Quora answers/month, 4 analytics reports, 4 SC checks — all without a single human prompt.
