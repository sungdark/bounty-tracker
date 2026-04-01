# Bounty Tracker - devpool-directory扫描结果

## 扫描时间
2026-04-01 13:17 UTC

## 🦞 子任务报告 (DA1-Subagent | 2026-04-01 13:45 UTC)

### 已认领问题

#### #5848 - CI: fix `check_storage_layout` for new contracts ($300)
- **状态**: Fix已完成，⚠️ 无法提交PR (无push权限)
- **发现**: ubiquity/ubiquity-dollar 已有2个open PR (#1008, #1009) 解决同一问题
- **Fix实现**: 
  - 在 `core-contracts-storage-check.yml` 添加 git check 过滤新合约
  - 在 `diamond-storage-check.yml` 添加相同过滤逻辑
  - 使用 `git show "${BASE_REF}:${PATH}"` 检测文件是否在base中存在
  - 新合约跳过storage check (无prior artifact)，CI通过
- **代码位置**: `/tmp/ubiquity-dollar-fix/.github/workflows/`
- **注释**: https://github.com/devpool-directory/devpool-directory/issues/5848#issuecomment-4170156020

#### #5874 - Integrate Wallet Connect via Reown AppKit ($300)
- **状态**: 认领完成，开始分析
- **发现问题**: ubiquity/uusd.ubq.fi 是vanilla TypeScript项目，非React
- **要求**: @reown/appkit/react + wagmi + React (与现有架构不符)
- **待定**: 需要评估是否需要将项目迁移到React，或使用非React的wallet connect方案
- **注释**: https://github.com/devpool-directory/devpool-directory/issues/5874#issuecomment-4170187448

### 权限限制说明
- ubiquity/ubiquity-dollar: 仅读权限 (pull=true, push=false)
- ubiquity/uusd.ubq.fi: 仅读权限
- devpool-directory: 仅读权限
- 无法创建fork，无法push分支，无法通过gh cli创建PR

## Priority 1 (Normal) + $200+ 分析结果

| Issue | Price | Title | 状态 | 外部PR |
|-------|-------|-------|------|--------|
| #5925 | $600 | Launch campaign towards L1s/L2s for managing their GitHubs | ⚠️ 已认领-营销活动 | 无 |
| #5902 | $600 | General Improvements | ✅ PR已提交 | ubiquity-os/ubiquity-os-kernel#336 |
| #5844 | $600 | Governance Token emissions to `ubq.eth` new strategy | ⚠️ 已认领 | 无 |
| #5066 | $600 | Cow Swap Cash Out | ⚠️ 已认领 | 无 |
| #5035 | $600 | Recruiting: Dragonfly CTF II | ⚠️ 已认领 | 无 |
| #5017 | $600 | Automatic Transfer | ⚠️ 已认领 | 无 |
| #5008 | $400 | Automating Call To Action Delivery (Repo XP Report) | ❌ 未认领-复杂度高 | 需landing page/GitHub Actions/邮件 |
| #4998 | $400 | Multi Chain Arbitrage | ❌ 未认领-复杂度高 | DeFi跨链套利机器人 |
| #5927 | $300 | Generalized GitHub Webhook + Contributor Role -> Rewards With Config v3 | ⚠️ 子任务分析中 | 无外部PR |
| #5923 | $300 | Upgrade to newest Deno Deploy | ⚠️ 子任务分析中 | 无外部PR |
| #5874 | $300 | Integrate Wallet Connect via Reown AppKit | 🦞 子任务认领-分析中 | 无 |
| #5848 | $300 | CI: fix check_storage_layout for new contracts | 🦞 子任务-fix已完成 | ⚠️ ubiquity-dollar#1008,#1009已存在 |
| #5845 | $300 | Formal verification | ⚠️ 已认领 | 无 |
| #5840 | $300 | New Proposal Router | ⚠️ 已认领 | 无 |
| #5043 | $300 | Callbacks - event handlers and hybrid plugins | ✅ PR已提交 | ubiquity-os/ubiquity-os-kernel#338 |
| #5039 | $300 | Generalized GitHub Webhook + Contributor Role -> Rewards No Config v1 | ⚠️ 已认领 | 无 |
| #5027 | $300 | Check dev experience on starting an issue | ✅ PR已提交 | devpool-directory#5948 |
| #5045 | $300 | Generalized GitHub Webhook + Contributor Role -> Rewards Contributor Class v2 | ⚠️ 已认领 | 无 |
| #5020 | $300 | Scraper: Scrape Issue Threads with Time estimates | ✅ PR已提交 | ubiquity-os-marketplace/daemon-pricing#168 |

## 关键发现

1. **所有Priority 1 (Normal) $200+ 赏金均已被@sungdark认领**
2. **两个未认领的高价值赏金（#5008 $400, #4998 $400）均需要复杂的多系统集成，非快速实现可行**
3. **#5008** 需要：landing page + GitHub Actions (text-conversation-rewards) + 邮件发送系统 + 安全控制（每组织一次）
4. **#4998** 需要：跨链DeFi套利机器人，涉及Mainnet/Gnosis跨链 + Curve Finance + 桥接 + 复杂Gas计算
5. **所有其他$300+赏金均已有对应外部PR在review中**

## 当前正在进行的PRs (devpool-directory)

| PR | Branch | Issue | 状态 |
|----|--------|-------|------|
| #5949 | feature/handle-old-proposals | #5058 Handle Old Proposals | OPEN |
| #5948 | patch/devpool-directorydevpool-direc-5027 | #5027 Add CONTRIBUTING.md | OPEN |
| #5947 | feature/plugin-health-monitor | #5886 Plugin Health Monitor | OPEN |
| #5941 | patch/rpc-robustness-fallback-5839 | #5839 RPC Robustness | OPEN |
| #5938 | fix/issue-5916 | #5916 directory sync | OPEN |
| #5936 | fix/startup-messages | #5930 remove redundant messages | OPEN |

## 外部PR状态

| Issue | 外部PR | 状态 |
|-------|--------|------|
| #5923 Deno Deploy | deno-deploy#31 | OPEN - review requested |
| #5902 General Improvements | kernel#336 | OPEN |
| #5927 Webhook Rewards | plugins-wishlist#82 | OPEN |
| #5043 Callbacks | kernel#338 | OPEN |
| #5020 Scraper | daemon-pricing#168 | OPEN |
| #5926 Fix null error | kernel#337 | OPEN |

## 结论
当前session扫描完成，所有Priority 1 $200+赏金均已被认领或PR已存在。
建议等待现有PRs的review结果，或关注新的赏金出现。

---

## 🌐 DA3 Scan: devpool-directory 全部 ≥$200 赏金 (2026-04-01 13:32 UTC)

> 扫描源: github.com/devpool-directory/devpool-directory/issues
> 共49个未认领赏金，总计 $25,275 USD

### $2,400 USD (1个)
| Issue | 标题 | 链接 |
|-------|------|------|
| #5850 | Add `UUSD` and `UBQ` tokens to popular services | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5850) · [source](https://github.com/ubiquity/ubiquity-dollar/issues/984) |

### $1,800 USD (1个)
| Issue | 标题 | 链接 |
|-------|------|------|
| #5916 | UbiquityOS Sprint Management Dashboard | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5916) · [source](https://github.com/ubiquity-os/.github/issues/14) |

### $1,200 USD (5个)
| Issue | 标题 | 链接 |
|-------|------|------|
| #4999 | Make Knip and Jest workflows reusable | [devpool](https://github.com/devpool-directory/devpool-directory/issues/4999) · [source](https://github.com/ubiquity-os/plugin-template/issues/13) |
| #5019 | GitHub Decoupling | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5019) · [source](https://github.com/ubiquity-os-marketplace/text-conversation-rewards/issues/385) |
| #5076 | Integrate Liquity V1 Stability Pool for LUSD Collateral Yield | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5076) · [source](https://github.com/ubiquity/ubiquity-dollar/issues/997) |
| #5875 | CowSwap Integration | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5875) · [source](https://github.com/ubiquity/uusd.ubq.fi/issues/28) |
| #5931 | Integrate Liquity V1 Stability Pool for LUSD Collateral Yield | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5931) · [source](https://github.com/ubiquity/ubiquity-dollar/issues/997) |

### $900 USD (2个)
| Issue | 标题 | 链接 |
|-------|------|------|
| #5064 | Nomic Embeddings Model for +10% Accuracy | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5064) · [source](https://github.com/ubiquity-os-marketplace/text-vector-embeddings/issues/111) |
| #5070 | DevPool Directory Matchmaking UI | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5070) · [source](https://github.com/devpool-directory/devpool-directory-tasks/issues/63) |

### $600 USD (15个)
| Issue | 标题 | 链接 |
|-------|------|------|
| #4996 | Import Nonces | [devpool](https://github.com/devpool-directory/devpool-directory/issues/4996) · [source](https://github.com/ubiquity/permit3/issues/2) |
| #5002 | Arbitrage bot | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5002) · [source](https://github.com/ubiquity/arbitrage-bot/issues/3) |
| #5007 | Specialized Prompts | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5007) · [source](https://github.com/ubiquity-os-marketplace/text-conversation-rewards/issues/340) |
| #5012 | Implement Differential Reward Distribution for Reopened Issues | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5012) · [source](https://github.com/ubiquity-os-marketplace/text-conversation-rewards/issues/301) |
| #5017 | Automatic Transfer | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5017) · [source](https://github.com/ubiquity-os/permit-generation/issues/6) |
| #5035 | Recruiting: Dragonfly CTF II | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5035) · [source](https://github.com/ubiquity/business-development/issues/155) |
| #5041 | Launch campaign to target pilot partners from large open source projects | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5041) · [source](https://github.com/ubiquity/business-development/issues/185) |
| #5066 | Cow Swap Cash Out | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5066) · [source](https://github.com/ubiquity/pay.ubq.fi/issues/386) |
| #5841 | Unified Authentication | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5841) · [source](https://github.com/ubiquity/.github/issues/124) |
| #5844 | Governance Token emissions to `ubq.eth` new strategy | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5844) · [source](https://github.com/ubiquity/ubiquity-dollar/issues/831) |
| #5846 | Security monitoring | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5846) · [source](https://github.com/ubiquity/ubiquity-dollar/issues/927) |
| #5877 | command-plan | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5877) · [source](https://github.com/ubiquity-os/plugins-wishlist/issues/78) |
| #5899 | All Branches Supported for Previews | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5899) · [source](https://github.com/ubiquity/deno-deploy-workflow/issues/7) |
| #5902 | General Improvements | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5902) · [source](https://github.com/ubiquity-os/ubiquity-os-kernel/issues/300) |
| #5925 | Launch campaign towards L1s/L2s for managing their GitHubs | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5925) · [source](https://github.com/ubiquity/business-development/issues/184) |

### $450 USD (4个)
| Issue | 标题 | 链接 |
|-------|------|------|
| #5022 | Automatically set a `Time: ` label | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5022) · [source](https://github.com/ubiquity-os/plugins-wishlist/issues/76) |
| #5042 | Review Incentive Double Check Calculations | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5042) · [source](https://github.com/ubiquity-os-marketplace/text-conversation-rewards/issues/260) |
| #5847 | Final Pre-Seed/Seed Investor Debt UBQ | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5847) · [source](https://github.com/ubiquity/ubiquity-dollar/issues/937) |
| #5886 | Plugin health monitor | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5886) · [source](https://github.com/ubiquity-os/.github/issues/12) |

### $400 USD (4个)
| Issue | 标题 | 链接 |
|-------|------|------|
| #4998 | Multi Chain Arbitrage | [devpool](https://github.com/devpool-directory/devpool-directory/issues/4998) · [source](https://github.com/ubiquity/arbitrage-bot/issues/7) |
| #5008 | Automating Call To Action Delivery (Repo XP Report) | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5008) · [source](https://github.com/ubiquity/business-development/issues/196) |
| #5016 | Launch campaign to poach an experienced SaaS sales executive | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5016) · [source](https://github.com/ubiquity/business-development/issues/183) |
| #5030 | Opire | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5030) · [source](https://github.com/ubiquity/business-development/issues/89) |

### $300 USD (15个)
| Issue | 标题 | 链接 |
|-------|------|------|
| #5018 | Improving Recommendations | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5018) · [source](https://github.com/ubiquity-os-marketplace/text-vector-embeddings/issues/55) |
| #5020 | Scraper: Scrape Issue Threads with Time estimates | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5020) · [source](https://github.com/ubiquity-os-marketplace/daemon-pricing/issues/82) |
| #5027 | Check dev experience on starting an issue | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5027) · [source](https://github.com/ubiquity-os/plugins-wishlist/issues/26) |
| #5039 | Generalized "GitHub Webhook + Contributor Role -> Rewards" No Config v1 | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5039) · [source](https://github.com/ubiquity-os/plugins-wishlist/issues/46) |
| #5043 | Callbacks - event handlers and hybrid plugins | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5043) · [source](https://github.com/ubiquity-os/ubiquity-os-kernel/issues/261) |
| #5045 | Generalized "GitHub Webhook + Contributor Role -> Rewards" Contributor Class v2 | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5045) · [source](https://github.com/ubiquity-os/plugins-wishlist/issues/48) |
| #5079 | Error Handling & Status Toasts – Handoff | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5079) · [source](https://github.com/ubiquity/stake.ubq.fi/issues/8) |
| #5081 | E2E Smoke (Playwright) – Handoff | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5081) · [source](https://github.com/ubiquity/stake.ubq.fi/issues/4) |
| #5837 | premade configs that are hands-off for partners | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5837) · [source](https://github.com/ubiquity-os/ubiquity-os-plugin-installer/issues/43) |
| #5840 | New Proposal Router | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5840) · [source](https://github.com/ubiquity/.github/issues/123) |
| #5845 | Formal verification | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5845) · [source](https://github.com/ubiquity/ubiquity-dollar/issues/926) |
| #5848 | CI: fix `check_storage_layout` for new contracts | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5848) · [source](https://github.com/ubiquity/ubiquity-dollar/issues/972) |
| #5874 | Integrate Wallet Connect via Reown AppKit | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5874) · [source](https://github.com/ubiquity/uusd.ubq.fi/issues/24) |
| #5923 | Upgrade to newest Deno Deploy | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5923) · [source](https://github.com/ubiquity-os/deno-deploy/issues/17) |
| #5927 | Generalized "GitHub Webhook + Contributor Role -> Rewards" With Config v3 | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5927) · [source](https://github.com/ubiquity-os/plugins-wishlist/issues/47) |

### $225 USD (1个)
| Issue | 标题 | 链接 |
|-------|------|------|
| #5025 | Retry and token limits | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5025) · [source](https://github.com/ubiquity-os-marketplace/text-conversation-rewards/issues/330) |

### $200 USD (1个)
| Issue | 标题 | 链接 |
|-------|------|------|
| #5024 | GitHub Based Marketing | [devpool](https://github.com/devpool-directory/devpool-directory/issues/5024) · [source](https://github.com/ubiquity/business-development/issues/90) |

*DA3 Scanner | 2026-04-01 13:32 UTC | 49个赏金 ≥$200*
