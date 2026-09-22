// Naturally Restful — merge per-subreddit harvests into the Reality Index dataset.
//
// Harvest method (Reddit 403-blocks plain scripts, so this is browser-based):
//   1. Playwright: navigate to https://www.reddit.com/r/<sub>/ (pass the one-time
//      "Prove your humanity" reCAPTCHA if shown — clearance persists).
//   2. browser_evaluate: fire-and-forget async harvest (12 supplement keyword
//      searches per subreddit, same-origin fetch, ~1s spacing, sentiment scored
//      in-page; see docs/reality-index.md for the exact snippet).
//   3. Poll `window.__result`, save each subreddit as data/reddit-<sub>.json.
//   4. Run this script to merge:  node scripts/reddit-index-merge.mjs
//
// Subreddits harvested: sleep, insomnia, Supplements, ashwagandha, Biohackers

import fs from 'node:fs';
import path from 'node:path';

const dataDir = path.resolve('data');
const files = fs.readdirSync(dataDir).filter((f) => /^reddit-([a-z-]+)\.json$/.test(f));

if (files.length === 0) {
  console.error('No data/reddit-<sub>.json files found. Harvest first (see header).');
  process.exit(1);
}

const merged = {};
const subs = [];

for (const f of files) {
  const d = JSON.parse(fs.readFileSync(path.join(dataDir, f), 'utf8'));
  if (!d?.sub || !d?.supps) continue;
  subs.push(d.sub);
  for (const [supp, r] of Object.entries(d.supps)) {
    const m = (merged[supp] ||= { posts: 0, upvotes: 0, comments: 0, pos: 0, neg: 0, quotes: [], forms: {}, perSub: {} });
    m.posts += r.posts; m.upvotes += r.upvotes; m.comments += r.comments;
    m.pos += r.pos; m.neg += r.neg;
    m.perSub[d.sub] = { posts: r.posts, pos: r.pos, neg: r.neg };
    for (const [k, v] of Object.entries(r.forms || {})) m.forms[k] = (m.forms[k] || 0) + v;
    m.quotes.push(...(r.quotes || []));
  }
}

for (const m of Object.values(merged)) {
  m.approvalPct = m.pos + m.neg > 0 ? Math.round((m.pos / (m.pos + m.neg)) * 100) : null;
  m.avgUps = m.posts ? Math.round(m.upvotes / m.posts) : 0;
  m.quotes = m.quotes.sort((a, b) => b.ups - a.ups).slice(0, 4);
  m.topForms = Object.entries(m.forms).sort((a, b) => b[1] - a[1]).slice(0, 5).map(([form, posts]) => ({ form, posts }));
}

const month = new Date().toISOString().slice(0, 7);
const totalUnique = files.reduce((s, f) => {
  const d = JSON.parse(fs.readFileSync(path.join(dataDir, f), 'utf8'));
  return s + (d.uniquePosts || 0);
}, 0);

const output = {
  generated: new Date().toISOString(),
  methodology: {
    source: 'Reddit public search API (top posts, all time), post titles + selftext; same-origin browser fetch',
    subreddits: subs,
    uniquePostsScanned: totalUnique,
    sentiment: 'keyword classes: 17 positive / 19 negative outcome phrases; approvalPct = positive/(positive+negative) posts',
    limits: 'max 50 search results per (subreddit, keyword); substring match required; comments not analyzed in v1; self-reported user sentiment, not clinical evidence',
  },
  supplements: Object.fromEntries(
    Object.entries(merged).sort((a, b) => b[1].posts - a[1].posts)
  ),
};

const outFile = path.join(dataDir, `reddit-index-${month}.json`);
fs.writeFileSync(outFile, JSON.stringify(output, null, 2));
console.log(`Merged ${files.length} subreddits, ${totalUnique} unique posts -> ${outFile}\n`);
console.log('Supplement          posts  approval  avgUps');
for (const [supp, m] of Object.entries(output.supplements)) {
  console.log(`${supp.padEnd(18)} ${String(m.posts).padStart(5)}  ${String(m.approvalPct ?? '—').padStart(5)}%  ${String(m.avgUps).padStart(6)}`);
}
