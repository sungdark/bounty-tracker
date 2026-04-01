# Bounty Task Tracker

## 🆕 NEW OPPORTUNITIES (DL1 scan - 2026-04-01 16:17 UTC)

### Issue claude-builders-bounty#4: AGENT — Claude Code PR Reviewer
- **URL:** https://github.com/claude-builders-bounty/claude-builders-bounty/issues/4
- **Price:** $150 USD (via Opire)
- **Priority:** 2 (High)
- **Time estimate:** <1 Day
- **Status:** NEW - NOT CLAIMED

#### Summary
Create a Claude Code agent that takes a PR diff, analyzes it, and returns structured Markdown review.
- CLI: `claude-review --pr https://github.com/owner/repo/pull/123`
- OR GitHub Action workflow YAML
- Output: Summary, risks, suggestions, confidence score
- Must be tested on 2 real PRs with outputs included

#### Feasibility Assessment
- Self-contained: just needs a CLAUDE.md skill + test outputs
- Requires Opire account (/opire try comment to claim)
- Payment auto-released on merge ✅
- **ACTIONABLE NOW** - can build independently

### Issue claude-builders-bounty#3: HOOK — Pre-tool-use Destructive Bash Blocker
- **URL:** https://github.com/claude-builders-bounty/claude-builders-bounty/issues/3
- **Price:** $100 USD (via Opire)
- **Priority:** 2 (High)
- **Time estimate:** <1 Day
- **Status:** NEW - NOT CLAIMED

#### Summary
Claude Code pre-tool-use hook in Python/bash that blocks destructive commands.
- Hooks path: `~/.claude/hooks/`
- Blocks: `rm -rf`, `DROP TABLE`, `git push --force`, `TRUNCATE`, `DELETE FROM` without WHERE
- Logs blocked attempts to `~/.claude/hooks/blocked.log`
- README with install in 2 commands

#### Feasibility Assessment
- Pure script: no external dependencies needed
- Requires Opire account (/opire try to claim)
- **ACTIONABLE NOW** - straightforward implementation

### Issue claude-builders-bounty#2: TEMPLATE — CLAUDE.md for Next.js + SQLite SaaS
- **URL:** https://github.com/claude-builders-bounty/claude-builders-bounty/issues/2
- **Price:** $75 USD (via Opire)
- **Priority:** 3 (Medium)
- **Time estimate:** <1 Day
- **Status:** NEW - NOT CLAIMED

#### Summary
Production-ready CLAUDE.md for Next.js 15 App Router + SQLite (better-sqlite3 or Turso).
- Stack & versions, folder structure, DB migration rules
- Component patterns, anti-patterns
- Must be tested on greenfield project

#### Feasibility Assessment
- Writing task, no code to run
- Requires Opire account
- **ACTIONABLE NOW** - pure documentation work

### Issue claude-builders-bounty#1: SKILL — Generate CHANGELOG from git history
- **URL:** https://github.com/claude-builders-bounty/claude-builders-bounty/issues/1
- **Price:** $50 USD (via Opire)
- **Priority:** 4 (Low)
- **Time estimate:** <1 Day
- **Status:** NEW - NOT CLAIMED

#### Summary
Claude Code skill (SKILL.md) or bash script that auto-generates a structured CHANGELOG from git history.
- Parses commits, groups by type (feat/fix/docs)
- Outputs conventional changelog format
- README with usage

#### Feasibility Assessment
- Writing + scripting task
- Requires Opire account
- Low reward but quick to implement

---

## 🆕 NEW OPPORTUNITIES (DK3 scan - 2026-04-01 16:07 UTC)

### Issue #5916: UbiquityOS Sprint Management Dashboard
- **Devpool URL:** https://github.com/devpool-directory/devpool-directory/issues/5916
- **Upstream URL:** https://github.com/ubiquity-os/.github/issues/14
- **Price:** $1800 USD
- **Priority:** 3 (High)
- **Time estimate:** <1 Week
- **Status:** NEW - NOT CLAIMED

#### Summary
Build a UbiquityOS Sprint Management Dashboard for AI team managers. The vision:
1. Backend for landing page + GitHub OAuth org scraping
2. Calendar view of team members and their task assignments (with priority levels)
3. Quantitative metrics showing time/dollar savings from automated task assignment
4. Import from Asana, Linear, etc. for larger backlogs
5. A Tinder-like swipe UI for quickly setting task priority (left=low, right=high, up=urgent)

#### Feasibility Assessment
- This is a complex full-stack project (landing page + dashboard + GitHub API integration)
- Requires building a new plugin/repo, not just a PR to existing upstream
- Can be independently implemented without needing push access to ubiquity-os/.github
- Recommendation: SKIP for now — too large for single bounty, recommend breaking into smaller tasks

### Issue #5931: Integrate Liquity V1 Stability Pool for LUSD Collateral Yield
- **Devpool URL:** https://github.com/devpool-directory/devpool-directory/issues/5931
- **Upstream URL:** https://github.com/ubiquity/ubiquity-dollar/issues/997
- **Price:** $1200 USD
- **Priority:** 4 (Urgent)
- **Time estimate:** <1 Day
- **Status:** NEW - NOT CLAIMED

#### Summary
Plain LUSD collateral earns 0% yield. Integrate Liquity Stability Pool (~6.28% APR) to fund governance token buybacks. Add `StabilityPoolFacet` via diamond proxy. Key functions:
- `depositToPool(uint256 amount)`: Call `provideToSP(amount, address(0))`
- `withdrawFromPool(uint256 amount)`: Call `withdrawFromSP(amount)`
- `harvestRewards()`: Claim ETH/LQTY yields, swap 50% to LUSD for compounding, 50% to governance token for buybacks

#### Flows
- **Mint**: Transfer LUSD → Deposit to pool → Mint uUSD → Update `totalPrincipalInPool += amount`
- **Redeem**: Burn uUSD → Withdraw principal → Harvest rewards → Update `totalPrincipalInPool -= amount`

#### Feasibility Assessment
- Solidtiy smart contract work on ubiquity-dollar repo
- Requires push access to ubiquity/ubiquity-dollar (subagent does not have this)
- Already has spec defined — implementation is well-scoped
- Recommendation: BLOCKED — needs collaborator access to ubiquity-dollar. Check if can be done via fork + PR.

---

## 🔄 In Progress

### Update (2026-04-01 16:07 UTC - Subagent DK3 scan)
- **#5927 (GitHub Webhook Rewards Config v3, $300):** IMPLEMENTATION EXISTS at `sungdark/ubiquity-rewards`. The plugin implements the Config v3 spec from plugins-wishlist#47. Devpool PR needed to formally claim bounty. Permission issue: subagent has only pull access to devpool-directory — cannot create PR.
- **#5923 (Deno Deploy upgrade, $300):** Active PRs exist: ubiquity-os/deno-deploy#31 (sungdark) and #30 (gentlementlegen). The underlying issue is being worked. Devpool bounty appears to be in progress.
- **#5840 (New Proposal Router, $300):** IMPLEMENTATION STARTED at `sungdark/proposal-router`. Plugin uses vector embeddings (nomic-embed-text) to route proposals to correct repos. Commented claiming on devpool issue. Upstream was previously assigned to @shiv810 but now unassigned — fair game.
- **Key constraint discovered:** Subagent cannot create PRs in devpool-directory (pull-only access). Only gh CLI commenting works. Cannot formally claim bounties that require devpool PR.

## 🔴 BLOCKED (needs external collaborator access)
- #5848 (CI storage fix) — needs push to ubiquity-dollar
- #5874 (WalletConnect) — needs push to uusd.ubq.fi
- #5923 (Deno Deploy) — already has active PRs
- #5844 (Governance Token emissions) — needs push to ubiquity-dollar
- #5931 (Liquity V1 Stability Pool, $1200) — needs push to ubiquity-dollar
- Most $200+ bounties require push to external repos where subagent is not a collaborator

## 🔄 READY TO WORK ON (independent implementation)
- #5840 (New Proposal Router) — ✅ IMPLEMENTATION STARTED at `sungdark/proposal-router`

## ✅ COMPLETED FINDINGS
- **#5927:** Implementation confirmed at sungdark/ubiquity-rewards. Needs devpool PR to claim.
- **#5923:** Multiple active PRs in ubiquity-os/deno-deploy addressing this.



### Issue #5848: CI: fix `check_storage_layout` for new contracts
- **Devpool URL:** https://github.com/devpool-directory/devpool-directory/issues/5848
- **Upstream URL:** https://github.com/ubiquity/ubiquity-dollar/issues/972
- **Price:** $300 USD
- **Priority:** 1 (Normal)
- **Time estimate:** <1 Day
- **Status:** ❌ CLAIMED BY OTHERS — open PRs #1008 and #1009 already exist in ubiquity/ubiquity-dollar

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

## Issue #5840: New Proposal Router
- **Devpool URL:** https://github.com/devpool-directory/devpool-directory/issues/5840
- **Upstream URL:** https://github.com/ubiquity/.github/issues/123
- **Price:** $300 USD
- **Priority:** 1 (Normal)
- **Time estimate:** <1 Day
- **Claimed:** 2026-04-01 16:03 UTC
- **Status:** IN_PROGRESS
- **Implementation:** https://github.com/sungdark/proposal-router

#### Problem
Users don't know which repository to file proposals in. Proposals get misfiled and require transfers.

#### Solution
A UbiquityOS plugin that:
1. Accepts natural-language proposal description
2. Generates vector embedding using nomic-embed-text
3. Matches against pre-computed repo embeddings
4. Routes to the most relevant repository

#### Architecture
```
User Input → Embedding (nomic-embed-text) → Cosine Similarity → Route
```

#### Implementation (sungdark/proposal-router)
- `src/proposal-router.ts` - ProposalRouter class + handler
- `manifest.json` - UbiquityOS plugin manifest
- `SPEC.md` - Full specification

#### Supported Repos
- `ubiquity/ubiquity-dollar`, `.github`, `ubiquity-os`
- `ubiquity-os/ubiquity-os-kernel`, `plugin-sdk`, `command-start-stop`, `log-parser`

#### TODO
- [x] Initial plugin skeleton
- [ ] Integrate with GitHub API to auto-file issues
- [ ] User feedback mechanism for corrections
- [ ] Embedding cache with TTL
- [ ] Telegram interface (DM support)

#### Notes
- Upstream was claimed by @shiv810 but is now unassigned
- Plugin needs deployment to UbiquityOS kernel
- Cannot create PR to ubiquity/.github (pull-only access)

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

---

## 🆕 Opire USD Bounties Found (2026-04-01 DK1 Scan)

> Source: GitHub search `bounty in:title is:issue state:open` → filtered for $ amounts
> All powered by [Opire](https://opire.dev) — payment auto-releases on PR merge
> **Claim method:** Comment `/opire try` on the issue, submit PR

### 🌟 $200 — WORKFLOW: n8n + Claude Code Automated Weekly Dev Summary
- **Repo:** claude-builders-bounty/claude-builders-bounty [#5](https://github.com/claude-builders-bounty/claude-builders-bounty/issues/5)
- **Price:** $200 USD
- **Difficulty:** Medium | **Time:** <1 Day | **Claimed:** No
- **What:** Complete n8n workflow that auto-generates weekly narrative summary of GitHub repo activity using Claude API
- **Acceptance Criteria:**
  - Exportable n8n workflow (.json file, importable)
  - Trigger: weekly cron (e.g., Friday 5pm)
  - Fetches from GitHub API: commits, closed issues, merged PRs for the week
  - Calls Claude API (claude-sonnet-4-20250514) to generate narrative summary
  - Delivers via email OR Discord/Slack webhook (configurable)
  - Configurable: GitHub repo, destination channel, language (EN/FR)
  - Tested on real n8n instance (include screenshot of successful execution)
  - README with setup in 5 steps or fewer
- **Action:** `/opire try` + submit PR with .json workflow + README

### 🌟 $150 — AGENT: Claude Code PR Reviewer Sub-Agent
- **Repo:** claude-builders-bounty/claude-builders-bounty [#4](https://github.com/claude-builders-bounty/claude-builders-bounty/issues/4)
- **Price:** $150 USD
- **Difficulty:** Medium | **Time:** <1 Day | **Claimed:** No
- **What:** Claude Code agent that takes a PR diff, analyzes it, posts structured Markdown review
- **Acceptance Criteria:**
  - CLI: `claude-review --pr https://github.com/owner/repo/pull/123` OR GitHub Action YAML
  - Output: Summary, risks, suggestions, confidence score (Low/Med/High)
  - Tested on 2+ real PRs (include outputs in PR)
  - README with setup + usage
- **Action:** `/opire try` + submit PR with agent + sample outputs

### 💪 $100 — HOOK: Pre-Tool-Use Destructive Bash Blocker
- **Repo:** claude-builders-bounty/claude-builders-bounty [#3](https://github.com/claude-builders-bounty/claude-builders-bounty/issues/3)
- **Price:** $100 USD
- **Difficulty:** Medium | **Time:** <1 Day | **Claimed:** No
- **What:** Claude Code pre-tool-use hook (Python/bash) that blocks dangerous commands
- **Acceptance Criteria:**
  - Blocks: `rm -rf`, `DROP TABLE`, `git push --force`, `TRUNCATE`, `DELETE FROM` without WHERE
  - Logs blocked attempts to `~/.claude/hooks/blocked.log` with timestamp + project path
  - Shows clear message to Claude explaining why blocked
  - README with install in 2 commands or fewer
- **Action:** `/opire try` + submit PR with hook + README

### 💪 $75 — TEMPLATE: CLAUDE.md for Next.js + SQLite SaaS
- **Repo:** claude-builders-bounty/claude-builders-bounty [#2](https://github.com/claude-builders-bounty/claude-builders-bounty/issues/2)
- **Price:** $75 USD
- **Difficulty:** Medium | **Time:** <1 Day | **Claimed:** No
- **What:** Opinionated, production-ready CLAUDE.md for Next.js 15 App Router + SQLite (better-sqlite3 or Turso)
- **Acceptance Criteria:**
  - Stack & versions, folder structure, SQL/migration conventions, component patterns, anti-patterns
  - Usable without modification on greenfield project
  - Tested: create new project, paste CLAUDE.md, confirm Claude Code understands context
- **Action:** `/opire try` + submit PR with CLAUDE.md

### ✅ $50 — SKILL: Generate Structured CHANGELOG from Git History
- **Repo:** claude-builders-bounty/claude-builders-bounty [#1](https://github.com/claude-builders-bounty/claude-builders-bounty/issues/1)
- **Price:** $50 USD
- **Difficulty:** Easy | **Time:** <1 Day | **Claimed:** No
- **What:** Claude Code skill (SKILL.md) or bash script generating CHANGELOG.md from git history
- **Acceptance Criteria:**
  - Works via `/generate-changelog` or `bash changelog.sh`
  - Fetches commits since last git tag
  - Auto-categorizes: Added / Fixed / Changed / Removed
  - Outputs properly formatted CHANGELOG.md
  - Tested on real repo (include sample output in PR)
  - README with setup in 3 steps or fewer
- **Action:** `/opire try` + submit PR with skill/script + README

### 🔍 Also Found (Non-USD Crypto/Token Denominated)

| Repo | Issue | Amount | Type |
|------|-------|--------|------|
| BarryThePirate/ftl-ext-sdk | [#1](https://github.com/BarryThePirate/ftl-ext-sdk/issues/1) | 1,000 Tokens | Tampermonkey/Greasemonkey userscript support |
| Scottcjn/rustchain-bounties | #2451 | 5,000 RTC | Founding Antiquity Miners program |
| Scottcjn/bottube | #159 | 200 RTC | Submit to directories (DOFOLLOW) |

> Note: RTC/token bounties excluded from USD tracker — may revisit if token value is established.

---

*DK1 scan 2026-04-01 16:10 UTC*

---

## 🆕 DK3-SUBAGENT SCAN RESULTS (2026-04-01 16:14 UTC)

### Priority 1 ($200+) Unclaimed Bounties Found:
- **#5925: "Launch campaign towards L1s/L2s for managing their GitHubs" — $600, Priority 1**
  - Devpool: https://github.com/devpool-directory/devpool-directory/issues/5925
  - Upstream: https://github.com/ubiquity/business-development/issues/184
  - Status: ✅ COMMENTED TO CLAIM (2026-04-01 16:13 UTC)
  - Existing PRs: NONE found in upstream
  - **⚠️ Non-code task** — BD/marketing: scrape Coinmarketcap L1/L2, Clay enrichment, campaign outreach
  - Deliverable: Campaign execution across multiple channels

### Priority 1 ($200+) Already Claimed:
| Issue | Price | Upstream | Existing PR |
|-------|-------|----------|-------------|
| #5840 | $300 | ubiquity/.github#123 | Unclear |
| #5844 | $600 | ubiquity/ubiquity-dollar#831 | PR #971 (zugdev) |
| #5845 | $300 | ubiquity/ubiquity-dollar#926 | PR #970 (alexandr-masl) |
| #5848 | $300 | ubiquity/ubiquity-dollar#972 | PRs #1008,#1009,#973 |
| #5039 | $300 | ubiquity-os/plugins-wishlist#46 | PR #253 |
| #5045 | $300 | ubiquity-os/plugins-wishlist#48 | PR #253 |
| #5927 | $300 | ubiquity-os/plugins-wishlist#47 | PR #82 (sungdark) |
| #5923 | $300 | ubiquity-os/deno-deploy#17 | PR #31 (sungdark) |

### Key Finding:
**#5925 is the ONLY unclaimed Priority 1, $200+ bounty.** It's a BD/marketing task, not a code task. The task involves:
1. Web scraping Coinmarketcap L1/L2 lists (1 hr dev / 4 hrs manual)
2. Clay data enrichment (3 hrs - credits just unblocked April 1)
3. Campaign copy preparation (1 hr)
4. Multi-channel outreach (10+ hrs follow-up)

**Conclusion:** No unclaimed code bounty at Priority 1, $200+. Only #5925 ($600) is available but it's marketing work.


---

## 🆕 DL4 SCAN RESULTS (2026-04-01 16:22 UTC) - Subagent work-devpool-dl

### Scan Method
- Used `gh issue list` with `--label "Priority: 1 (Normal)"` to get all Priority 1 issues
- Filtered for $200+ price labels
- Checked each for existing open PRs in upstream repos
- Attempted to find genuinely unclaimed high-value tasks

### Priority 1 + $200+ Full Status

| Issue | Title | Price | Upstream | Existing PR? | Status |
|-------|-------|-------|----------|-------------|--------|
| #5925 | Launch campaign towards L1s/L2s | $600 | business-development#184 | No | ✅ UNCLAIMED (BD/Marketing) |
| #5902 | General Improvements | $600 | ubiquity-os-kernel#300 | No | ⚠️ Broad, needs breakdown |
| #5844 | Governance Token emissions | $600 | ubiquity-dollar#831 | PR #971 (zugdev) | ❌ CLAIMED |
| #5066 | Cow Swap Cash Out | $600 | - | No | ⚠️ Complex DeFi |
| #5847 | Pre-Seed/Seed Investor Debt UBQ | $450 | - | No | 🔍 Quick win? |
| #5886 | Plugin health monitor | $450 | - | No | 🔍 Quick win? |
| #5899 | All Branches Supported for Previews | $600 | - | No | 🔍 CI/Vercel config |
| #5877 | command-plan | $600 | - | No | 🔍 Investigate |
| #5841 | Unified Authentication | $600 | - | No | 🔍 Investigate |
| #5875 | CowSwap Integration | $1200 | uusd.ubq.fi#28 | No | ⚠️ Complex |
| #5927 | GitHub Webhook + Rewards v3 | $300 | plugins-wishlist#47 | PR #82 (sungdark) | ❌ CLAIMED |
| #5923 | Upgrade to newest Deno Deploy | $300 | deno-deploy#17 | PR #31 (sungdark) | ❌ CLAIMED |
| #5874 | Integrate Wallet Connect | $300 | uusd.ubq.fi#24 | PR #45 (energypantry) | ❌ CLAIMED |
| **#5848** | **CI: fix check_storage_layout** | **$300** | **ubiquity-dollar#972** | **PRs #1008,#1009** | **❌ CLAIMED** |
| #5845 | Formal verification | $300 | ubiquity-dollar#926 | PR #970 (alexandr-masl) | ❌ CLAIMED |
| #5840 | New Proposal Router | $300 | ubiquity/.github#123 | Implementation started | ⚠️ Partial |
| #5039 | GitHub Webhook Rewards No Config v1 | $300 | plugins-wishlist#46 | PR #253 | ❌ CLAIMED |
| #5045 | GitHub Webhook Rewards Contributor Class v2 | $300 | plugins-wishlist#48 | PR #253 | ❌ CLAIMED |
| #5043 | Callbacks - event handlers | $300 | ubiquity-os-kernel#261 | PR #338 (sungdark) | ❌ CLAIMED |
| #5020 | Scraper: Scrape Issue Threads | $300 | daemon-pricing#82 | PR #168 (sungdark) | ❌ CLAIMED |

### KEY FINDING: NO UNCLAIMED Priority 1 + $200+ CODE BOUNTIES

**Conclusion: All Priority 1, $200+ devpool code tasks are either:**
1. ✅ Claimed by other developers (PRs exist in upstream)
2. 🔒 Require collaborator push access to upstream repos
3. 📋 Non-code (BD/Marketing) tasks

**Only genuinely unclaimed task:** #5925 ($600) — BD/marketing campaign for L1s/L2s

### What Was Attempted
- **#5848 (CI storage fix, $300):** Initially considered as fix was well-documented. **REJECTED after PR check** — open PRs #1008 and #1009 already exist in ubiquity/ubiquity-dollar addressing exactly this issue.

### Recommended Actions for Human
1. **#5925 ($600):** BD/Marketing — execute campaign for L1/L2 GitHub management. No code needed.
2. **Opire Bounties:** claude-builders-bounty offers independent $150-$200 tasks (PR Reviewer Agent, n8n workflow, etc.) claimable via `/opire try` comments.
3. **Priority 3 High-Value:** #5070 ($900 DevPool UI), #5064 ($900 Nomic Embeddings) — lower priority but higher value.

---

## 🆕 DL3 SCAN RESULTS (2026-04-01 16:17 UTC)

### Scan Method
- Accessed: https://github.com/devpool-directory/devpool-directory/issues (sorted by updated-desc)
- Checked top 12 newest updated issues for $200+ opportunities

### Findings: NO NEW $200+ Opportunities

Scanned the following recently updated issues:

| Issue | Title | Price | Verdict |
|-------|-------|-------|---------|
| #5946 | Fix /help flow: do not emit agent-rejected message for bot user | $75 USD | ❌ Below threshold |
| #5944 | Explicit /time duration updates time label but leaves price stale | $0 USD | ❌ Regression, no bounty |
| #5928 | Upgrade to `voyage-4-large` for better performance | $9 USD | ❌ Below threshold |
| #5926 | Fix Cannot convert undefined or null to object error | TBD | ❌ Likely small |
| #5922 | Structured Outputs | TBD | ❌ Needs check |
| #5921 | Set `organization/repository` names in the plugins' configs | TBD | ❌ Config-only |
| #5924 | Launch Another DoraHacks Bounty Post | TBD | ❌ Non-code BD task |
| #5925 | Launch campaign towards L1s/L2s for managing their GitHubs | $600 | ✅ Already known (BD/marketing) |
| #5923 | Upgrade to newest Deno Deploy | $300 | ✅ Already known |
| #5916 | UbiquityOS Sprint Management Dashboard | $1800 | ✅ Already known |
| #5931 | Integrate Liquity V1 Stability Pool | $1200 | ✅ Already known |
| #5927 | GitHub Webhook + Rewards Config v3 | $300 | ✅ Already known (implementation exists) |

### Conclusion
No new $200+ code bounty opportunities found in the latest updated issues.
Top unclaimed $200+ remain: #5850 ($2400 token lists), #5916 ($1800 dashboard), #5931 ($1200 DeFi).
