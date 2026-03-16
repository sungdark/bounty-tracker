
import re
from datetime import datetime

with open('tasks.md', 'r') as f:
    content = f.read()

# Calculate stats
total_pending = 0
total_merged = 0
usd_pending = 0
usd_merged = 0

for line in content.split('\n'):
    if (line.startswith('| BT-') or line.startswith('| BT-OLD-')) and not 'ID' in line:
        parts = [p.strip() for p in line.split('|') if p.strip()]
        if len(parts) >= 8:
            reward = parts[4]
            currency = parts[5]
            value = parts[6]
            status = parts[7]
            try:
                v = float(value)
                if currency == 'USD':
                    if status in ['pr_open', 'open', 'new', 'pr_open_alt']:
                        usd_pending += v
                    elif status in ['merged']:
                        usd_merged += v
            except Exception as e:
                pass

print(f'✅ 核心数据:')
print(f'总待结算: ${usd_pending:.2f} USD')
print(f'已合并待结算: ${usd_merged:.2f} USD')
