// STATUS 2026-09-22: Reddit 403-blocks all direct script access to *.json
// endpoints (and Pullpush is now paywalled). Harvesting moved to the Playwright
// browser method — see the header of scripts/reddit-index-merge.mjs for the
// exact procedure, and docs/reality-index.md for the harvest snippet.
//
// This file is kept as a tombstone so the old cron/automation prompts that
// reference it fail loudly instead of silently returning empty data.
//
// Usage (prints instructions):
//   node scripts/reddit-mine.mjs

console.log(`
reddit-mine.mjs is retired — Reddit blocks direct API scraping (HTTP 403).

To harvest the Reality Index:
  1. Playwright: navigate to https://www.reddit.com/r/<sub>/
     (pass the one-time reCAPTCHA if it appears; clearance persists)
  2. browser_evaluate the harvest snippet from docs/reality-index.md
     (fire-and-forget; ~25s per subreddit; 12 supplement keywords)
  3. Poll window.__result until it is an object, save via the
     filename arg as data/reddit-<sub>.json (lowercase!)
  4. node scripts/reddit-index-merge.mjs   -> data/reddit-index-YYYY-MM.json

Subreddits: sleep, insomnia, Supplements, ashwagandha, Biohackers
`);
