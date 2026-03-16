
# Manual calculation from the table above
# | BT-OLD-0001 | ... | $15 | USD | 15 | pr_open
# | BT-OLD-0002 | ... | $10 | USD | 10 | pr_open
# | BT-OLD-0003 | ... | $2500 | USD | 2500 | pr_open
# | BT-OLD-0004 | ... | $50 | USD | 50 | pr_open_alt (废弃，排除)
# | BT-OLD-0005 | ... | $50 | USD | 50 | pr_open
# | BT-OLD-0006 | ... | $200 | USD | 200 | pr_open
# | BT-0080 | ... | $200 | USD | 200 | pr_open

usd_pending = 15 + 10 + 2500 + 50 + 200 + 200
# BT-OLD-0004 excluded (废弃)
usd_merged = 0  # No USD merged tasks yet

high_value = [
    ("BT-OLD-0003", "tenstorrent/tt-metal", 2500, "pr_open"),
    ("BT-OLD-0006", "CapSoftware/Cap", 200, "pr_open"),
    ("BT-0080", "lwouis/alt-tab-macos", 200, "pr_open"),
    ("BT-OLD-0005", "tscircuit/circuitjson.com", 50, "pr_open"),
    ("BT-OLD-0001", "Mint-Claw/market-monitor", 15, "pr_open"),
    ("BT-OLD-0002", "Mint-Claw/content-split", 10, "pr_open"),
]

new_opportunities = [
    ("BT-0130", "Scottcjn/rustchain-bounties", "https://github.com/Scottcjn/rustchain-bounties/issues/2127", "25 RTC", "open", "修复Beacon Atlas自动注册和rustchain.org路由问题"),
    ("BT-0129", "Scottcjn/rustchain-bounties", "https://github.com/Scottcjn/rustchain-bounties/issues/2103", "1-25 RTC", "open", "Star+关注领RTC，简单易做"),
    ("BT-0128", "SPLURT-Station/S.P.L.U.R.T-tg", "https://github.com/SPLURT-Station/S.P.L.U.R.T-tg/issues/871", "未公开", "open", "口红唇印爪印印章功能开发"),
    ("BT-0127", "SPLURT-Station/S.P.L.U.R.T-tg", "https://github.com/SPLURT-Station/S.P.L.U.R.T-tg/issues/872", "未公开", "open", "警卫身体摄像头游戏功能开发"),
]

# Risk points
risks = [
    ("BT-OLD-0003", "tenstorrent/tt-metal", "PR提交超过2周无反馈，需要跟进"),
    ("BT-OLD-0006", "CapSoftware/Cap", "PR提交超过2周无反馈，需要跟进"),
]

print("✅ 核心数据:")
print(f"总待结算: ${usd_pending} USD")
print(f"已合并待结算: ${usd_merged} USD")
print()
print("✅ 高价值任务状态 (≥$5):")
for id, project, val, status in sorted(high_value, key=lambda x: -x[2]):
    print(f"• {id} {project}: ${val} - {status}")
print()
print("✅ 新机会（今日扫描新增):")
for id, project, url, val, status, note in new_opportunities:
    print(f"• {id} {project}: {val} - {status} - {note}")
print()
print("✅ 风险点:")
for id, project, note in risks:
    print(f"• {id} {project}: {note}")
