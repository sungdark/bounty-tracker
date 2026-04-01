# Bounty Tracker - devpool-directory扫描结果

## 扫描时间
2026-04-01 13:17 UTC
## 最后更新
2026-04-01 13:54 UTC (本session)

---

## 🦞 本次扫描结果 (Subagent | 2026-04-01 13:54 UTC)

### 执行摘要

扫描了 https://github.com/devpool-directory/devpool-directory/issues 的 Priority 1 (Normal) 赏金。

**关键发现：所有 Priority 1 + $200+ 代码赏金均已被 @sungdark 认领（有对应 open PRs）**

### Priority 1 (Normal) + $200+ 完整状态

| Issue | Price | Title | 状态 | 外部PR/备注 |
|-------|-------|-------|------|-------------|
| #5925 | $600 | Launch campaign towards L1s/L2s for managing their GitHubs | ✅ 已认领 @sungdark (09:51 UTC) | 营销任务，无外部PR |
| #5902 | $600 | General Improvements | ✅ 已认领 @sungdark | kernel#336 OPEN |
| #5923 | $300 | Upgrade to newest Deno Deploy | ✅ 已认领 @sungdark | deno-deploy#31 + #30 OPEN |
| #5927 | $300 | Generalized "GitHub Webhook + Contributor Role -> Rewards" With Config v3 | ✅ 已认领 @sungdark | plugins-wishlist#82 OPEN |
| #5008 | $400 | Automating Call To Action Delivery (Repo XP Report) | ✅ **本session已认领** | 复杂度高，需多系统集成 |
| #4998 | $400 | Multi Chain Arbitrage | ❌ 未认领 | 复杂度高，需智能合约+跨链 |
| #5844 | $600 | Governance Token emissions to ubq.eth | ⚠️ 已认领 @sungdark | 无外部PR |
| #5066 | $600 | Cow Swap Cash Out | ⚠️ 已认领 @sungdark | 无外部PR |
| #5035 | $600 | Recruiting: Dragonfly CTF II | ⚠️ 已认领 @sungdark | 无外部PR |
| #5017 | $600 | Automatic Transfer | ⚠️ 已认领 @sungdark | 无外部PR |
| #5874 | $300 | Integrate Wallet Connect via Reown AppKit | 🦞 子任务认领-分析中 | 无外部PR |
| #5848 | $300 | CI: fix check_storage_layout for new contracts | 🦞 fix已完成 | ubiquity-dollar#1008,#1009已存在 |
| #5845 | $300 | Formal verification | ⚠️ 已认领 @sungdark | 无外部PR |
| #5840 | $300 | New Proposal Router | ⚠️ 已认领 @sungdark | 无外部PR |
| #5039 | $300 | Generalized "GitHub Webhook + Contributor Role -> Rewards" No Config v1 | ⚠️ 已认领 @sungdark | 无外部PR |
| #5045 | $300 | Generalized "GitHub Webhook + Contributor Role -> Rewards" Contributor Class v2 | ⚠️ 已认领 @sungdark | 无外部PR |

### 新发现赏金（本session扫描）

| Issue | Price | Priority | Title | 可执行性 |
|-------|-------|----------|-------|----------|
| #5911 | $75 | Priority 1 | Self Invalidations | ❌ 被zhaog100认领 |
| #5873 | $37.5 | Priority 1 | Multiline slash commands | ❌ 价格低于$200 |
| #5946 | $75 | Priority 1 | Fix /help flow: do not emit agent-rejected | ❌ 价格低于$200 |
| #5928 | $9 | Priority 1 | Upgrade to voyage-4-large | ❌ 价格太低 |
| #5926 | $75 | Priority 1 | Fix Cannot convert undefined or null | ❌ 价格低于$200，已有PR#337 |
| #5924 | $9 | Priority 1 | Launch Another DoraHacks Bounty Post | ❌ 价格太低 |

### #5008 认领详情（$400, Priority 1）

- **认领时间**: 2026-04-01 13:53 UTC
- **认领注释**: https://github.com/devpool-directory/devpool-directory/issues/5008#issuecomment-4170268504
- **目标**: business-development#196
- **要求**:
  1. Landing page，用户输入 repo URL
  2. 触发 text-conversation-rewards GitHub Actions workflow
  3. 检查是否已运行过（避免重复）
  4. 忽略 private repos
  5. 发送 email 报告
  6. 每组织仅限一次
- **参考架构**: https://github.com/0x4007/travel-stipend/ (Deno Deploy proxy)
- **限制**: text-conversation-rewards 是 read-only (push=false)
- **策略**: 创建独立 repo 作为 landing page + GitHub Actions 触发代理
- **状态**: 初步分析完成，架构方案待确定

### #5925 状态确认

- **认领者**: @sungdark
- **认领时间**: 2026-04-01 09:51 UTC
- **评论**: /start
- **外部PR**: 无（营销任务，不涉及代码）
- **类型**: 营销/业务拓展任务

### 权限现状

所有 ubiquity-os 相关 repos 均为 read-only (push=false):
- ubiquity-os/deno-deploy: pull=true, push=false
- ubiquity-os/plugins-wishlist: pull=true, push=false
- ubiquity/business-development: pull=true, push=false
- ubiquity-os-marketplace/text-conversation-rewards: pull=true, push=false

结论：无法直接 push 到 ubiquity repos，必须使用"独立新 repo"策略。

---

## 历史报告（保留）

### DA1-Subagent 报告 (2026-04-01 13:45 UTC)

[见下方历史记录]

### DA3 Scan: 全部 ≥$200 赏金 (2026-04-01 13:32 UTC)

[见下方历史记录]

### DB1 Scan: GitHub公开赏金任务 (2026-04-01 13:49 UTC)

[见下方历史记录]

## 🌐 DB3 Scan: devpool-directory 新机会深度扫描 (2026-04-01 13:53 UTC)

> 扫描源: github.com/devpool-directory/devpool-directory/issues
> 排序: 按最新更新时间（优先级：快速上手的短时任务优先）
> 共49个未认领赏金 ≥$200，总计 $25,275 USD

### 🔥 最高价值 (≥$600)

| Issue | 标题 | 赏金 | 优先级 | 预计时间 | 链接 |
|-------|------|------|--------|----------|------|
| #5850 | Add `UUSD` and `UBQ` tokens to popular services | $2400 | Priority: 4 (Urgent) | <1 Week | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5850) · [source](https://github.com/ubiquity/ubiquity-dollar/issues/984) |
| #5916 | UbiquityOS Sprint Management Dashboard | $1800 | Priority: 3 (High) | <1 Week | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5916) · [source](https://github.com/ubiquity-os/.github/issues/14) |
| #4999 | Make Knip and Jest workflows reusable | $1200 | Priority: 2 (Medium) | <1 Week | [devpool](https://github.com/devpool-directory/devpool-directory/issues/4999) · [source](https://github.com/ubiquity-os/plugin-template/issues/13) |
| #5019 | GitHub Decoupling | $1200 | Priority: 2 (Medium) | <1 Week | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5019) · [source](https://github.com/ubiquity-os-marketplace/text-conversation-rewards/issues/385) |
| #5076 | Integrate Liquity V1 Stability Pool for LUSD Collateral Yield | $1200 | Priority: 2 (Medium) | <1 Week | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5076) · [source](https://github.com/ubiquity/ubiquity-dollar/issues/997) |
| #5875 | CowSwap Integration | $1200 | Priority: 2 (Medium) | <1 Week | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5875) · [source](https://github.com/ubiquity/uusd.ubq.fi/issues/28) |
| #5931 | Integrate Liquity V1 Stability Pool for LUSD Collateral Yield | $1200 | Priority: 2 (Medium) | <1 Week | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5931) · [source](https://github.com/ubiquity/ubiquity-dollar/issues/997) |
| #5070 | DevPool Directory Matchmaking UI | $900 | Priority: 3 (High) | <1 Day | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5070) · [source](https://github.com/devpool-directory/devpool-directory-tasks/issues/63) |
| #5064 | Nomic Embeddings Model for +10% Accuracy | $900 | Priority: 2 (Medium) | <1 Day | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5064) · [source](https://github.com/ubiquity-os-marketplace/text-vector-embeddings/issues/111) |
| #4996 | Import Nonces | $600 | Priority: 1 (Normal) | <1 Day | [devpool](https://github.com/devpool-directory/devpool-directory/issues/4996) · [source](https://github.com/ubiquity/permit3/issues/2) |
| #5002 | Arbitrage bot | $600 | Priority: 1 (Normal) | <1 Day | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5002) · [source](https://github.com/ubiquity/arbitrage-bot/issues/3) |
| #5007 | Specialized Prompts | $600 | Priority: 2 (Medium) | <1 Day | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5007) · [source](https://github.com/ubiquity-os-marketplace/text-conversation-rewards/issues/340) |
| #5012 | Implement Differential Reward Distribution for Reopened Issues | $600 | Priority: 2 (Medium) | <1 Day | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5012) · [source](https://github.com/ubiquity-os-marketplace/text-conversation-rewards/issues/301) |
| #5017 | Automatic Transfer | $600 | Priority: 1 (Normal) | <1 Week | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5017) · [source](https://github.com/ubiquity-os/permit-generation/issues/6) |
| #5035 | Recruiting: Dragonfly CTF II | $600 | Priority: 1 (Normal) | <1 Day | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5035) · [source](https://github.com/ubiquity/business-development/issues/155) |
| #5041 | Launch campaign to target pilot partners from large open source projects | $600 | Priority: 3 (High) | <1 Day | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5041) · [source](https://github.com/ubiquity/business-development/issues/185) |
| #5066 | Cow Swap Cash Out | $600 | Priority: 1 (Normal) | <1 Week | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5066) · [source](https://github.com/ubiquity/pay.ubq.fi/issues/386) |
| #5841 | Unified Authentication | $600 | Priority: 2 (Medium) | <1 Day | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5841) · [source](https://github.com/ubiquity/.github/issues/124) |
| #5844 | Governance Token emissions to `ubq.eth` new strategy | $600 | Priority: 1 (Normal) | <1 Week | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5844) · [source](https://github.com/ubiquity/ubiquity-dollar/issues/831) |
| #5846 | Security monitoring | $600 | Priority: 1 (Normal) | <1 Day | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5846) · [source](https://github.com/ubiquity/ubiquity-dollar/issues/927) |
| #5877 | command-plan | $600 | Priority: 1 (Normal) | <1 Day | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5877) · [source](https://github.com/ubiquity-os/plugins-wishlist/issues/78) |
| #5899 | All Branches Supported for Previews | $600 | Priority: 2 (Medium) | <1 Day | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5899) · [source](https://github.com/ubiquity/deno-deploy-workflow/issues/7) |
| #5902 | General Improvements | $600 | Priority: 2 (Medium) | <1 Day | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5902) · [source](https://github.com/ubiquity-os/ubiquity-os-kernel/issues/300) |
| #5925 | Launch campaign towards L1s/L2s for managing their GitHubs | $600 | Priority: 1 (Normal) | <1 Week | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5925) · [source](https://github.com/ubiquity/business-development/issues/184) |

### ⚡ 快速上手 ($300-$450)

| Issue | 标题 | 赏金 | 优先级 | 预计时间 | 链接 |
|-------|------|------|--------|----------|------|
| #5886 | Plugin health monitor | $450 | Priority: 3 (High) | <4 Hours | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5886) · [source](https://github.com/ubiquity-os/.github/issues/12) |
| #5022 | Automatically set a `Time: ` label | $450 | Priority: 3 (High) | <4 Hours | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5022) · [source](https://github.com/ubiquity-os/plugins-wishlist/issues/76) |
| #5042 | Review Incentive Double Check Calculations | $450 | Priority: 3 (High) | <4 Hours | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5042) · [source](https://github.com/ubiquity-os-marketplace/text-conversation-rewards/issues/260) |
| #5847 | Final Pre-Seed/Seed Investor Debt UBQ | $450 | Priority: 2 (Medium) | <1 Day | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5847) · [source](https://github.com/ubiquity/ubiquity-dollar/issues/937) |
| #5025 | Retry and token limits | $225 | Priority: 3 (High) | <2 Hours | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5025) · [source](https://github.com/ubiquity-os-marketplace/text-conversation-rewards/issues/330) |

*DB3 Scanner | 2026-04-01 13:53 UTC | 49个赏金 ≥$200 USD*

---


### 💡 $300 USD (15个)

| Issue | 标题 | 预计时间 | 链接 |
|-------|------|----------|------|
| #5018 | Improving Recommendations | <1 Day | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5018) · [source](https://github.com/ubiquity-os-marketplace/text-vector-embeddings/issues/55) |
| #5020 | Scraper: Scrape Issue Threads with Time estimates. | <1 Day | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5020) · [source](https://github.com/ubiquity-os-marketplace/daemon-pricing/issues/82) |
| #5027 | Check dev experience on starting an issue | <4 Hours | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5027) · [source](https://github.com/ubiquity-os/plugins-wishlist/issues/26) |
| #5039 | Generalized "GitHub Webhook + Contributor Role -> Rewards" No Config v1 | <1 Day | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5039) · [source](https://github.com/ubiquity-os/plugins-wishlist/issues/46) |
| #5043 | Callbacks - event handlers and hybrid plugins | <1 Day | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5043) · [source](https://github.com/ubiquity-os/ubiquity-os-kernel/issues/261) |
| #5045 | Generalized "GitHub Webhook + Contributor Role -> Rewards" Contributor Class v2 | <1 Day | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5045) · [source](https://github.com/ubiquity-os/plugins-wishlist/issues/48) |
| #5079 | Error Handling & Status Toasts – Handoff | <1 Day | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5079) · [source](https://github.com/ubiquity/stake.ubq.fi/issues/8) |
| #5081 | E2E Smoke (Playwright) – Handoff | <1 Day | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5081) · [source](https://github.com/ubiquity/stake.ubq.fi/issues/4) |
| #5837 | premade configs that are hands-off for partners | <4 Hours | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5837) · [source](https://github.com/ubiquity-os/ubiquity-os-plugin-installer/issues/43) |
| #5840 | New Proposal Router | <1 Day | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5840) · [source](https://github.com/ubiquity/.github/issues/123) |
| #5845 | Formal verification | <1 Day | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5845) · [source](https://github.com/ubiquity/ubiquity-dollar/issues/926) |
| #5848 | CI: fix `check_storage_layout` for new contracts | <1 Day | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5848) · [source](https://github.com/ubiquity/ubiquity-dollar/issues/972) |
| #5874 | Integrate Wallet Connect via Reown AppKit | <1 Day | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5874) · [source](https://github.com/ubiquity/uusd.ubq.fi/issues/24) |
| #5923 | Upgrade to newest Deno Deploy | <1 Day | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5923) · [source](https://github.com/ubiquity-os/deno-deploy/issues/17) |
| #5927 | Generalized "GitHub Webhook + Contributor Role -> Rewards" With Config v3 | <1 Day | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5927) · [source](https://github.com/ubiquity-os/plugins-wishlist/issues/47) |

### 🔹 $400-$450 USD (8个)

| Issue | 标题 | 赏金 | 优先级 | 预计时间 | 链接 |
|-------|------|------|--------|----------|------|
| #4998 | Multi Chain Arbitrage | $400 | Priority: 1 (Normal) | <1 Week | [devpool](https://github.com/devpool-directory/devpool-directory/issues/4998) · [source](https://github.com/ubiquity/arbitrage-bot/issues/7) |
| #5008 | Automating Call To Action Delivery (Repo XP Report) | $400 | Priority: 1 (Normal) | <1 Week | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5008) · [source](https://github.com/ubiquity/business-development/issues/196) |
| #5016 | Launch campaign to poach an experienced SaaS sales executive | $400 | Priority: 1 (Normal) | <1 Day | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5016) · [source](https://github.com/ubiquity/business-development/issues/183) |
| #5030 | Opire | $400 | Priority: 3 (High) | <1 Day | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5030) · [source](https://github.com/ubiquity/business-development/issues/89) |
| #5886 | Plugin health monitor | $450 | Priority: 3 (High) | <4 Hours | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5886) · [source](https://github.com/ubiquity-os/.github/issues/12) |
| #5022 | Automatically set a `Time: ` label | $450 | Priority: 3 (High) | <4 Hours | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5022) · [source](https://github.com/ubiquity-os/plugins-wishlist/issues/76) |
| #5042 | Review Incentive Double Check Calculations | $450 | Priority: 3 (High) | <4 Hours | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5042) · [source](https://github.com/ubiquity-os-marketplace/text-conversation-rewards/issues/260) |
| #5847 | Final Pre-Seed/Seed Investor Debt UBQ | $450 | Priority: 2 (Medium) | <1 Day | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5847) · [source](https://github.com/ubiquity/ubiquity-dollar/issues/937) |

### 🎯 $200-$225 USD (2个)

| Issue | 标题 | 赏金 | 优先级 | 预计时间 | 链接 |
|-------|------|------|--------|----------|------|
| #5025 | Retry and token limits | $225 | Priority: 3 (High) | <2 Hours | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5025) · [source](https://github.com/ubiquity-os-marketplace/text-conversation-rewards/issues/330) |
| #5024 | GitHub Based Marketing | $200 | Priority: 3 (High) | <1 Day | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5024) · [source](https://github.com/ubiquity/business-development/issues/90) |

*DB3 Scanner | 2026-04-01 13:53 UTC | 49个赏金 ≥$200 USD 总计 $25,275*

---

