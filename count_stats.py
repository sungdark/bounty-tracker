
import sys
import re
from datetime import datetime

# Count tasks by status
status_counts = {}
total_value = 0.0
with open('tasks.md', 'r') as f:
    for line in f:
        if '|' not in line or line.startswith('|---') or line.startswith('#') or 'ID' in line:
            continue
        parts = [p.strip() for p in line.split('|') if p.strip()]
        # columns: 0=ID, 1=accept_time, 2=source, 3=project, 4=reward, 5=github, 6=status, 7=last_update, 8=notes
        if len(parts) >= 7:
            status = parts[6]
            if status not in status_counts:
                status_counts[status] = 0
            status_counts[status] += 1

# Calculate approximate total value
def parse_reward(reward_str):
    if reward_str in ['$0+ USD', 'varies USD', 'varies PKR', 'varies INR', 'stipend USD', 'SCAM ALERT', '$0 USD', 'SCAM', '$0+', 'varies']:
        return 0.0
    # Extract USD/USDC/USDT values with "up to" handling
    up_to_match = re.search(r'up to\s+([\d,]+)\s*(USD|USDC|USDT)', reward_str, re.IGNORECASE)
    if up_to_match:
        # only count max as potential, not guaranteed
        return float(up_to_match.group(1).replace(',', ''))
    usd_match = re.search(r'([\d,]+)\s*(USD|USDC|USDT)', reward_str, re.IGNORECASE)
    if usd_match:
        return float(usd_match.group(1).replace(',', ''))
    # RTC roughly approximate 1 RTC = $0.5
    rtc_match = re.search(r'([\d,]+)\s*RTC', reward_str, re.IGNORECASE)
    if rtc_match:
        return float(rtc_match.group(1)) * 0.5
    # SATS roughly 1000 SATS = $0.05
    sats_match = re.search(r'([\d,]+)\s*SATS', reward_str, re.IGNORECASE)
    if sats_match:
        return float(sats_match.group(1)) * 0.00005
    # EUR approximate 1 EUR = $1.05
    eur_match = re.search(r'([\d,]+)\s*EUR', reward_str, re.IGNORECASE)
    if eur_match:
        return float(eur_match.group(1)) * 1.05
    # 100 ISNAD ~ $0
    isnad_match = re.search(r'([\d,]+)\s*ISNAD', reward_str, re.IGNORECASE)
    if isnad_match:
        return 0.0
    # fixed reward like "$2000 USD"
    fixed_match = re.search(r'\$([\d,]+)', reward_str)
    if fixed_match:
        return float(fixed_match.group(1).replace(',', ''))
    return 0.0

with open('tasks.md', 'r') as f:
    for line in f:
        if '|' not in line or line.startswith('|---') or line.startswith('#') or 'ID' in line:
            continue
        parts = [p.strip() for p in line.split('|') if p.strip()]
        if len(parts) >= 5:
            reward = parts[4]
            total_value += parse_reward(reward)

print(f'Status counts: {status_counts}')
print(f'Approximate total potential value (USD): ${total_value:.2f}')
print(f'Last scan: {datetime.utcnow().isoformat()} UTC')

# Count total tasks
total_tasks = sum(status_counts.values())
print(f'Total tracked tasks: {total_tasks}')
