# Naturally Restful

Static content site for the sleep & stress supplements niche (US/UK/CA/AU audience).
Built with [Astro](https://astro.build) · hosted free on [Cloudflare Pages](https://pages.cloudflare.com) · total cost: the domain (~$2/yr on .xyz promo).

## Quick start (local)

```bash
npm install
npm run dev       # http://localhost:4321
npm run build     # production build → ./dist
```

## Deploy to Cloudflare Pages (free, ~10 minutes)

1. **Push this folder to GitHub.** Create a repo (e.g. `naturally-restful`), commit, push.
2. **Connect Cloudflare Pages.** dash.cloudflare.com → Workers & Pages → Create → Pages →
   "Connect to Git" → pick the repo.
3. **Build settings:**
   - Framework preset: **Astro** (or manual: build command `npm run build`, output dir `dist`)
   - Node version: leave default
4. **Deploy.** First deploy takes ~2 minutes. You get a free `*.pages.dev` URL immediately.
5. **Custom domain:** Pages project → Custom domains → Add `naturallyrestful.xyz`.
   If the domain's DNS is already on Cloudflare, it's one click. If you bought it elsewhere
   (Porkbun/Namecheap), either move nameservers to Cloudflare (recommended, free) or add a
   CNAME record `www`/`@` → `<your-project>.pages.dev` per the Pages instructions.
6. **Verify:** `https://naturallyrestful.xyz` loads, `https://naturallyrestful.xyz/sitemap-index.xml` shows the sitemap.

## Writing articles (the whole workflow)

1. Create `src/content/articles/my-article-slug.md`
2. Copy the frontmatter pattern from an existing article:
   ```yaml
   ---
   title: "..."
   description: "..."        # also the meta description — write it carefully
   pubDate: 2026-09-20
   type: article             # article | review | comparison
   products:                 # optional; links resolve via public/_redirects
     - name: "..."
       slug: magnesium-glycinate
       blurb: "..."
       badge: "Top Pick"     # optional
   ---
   ```
3. Write in markdown below the frontmatter. Commit + push → Cloudflare rebuilds automatically.

**Ad policy is enforced by the template:** `type: article` shows ad slots;
`review`/`comparison` pages never show ads (they're affiliate pages — mixing violates
AdSense policy). Don't fight this; it's protecting your account.

## Affiliate links (never paste raw links in articles)

All outbound affiliate links go through `/go/<slug>` redirects defined in **`public/_redirects`**.
To change an affiliate program, destination URL, or tracking: edit one line there.
Articles always reference the slug, never the destination.

## Pre-launch TODO checklist

- [ ] Buy `naturallyrestful.xyz` (~$2 first year at Porkbun — includes free WHOIS privacy)
- [ ] Get a Web3Forms access key (free, web3forms.com) → replace `YOUR-WEB3FORMS-ACCESS-KEY` in `src/pages/contact.astro`
- [ ] Create `hello@naturallyrestful.xyz` (Cloudflare Email Routing is free) → update contact + privacy pages
- [ ] Connect the email opt-in to a real provider (MailerLite/ConvertKit/Buttondown free tier) → `src/components/EmailOptin.astro`
- [ ] Replace example.com URLs in `public/_redirects` with real affiliate links (iHerb/Amazon)
- [ ] Apply: iHerb affiliates, Amazon Associates (easy approvals — start here)

## Later (in this order)

1. **Google Search Console** — add the site now, submit sitemap, verify after a few articles.
2. **Google AdSense** — apply after ~20 articles + some Search Console impressions. Paste the
   loader script where marked in `src/layouts/BaseLayout.astro`, fill the AdSlot components.
   Before serving ads to EEA/UK visitors, swap the placeholder banner for a **Google-certified
   CMP** (see note in `src/components/ConsentBanner.astro`).
3. **CPA networks** (MaxBounty-tier) — apply once the site visibly has content and traffic.
   Phone interview prep: "organic SEO content site in sleep/stress niche, US/UK traffic."
   Add 2–3 offers max, on the review/comparison templates, never on article pages with ads.

## Legal pages included (do not delete)

`/disclosure` · `/medical-disclaimer` · `/privacy` — these get you past AdSense review,
CPA network review, and FTC/ASA/EU rules. Review them yearly.

## Site structure

```
src/
  content.config.ts        # article schema (title/description/type/products)
  content/articles/        # ← your markdown articles
  layouts/BaseLayout.astro # <head>, SEO, canonical, OG tags
  components/              # header, footer, AdSlot, AffiliateBox, consent, optin
  pages/                   # home, articles, comparison, trust/legal pages
public/
  _redirects               # /go/* affiliate redirect system (edit here)
  robots.txt
docs/
  content-calendar.md      # the 24-article plan
```
