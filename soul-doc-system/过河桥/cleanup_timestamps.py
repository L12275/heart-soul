#!/usr/bin/env python3
"""清理重复的 > **最后更新** 行（新时间戳块后面的旧行）"""

import os
import re

CENTRAL_PATH = r"C:\Users\a1227\.halo\temp\artifacts\中央灵魂文档系统"

def clean_duplicate_timestamp(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except:
        return False

    original = ''.join(lines)
    cleaned = []
    i = 0
    removed = False

    while i < len(lines):
        line = lines[i]

        # 检查是否是新的时间戳块（创建时间 + 更新时间 + 提示语）
        if '创建时间' in line and '更新时间' in lines[i+1] if i+1 < len(lines) else False:
            # 收集新时间戳块（3行）
            cleaned.append(line)
            cleaned.append(lines[i+1])
            cleaned.append(lines[i+2])
            i += 3
            # 跳过空行
            while i < len(lines) and lines[i].strip() == '':
                cleaned.append(lines[i])
                i += 1
            # 检查下一行是否是旧的 > **最后更新**，如果是就跳过
            if i < len(lines) and re.match(r'> \*\*最后更新\*\*[：:]\s*\d{4}-\d{2}-\d{2}T\d{2}:\d{2}', lines[i]):
                i += 1  # 跳过旧的
                removed = True
            continue

        cleaned.append(line)
        i += 1

    result = ''.join(cleaned)
    if result != original:
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(result)
            return removed
        except:
            return False
    return False

count = 0
for root, dirs, files in os.walk(CENTRAL_PATH):
    for filename in files:
        if filename.endswith('.md'):
            filepath = os.path.join(root, filename)
            if clean_duplicate_timestamp(filepath):
                count += 1
                rel = filepath[len(CENTRAL_PATH)+1:]
                print(f"  清理: {rel}")

print(f"\n清理完成: 移除了 {count} 个文件中的重复旧时间戳")
