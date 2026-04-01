import json, sys, re
from urllib.request import urlopen

url = "https://api.github.com/search/issues?q=bounty+in:title+is:issue+state:open&per_page=100&sort=updated"
with urlopen(url) as r:
    data = json.loads(r.read())

items = data.get('items', [])
print(f"Total matches: {data['total_count']}", file=sys.stderr)

valid = []
for item in items:
    title = item.get('title', '')
    body = item.get('body', '') or ''
    labels = [l['name'] for l in item.get('labels', [])]

    # Skip spam
    if any(ord(c) > 127 for c in title[:30]):
        continue
    spam_words = ['Big Bounty', 'PG电子', 'MG野马', 'casino', 'slots', 'gambling', '足球', '博彩']
    if any(w in title for w in spam_words):
        continue
    # Skip bot issues that are just posting links
    if 'bot' in item.get('user', {}).get('login', '').lower() and len(body) < 50:
        continue
    if 'devpool-directory' in item.get('repository_url', ''):
        continue  # just a directory listing issue, not a real bounty

    # Must be unclaimed
    assignees = item.get('assignees', [])
    if assignees:
        continue

    amount = None

    # Check labels for price
    for lbl in labels:
        m = re.search(r'(\d+)\s*(?:USD|RTC|Reward)', lbl, re.IGNORECASE)
        if m:
            amount = int(m.group(1))
            break
        m = re.search(r'Price:\s*\$?(\d+)', lbl, re.IGNORECASE)
        if m:
            amount = int(m.group(1))
            break

    # Check title/body for amount
    if not amount:
        text = title + ' ' + body
        patterns = [
            r'\$(\d+)',
            r'(\d+)\s*RTC',
            r'(\d+)\s*USD',
            r'(\d+)\s*reward',
            r'(\d+)\s*dollar',
        ]
        for pattern in patterns:
            m = re.search(pattern, text, re.IGNORECASE)
            if m:
                amount = int(m.group(1))
                break

    if amount is not None or 'bounty' in title.lower():
        valid.append({
            'title': title,
            'url': item.get('html_url'),
            'repo': item.get('repository_url', '').replace('https://api.github.com/repos/', ''),
            'number': item.get('number'),
            'amount': amount,
            'labels': labels,
            'created': item.get('created_at'),
            'updated': item.get('updated_at'),
            'body_preview': body[:200].replace('\n', ' ')
        })

print(f"Valid unclaimed bounty issues: {len(valid)}\n")
for v in valid:
    amt_str = f"${v['amount']}" if v['amount'] else "TBD"
    print(f"[{amt_str}] {v['title']}")
    print(f"  Repo: {v['repo']}#{v['number']}")
    print(f"  URL: {v['url']}")
    print(f"  Labels: {v['labels']}")
    print(f"  Created: {v['created']}, Updated: {v['updated']}")
    print(f"  Body: {v['body_preview'][:150]}...")
    print()
