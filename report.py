import json, os

# 读取仓库实际数据（这里先模拟，实际根据仓库结构调整）
data = {
    "pending_payout": 1250.75,
    "active_prs": 7,
    "key_tasks": [
        "solana-program-bug #42: $350 待合并",
        "uniswap-interface-bug #18: $220 审核中"
    ],
    "next_hour": [
        "提交2个待审核PR",
        "跟进3个已合并结算申请"
    ]
}

# 生成战报
report = "【整点赚钱战报 🦞】\n"
report += f"💸 待结算：${data['pending_payout']:.2f}\n"
report += f"🚀 在途PR：{data['active_prs']}个\n"
report += "📌 重点进度：\n"
for t in data['key_tasks']:
    report += f"  • {t}\n"
report += "⏭️  下小时计划：\n"
for t in data['next_hour']:
    report += f"  • {t}\n"

print(report[:300])
