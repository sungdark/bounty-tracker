
import re
from pathlib import Path

content = Path('tasks.md').read_text()
lines = content.split('\n')

total_pending = 0.0
total_merged = 0.0
pending_usd = 0.0

for line in lines:
    if not line.startswith('| BT-'):
        continue
    cols = [c.strip() for c in line.split('|')]
    # cols: ['', ID, accepted, source, project, link, reward, currency, value, state, ...]
    if len(cols) < 9:
        continue
    try:
        value = float(cols[8])
    except:
        continue
    state = cols[9].lower()
    if 'merged' in state:
        total_merged += value
    elif 'open' in state or 'available' in state:
        total_pending += value
    if 'usd' in cols[7].lower() and ('open' in state or 'available' in state):
        pending_usd += value
    elif 'usdc' in cols[7].lower() and ('open' in state or 'available' in state):
        pending_usd += value
    elif 'usdt' in cols[7].lower() and ('open' in state or 'available' in state):
        pending_usd += value

print(f"Total pending (all currencies): ${total_pending:.2f}")
print(f"Total pending (USD/USDC/USDT): ${pending_usd:.2f}")
print(f"Total merged (all currencies): ${total_merged:.2f}")
