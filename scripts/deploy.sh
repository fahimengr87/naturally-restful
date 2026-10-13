#!/usr/bin/env bash
# Fail-safe deploy for Naturally Restful.
# The Oct 13 outage happened because `npm run build | tail` masked a build
# failure (pipe exit code = 0) and an empty dist/ shipped. This script makes
# that impossible: no pipes around the build, page-count gate, post-deploy
# verification. Use `npm run deploy` — never chain wrangler by hand.
set -euo pipefail
cd "$(dirname "$0")/.."

MIN_PAGES=100   # site has 121 pages; anything under 100 means the build broke
URL="https://naturallyrestful.xyz/"

echo "[1/4] Building..."
npm run build

echo "[2/4] Sanity-checking dist/..."
if [ ! -d dist ]; then echo "FAIL: dist/ does not exist — build produced nothing. Aborting."; exit 1; fi
PAGES=$(find dist -name "*.html" | wc -l | tr -d ' ')
if [ "$PAGES" -lt "$MIN_PAGES" ]; then
  echo "FAIL: only $PAGES HTML pages in dist/ (expected >= $MIN_PAGES). Half-built site — Aborting BEFORE deploy."
  exit 1
fi
echo "      $PAGES pages OK"

echo "[3/4] Deploying..."
CI=true npx wrangler pages deploy dist --project-name naturally-restful --branch main

echo "[4/4] Verifying production..."
sleep 12
if ! curl -fsS -o /dev/null "$URL"; then
  echo "FAIL: $URL did not return 200 after deploy. Check Cloudflare Pages — previous good deployment can be restored from the dashboard (Projects > naturally-restful > Deployments > ... > Rollback)."
  exit 1
fi
echo "OK: $PAGES pages live at $URL"
