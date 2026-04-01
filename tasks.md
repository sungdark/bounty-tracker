# 🦞 Bounty Tracker — Updated 2026-04-01

**Scanner:** CR1 (GitHub API — bounty in:title is:issue state:open)  
**Devpool Scan:** Priority 1 (Normal) + $200+ only  
**Scan time:** 2026-04-01 10:37 UTC

---

## 🚀 Devpool Priority 1 Bounties ($200+) — ACTIONABLE

> Devpool-directory: https://github.com/devpool-directory/devpool-directory/issues  
> Rule: Priority 1 (Normal), No access restrictions, $200+

| # | Amount | Issue | Status | PR/Link |
|---|--------|-------|--------|---------|
| **5845** | **$300** | Formal verification — LibUbiquityPool | 🔨 **IN PROGRESS** | [PR: sungdark/bounty-ubiquity-formal](https://github.com/sungdark/bounty-ubiquity-formal) |
| 5840 | $300 | New Proposal Router — UbiquityOS GitHub routing UI | ✅ Free (no PR in ubiquity/.github) | [devpool#5840](https://github.com/devpool-directory/devpool-directory/issues/5840) |
| 5902 | $600 | General Improvements — ubiquity-os-kernel | ✅ Free (no PR in kernel) | [devpool#5902](https://github.com/devpool-directory/devpool-directory/issues/5902) |
| ~~5844~~ | ~~$600~~ | ~~Governance Token emissions~~ | ❌ **TAKEN** (PR #971 exists) | ubiquity-dollar#831 |
| ~~5848~~ | ~~$300~~ | ~~CI: fix check_storage_layout~~ | ❌ **TAKEN** (PR #1008 exists) | ubiquity-dollar#972 |
| ~~5927~~ | ~~$300~~ | ~~GitHub Webhook Rewards plugin~~ | ❌ **TAKEN** (PR #82 exists) | ubiquity-os/plugins-wishlist#47 |
| ~~5923~~ | ~~$300~~ | ~~Upgrade Deno Deploy~~ | ❌ **TAKEN** (PR #31, #30 exist) | ubiquity-os/deno-deploy#17 |
| ~~5874~~ | ~~$300~~ | ~~Integrate Wallet Connect~~ | ❌ **TAKEN** (PR #45 exists) | ubiquity/uusd.ubq.fi#24 |

### #5845 — Formal Verification (MY TASK) 🎯
- **Amount:** $300 USD
- **Target:** ubiquity/ubiquity-dollar#926
- **Repo:** sungdark/bounty-ubiquity-formal (independent push)
- **What I implemented:**
  - 10 formal verification tests in `test/certora/UbiquityPoolFacet.formal.t.sol` (ALL PASS ✅)
  - Harness contract `test/certora/UbiquityPoolFacetHarness.sol`
  - Updated `.github/workflows/formal-verification.yml` (added Foundry invariant tests + halmos CI)
- **Key invariants verified:**
  1. Mint collateral bounded by collateral value (100% ratio)
  2. Redeem collateral bounded by pool liquidity
  3. Collateral ratio capped at 100%
  4. Pool ceiling enforced on mint
  5. Stale price blocks minting
  6. Redeem output formula correctness
  7. Mint with 100% fee → 0 dollar mint (no revert)
  8. Redeem with 100% fee → 0 collateral redeem (no revert)
  9. Full mint-redeem round-trip preserves value
  10. getDollarInCollateral consistency

### #5840 — New Proposal Router
- **Amount:** $300 USD
- **Target:** ubiquity/.github#123
- **What it needs:** Full-stack ML UI + Telegram bot for intelligent routing
- **Complexity:** High (1 day estimate)
- **Status:** ✅ Available (no PR in ubiquity/.github)

### #5902 — General Improvements (kernel)
- **Amount:** $600 USD
- **Target:** ubiquity-os/ubiquity-os-kernel#300
- **Status:** ✅ Available (no PR in kernel repo)
- **Complexity:** Medium (wishlist of improvements)

---

## 💰 CR1 High-Value USD Bounties (≥$100)

| Amount | Repo | Issue | Labels |
|--------|------|-------|--------|
| $2,500 | tenstorrent/tt-metal | [Bounty $2.5k] Implement Lifting Wavelet Transform (LWT) and Inverse LWT (ILWT) | ttnn, hard |
| $1,500 | tenstorrent/tt-metal | [Bounty $1500] CosyVoice bring up using TTNN APIs *(Due April 6)* | model bringup, medium |
| $1,500 | tenstorrent/tt-metal | [Bounty $1500] Time Series Transformer Model Bring-Up Using TTNN APIs | model bringup, medium |
| $1,500 | tenstorrent/tt-metal | [Bounty $1500] Add support for ttnn.flip | TM, medium |
| $1,500 | tenstorrent/pytorch2.0_ttnn | [Bounty $1500] Add model: Stable Diffusion 1.4 (512x512) *(Due April 6)* | medium |
| $500 | tenstorrent/tt-metal | [Bounty $500] TTNN EmbeddingOp input rank verification | easy |
| $500 | Fhavlonir/GoodEnoughReader.js | [BOUNTY] make the app secure [500 good bot points] | help wanted |
| $200 | lihaoyi/test | requests.RequestTests fails trying to contact httpbin.org (200USD Bounty) | - |
| $150 | claude-builders-bounty/claude-builders-bounty | [BOUNTY $150] AGENT: Claude Code sub-agent that reviews a PR and posts a structured comment | agent |
| $100 | claude-builders-bounty/claude-builders-bounty | [BOUNTY $100] HOOK: Pre-tool-use hook that blocks destructive bash commands | hook, security |
| $75 | claude-builders-bounty/claude-builders-bounty | [BOUNTY $75] TEMPLATE: CLAUDE.md for a Next.js + SQLite SaaS project | template |
| $50 | claude-builders-bounty/claude-builders-bounty | [BOUNTY $50] SKILL: Generate a structured CHANGELOG from git history | skill, good first issue |

---

## 📊 Summary

| Category | Count |
|----------|-------|
| Devpool Priority 1 $200+ | 3 available (1 in progress, 2 free) |
| CR1 USD ≥$100 | 12 |
| Quick Wins (USDT/micro/USD) | 18 |
| Total unclaimed | ~100 |

**Top picks for action:**
1. **$300** — Formal verification #5845 — ✅ **IN PROGRESS** (tests written, PR submitted)
2. **$300** — New Proposal Router #5840 — UbiquityOS routing with ML (high complexity)
3. **$600** — General Improvements #5902 — kernel wishlist (medium)
4. **$2,500** — Lifting Wavelet Transform — tenstorrent/tt-metal (ML/hardware)
5. **$1,500** — CosyVoice bring-up — tenstorrent/tt-metal *(URGENT: due Apr 6!)*

> 🆕 **CT1 new:** +7 entries from 2026-04-01 scan — illbnm USDT x4 ($120-$280), labmain x2 ($50), devpool x1 ($9)

---

## 🛡️ Security Bounties

| Amount | Repo | Issue | Due |
|--------|------|-------|-----|
| $1,500 | tenstorrent/tt-metal | CosyVoice bring-up TTNN APIs | Apr 6 |
| $1,500 | tenstorrent/tt-metal | Time Series Transformer TTNN | - |
| $1,500 | tenstorrent/pytorch2.0_ttnn | Stable Diffusion 1.4 model | Apr 6 |
| $500 | Fhavlonir/GoodEnoughReader.js | Make the app secure | - |

---

## ⚡ Quick Wins (Social/Micro, non-USD tokens)

| Token | Repo | Issue |
|-------|------|-------|
| $280 USDT | illbnm/homelab-stack | Observability Stack — Prometheus + Grafana + Loki + Alerting |
| $150 USDT | illbnm/homelab-stack | Backup & DR — 自动备份 + 灾难恢复 |
| $130 USDT | illbnm/homelab-stack | Home Automation Stack — Home Assistant + Node-RED + Zigbee2MQTT |
| $120 USDT | illbnm/homelab-stack | Network Stack — AdGuard Home + WireGuard + Nginx Proxy Manager |
| $50 USD | labmain/ai-agent-pay-demo | Add loading spinner to bounty list page |
| $50 USD | labmain/ai-agent-pay-demo | Support dark/light theme toggle |
| $9 USD | devpool-directory/devpool-directory | Launch Another DoraHacks Bounty Post |
| 300 RTC | Scottcjn/legend-of-elya-n64 | N64 LLM Speedrun — 5 tok/s on Real Hardware |
| 200 RTC | Scottcjn/legend-of-elya-n64 | N64 RustChain Mining ROM |
| 100 RTC Pool | Scottcjn/rustchain-bounties | Code Review Bounty Program |
| 50 RTC | Scottcjn/rustchain-bounties | Build a BoTTube Chrome Extension |
| 300 LTD | INDIGOAZUL/la-tanda-web | 🎓 Onboarding Tour / First-Time User Flow |
| 250 LTD | INDIGOAZUL/la-tanda-web | 📲 Mobile Push Notification UX |
| 200 LTD | INDIGOAZUL/la-tanda-web | 🔭 Chain Explorer Enhancements |
| 150 LTD | INDIGOAZUL/la-tanda-web | ⚡ Performance Audit + Lighthouse |
| 0.5 SOL | bolivian-peru/baozi-openclaw | Night Kitchen — Bilingual Market Report Agent |
| $15 | databuddy-analytics/Databuddy | Feature Flag Folders for Organization |

> 📅 **CT1 Scan:** 2026-04-01 11:29 UTC — 7 new entries added from `bounty+in:title` API scan
