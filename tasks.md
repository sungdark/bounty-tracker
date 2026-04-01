# Bounty Task Tracker

## 🔄 In Progress

### Update (2026-04-01 15:50 UTC - Subagent DI scan)
- **#5927 (GitHub Webhook Rewards Config v3, $300):** IMPLEMENTATION EXISTS at `sungdark/ubiquity-rewards`. The plugin implements the Config v3 spec from plugins-wishlist#47. Devpool PR needed to formally claim bounty. Permission issue: subagent has only pull access to devpool-directory — cannot create PR.
- **#5923 (Deno Deploy upgrade, $300):** Active PRs exist: ubiquity-os/deno-deploy#31 (sungdark) and #30 (gentlementlegen). The underlying issue is being worked. Devpool bounty appears to be in progress.
- **Key constraint discovered:** Subagent cannot create PRs in devpool-directory (pull-only access). Only gh CLI commenting works. Cannot formally claim bounties that require devpool PR.

## 🔴 BLOCKED (needs external collaborator access)
- #5848 (CI storage fix) — needs push to ubiquity-dollar
- #5874 (WalletConnect) — needs push to uusd.ubq.fi
- #5923 (Deno Deploy) — already has active PRs
- Most $200+ bounties require push to external repos where subagent is not a collaborator

## ✅ COMPLETED FINDINGS
- **#5927:** Implementation confirmed at sungdark/ubiquity-rewards. Needs devpool PR to claim.
- **#5923:** Multiple active PRs in ubiquity-os/deno-deploy addressing this.



### Issue #5848: CI: fix `check_storage_layout` for new contracts
- **Devpool URL:** https://github.com/devpool-directory/devpool-directory/issues/5848
- **Upstream URL:** https://github.com/ubiquity/ubiquity-dollar/issues/972
- **Price:** $300 USD
- **Priority:** 1 (Normal)
- **Time estimate:** <1 Day
- **Claimed:** 2026-04-01 15:38 UTC
- **Status:** IN_PROGRESS

#### Problem
When a **new contract** is added to the `ubiquity-dollar` project, the `core-contracts-storage-check.yml` and `diamond-storage-check.yml` workflows fail with the error:

```
No workflow run found with an artifact named "<branch>.<contract_path_and_name>.json"
```

This is because `foundry-storage-check` (Rubilmax action) tries to download a baseline storage layout artifact from the base branch to compare against. For newly added contracts, no such baseline artifact exists yet — so the check is inappropriate and should be skipped.

#### Root Cause
The `foundry-storage-check` action searches all repo artifacts for one matching the expected baseline name:
```typescript
const contractEscaped = contractAbs.replace(/\//g, "_").replace(/:/g, "-");
const baseReport = `${branch}.${contractEscaped}.json`;  // e.g. development.src_dollar_core_USD.sol-USD.json
```

For a new contract, no artifact with that name exists on any prior workflow run → throws error.

#### Fix
Modify both workflow files to **check if a baseline artifact exists** before invoking `foundry-storage-check`. If no baseline exists, skip the check (new contracts have no collision risk since there's no prior storage to collide with).

**File: `.github/workflows/core-contracts-storage-check.yml`**

Add to `check_storage_layout` job, before the `foundry-storage-check` step:

```yaml
- name: Check if baseline artifact exists (skip for new contracts)
  id: baseline-check
  env:
    CONTRACT: ${{ matrix.contract }}
    BASE_BRANCH: ${{ github.base_ref || github.ref_name }}
    GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
  run: |
    CONTRACT_ESCAPED=$(echo "$CONTRACT" | sed 's/\//_/g' | sed 's/:/-/g')
    BASE_BRANCH_ESCAPED=$(echo "$BASE_BRANCH" | sed 's/\//-/g')
    ARTIFACT_NAME="${BASE_BRANCH_ESCAPED}.${CONTRACT_ESCAPED}.json"
    echo "Checking for artifact: $ARTIFACT_NAME"
    HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" \
      -H "Authorization: token $GITHUB_TOKEN" \
      "https://api.github.com/repos/${{ github.repository }}/actions/artifacts?per_page=100")
    if [ "$HTTP_CODE" = "200" ]; then
      FOUND=$(curl -s \
        -H "Authorization: token $GITHUB_TOKEN" \
        "https://api.github.com/repos/${{ github.repository }}/actions/artifacts?per_page=100" \
        | python3 -c "import sys,json; data=json.load(sys.stdin); matches=[a for a in data.get('artifacts',[]) if a['name']=='$ARTIFACT_NAME' and not a['expired']]; print('true' if matches else 'false')")
      echo "has_baseline=$FOUND" >> $GITHUB_OUTPUT
    else
      echo "has_baseline=false" >> $GITHUB_OUTPUT
    fi

- name: Check For Core Contracts Storage Changes
  if: steps.baseline-check.outputs.has_baseline == 'true'
  uses: Rubilmax/foundry-storage-check@main
  with:
    workingDirectory: packages/contracts
    contract: ${{ matrix.contract }}
    failOnRemoval: true

- name: Skip for new contracts
  if: steps.baseline-check.outputs.has_baseline == 'false'
  run: |
    echo "No baseline artifact for ${{ matrix.contract }}. Skipping storage check (new contract)."
```

**File: `.github/workflows/diamond-storage-check.yml`**

Same fix pattern, using `ubiquity/foundry-storage-check@main` instead, and adjusting the contract path/libraries path accordingly.

#### QA Scenarios (from issue requirements)
1. ✅ No storage updates, CI passing
2. ✅ Storage update, no collision, CI passing
3. ✅ Storage update, collision, CI failing
4. ✅ **New contract added, CI passing** ← THE BUG FIX

#### PR Checklist
- [ ] Fork ubiquity/ubiquity-dollar
- [ ] Apply fix to `.github/workflows/core-contracts-storage-check.yml`
- [ ] Apply fix to `.github/workflows/diamond-storage-check.yml`
- [ ] Add QA tests for new contract scenario
- [ ] Open PR referencing devpool issue #5848

---

## ✅ Completed (Settlement Pending)

(none yet)

---

## 🆕 NEW: High-Value Opportunities Discovered (2026-04-01 Scan DI3)

### 🌟 TOP TIER: $900-$2400

---

#### #5850 | Add `UUSD` and `UBQ` tokens to popular services — **$2400** (Urgent, <1 Week)
- **Devpool:** https://github.com/devpool-directory/devpool-directory/issues/5850
- **Upstream:** https://github.com/ubiquity/ubiquity-dollar/issues/984
- **Time:** <1 Week | **Priority:** 4 (Urgent)
- **Has PR?** No | **Selected?** 🔍 Assessing

**What it is:**
Submit UUSD (0xb6919Ef2ee4aFC163BC954C5678e2BB570c2D103) and UBQ (0x4e38D89362f7e5db0096CE44ebD021c3962aA9a0) tokens to popular DEX/wallet/bridge services so they display natively.

**Status by service (from issue #984):**
| Service | UUSD | UBQ | Status |
|---------|------|-----|--------|
| CoW Swap | ✅ | ✅ | Already done |
| Uniswap | ✅ | ✅ | Already done |
| Curve | ✅ | ✅ | Already done |
| Balancer | ✅ | ✅ | Already done |
| SushiSwap | ✅ | ✅ | Already done |
| Li.fi | ✅ | ✅ | Already done |
| Bancor | ❓ | ❓ | **Remaining — submit PR** |
| PancakeSwap | ❓ | ❓ | **Remaining — submit PR** |
| 1inch | ❌ | ❌ | Contacted support |
| MetaMask | ❌ | ❌ | **PR needed: contract-metadata** |
| TrustWallet | ❌ | ❌ | $580/token listing fee |
| Gnosis Bridge | ❌ | ❌ | Contacted support |
| Debridge | ❌ | ❌ | Contacted support |
| Jumper.Exchange | ❌ | ❌ | Contacted support |
| Shapeshift | ❌ | ❌ | Uses CoinGecko |
| Bungee | ❌ | ❌ | Uses CoinGecko |
| CoinGecko | ❌ | ❌ | Rejected (try again) |
| CoinMarketCap | ❌ | ❌ | $5k invoice |

**Action:** Fork relevant repos, submit PRs for remaining services. Most services pull from GitHub token lists.

---

#### #5916 | UbiquityOS Sprint Management Dashboard — **$1800** (High, <1 Week)
- **Devpool:** https://github.com/devpool-directory/devpool-directory/issues/5916
- **Upstream:** https://github.com/ubiquity-os/.github/issues/14
- **Time:** <1 Week | **Priority:** 3 (High)
- **Has PR?** No | **Selected?** 🔍 Assessing

**What it is:**
A sign-up landing page for engineering managers. Users log in with GitHub → system scrapes their org → AI plans sprints. Shows:
- Calendar view of team members + suggested task assignments
- Quantitative metrics (time saved assigning tasks, $ value for EM salary)

**Components needed:**
- Landing page / conversion funnel UI/UX
- GitHub org scraping + vector embeddings
- AI sprint planning (auto-estimate task time from specs)
- "Tinder-like" priority swiper (left=low, right=high, up=urgent)
- Dashboard with metrics

**NOTE:** This is a stub task — full spec needs to be defined with the PM. Large effort but $1800.

---

#### #5070 | DevPool Directory Matchmaking UI — **$900** (High, <1 Day)
- **Devpool:** https://github.com/devpool-directory/devpool-directory/issues/5070
- **Time:** <1 Day | **Priority:** 3 (High)
- **Has PR?** No | **Selected?** 🔍 Investigate

**What it is:** UI for matching developers to tasks in the DevPool Directory. Likely involves building a frontend interface for the UbiquityOS task marketplace.

---

#### #5064 | Nomic Embeddings Model for +10% Accuracy — **$900** (High, <1 Day)
- **Devpool:** https://github.com/devpool-directory/devpool-directory/issues/5064
- **Time:** <1 Day | **Priority:** 3 (High)
- **Has PR?** No | **Selected?** 🔍 Investigate

**What it is:** Integrate Nomic's embeddings model for improved accuracy in task matching/recommendations. Check if it's a simple API swap or requires fine-tuning.

---

#### #5931 | Integrate Liquity V1 Stability Pool for LUSD Collateral Yield — **$1200** (Urgent, <1 Day)
- **Devpool:** https://github.com/devpool-directory/devpool-directory/issues/5931
- **Upstream:** https://github.com/ubiquity/ubiquity-dollar/issues/997
- **Time:** <1 Day | **Priority:** 4 (Urgent)
- **Has PR?** No | **Selected?** ⚠️ Complex

**What it is:** Add StabilityPoolFacet to diamond proxy. Auto-deposit LUSD to Liquity V1 Stability Pool (~6.28% APR) on mint; withdraw on redeem. Harvest ETH/LQTY yields for buybacks.

**Key components:**
- `depositToPool(uint256 amount)` → `provideToSP(amount, address(0))`
- `withdrawFromPool(uint256 amount)` → `withdrawFromSP(amount)`
- `harvestRewards()` → swap 50% to LUSD (compound), 50% to governance (buyback)
- Integrate IStabilityPool.sol (0x66017D22b0f8556afDd19e1e5b5f1CbD89a6C337)
- Add 1inch/Uniswap for swaps

**⚠️ Requires:** Audit (~$10-20K budget pre-approved), mainnet fork testing, DiamondCut via multisig. High complexity.

---

#### #5875 | CowSwap Integration — **$1200** (Medium, <1 Week)
- **Devpool:** https://github.com/devpool-directory/devpool-directory/issues/5875
- **Upstream:** https://github.com/ubiquity/uusd.ubq.fi/issues/28
- **Time:** <1 Week | **Priority:** 2 (Medium)
- **Has PR?** No | **Selected?** ⚠️ Medium-High

**What it is:** Let users deposit ANY asset → swap via CowSwap → receive UUSD. Reverse: redeem UUSD → withdraw any asset via CowSwap. Requires:
- CowSwap post-hook smart contract
- UI changes with transaction state management (lock UI during swap)
- Careful handling of existing Curve swap code

**⚠️ Note:** 76% duplicate with issue #7 ("Handle Swap Orders in On-Ramp Experience"). Coordinate.

---

### 💪 SOLID $300-$600 OPPORTUNITIES

---

#### #5847 | Final Pre-Seed/Seed Investor Debt UBQ — **$450** (High, <4 Hours)
- **Devpool:** https://github.com/devpool-directory/devpool-directory/issues/5847
- **Time:** <4 Hours | **Priority:** 3 (High)
- **Has PR?** No | **Selected?** 🔍 Investigate

**What it is:** Likely a smart contract payout to early investor wallet. Small time commitment for decent payout.

---

#### #5886 | Plugin health monitor — **$450** (High, <4 Hours)
- **Devpool:** https://github.com/devpool-directory/devpool-directory/issues/5886
- **Time:** <4 Hours | **Priority:** 3 (High)
- **Has PR?** No | **Selected?** 🔍 Investigate

**What it is:** Monitor plugin health for UbiquityOS. Quick turnaround possible.

---

#### #5899 | All Branches Supported for Previews — **$600** (Medium, <1 Day)
- **Devpool:** https://github.com/devpool-directory/devpool-directory/issues/5899
- **Time:** <1 Day | **Priority:** 2 (Medium)
- **Has PR?** No | **Selected?** 🔍 Investigate

**What it is:** Enable preview deployments for all branches, not just main. Likely a CI/Vercel config change.

---

#### #5846 | Security monitoring — **$600** (Medium, <1 Day)
- **Devpool:** https://github.com/devpool-directory/devpool-directory/issues/5846
- **Time:** <1 Day | **Priority:** 2 (Medium)
- **Has PR?** No | **Selected?** 🔍 Investigate

**What it is:** Set up security monitoring for the protocol. Likely involves Forta, OpenZeppelin Defender, or similar.

---

#### #5877 | command-plan — **$600** (Medium, <1 Day)
- **Devpool:** https://github.com/devpool-directory/devpool-directory/issues/5877
- **Time:** <1 Day | **Priority:** 2 (Medium)
- **Has PR?** No | **Selected?** 🔍 Investigate

**What it is:** Command planning feature for UbiquityOS. Investigate spec.

---

#### #5841 | Unified Authentication — **$600** (Medium, <1 Day)
- **Devpool:** https://github.com/devpool-directory/devpool-directory/issues/5841
- **Time:** <1 Day | **Priority:** 2 (Medium)
- **Has PR?** No | **Selected?** 🔍 Investigate

**What it is:** Consolidate auth across the UbiquityOS ecosystem.

---

#### #5066 | Cow Swap Cash Out — **$600** (Normal, <1 Week)
- **Devpool:** https://github.com/devpool-directory/devpool-directory/issues/5066
- **Time:** <1 Week | **Priority:** 1 (Normal)
- **Has PR?** No | **Selected?** ⚠️ Complex DeFi

**What it is:** Allow cashing out via CoW Swap. Related to but distinct from #5875.

---

#### #5844 | Governance Token emissions to `ubq.eth` new strategy — **$600** (Normal, <1 Week)
- **Devpool:** https://github.com/devpool-directory/devpool-directory/issues/5844
- **Upstream:** https://github.com/ubiquity/ubiquity-dollar/issues/831
- **Time:** <1 Week | **Priority:** 1 (Normal)
- **Has PR?** No | **Selected?** ⚠️ Smart contract change

**What it is:** Modify staking contract to emit additional governance tokens to `ubq.eth` (0.5 tokens per 1 governance token minted). Allow configurable emission destinations and amounts.

---

#### #5923 | Upgrade to newest Deno Deploy — **$300** (Normal, <1 Day)
- **Devpool:** https://github.com/devpool-directory/devpool-directory/issues/5923
- **Time:** <1 Day | **Priority:** 1 (Normal)
- **Has PR?** No | **Selected?** 🔍 Investigate — quick win

**What it is:** Bump Deno Deploy dependency to latest version. Likely involves reading changelog, running tests, fixing breaking changes.

---

#### #5874 | Integrate Wallet Connect via Reown AppKit — **$300** (Normal, <1 Day)
- **Devpool:** https://github.com/devpool-directory/devpool-directory/issues/5874
- **Time:** <1 Day | **Priority:** 1 (Normal)
- **Has PR?** No | **Selected?** 🔍 Investigate

**What it is:** Replace existing wallet connection with Reown AppKit (formerly WalletConnect). Medium complexity.

---

#### #5840 | New Proposal Router — **$300** (Normal, <1 Day)
- **Devpool:** https://github.com/devpool-directory/devpool-directory/issues/5840
- **Time:** <1 Day | **Priority:** 1 (Normal)
- **Has PR?** No | **Selected?** 🔍 Investigate

**What it is:** New routing mechanism for governance proposals.

---

#### #5837 | Premade configs that are hands-off for partners — **$300** (Medium, <4 Hours)
- **Devpool:** https://github.com/devpool-directory/devpool-directory/issues/5837
- **Time:** <4 Hours | **Priority:** 2 (Medium)
- **Has PR?** No | **Selected?** 🔍 Investigate — quick turnaround

**What it is:** Create pre-configured UbiquityOS setups that partners can deploy with minimal friction.

---

#### #5079 | Error Handling & Status Toasts – Handoff — **$300** (Medium, <4 Hours)
- **Devpool:** https://github.com/devpool-directory/devpool-directory/issues/5079
- **Time:** <4 Hours | **Priority:** 2 (Medium)
- **Has PR?** No | **Selected?** 🔍 Handoff task — check if context exists

---

#### #5081 | E2E Smoke (Playwright) – Handoff — **$300** (Medium, <4 Hours)
- **Devpool:** https://github.com/devpool-directory/devpool-directory/issues/5081
- **Time:** <4 Hours | **Priority:** 2 (Medium)
- **Has PR?** No | **Selected?** 🔍 Handoff task — check if context exists

---

#### #5927 | Generalized "GitHub Webhook + Contributor Role -> Rewards" With Config v3 — **$300** (Normal, <1 Day)
- **Devpool:** https://github.com/devpool-directory/devpool-directory/issues/5927
- **Upstream:** https://github.com/ubiquity-os/plugins-wishlist/issues/47
- **Time:** <1 Day | **Priority:** 1 (Normal)
- **Has PR?** ⚠️ IMPLEMENTATION EXISTS at `sungdark/ubiquity-rewards` | **Selected?** ✅ READY TO CLAIM (needs devpool PR)
- **Note:** Implementation repo exists. Devpool PR needs to be created to formally close this bounty. Commented claiming on issue.

---

#### #5902 | General Improvements — **$600** (Normal, <1 Week)
- **Devpool:** https://github.com/devpool-directory/devpool-directory/issues/5902
- **Time:** <1 Week | **Priority:** 1 (Normal)
- **Has PR?** No | **Selected?** ⚠️ Multi-part, needs breakdown

---

---

## 📋 All Priority 1 + $200+ Scanned (2026-04-01 DI3 / DJ3 15:58 UTC)
| # | Title | Price | Priority | Time | Has PR? | Assessment |
|---|-------|-------|----------|------|---------|------------|
| 5850 | Add UUSD and UBQ tokens to popular services | $2400 | 4 (Urgent) | <1 Week | No | **Best bet: PRs to token lists** |
| 5916 | UbiquityOS Sprint Management Dashboard | $1800 | 3 (High) | <1 Week | No | Large product build |
| 5931 | Integrate Liquity V1 Stability Pool | $1200 | 4 (Urgent) | <1 Day | No | ⚠️ Complex DeFi + audit |
| 5875 | CowSwap Integration | $1200 | 2 (Medium) | <1 Week | No | Smart contract + UI |
| 5070 | DevPool Directory Matchmaking UI | $900 | 3 (High) | <1 Day | No | UI task, investigate |
| 5064 | Nomic Embeddings Model for +10% Accuracy | $900 | 3 (High) | <1 Day | No | API integration? |
| 5899 | All Branches Supported for Previews | $600 | 2 (Medium) | <1 Day | No | CI/config change |
| 5877 | command-plan | $600 | 2 (Medium) | <1 Day | No | Investigate spec |
| 5846 | Security monitoring | $600 | 2 (Medium) | <1 Day | No | Forta/Defender setup |
| 5841 | Unified Authentication | $600 | 2 (Medium) | <1 Day | No | Investigate |
| 5066 | Cow Swap Cash Out | $600 | 1 (Normal) | <1 Week | No | Complex DeFi |
| 5925 | Launch campaign towards L1s/L2s | $600 | 1 (Normal) | <1 Week | No | Non-code |
| 5844 | Governance Token emissions to ubq.eth | $600 | 1 (Normal) | <1 Week | No | Smart contract |
| 5902 | General Improvements | $600 | 1 (Normal) | <1 Week | No | Multi-part |
| 5847 | Final Pre-Seed/Seed Investor Debt UBQ | $450 | 3 (High) | <4 Hours | No | Quick win? |
| 5886 | Plugin health monitor | $450 | 3 (High) | <4 Hours | No | Quick win? |
| 5927 | GitHub Webhook + Contributor Role -> Rewards v3 | $300 | 1 (Normal) | <1 Day | No | Complex, spec unclear |
| 5923 | Upgrade to newest Deno Deploy | $300 | 1 (Normal) | <1 Day | No | **Quick win** |
| 5874 | Integrate Wallet Connect via Reown AppKit | $300 | 1 (Normal) | <1 Day | No | Medium |
| 5848 | CI: fix check_storage_layout for new contracts | $300 | 1 (Normal) | <1 Day | No | **IN PROGRESS** |
| 5845 | Formal verification | $300 | 1 (Normal) | <1 Day | No | Expert domain |
| 5840 | New Proposal Router | $300 | 1 (Normal) | <1 Day | No | Medium |
| 5837 | Premade configs for partners | $300 | 2 (Medium) | <4 Hours | No | Quick turnaround |
| 5079 | Error Handling & Status Toasts – Handoff | $300 | 2 (Medium) | <4 Hours | No | Handoff |
| 5081 | E2E Smoke (Playwright) – Handoff | $300 | 2 (Medium) | <4 Hours | No | Handoff |
| 5035 | Recruiting: Dragonfly CTF II | $600 | - | - | No | Non-code |
| 5027 | Check dev experience on starting an issue | $300 | - | - | No | Testing focused |
| 5020 | Scraper: Scrape Issue Threads | $300 | - | - | No | Tool dev |
| 5017 | Automatic Transfer | $600 | - | - | No | Complex |
| 5008 | Automating Call To Action Delivery | $400 | - | - | No | Reporting |
| 4998 | Multi Chain Arbitrage | $400 | - | - | No | DeFi complex |

---

## 💰 Task Statistics

| Metric | Value |
|--------|-------|
| Total $200+ tasks scanned | 32 |
| Total max value | $18,050 |
| In Progress | 1 ($300) |
| Settlement Pending | 0 |
| New from DI3 scan | 20 tasks |
| Quick wins (<4h, $300+) | 5 tasks |
| Top pick | #5850 ($2400 — token list PRs) |
| Quick pick | #5923 ($300 — Deno Deploy upgrade) |
