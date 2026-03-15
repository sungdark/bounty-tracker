
import re
from datetime import datetime

with open('tasks.md', 'r') as f:
    content = f.read()

total_usd = 0
pr_open = 0
merged_pending = 0
high_value = []
new_today = 0
total_tasks = 0

lines = content.split('\n')
for line in lines:
    if '| BT-' in line and not 'ID |' in line and not '----|' in line:
        total_tasks += 1
        cols = [c.strip() for c in line.split('|') if c.strip()]
        if len(cols) >= 8:
            reward_value = cols[6]
            status = cols[7]
            try:
                val = float(reward_value)
                total_usd += val
            except:
                val = 0
                pass
            if status == 'pr_open' or status == 'ready_pr' or status == 'pr_open_alt':
                pr_open += 1
            if status == 'merged' and '待结算' in line:
                merged_pending += 1
            if val >= 5:
                currency = cols[5]
                if currency in ['USD', 'EUR', 'GBP', 'USDC']:
                    if (currency in ['USD', 'EUR', 'GBP'] and val >= 100) or (currency == 'USDC' and val >= 100):
                        high_value.append((cols[0], val, status))
            date_col = cols[1]
            if '2026-03-15' in date_col:
                new_today += 1

output = f"""💰 整点赚钱战报 - {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}

✅ 核心数据：
- 今日新增赏金机会：{new_today} 个
- 总任务数：{total_tasks}
- 累计潜在奖励价值：${total_usd:.2f}
- PR审核中任务：{pr_open} 个
- 已合并待结算：{merged_pending} 个

✅ 高价值任务（≥$100）状态：
"""

if len(high_value) > 8:
    for hv in high_value[:8]:
        output += f"• {hv[0]}: ${hv[1]} - {hv[2]}\n"
    output += f"... 还有 {len(high_value) - 8} 个高价值任务未列出\n"
else:
    for hv in high_value:
        output += f"• {hv[0]}: ${hv[1]} - {hv[2]}\n"

output += """
✅ 新发现机会：
• BT-0108: Twilio bug bounty ($100+)
• BT-0109: DoorDash bug bounty ($100+)
• 新增参考数据源：arkadiyt/bounty-targets-data（233个开放赏金项目每小时更新）

✅ 风险点：
• 大量高价值漏洞赏金项目需要安全研究能力，需要安排优先级逐步评估
• 部分RustChain小额任务还未认领，可快速执行累积奖励
"""

print(output)
