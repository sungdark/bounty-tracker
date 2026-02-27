# Bounty Tracker (sungdark)

用于记录已接/在途/已完成 bounty，作为整点战报的数据基线。

## 字段说明
- id: 本地唯一任务编号
- accepted_at_utc: 接单时间（UTC）
- source: github
- repo: 目标仓库
- issue_url: 任务链接
- reward: 奖励原文
- reward_type: USD/RTC/ISNAD/SATS/POINTS/UNKNOWN
- reward_value: 数值（可空）
- status: accepted|in_progress|pr_open|merged|paid|blocked|dropped
- pr_url: PR 链接（可空）
- claim_url: claim/回帖链接（可空）
- last_update_utc: 最近更新时间（UTC）
- notes: 备注
