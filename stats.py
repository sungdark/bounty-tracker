#!/usr/bin/env python3
import re
from datetime import datetime

total_usd = 0
high_value_open = 0
merged_pending = 0
task_count = 0

# RTC -> USD conversion rate: 1 RTC = 0.1 USD
rtc_rate = 0.1

with open('tasks.md', 'r') as f:
    lines = f.readlines()

for line in lines:
    if not line.startswith('| BT-'):
        continue
    task_count += 1
    cols = [c.strip() for c in line.split('|')[1:-1]]
    # Columns: ID, 接受时间, 来源, 项目, 任务链接, 奖励, 货币类型, 奖励价值, 状态, PR链接, 认领链接, 最后更新, 备注
    # 索引0:ID, 1:接受时间, 2:来源, 3:项目, 4:任务链接, 5:奖励, 6:货币类型, 7:奖励价值, 8:状态, 9:PR链接, 10:认领链接, 11:最后更新, 12:备注
    if len(cols) >= 8:
        val = cols[7]  # 奖励价值在第8列
        try:
            val_float = float(val)
            currency = cols[6]
            # 转换RTC到USD
            if currency == 'RTC':
                val_float = val_float * rtc_rate
            total_usd += val_float
        except:
            val_float = 0
            pass
        status = cols[8]  # 状态在第9列
        if status in ['open', 'pr_open', 'pr_open_alt', 'new', 'ready_pr'] and val_float >= 5:
            high_value_open += 1
        if status in ['merged'] and val_float > 0:
            merged_pending += val_float

print(f'📊 Bounty Tracker 统计')
print(f'总任务数: {task_count}')
print(f'总待结算 (已合并): ${merged_pending:.2f}')
print(f'总潜在可获得 (开放任务USD估值): ${total_usd:.2f}')
print(f'开放高价值任务 (≥$5): {high_value_open}')
