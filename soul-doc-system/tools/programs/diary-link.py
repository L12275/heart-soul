#!/usr/bin/env python3
"""日记交叉引用生成
用法: python diary-link.py <diary-file.md>
为日记条目自动生成相关 sections/ 链接。
"""
import sys, os, re

def find_related(diary_path, sections_root="."):
    """根据日记内容匹配相关sections文件"""
    with open(diary_path, "r", encoding="utf-8") as f:
        content = f.read()
    keywords = re.findall(r"[a-z]{3,}", content.lower())
    related = []
    for dirpath, _, files in os.walk(os.path.join(sections_root, "sections")):
        for fname in files:
            if not fname.endswith(".md"):
                continue
            fpath = os.path.join(dirpath, fname)
            with open(fpath, "r", encoding="utf-8") as sf:
                sec_content = sf.read().lower()
            score = sum(1 for kw in keywords if kw in sec_content)
            if score > 2:
                rel_path = os.path.relpath(fpath, sections_root)
                related.append((score, rel_path))
    related.sort(reverse=True)
    return [r[1] for r in related[:5]]

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: python diary-link.py <diary-file.md>")
        sys.exit(1)
    diary = sys.argv[1]
    root = os.path.dirname(os.path.dirname(diary))  # parent of diary/ = soul-doc root
    links = find_related(diary, root)
    if links:
        print("related sections:")
        for l in links:
            print(f"  - {l}")
    else:
        print("no related sections found.")
