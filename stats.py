
with open('tasks.md', 'r') as f:
    lines = f.readlines()

usd_pending = 0
usd_merged = 0
high_value_pending = []

for line in lines:
    if (line.startswith('| BT-') or line.startswith('| BT-OLD-')) and not 'ID' in line:
        cols = [c.strip() for c in line.split('|') if c.strip()]
        # columns: 0=ID, 1=accept time, 2=source, 3=project, 4=url, 5=reward, 6=currency, 7=value, 8=status ...
        if len(cols) >= 8:
            currency = cols[5]
            try:
                value = float(cols[6])
                status = cols[7]
                if currency == 'USD':
                    if status in ['pr_open', 'open', 'new', 'pr_open_alt']:
                        if '废弃' not in line:
                            usd_pending += value
                            if value >= 5:
                                task_id = cols[0]
                                project = cols[3]
                                url = cols[4]
                                high_value_pending.append(f'- {task_id}: {project} - ${value} - {status}')
                    elif status == 'merged':
                        usd_merged += value
            except Exception as e:
                pass

print(f'✅ 核心数据:')
print(f'总待结算: ${usd_pending:.2f} USD')
print(f'已合并待结算: ${usd_merged:.2f} USD')
print()
print(f'✅ 高价值任务状态 (≥$5):')
for t in high_value_pending:
    print(t)
