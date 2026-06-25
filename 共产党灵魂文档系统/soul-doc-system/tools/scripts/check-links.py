#!/usr/bin/env python3
"""文档链接有效性检查
用法: python check-links.py [soul-doc-root]
递归扫描所有 .md 文件，检查内部链接是否存在。
"""
import sys, os, re

def check_links(root="."):
    broken = []
    for dirpath, _, files in os.walk(root):
        for fname in files:
            if not fname.endswith(".md"):
                continue
            fpath = os.path.join(dirpath, fname)
            with open(fpath, "r", encoding="utf-8") as f:
                content = f.read()
            # find markdown links: [text](path)
            for m in re.finditer(r"\[.*?\]\(([^)]+)\)", content):
                link = m.group(1)
                if link.startswith("http"):
                    continue  # skip external links
                target = os.path.normpath(os.path.join(dirpath, link))
                if not os.path.exists(target):
                    broken.append((fpath, link, target))
    if broken:
        print(f"broken links: {len(broken)}")
        for src, link, target in broken:
            print(f"  {src}: {link} → {target}")
        sys.exit(1)
    else:
        print("all internal links valid.")

if __name__ == "__main__":
    root = sys.argv[1] if len(sys.argv) > 1 else "."
    check_links(root)
