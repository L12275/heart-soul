#!/usr/bin/env python3
"""
更新文件末尾的 *最后更新* 时间戳为 *更新时间*。
只处理文件末尾附近的最后更新（footer metadata），不处理内容中的时间戳说明。
"""

import os
import re

CENTRAL_PATH = r"C:\Users\a1227\.halo\temp\artifacts\中央灵魂文档系统"
NOW = "2026-06-27T21:57"  # 与header更新时间一致

def update_footer_timestamp(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except:
        return False

    original = content

    # 查找文件末尾的 *最后更新*（在最后20行内）
    lines = content.split('\n')
    last_20 = lines[-20:] if len(lines) >= 20 else lines

    # 只在末尾区域查找 *最后更新：...*
    footer_pattern = re.compile(r'\*最后更新[：:]\s*[\d\- \t:]+?\*')
    hint_line = '*每次更新文件，就要同时更新时间戳*'

    # 检查末尾是否有 最后更新
    has_footer_timestamp = False
    for line in last_20:
        if re.search(r'\*最后更新[：:]', line):
            has_footer_timestamp = True
            break

    if not has_footer_timestamp:
        return False

    # 替换末尾的 *最后更新* 为 *更新时间*
    # 策略：从后往前找，替换最后出现的一个
    new_content = content
    matches = list(footer_pattern.finditer(content))
    if matches:
        last_match = matches[-1]
        old_text = last_match.group(0)
        # 提取时间部分
        time_match = re.search(r'[\d]{4}-[\d]{2}-[\d]{2}[ \t]*[\d:]+', old_text)
        if time_match:
            old_time = time_match.group(0)
            # 转换为分钟级格式
            new_time = old_time.replace(' ', 'T')
            if 'T' not in new_time:
                new_time = new_time.replace(' ', 'T')
            # 替换
            new_text = f'*更新时间：{new_time}*'
            # 在原位置附近添加提示语
            new_content = content[:last_match.start()] + new_text + '\n' + hint_line + content[last_match.end():]
        else:
            new_text = f'*更新时间：{NOW}*'
            new_content = content[:last_match.start()] + new_text + '\n' + hint_line + content[last_match.end():]

    if new_content != original:
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True
        except:
            return False
    return False

count = 0
for root, dirs, files in os.walk(CENTRAL_PATH):
    for filename in files:
        if filename.endswith('.md'):
            filepath = os.path.join(root, filename)
            if update_footer_timestamp(filepath):
                count += 1
                rel = filepath[len(CENTRAL_PATH)+1:]
                # 只打印关键文件
                if any(k in rel for k in ['master-soul', 'system-prompt', 'README', '电路板', '元规则', 'SOP']):
                    print(f"  更新footer: {rel}")

print(f"\nFooter时间戳更新完成: 更新了 {count} 个文件")
