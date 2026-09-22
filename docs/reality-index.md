# Sleep Supplement Reality Index — operating manual

The Reality Index is the site's original-data product: monthly, Reddit-mined, citable.
First edition: September 2026 (`/data/2026-09`, dataset `data/reddit-index-2026-09.json`).

## Live pages

- Hub: https://naturallyrestful.xyz/data/ (auto-lists editions; currently hand-maintained list)
- Report #001: https://naturallyrestful.xyz/data/2026-09/

## How to harvest (Reddit blocks scripts — this is browser-based)

Direct `*.json` access from Node/curl returns 403 (Pullpush is paywalled). Use the
Playwright browser:

1. `browser_navigate` to `https://www.reddit.com/r/<sub>/` — if a "Prove your humanity"
   reCAPTCHA appears, click the checkbox once; clearance persists for the session.
2. `browser_evaluate` the fire-and-forget harvest below (works per subreddit, ~25s;
   the tool's 30s cap is why it must NOT be awaited inline).
3. Poll `window.__done ? window.__result : 'still running'` and save via the
   evaluate tool's `filename` arg as `data/reddit-<sub>.json` — **lowercase sub name**,
   and only after confirming the result is an object (a 15-byte file means you saved
   the "still running" string — re-poll).
4. Merge: `node scripts/reddit-index-merge.mjs` → `data/reddit-index-YYYY-MM.json`
5. Pin generator: `python scripts/make-pins-reality.py`

Subreddits: sleep, insomnia, Supplements, ashwagandha, Biohackers
Keywords: melatonin, magnesium, ashwagandha, glycine, theanine, apigenin, gaba,
valerian, cbd, 5-htp, tart cherry, reishi

### Harvest snippet (paste into browser_evaluate; starts async, returns immediately)

```js
() => {
  if (window.__started) return 'already running';
  window.__started = true; window.__done = false;
  const SUPS = {'melatonin':'Melatonin','magnesium':'Magnesium','ashwagandha':'Ashwagandha','glycine':'Glycine','theanine':'L-Theanine','apigenin':'Apigenin','gaba':'GABA','valerian':'Valerian root','cbd':'CBD','5-htp':'5-HTP','tart cherry':'Tart cherry','reishi':'Reishi'};
  const POS = ['works','worked','helps','helped','game changer','amazing','sleep like a rock','knocked me out','life saver','huge difference','big difference','solid sleep','best sleep','finally sleeping','sleeping better','noticeable difference','transformed'];
  const NEG = ['did nothing','does nothing','no effect','no effects',"didn't work",'didnt work',"doesn't work",'doesnt work','waste of money','stopped working','no difference','gave up','useless','worthless','snake oil','made it worse','did not work','zero effect','felt nothing'];
  const wait = ms => new Promise(r=>setTimeout(r,ms));
  const sub = (location.pathname.split('/')[2] || 'sleep').toLowerCase();
  (async () => {
    const byId = new Map(); const perS = {};
    for (const kw of Object.keys(SUPS)) {
      try {
        const r = await fetch(`/r/${sub}/search.json?q=${encodeURIComponent(kw)}&restrict_sr=1&sort=top&t=all&limit=50&raw_json=1`);
        if (r.ok) { const j = await r.json();
          for (const c of (j?.data?.children||[])) {
            const d = c.data; if (!d || d.stickied) continue;
            const text = ((d.title||'') + '\n' + (d.selftext||'')).slice(0,5000);
            if (!text.toLowerCase().includes(kw)) continue;
            if (!byId.has(d.id)) byId.set(d.id, {ups:d.ups||0, nc:d.num_comments||0, title:(d.title||'').slice(0,120), text, perma:'https://www.reddit.com'+d.permalink, dt:new Date(d.created_utc*1000).toISOString().slice(0,10)});
            (perS[kw] = perS[kw] || []).push(d.id);
          } }
      } catch(e) {}
      await wait(900 + Math.random()*400);
    }
    const out = {sub, uniquePosts: byId.size, supps:{}};
    for (const [kw, ids] of Object.entries(perS)) {
      let ups=0, nc=0, pos=0, neg=0; const quotes=[]; const forms={};
      for (const id of ids) {
        const p = byId.get(id); const t = p.text.toLowerCase();
        ups+=p.ups; nc+=p.nc;
        const hasPos = POS.some(x=>t.includes(x)); const hasNeg = NEG.some(x=>t.includes(x));
        if (hasPos) pos++; if (hasNeg) neg++;
        if ((hasPos||hasNeg) && p.ups>=50 && quotes.length<3) quotes.push({s:hasPos&&hasNeg?'mixed':(hasPos?'pos':'neg'), q:(p.title+'. '+p.text).slice(0,200).replace(/\s+/g,' '), ups:p.ups, perma:p.perma});
        for (const f of ['glycinate','threonate','bisglycinate','citrate','oxide','ksm-66','ksm66','sensoril','gummies','gummy','sublingual','extended release']) if (t.includes(f)) forms[f]=(forms[f]||0)+1;
      }
      out.supps[SUPS[kw]] = {posts:ids.length, upvotes:ups, comments:nc, pos, neg, quotes:quotes.sort((a,b)=>b.ups-a.ups), forms};
    }
    window.__result = out; window.__done = true;
  })();
  return 'harvest started for r/' + sub;
}
```

## Monthly edition checklist

1. Harvest the 5 subreddits (above) → merge → new `data/reddit-index-YYYY-MM.json`
2. Create `src/pages/data/YYYY-MM.astro` modeled on `2026-09.astro`
   (update the JSON import; add trend callouts vs previous month)
3. Add the edition to the list in `src/pages/data/index.astro`
4. Generate chart pins: extend `scripts/make-pins-reality.py`, run it
5. Build + deploy (standard command), IndexNow the new URL, git sync
6. Publish 1 chart pin per day max (see Pinterest playbook — domain flag recovery)
7. Quora/Medium: one answer/post citing the new numbers (with link on Quora after karma)

## Methodology rules (do not break)

- A post counts for a supplement only if the name literally appears in title/body
- approvalPct = pos/(pos+neg); posts with no outcome language don't vote
- Always publish the "self-reported sentiment, not clinical evidence" caveat
- Never round in the dataset; round only in prose
