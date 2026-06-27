#!/usr/bin/env python3
"""
批量更新所有 .md 文件的时间戳格式。

旧格式：
  > **最后更新**：YYYY-MM-DDTHH:MM

新格式：
  > **创建时间**：YYYY-MM-DDTHH:MM
  > **更新时间**：YYYY-MM-DDTHH:MM
  > 每次更新文件，就要同时更新时间戳

规则：
- 创建时间：保留原始时间（从旧格式推断或保持已有）
- 更新时间：每次运行脚本时更新为当前时间
- 如果已有创建时间+更新时间，只更新时间
- 如果只有最后更新，推断创建时间=最后更新时间，然后更新 更新时间
"""

import os
import re
import sys
from datetime import datetime, timezone, timedelta

# 中央灵魂文档系统根目录
CENTRAL_PATH = r"C:\Users\a1227\.halo\temp\artifacts\中央灵魂文档系统"

# 当前时间（分钟级格式）
NOW = datetime.now(timezone(timedelta(hours=8))).strftime("%Y-%m-%dT%H:%M")


def process_file(filepath):
    """处理单个 .md 文件的时间戳更新"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"  读取失败: {filepath} - {e}")
        return False

    original = content
    updated = False

    # 情况1：已有 创建时间 + 更新时间 + 提示语 → 只更新 更新时间
    if re.search(r'创建时间[：:]\s*\d{4}-\d{2}-\d{2}T\d{2}:\d{2}', content):
        # 只更新 更新时间
        content = re.sub(
            r'(> \*\*更新时间\*\*[：:])\s*\d{4}-\d{2}-\d{2}T\d{2}:\d{2}',
            f'\\1 {NOW}',
            content
        )
        # 确保提示语存在
        if '每次更新文件，就要同时更新时间戳' not in content:
            content = content.replace(
                '> **更新时间**',
                '> **更新时间**\n> 每次更新文件，就要同时更新时间戳'
            )
        updated = True

    # 情况2：有 最后更新 但没有 创建时间 → 升级
    elif re.search(r'最后更新[：:]\s*\d{4}-\d{2}-\d{2}T\d{2}:\d{2}', content):
        # 提取最后更新的时间作为创建时间
        match = re.search(r'最后更新[：:]\s*(\d{4}-\d{2}-\d{2}T\d{2}:\d{2})', content)
        created_time = match.group(1) if match else NOW

        # 替换 最后更新 行
        content = re.sub(
            r'> \*\*最后更新\*\*[：:]\s*\d{4}-\d{2}-\d{2}T\d{2}:\d{2}',
            f'> **创建时间**：{created_time}\n> **更新时间**：{NOW}\n> 每次更新文件，就要同时更新时间戳',
            content
        )
        updated = True

    # 情况3：没有任何时间戳 → 在橄榄枝header后添加
    elif '╔' in content and '╚' in content:
        # 在橄榄枝header结束后插入时间戳
        header_end = content.find('╚')
        if header_end != -1:
            # 找到header的结束行
            end_line = content.find('\n', header_end)
            if end_line != -1:
                # 在header结束后插入
                insert_pos = content.find('\n\n', end_line)
                if insert_pos != -1:
                    timestamp_block = f'\n> **创建时间**：{NOW}\n> **更新时间**：{NOW}\n> 每次更新文件，就要同时更新时间戳\n'
                    content = content[:insert_pos] + timestamp_block + content[insert_pos:]
                    updated = True

    if updated and content != original:
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        except Exception as e:
            print(f"  写入失败: {filepath} - {e}")
            return False

    return False


def main():
    count = 0
    errors = 0

    for root, dirs, files in os.walk(CENTRAL_PATH):
        for filename in files:
            if filename.endswith('.md'):
                filepath = os.path.join(root, filename)
                if process_file(filepath):
                    count += 1
                    print(f"  更新: {filepath[len(CENTRAL_PATH)+1:]}")
                elif '最后更新' in open(filepath, 'r', encoding='utf-8').read() or '创建时间' in open(filepath, 'r', encoding='utf-8').read():
                    pass  # 已是最新格式
                elif '╔' in open(filepath, 'r', encoding='utf-8').read():
                    pass  # 有header但无时间戳（已处理或不需要）

    print(f"\n完成: 更新了 {count} 个文件")
    print(f"当前时间: {NOW}")


if __name__ == '__main__':
    main()
