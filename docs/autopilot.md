# Naturally Restful — Weekly Autopilot

To arm the weekly schedule (every Sunday 10:00), open a NEW ZCode chat and paste:

> Read C:/Users/Fahim/ZCodeProject/naturallyrestful/docs/autopilot.md and register its automation with CronCreate exactly as specified.

## Automation spec (for the registering session)

- **CronCreate:** `cron: "0 10 * * 0"`, recurring, title "Weekly article + pin publish (Naturally Restful)"
- **Prompt for each run:**
  1. **PICK** the first unchecked topic in `docs/article-queue-extended.md` (if all done, refresh the comparison page's "Updated" date instead).
  2. **WRITE** `src/content/articles/<slug>.md` in the site's established format: honest, research-cited (human trials only), structure/function claims only, who-should-skip section, 2–4 interlinks + /best-sleep-supplements, 500–800 words. Study existing articles' tone first.
  3. **TICK** the checkbox in the queue file.
  4. **BUILD + DEPLOY:** `cd /c/Users/Fahim/ZCodeProject/naturallyrestful && npm run build && CI=true npx wrangler pages deploy dist --project-name naturally-restful --branch main`
  5. **PIN:** generate a 1000×1500 branded pin (PIL; navy gradient, cream crescent moon, stars, bold white title, kicker label, naturallyrestful.xyz footer — copy the pattern from existing pins in C:/Users/Fahim/ZCodeProject/pinterest-pins/). Publish via the Playwright browser to https://www.pinterest.com/pin-creation-tool/ (session logged in as Naturally Restful): upload image (must be under C:/Users/Fahim/ZCodeProject), fill Title / 2-sentence Description / article Link, select board (Sleep Supplements or Stress & Adaptogens), Publish with Escape+force-click. If the session expired, skip and note it.
  6. **PING INDEXNOW** (Bing/DuckDuckGo/Yandex instant indexing): KEY=$(cat scripts/.indexnow-key) then POST JSON {"host":"naturallyrestful.xyz","key":KEY,"urlList":["<new article URL>"]} to https://www.bing.com/indexnow
  7. **SYNC:** git add/commit/push to origin main.
  8. **REPORT (<150 words):** article title, live URL (verify HTTP 200), pin status, total article count.

## Notes
- Quality over cadence: if a topic needs better sourcing than available, swap to the next topic and note why.
- The user reviews titles in git commits; nothing irreversible happens without git history.
