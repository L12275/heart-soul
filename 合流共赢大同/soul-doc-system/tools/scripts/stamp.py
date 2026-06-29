#!/usr/bin/env python3
"""文件时间戳标注
用法: cd 模型隔离区 && python soul-doc-system/tools/scripts/stamp.py
给所有markdown文件添加/更新时间戳标记。
格式: YYYY-MM-DD HH:MM（分钟级）
"""
import os, sys, datetime, re

def get_timestamp():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M')

def stamp_file(filepath):
    """给文件添加/更新时间戳"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    now = get_timestamp()
    old_ts = re.search(r'\*最后更新[：:]\s*(\d{4}-\d{2}-\d{2} \d{2}:\d{2})\*', content)
    if old_ts:
        content = content.replace(old_ts.group(0), f'*最后更新：{now}*')
    else:
        # Add timestamp at the bottom
        if content and not content.endswith('\n'):
            content += '\n'
        content += f'\n---\n*最后更新：{now}*\n'
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    return True

def main():
    base = sys.argv[1] if len(sys.argv) > 1 else "."
    count = 0
    for root, dirs, files in os.walk(base):
        dirs[:] = [d for d in dirs if d not in {'.git', '__pycache__', 'node_modules', '.venv', 'venv'}]
        for f in files:
            if f.endswith('.md'):
                filepath = os.path.join(root, f)
                try:
                    if stamp_file(filepath):
                        count += 1
                except Exception as e:
                    print(f"Error: {filepath}: {e}")
    print(f"Stamped {count} files")

if __name__ == "__main__":
    main()
