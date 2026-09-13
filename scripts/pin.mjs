#!/usr/bin/env node
/**
 * Pinterest auto-publisher for Naturally Restful.
 * Uses the official Pinterest API v5 with a personal access token.
 *
 * Token lives in scripts/.pinterest-token (gitignored — never commit).
 * App: "Naturally Restful Publisher" (App ID 1611322)
 *
 * Usage:
 *   node scripts/pin.mjs boards
 *   node scripts/pin.mjs --image path/pin.png --title "..." \
 *        --desc "..." --link https://naturallyrestful.xyz/... --board "Sleep Supplements"
 */
import { readFileSync, existsSync } from 'node:fs';
import { resolve, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const TOKEN_FILE = resolve(ROOT, 'scripts/.pinterest-token');
const API = 'https://api.pinterest.com/v5';

function token() {
  if (!existsSync(TOKEN_FILE)) {
    console.error('missing scripts/.pinterest-token — paste the access token from developers.pinterest.com (app Manage page) into that file');
    process.exit(1);
  }
  return readFileSync(TOKEN_FILE, 'utf8').trim();
}

async function api(path, opts = {}) {
  const res = await fetch(API + path, {
    ...opts,
    headers: { Authorization: `Bearer ${token()}`, ...(opts.headers || {}) },
  });
  const body = await res.json().catch(() => ({}));
  if (!res.ok) {
    console.error(`API ${res.status}:`, JSON.stringify(body).slice(0, 300));
    process.exit(1);
  }
  return body;
}

async function listBoards() {
  const out = [];
  let cursor;
  do {
    const q = cursor ? `?cursor=${encodeURIComponent(cursor)}&page_size=50` : '?page_size=50';
    const data = await api(`/boards${q}`);
    out.push(...(data.items || []).map((b) => ({ id: b.id, name: b.name })));
    cursor = data.bookmark;
  } while (cursor && out.length < 200);
  return out;
}

async function createPin({ image, title, desc, link, board }) {
  const boards = await listBoards();
  const boardHit = boards.find((b) => b.name.toLowerCase() === board.toLowerCase());
  if (!boardHit) {
    console.error(`board "${board}" not found. Available:`, boards.map((b) => b.name).join(' | '));
    process.exit(1);
  }
  const buf = readFileSync(image);
  const form = new FormData();
  form.append('payload', JSON.stringify({
    title: title.slice(0, 100),
    description: (desc || '').slice(0, 500),
    link,
    board_id: boardHit.id,
    media_source: { source_type: 'image', content_type: 'image/png' },
  }));
  form.append('file', new Blob([buf], { type: 'image/png' }), 'pin.png');
  const created = await api('/pins', { method: 'POST', body: form });
  console.log('PIN PUBLISHED:', `https://www.pinterest.com/pin/${created.id}/`);
  console.log(`  board: ${boardHit.name} | link: ${link}`);
  return created;
}

// ---- CLI ----
const args = process.argv.slice(2);
if (args[0] === 'boards') {
  const boards = await listBoards();
  console.log(boards.map((b) => `${b.name}\t${b.id}`).join('\n'));
  process.exit(0);
}
const flag = (name) => {
  const i = args.indexOf(`--${name}`);
  return i >= 0 ? args[i + 1] : null;
};
const image = flag('image');
const title = flag('title');
const link = flag('link');
const board = flag('board');
const desc = flag('desc');
if (!image || !title || !link || !board) {
  console.error('need --image --title --link --board (--desc optional)');
  process.exit(1);
}
await createPin({ image, title, desc, link, board });
