# Bounty Tracker - devpool-directory扫描结果

## 扫描时间
2026-04-01 13:17 UTC

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
| #5927 | $300 | Generalized GitHub Webhook + Contributor Role -> Rewards With Config v3 | ✅ PR已提交 | ubiquity-os/plugins-wishlist#82 |
| #5923 | $300 | Upgrade to newest Deno Deploy | ✅ PR已提交 | ubiquity-os/deno-deploy#31 |
| #5874 | $300 | Integrate Wallet Connect via Reown AppKit | ⚠️ 已认领 | 无 |
| #5848 | $300 | CI: fix check_storage_layout for new contracts | ⚠️ 已认领 | 无 |
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
