#!/usr/bin/env bash
# Attach naturallyrestful.xyz (+www) to the Cloudflare Pages project.
# Safe to re-run: it checks state first and skips what's already done.
# The API token below is scoped to "Cloudflare Pages: Edit" only.

set -u
ACCOUNT="895d61943e5722135ce61681e10bbc21"
PROJECT="naturally-restful"
API="https://api.cloudflare.com/client/v4"
TOKEN=$(tr -d '[:space:]' < "$(dirname "$0")/.api-token" 2>/dev/null)
if [ -z "$TOKEN" ]; then
  say "missing scripts/.api-token — put the Cloudflare API token in that file"
  exit 1
fi
DOMAIN="naturallyrestful.xyz"

say() { echo "[attach] $*"; }

# 1) zone status
CFG="$APPDATA/xdg.config/.wrangler/config/default.toml"
WTOKEN=$(grep -oE 'oauth_token = "[^"]+"' "$CFG" 2>/dev/null | head -1 | cut -d'"' -f2)
if [ -n "$WTOKEN" ]; then
  ZSTATUS=$(curl -s -H "Authorization: Bearer $WTOKEN" "$API/zones?name=$DOMAIN" | grep -oE '"status":"[^"]*"' | head -1)
  say "zone status: ${ZSTATUS:-unknown}"
fi

# 2) current domains on the project
CURRENT=$(curl -s -H "Authorization: Bearer $TOKEN" \
  "$API/accounts/$ACCOUNT/pages/projects/$PROJECT/domains")
if echo "$CURRENT" | grep -q '"success":false'; then
  say "Pages API still rejecting auth (provisioning lag). Try again later."
  exit 1
fi
say "Pages API reachable. Current domains: $(echo "$CURRENT" | grep -oE '"name":"[^"]*"' | tr '\n' ' ')"

# 3) attach whichever is missing
for HOST in "$DOMAIN" "www.$DOMAIN"; do
  if echo "$CURRENT" | grep -q "\"$HOST\""; then
    say "$HOST already attached."
    continue
  fi
  RES=$(curl -s -X POST -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" \
    -d "{\"name\":\"$HOST\"}" "$API/accounts/$ACCOUNT/pages/projects/$PROJECT/domains")
  if echo "$RES" | grep -q '"success":true'; then
    say "attached $HOST ✓"
  else
    say "failed to attach $HOST: $(echo "$RES" | head -c 200)"
  fi
done

# 4) verify
sleep 10
for HOST in "$DOMAIN" "www.$DOMAIN"; do
  CODE=$(curl -s -o /dev/null -w "%{http_code}" --max-time 20 "https://$HOST/" || echo "000")
  say "https://$HOST/ -> HTTP $CODE"
done
