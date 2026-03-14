#!/usr/bin/env python3
import csv
import json
import os
import time
import requests
from datetime import datetime, timezone
import subprocess

# 配置
BOUNTIES_CSV = "bounties.csv"
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")
HEADERS = {"Authorization": f"token {GITHUB_TOKEN}"} if GITHUB_TOKEN else {}

# 扫描目标
SCAN_TARGETS = [
    # GitHub赏金相关话题
    {"name": "GitHub Bounties", "query": "label:bounty is:issue is:open", "type": "github_search"},
    {"name": "Bug Bounty Programs", "url": "https://github.com/arkadiyt/bounty-targets-data/raw/main/data/hackerone_data.json", "type": "json"},
    {"name": "Bugcrowd Programs", "url": "https://github.com/arkadiyt/bounty-targets-data/raw/main/data/bugcrowd_data.json", "type": "json"},
]

def load_existing_bounties():
    """加载已有的赏金记录，避免重复"""
    existing = set()
    if os.path.exists(BOUNTIES_CSV):
        with open(BOUNTIES_CSV, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                existing.add(row["url"])
    return existing

def save_bounty(bounty):
    """保存新的赏金机会到CSV"""
    file_exists = os.path.exists(BOUNTIES_CSV)
    fieldnames = ["time", "source", "title", "url", "amount", "status", "notes"]
    
    with open(BOUNTIES_CSV, "a", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow(bounty)
    print(f"✅ 新增赏金机会: {bounty['title']} ({bounty['amount']})")

def scan_github_bounties(existing_urls):
    """扫描GitHub公开赏金问题"""
    print("🔍 扫描GitHub赏金问题...")
    try:
        # GitHub搜索API：搜索带有bounty标签的公开issue
        url = "https://api.github.com/search/issues"
        params = {"q": "label:bounty is:issue is:open", "per_page": 50, "sort": "updated", "order": "desc"}
        response = requests.get(url, headers=HEADERS, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        new_count = 0
        for item in data.get("items", []):
            issue_url = item["html_url"]
            if issue_url in existing_urls:
                continue
                
            # 提取赏金金额（从标题或body中识别）
            title = item["title"]
            body = item.get("body", "")
            amount = "未知"
            # 简单的金额识别逻辑
            for text in [title, body]:
                if "$" in text:
                    import re
                    matches = re.findall(r"\$(\d+(?:\.\d{1,2})?)", text)
                    if matches:
                        amount = f"${max(map(float, matches))}"
                        break
                        
            bounty = {
                "time": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
                "source": "GitHub",
                "title": title,
                "url": issue_url,
                "amount": amount,
                "status": "待评估",
                "notes": f"仓库: {item['repository_url'].replace('https://api.github.com/repos/', '')}, 更新时间: {item['updated_at']}"
            }
            save_bounty(bounty)
            new_count += 1
            
        print(f"✅ GitHub扫描完成，新增 {new_count} 个机会")
        return new_count
    except Exception as e:
        print(f"❌ GitHub扫描失败: {str(e)}")
        return 0

def scan_bounty_platforms(existing_urls):
    """扫描HackerOne/Bugcrowd等平台的公开赏金项目"""
    print("🔍 扫描公开赏金平台项目...")
    new_count = 0
    
    # HackerOne
    try:
        response = requests.get("https://github.com/arkadiyt/bounty-targets-data/raw/main/data/hackerone_data.json", timeout=10)
        programs = response.json()
        for program in programs[:20]:  # 取前20个最新的
            program_url = f"https://hackerone.com/{program['handle']}"
            if program_url in existing_urls:
                continue
                
            bounty = {
                "time": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
                "source": "HackerOne",
                "title": program["name"],
                "url": program_url,
                "amount": program.get("offers_bounties", False) and "有赏金" or "无公开赏金",
                "status": "待评估",
                "notes": f"平台: HackerOne, 范围数量: {len(program.get('targets', {}).get('in_scope', []))}"
            }
            save_bounty(bounty)
            new_count += 1
    except Exception as e:
        print(f"❌ HackerOne扫描失败: {str(e)}")
    
    # Bugcrowd
    try:
        response = requests.get("https://github.com/arkadiyt/bounty-targets-data/raw/main/data/bugcrowd_data.json", timeout=10)
        programs = response.json()
        for program in programs[:20]:  # 取前20个最新的
            program_url = program.get("program_url", "")
            if not program_url or program_url in existing_urls:
                continue
                
            bounty = {
                "time": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
                "source": "Bugcrowd",
                "title": program["name"],
                "url": f"https://bugcrowd.com{program_url}",
                "amount": program.get("max_payout", "未知"),
                "status": "待评估",
                "notes": f"平台: Bugcrowd, 最高奖励: {program.get('max_payout', '未知')}"
            }
            save_bounty(bounty)
            new_count += 1
    except Exception as e:
        print(f"❌ Bugcrowd扫描失败: {str(e)}")
    
    print(f"✅ 赏金平台扫描完成，新增 {new_count} 个机会")
    return new_count

def git_push_changes():
    """推送更新到GitHub仓库"""
    print("📤 推送更新到GitHub仓库...")
    try:
        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M")
        subprocess.run(["git", "add", "."], check=True, capture_output=True)
        subprocess.run(["git", "commit", "-m", f"scan: update bounty opportunities {timestamp}"], check=True, capture_output=True)
        subprocess.run(["git", "push"], check=True, capture_output=True)
        print("✅ 推送成功")
    except subprocess.CalledProcessError as e:
        print(f"❌ 推送失败: {e.stderr.decode()}")
    except Exception as e:
        print(f"❌ Git操作失败: {str(e)}")

def main():
    print(f"🚀 开始赏金机会扫描 - {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}")
    os.chdir("/root/.openclaw/workspace/bounty-tracker")
    
    # 拉取最新代码
    subprocess.run(["git", "pull"], capture_output=True)
    
    existing_urls = load_existing_bounties()
    print(f"📋 已有 {len(existing_urls)} 条记录")
    
    total_new = 0
    total_new += scan_github_bounties(existing_urls)
    total_new += scan_bounty_platforms(existing_urls)
    
    if total_new > 0:
        # 生成扫描结果文件
        scan_file = f"scan-results/{datetime.now(timezone.utc).strftime('%Y-%m-%d_%H%M')}_scan_results.md"
        with open(scan_file, "w", encoding="utf-8") as f:
            f.write(f"# 赏金扫描结果 - {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}\n\n")
            f.write(f"## 扫描概览\n")
            f.write(f"- 新增机会: {total_new} 个\n")
            f.write(f"- 累计记录: {len(existing_urls) + total_new} 个\n\n")
            f.write(f"## 高价值机会（≥$50）\n")
            # 读取刚新增的高价值机会
            with open(BOUNTIES_CSV, "r", encoding="utf-8") as csvf:
                reader = csv.DictReader(csvf)
                high_value = []
            for row in reader:
                if row["amount"].startswith("$"):
                    try:
                        amount = float(row["amount"][1:].replace(",", ""))
                        if amount >= 50:
                            high_value.append(row)
                    except ValueError:
                        # 跳过无法解析的金额
                        pass
                for row in high_value[-total_new:]:  # 只显示本次新增的
                    f.write(f"- [{row['title']}]({row['url']}) - {row['amount']}\n")
        
        git_push_changes()
    else:
        print("ℹ️ 本次扫描未发现新的机会")
    
    print(f"🏁 扫描完成，共新增 {total_new} 个赏金机会")
    return total_new

if __name__ == "__main__":
    main()
