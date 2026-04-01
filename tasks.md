# Bounty Tracker — Scanned 2026-04-01 11:59 UTC

Source: GitHub search `bounty in:title is:issue state:open` (per_page=100, sorted by updated)
Scanner: CW1 subagent — GitHub API primary scan

---

## 🔥 NEWLY FOUND THIS SCAN (CW1)

### [NEW] aukilabs/splatter-server#5 — [Bounty | 50 USD] Generate preview images for splatter node
- **URL:** https://github.com/aukilabs/splatter-server/issues/5
- **Reward:** $50 USD
- **Difficulty:** Medium — Rust runner + Python (nerfstudio ns-render) pipeline work
- **Status:** 🟢 UNCLAIMED (no assignee)
- **Summary:** After Gaussian Splat training completes, render 2 preview images (top-down + angled ¾-view) and upload as domain artifacts alongside the .splat file. Step 1: read splat.ply bounding box → Step 2: use ns-render for 2 camera poses → Step 3: upload as splat_preview_top / splat_preview_angle → Update runner/src/lib.rs → Update README.
- **Acceptance:** 2 preview images rendered, saved to job_root_path/refined/splatter/, uploaded to domain, best-effort (warn not fail on error), README updated.

### [NEW] aukilabs/splatter-server#6 — [Bounty | 50 USD] Generate preview video for splatter node
- **URL:** https://github.com/aukilabs/splatter-server/issues/6
- **Reward:** $50 USD
- **Difficulty:** Medium — Rust runner + Python (nerfstudio ns-render) + ffmpeg pipeline
- **Status:** 🟢 UNCLAIMED (no assignee)
- **Summary:** After Gaussian Splat training completes, render a short orbital preview video (5-10s, 30fps, MP4 H.264). Compute bounding box → generate orbital camera path JSON → ns-render frames → ffmpeg encode → upload as splat_preview_video → clean up temp frames → best-effort (warn not fail).
- **Acceptance:** Orbital video rendered (270°+ at ~45° elevation), 5-10s at 30fps, H.264 MP4, uploaded to domain, frames cleaned up, README updated.

### [NEW] illbnm/homelab-stack#13 — [BOUNTY $80] Notifications — Gotify + Apprise
- **URL:** https://github.com/illbnm/homelab-stack/issues/13
- **Reward:** $80 USDT
- **Difficulty:** Medium — Docker/homelab stack setup
- **Status:** 🟢 UNCLAIMED (no assignee, 138 comments)
- **Summary:** Implement unified notification center with ntfy + Gotify. Configure server.yml, write scripts/notify.sh wrapper, configure Alertmanager webhook, integrate Watchtower/Gitea/HomeAssistant/UptimeKuma. Requires ntfy Web UI + mobile push + notify.sh script + all service integrations + README.
- **Acceptance:** ntfy UI accessible, mobile push works, notify.sh works, Alertmanager+Watchtower notifications fire, README complete.

### [NEW] illbnm/homelab-stack#2 — [BOUNTY $160] Media Stack — Jellyfin + Sonarr + Radarr + qBittorrent
- **URL:** https://github.com/illbnm/homelab-stack/issues/2
- **Reward:** $160 USD
- **Difficulty:** Medium-Hard — Docker homelab media stack
- **Status:** 🟢 UNCLAIMED (no assignee)
- **Labels:** bounty, medium
- **Summary:** Full media stack setup with Docker Compose.

### [NEW] fredldotme/ISODriveUT#12 — [Bounty: $50 USD]
- **URL:** https://github.com/fredldotme/ISODriveUT/issues/12
- **Reward:** $50 USD (~49 EUR via PayPal)
- **Difficulty:** Unknown — mobile app (Ubuntu Touch)
- **Status:** 🟢 UNCLAIMED (no assignee, 13 comments)
- **Summary:** Allow custom mount paths (/documents/iso or /documents/flashdrive) and support .img file mounting like a flash drive on Ubuntu Touch. Boot .img files like opnsense.
- **Note:** Repo is for Ubuntu Touch — requires mobile Linux dev environment.

### [NEW] microg/GmsCore#2994 — [BOUNTY] RCS Support [14999$]
- **URL:** https://github.com/microg/GmsCore/issues/2994
- **Reward:** $14,999 (label confirms bounty)
- **Difficulty:** Very Hard — Android/RCS/Android framework work
- **Status:** 🟢 UNCLAIMED (no assignee)
- **Labels:** bounty (green), enhancement
- **Summary:** Enable Google Messages + microG to use RCS functionality. Requires implementing missing components in microG for RCS authentication/attestation. No rooting/Magisk allowed, must work on locked bootloader. Compatibility with recent Google Messages versions desired.
- **Warning:** Very complex (313 comments, massive scope). Only worth attempting if you have deep Android/microG expertise.

### [NEW] Scottcjn/rustchain-bounties#2274 — [Bounty: 50 RTC] CVPR 2026 Human Evaluation
- **URL:** https://github.com/Scottcjn/rustchain-bounties/issues/2274
- **Reward:** 50 RTC (~$5 USD)
- **Difficulty:** Easy — human evaluation, no coding
- **Status:** 🟢 UNCLAIMED (no assignee)
- **Deadline:** April 3, 2026 — first 5 qualified evaluators
- **Requirements:** LLM/AI or computer vision/video generation background OR visual design/animation background.
- **Summary:** Watch 14 blinded video pairs (~30 min), answer 3 questions per pair (which looks better / more expressive / preference). Apply by commenting on main issue with your qualifications.
- **Note:** Very small reward but extremely easy task with deadline.

---

## 📋 Existing Tasks (from other scanners)

> The following tasks are already tracked — see previous scanner outputs for full details.

### High-Value USD Bounties (≥$200, already in tracker)

| # | Repo | Issue | Reward | Status | Notes |
|---|---|---|---|---|---|
| 1 | devpool-directory#5850 | UUSD+UBQ token integration | $2,400 | 🟢 UNCLAIMED | DeFi, urgent |
| 2 | devpool-directory#5916 | UbiquityOS Sprint Dashboard | $1,800 | 🟢 UNCLAIMED | Full-stack |
| 3 | devpool-directory#5935 | Plugin build artifacts RFC | $1,200 | 🟢 UNCLAIMED | 3-week timeline |
| 4 | devpool-directory#5931 | Liquity V1 Stability Pool | $1,200 | 🟢 UNCLAIMED | Urgent deadline |
| 5 | devpool-directory#5875 | CowSwap Integration | $1,200 | 🟢 UNCLAIMED | DeFi |
| 6 | devpool-directory#4999 | Knip+Jest reusable workflows | $1,200 | 🟢 UNCLAIMED | TypeScript/Node CI |
| 7 | devpool-directory#5019 | GitHub Decoupling | $1,200 | 🟢 UNCLAIMED | Ubiquity OS core |
| 8 | devpool-directory#5070 | DevPool Matchmaking UI | $900 | 🟢 UNCLAIMED | Short deadline |
| 9 | devpool-directory#5064 | Nomic Embeddings | $900 | 🟢 UNCLAIMED | ML embeddings |
| 10 | devpool-directory#5017 | Automatic Transfer | $600 | 🟢 UNCLAIMED | Permit generation |
| 11 | devpool-directory#5041 | Launch campaign L1s/L2s | $600 | 🟢 UNCLAIMED | BD/sales |
| 12 | devpool-directory#5925 | L1/L2 GitHub campaign | $600 | 🟢 UNCLAIMED | BD |
| 13 | devpool-directory#5002 | Arbitrage bot | $600 | 🟢 UNCLAIMED | Hard |
| 14 | devpool-directory#5844 | Governance token emissions | $600 | 🟢 UNCLAIMED | Smart contracts |
| 15 | devpool-directory#5846 | Security monitoring | $600 | 🟢 UNCLAIMED | Security |
| 16 | devpool-directory#5841 | Unified Authentication | $600 | 🟢 UNCLAIMED | Auth system |
| 17 | devpool-directory#5012 | Differential Reward Distribution | $600 | 🟢 UNCLAIMED | Reward logic |
| 18 | devpool-directory#5007 | Specialized Prompts | $600 | 🟢 UNCLAIMED | Prompt engineering |
| 19 | devpool-directory#5066 | Cow Swap Cash Out | $600 | 🟢 UNCLAIMED | DeFi |
| 20 | devpool-directory#4996 | Import Nonces | $600 | 🟢 UNCLAIMED | Permit3 |
| 21 | devpool-directory#5899 | All Branches Previews | $600 | 🟢 UNCLAIMED | Deno deploy |
| 22 | devpool-directory#5877 | command-plan plugin | $600 | 🟢 UNCLAIMED | Plugin dev |
| 23 | devpool-directory#5043 | Callbacks/event handlers | $300 | 🚀 IN PROGRESS | PR #338 |
| 24 | devpool-directory#5886 | Plugin health monitor | $450 | 🟢 UNCLAIMED | 4 hours |
| 25 | devpool-directory#5022 | Auto Time label | $450 | 🟢 UNCLAIMED | 4 hours |
| 26 | devpool-directory#5896 | Wrong Config fix | $450 | 🟢 UNCLAIMED | 4 hours |
| 27 | devpool-directory#5042 | Review Incentive calculations | $450 | 🟢 UNCLAIMED | 4 hours |
| 28 | devpool-directory#5940 | GraphQL PR lookups | $375 | 🟢 UNCLAIMED | 1 hour |
| 29 | devpool-directory#5005 | Agent bridge kernel | $225 | 🟢 UNCLAIMED | 2 hours |
| 30 | devpool-directory#5025 | Retry + token limits | $225 | 🟢 UNCLAIMED | 2 hours |
| 31 | devpool-directory#5044 | Permit batch claiming | $225 | 🟢 UNCLAIMED | 2 hours |
| 32 | devpool-directory#5902 | General OS improvements | $600 | 🟢 UNCLAIMED | Medium-Hard |

### Already In Progress

| # | Repo | Issue | Reward | PR | Status |
|---|---|---|---|---|---|
| 1 | devpool-directory#5043 | Callbacks/event handlers | $300 | ubiquity-os/ubiquity-os-kernel#338 | 🚀 IN PROGRESS |

### Other Valid Bounties

| Repo | Issue | Reward | Status |
|---|---|---|---|
| lihaoyi/test | #1219 | $200 USD | 🟢 UNCLAIMED |
| claude-builders-bounty | #5 | $200 (Opire) | 🟢 UNCLAIMED |
| claude-builders-bounty | #4 | $150 (Opire) | 🟢 UNCLAIMED |
| claude-builders-bounty | #3 | $100 (Opire) | 🟢 UNCLAIMED |
| claude-builders-bounty | #2 | $75 (Opire) | 🟢 UNCLAIMED |
| claude-builders-bounty | #1 | $50 (Opire) | 🟢 UNCLAIMED |
| illbnm/homelab-stack | #7 | $130 USD | 🟢 UNCLAIMED |
| CapSoftware/Cap | #1540 | $200 USD | 🟢 UNCLAIMED |

---

## ⚠️ Skipped / Low Value / Not Worth Doing

| Issue | Reason |
|---|---|
| tenstorrent/tt-metal#32178 — $1,500 | ALREADY ASSIGNED (w1zzx) |
| ritik4ever/stellar-bounty-board#5 | ALREADY ASSIGNED (zicaiw625) |
| ResearchHub/issues#466 | ALREADY ASSIGNED (yattias) — just a UI discussion |
| evilew/GS13-Outdated#188 — $50 | LOCKED issue |
| devpool-directory#5924 — $9 | Trivial devpool bot task |
| bisq-network/growth#290 — $250 | Non-technical (podcast guest) |
| INDIGOAZUL/la-tanda-web#86 — 150 LTD | Obscure LTD token, unverified value |
| FreezingMoon/AncientBeast (various) | XTR token, obscure, 2-10 XTR each |
| privacybydesign/vcmrtd#71 | Has "bounty" in title but NO amount specified |
| boligian-peru/marketplace-service-template#149 | Someone claiming the bounty, not an active bounty listing |
| prosavp/oam9#1047 | SPAM — gambling links |
| JeremyKono/hummingbot#3 | $1k but body is empty template — VERIFY FIRST |

---

## 📊 CW1 Scan Summary

| Category | Count |
|---|---|
| New bounties found (this scan) | 8 |
| High-value $200+ unclaimed | 32+ (devpool + others) |
| Already in progress | 1 |
| Already claimed/assigned | 4 |
| Spam/garbage filtered | ~20+ |
| Total matched (API total_count) | 5,355 |

**Scanned at:** 2026-04-01 11:59 UTC
**Scanner:** CW1 subagent — GitHub API primary scan
