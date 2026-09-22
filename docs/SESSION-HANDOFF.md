# SESSION HANDOFF — Naturally Restful
# Read this file FIRST in every new chat. It contains everything needed for continuity.

## ONE-LINE STARTER (paste this in the new chat):

> Read C:/Users/Fahim/ZCodeProject/naturallyrestful/docs/SESSION-HANDOFF.md and follow its instructions exactly. Then acknowledge you're ready.

---

## PROJECT SUMMARY

**Site:** Naturally Restful (naturallyrestful.xyz) — sleep & stress supplement review site
**Owner:** Fahim Mahmood (fahim.mahmood6@gmail.com)
**Total spend:** ~$2 (domain only, .xyz promo at Namecheap)
**Age:** Launched Sep 11, 2026
**Domain expires:** Sep 11, 2027
**Hosting:** Cloudflare Pages (free, project name: naturally-restful)
**GitHub:** github.com/fahimengr87/naturally-restful
**Project root:** C:/Users/Fahim/ZCodeProject/naturallyrestful

## CURRENT STATE (as of Sep 22, 2026)

### Website
- 42 pages live (27 articles + comparison + FAQ + glossary + trust pages)
- All SEO features: hreflang (en-US, en, x-default), schema (Article, FAQ, Breadcrumb), OG cards, RSS feed, related articles mesh, security headers, GDPR consent banner
- Voice: CONFIDENT HUMAN — zero hedging, actual opinions, varied rhythm, direct address
- Deployed via: `cd /c/Users/Fahim/ZCodeProject/naturallyrestful && npm run build && CI=true npx wrangler pages deploy dist --project-name naturally-restful --branch main`

### Monetization
- **SellHealth: APPROVED & EARNING** ✅
  - Affiliate ID: 995971
  - Product: CortiSync (KSM-66 ashwagandha, 50% commission)
  - Tracking link: https://www.cortisync.com/ct/995971
  - All 10 /go/ redirect slots point to CortiSync (defined in public/_redirects)
  - Product boxes on all flagship articles reference CortiSync with honest contextual connections
  - Payout: NOT YET SET UP — needs wire transfer details to Dutch-Bangla Bank (user must do this)
  - Affiliate manager: Bruce Morrey (bruce@sellhealth.com)
  - Portal: affiliates.sellhealth.com (username: naturallyrestful)
- **MaxBounty: REVIEWING** ⏳
  - Submitted Sep 13, confirmed Sep 18
  - Proactive follow-up email sent Sep 22
  - Next step: phone interview (prep kit at docs/maxbounty-phone-prep.md)
- **iHerb: RECONSIDERING** ⏳
  - Original application rejected, reconsideration emails sent Sep 13 and Sep 22
  - Contact: Joan C. (affiliates@iherb.com)
  - Partnerize app: "Naturally Restful Publisher" (App ID 1611322)

### Traffic Channels
- **Pinterest:** 16+ pins, claimed domain, 2 boards (Sleep Supplements: 10, Stress & Adaptogens: 5)
  - Profile: pinterest.com/naturallyrestful
  - Session works via cookie transplant from Firefox
  - Publishing method: Playwright browser → pin-creation-tool → upload → fill → publish (Escape+force-click)
- **Quora:** 3 answers live (melatonin, magnesium, "are supplements a scam?")
  - Profile: quora.com/profile/Fahim-Mahmood-1-1
  - Credential: "Sleep & Stress Supplement Researcher at naturallyrestful.xyz"
  - Pre-written answers in docs/quora-answer-kit.md
- **Medium:** 2 articles published
  - "Your Melatonin Bottle Is Lying to You" (melatonin)
  - "Stop Buying the Wrong Magnesium for Sleep" (magnesium)
  - Profile: medium.com/@fahim.mahmood6
- **Facebook:** Page live at facebook.com/NaturallyRestful
  - 3 posts + 1 video reel published
  - Native content strategy in docs/facebook-native-posts.md
- **Google:** Search Console verified, sitemap submitted, sandbox period active (until ~Oct 2)
- **Bing:** IndexNow submitted (all URLs) — key stored in scripts/.indexnow-key
- **Email newsletter:** Placeholder (not connected to a provider yet)

### Analytics (Sep 22)
- Total 11-day: 12,509 requests, 2,747 page views, 2,116 unique visitors
- EU traffic: 50.7% (Netherlands 30.5%, Germany 19.8%)
- US traffic: 13.4% (hreflang en-US just deployed to boost this)
- Most traffic is bots/crawlers; real humans estimated 30-80/day

## KEY FILES (all in project root)

| File | What it contains |
|---|---|
| `docs/affiliate-launch-kit.md` | Master profile, application answers, phone scripts |
| `docs/quora-answer-kit.md` | Pre-written Quora answers + posting protocol |
| `docs/guest-post-pitches.md` | 3 pitch emails for OdeSleep, Sleepify Lab, Intelligent Labs |
| `docs/facebook-native-posts.md` | Algorithm-optimized FB posts + posting schedule |
| `docs/facebook-page-kit.md` | Page setup guide + first posts |
| `docs/maxbounty-phone-prep.md` | Phone interview preparation kit |
| `docs/reach-engine.md` | 4 automation specs (arm in new chat) |
| `docs/autopilot.md` | Weekly content automation spec |
| `docs/pinterest-playbook.md` | Pinterest strategy + cadence |
| `docs/content-calendar.md` | Season 1 (complete, 24/24) |
| `docs/article-queue-extended.md` | Season 2 queue (some done, ~10 remaining) |
| `scripts/pin.mjs` | Pinterest API script (not usable — trial access blocked) |
| `scripts/attach-domain.sh` | Domain attach script |
| `scripts/.indexnow-key` | Bing IndexNow API key |
| `scripts/.pinterest-secret` | Pinterest app secret |
| `scripts/.api-token` | Cloudflare Pages DNS token |

## CRITICAL TECHNICAL NOTES

1. **Browser automation:** Use Playwright MCP tools (not the in-app browser). Cookie transplant from Firefox works for Pinterest, Quora, Facebook, Medium. Does NOT work for Gmail (use direct login in Playwright window). SellHealth portal auto-fills from saved credentials.

2. **Pinterest publishing:** Always use Escape + force-click for the Publish button (overlays intercept normal clicks). Board dropdown: force-click → select board by text → Escape → force-click Publish.

3. **Gmail sending:** Transplant cookies → navigate to mail.google.com → Compose → fill → Send. Works reliably.

4. **Deploy command:** `cd /c/Users/Fahim/ZCodeProject/naturallyrestful && npm run build && CI=true npx wrangler pages deploy dist --project-name naturally-restful --branch main`

5. **Git sync:** `cd /c/Users/Fahim/ZCodeProject/naturallyrestful && git add -A && git commit -m "message" && git push -q origin main`

6. **Voice rule:** Every article must sound like a well-read friend who genuinely cares — confident, zero hedging, actual opinions, varied rhythm. No "may potentially perhaps." See existing articles for reference.

7. **Security scanner:** Mimosa runs on git commits. High-severity blocks pushes. Current state: medium-level findings in other projects (llm-stack, malware-shield), non-blocking.

8. **Cookie transplant pattern:**
   - Firefox profile: `$APPDATA/Mozilla/Firefox/Profiles/n7obr8qs.default-release-1786376006444`
   - Copy cookies.sqlite → extract via Python sqlite3 → inject via Playwright `page.context().addCookies()`

## AUTOMATIONS STATUS

| Automation | Status | How to arm |
|---|---|---|
| Weekly Content Engine (Sunday 10 AM) | ✅ ARMED | Already registered |
| Daily Quora Engine (weekdays 9 AM) | ✅ ARMED | Already registered |
| Monthly Analytics | ❌ Not armed | CronCreate needed |
| Weekly Search Console | ❌ Not armed | CronCreate needed |

## PENDING USER ACTIONS

1. **Set up SellHealth payout** — email Bruce with Dutch-Bangla wire details (SWIFT: DBBLBDDH)
2. **Send 3 guest post pitches** — copy from docs/guest-post-pitches.md
3. **Answer MaxBounty phone call** — prep at docs/maxbounty-phone-prep.md
4. **Connect email newsletter** — sign up for MailerLite/ConvertKit free tier
5. **Set Facebook page username** — facebook.com/NaturallyRestful (in page settings)

## WHAT TO DO IN A NEW CHAT

1. Read this file
2. Acknowledge continuity
3. Ask what the user needs
4. If user says "write" → write next article from docs/article-queue-extended.md
5. If user says "pin" → create and publish Pinterest pin
6. If user says "quora answer" → post next Quora answer
7. If user says "check analytics" → pull Cloudflare GraphQL data
8. If user says "check networks" → check SellHealth/MaxBounty/iHerb status
9. If user has an approval email → extract tracking links and wire them in
10. Follow the voice rules and technical notes above

## IMPORTANT CONTEXT

- User's wife's Gmail (afrozapopy85@gmail.com) owns the Search Console property
- User is in Bangladesh (Dhaka) — Bangladesh traffic shows in Cloudflare analytics
- User has Pinterest and Facebook marketing experience (his unfair advantage)
- The site targets US/UK/CA/AU primarily, EU secondarily
- CortiSync is the only live revenue product — more diversification when other networks approve
- Google sandbox lifts ~Oct 2 (Day 21) — Search Console impressions should appear then
