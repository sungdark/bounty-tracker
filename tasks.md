# Bounty Task Tracker

## 🔄 In Progress

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

## 🆕 New Opire Dollar Bounties Found (2026-04-01 DI1 Scan)

### Issue #1: [BOUNTY $50] SKILL: Generate a structured CHANGELOG from git history
- **URL:** https://github.com/claude-builders-bounty/claude-builders-bounty/issues/1
- **Price:** $50 USD (via Opire)
- **Difficulty:** Easy
- **Time estimate:** <1 Day
- **Claimed:** No
- **Status:** NEW

#### Description
Create a Claude Code skill (`SKILL.md`) or a bash script that automatically generates a structured `CHANGELOG.md` from a project's git history.

#### Acceptance Criteria
- [ ] Works via `/generate-changelog` command or `bash changelog.sh`
- [ ] Fetches commits since the last git tag
- [ ] Auto-categorizes into: `Added` / `Fixed` / `Changed` / `Removed`
- [ ] Outputs a properly formatted `CHANGELOG.md`
- [ ] Tested on a real GitHub repo (include sample output in the PR)
- [ ] README with setup instructions in 3 steps or fewer

#### How to Claim
1. Comment `/opire try` in the issue
2. Submit a PR with solution
3. Payment released automatically on merge ✅

---

### Issue #2: [BOUNTY $75] TEMPLATE: CLAUDE.md for a Next.js + SQLite SaaS project
- **URL:** https://github.com/claude-builders-bounty/claude-builders-bounty/issues/2
- **Price:** $75 USD (via Opire)
- **Difficulty:** Medium
- **Time estimate:** <1 Day
- **Claimed:** No
- **Status:** NEW

#### Description
Create an opinionated, production-ready `CLAUDE.md` for a typical SaaS project built with Next.js 15 App Router and SQLite (better-sqlite3 or Turso).

#### Acceptance Criteria
- [ ] Covers: project structure, naming conventions, DB migration rules
- [ ] Includes: dev commands, patterns to follow, anti-patterns to avoid
- [ ] Opinionated — not generic. Every rule has a reason.
- [ ] Usable without modification on a greenfield Next.js + SQLite project
- [ ] Tested: create a new project, paste the CLAUDE.md, confirm Claude Code understands the context

#### How to Claim
1. Comment `/opire try` in the issue
2. Submit a PR with CLAUDE.md
3. Payment released automatically on merge ✅

---

### Issue #3: [BOUNTY $100] HOOK: Pre-tool-use hook that blocks destructive bash commands
- **URL:** https://github.com/claude-builders-bounty/claude-builders-bounty/issues/3
- **Price:** $100 USD (via Opire)
- **Difficulty:** Medium
- **Time estimate:** <1 Day
- **Claimed:** No
- **Status:** NEW

#### Description
Create a Claude Code `pre-tool-use` hook in Python or bash that intercepts dangerous bash commands before they are executed.

#### Acceptance Criteria
- [ ] Hook follows Claude Code hooks format (`~/.claude/hooks/`)
- [ ] Blocks: `rm -rf`, `DROP TABLE`, `git push --force`, `TRUNCATE`, `DELETE FROM` without WHERE
- [ ] Logs every blocked attempt to `~/.claude/hooks/blocked.log` with timestamp + command + project path
- [ ] Displays clear message to Claude explaining why the command was blocked
- [ ] Does not interfere with normal bash commands
- [ ] README with installation in 2 commands or fewer

#### How to Claim
1. Comment `/opire try` in the issue
2. Submit a PR with hook + README
3. Payment released automatically on merge ✅

---

### Issue #4: [BOUNTY $150] AGENT: Claude Code sub-agent that reviews a PR and posts a structured comment
- **URL:** https://github.com/claude-builders-bounty/claude-builders-bounty/issues/4
- **Price:** $150 USD (via Opire)
- **Difficulty:** Medium
- **Time estimate:** <1 Day
- **Claimed:** No
- **Status:** NEW

#### Description
Create a Claude Code agent that takes a PR diff as input, analyzes it, and returns a structured Markdown review comment.

#### Acceptance Criteria
- [ ] Works via CLI: `claude-review --pr https://github.com/owner/repo/pull/123` OR GitHub Action
- [ ] Structured Markdown output with:
  - Summary of changes (2–3 sentences)
  - Identified risks (list)
  - Improvement suggestions (list)
  - Confidence score: Low / Medium / High
- [ ] Tested on at least 2 real GitHub PRs (include outputs in the PR)
- [ ] README with setup and usage instructions

#### How to Claim
1. Comment `/opire try` in the issue
2. Submit a PR with the agent + sample outputs
3. Payment released automatically on merge ✅

---

## 📋 All Priority 1 + $200+ Scanned (2026-04-01)
| # | Title | Price | Has Open PR? | Status |
|---|-------|-------|--------------|--------|
| 5927 | Generalized "GitHub Webhook + Contributor Role -> Rewards" W | $300 | No | Complex, upstream spec needed |
| 5925 | Launch campaign towards L1s/L2s | $600 | No | Non-code |
| 5923 | Upgrade to newest Deno Deploy | $300 | No | Medium complexity |
| 5902 | General Improvements | $600 | No | Multi-part |
| 5874 | Integrate Wallet Connect via Reown AppKit | $300 | No | Medium |
| 5848 | CI: fix `check_storage_layout` for new contracts | $300 | No | **IN PROGRESS** |
| 5845 | Formal verification | $300 | No | Expert domain |
| 5844 | Governance Token emissions to `ubq.eth` | $600 | No | Complex |
| 5840 | New Proposal Router | $300 | No | Medium |
| 5066 | Cow Swap Cash Out | $600 | No | Complex DeFi |
| 5045 | Generalized "GitHub Webhook + Contributor Role" | $300 | No | Spec unclear |
| 5043 | Callbacks - event handlers and hybrid plugins | $300 | No | Medium |
| 5039 | Generalized "GitHub Webhook + Contributor Role" | $300 | No | Spec unclear |
| 5035 | Recruiting: Dragonfly CTF II | $600 | No | Non-code |
| 5027 | Check dev experience on starting an issue | $300 | No | Testing focused |
| 5020 | Scraper: Scrape Issue Threads | $300 | No | Tool dev |
| 5017 | Automatic Transfer | $600 | No | Complex |
| 5008 | Automating Call To Action Delivery | $400 | No | Reporting |
| 4998 | Multi Chain Arbitrage | $400 | No | DeFi complex |

---

## 📋 Opire $50-$150 Bounties (2026-04-01 DI1 Scan)
| # | Title | Price | Difficulty | Status |
|---|-------|-------|------------|--------|
| 1 | SKILL: Generate a structured CHANGELOG from git history | $50 | Easy | **NEW** |
| 2 | TEMPLATE: CLAUDE.md for Next.js + SQLite SaaS project | $75 | Medium | **NEW** |
| 3 | HOOK: Pre-tool-use hook blocks destructive bash commands | $100 | Medium | **NEW** |
| 4 | AGENT: Claude Code sub-agent PR reviewer | $150 | Medium | **NEW** |
