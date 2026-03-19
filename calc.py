
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
    # New columns: ['', ID, 接受时间, 来源, 项目, 奖励, github项目地址, 状态, 最后更新, 备注]
    # cols indexes: 0:empty, 1:ID, 2:accepted, 3:source, 4:project, 5:reward, 6:url, 7:state, 8:updated, 9:notes
    if len(cols) < 9:
        continue
    
    # Extract numeric value from reward column
    reward_text = cols[5].lower()
    # Find the first number in reward text
    match = re.search(r'(\d+(\.\d+)?)', reward_text)
    if not match:
        continue
    try:
        value = float(match.group(1))
    except:
        continue
    
    state = cols[7].lower()
    if 'merged' in state:
        total_merged += value
    elif 'open' in state or 'available' in state or 'comment' in state:
        total_pending += value
    
    # Check if it's USD-based currency
    if 'usd' in reward_text and ('open' in state or 'available' in state or 'comment' in state):
        pending_usd += value
    elif 'usdc' in reward_text and ('open' in state or 'available' in state or 'comment' in state):
        pending_usd += value
    elif 'usdt' in reward_text and ('open' in state or 'available' in state or 'comment' in state):
        pending_usd += value

print(f"Total pending (all currencies, numeric extracted): ${total_pending:.2f}")
print(f"Total pending (USD/USDC/USDT only): ${pending_usd:.2f}")
print(f"Total merged (all currencies, numeric extracted): ${total_merged:.2f}")
