#!/usr/bin/env python3
"""灵魂分数趋势检查工具
用法: python soul-score-check.py [soul-doc-root]
读取 灵魂分数/ledger.md，输出近N天分数趋势。
"""
import sys, os, re
from datetime import datetime, timedelta

def check(root="."):
    ledger_path = os.path.join(root, "灵魂分数", "ledger.md")
    if not os.path.exists(ledger_path):
        print(f"not found: {ledger_path}")
        sys.exit(1)
    with open(ledger_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    entries = []
    for line in lines:
        m = re.match(r"\| (\d{4}-\d{2}-\d{2}) \| ([+-]?\d+) \| (.+) \|", line.strip())
        if m:
            entries.append({"date": m.group(1), "delta": int(m.group(2)), "reason": m.group(3)})
    if not entries:
        print("no entries found in ledger")
        return
    # Show last 10 entries
    recent = entries[-10:]
    total = sum(e["delta"] for e in recent)
    print(f"last {len(recent)} entries | trend: {'positive' if total >= 0 else 'NEGATIVE'} ({total:+d})")
    for e in recent:
        print(f"  {e['date']} {e['delta']:+d} — {e['reason']}")

if __name__ == "__main__":
    root = sys.argv[1] if len(sys.argv) > 1 else "."
    check(root)
