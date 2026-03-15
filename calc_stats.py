
import re
from datetime import datetime

with open('tasks.md', 'r') as f:
    content = f.read()

# Calculate stats
total_pending = 0.0
total_merged = 0.0
usd_pending = 0.0
pr_open = 0
new_opportunities = 0
needs_followup = 0

lines = content.splitlines()
for line in lines:
    if '| BT-' not in line or 'ID' in line or '----' in line:
        continue
    cols = [col.strip() for col in line.split('|') if col.strip()]
    if len(cols) < 8:
        continue
    reward_val = cols[7]
    state = cols[8]
    currency = cols[6]
    try:
        val = float(reward_val)
    except:
        val = 0
    if state == 'pr_open' or state == 'ready_pr' or state == 'open':
        total_pending += val
        if currency == 'USD' or currency == 'USDC':
            usd_pending += val
        if state in ('pr_open', 'ready_pr'):
            pr_open += 1
        if state == 'open' or state == 'new':
            new_opportunities += 1
    if state == 'merged' or state == 'submitted':
        if currency == 'USD' or currency == 'USDC':
            total_merged += val

# Count overdue (no update > 14 days)
    if len(cols) >= 11:
        last_update = cols[10]
        try:
            # Parse ISO date
            if 'T' in last_update:
                dt = datetime.fromisoformat(last_update.split('+')[0])
                delta = (datetime.utcnow() - dt).days
                if delta > 14 and state in ('pr_open', 'open'):
                    needs_followup += 1
        except:
            pass

print(f'''
✅ 核心数据:
- 总待结算法币: ${usd_pending:.2f}
- 已到账法币: ${total_merged:.2f}
- PR审核中: {pr_open}
- 新机会未认领: {new_opportunities}
- 超期需要跟进: {needs_followup}
''')
