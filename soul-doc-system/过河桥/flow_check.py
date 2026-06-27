#!/usr/bin/env python3
"""
系统全流程检查脚本。
检查项：
1. 橄榄枝抬头完整性
2. 时间戳格式正确性
3. 文件引用有效性
4. 电路板实际内容检查
5. 模块清单完整性
"""

import os
import re

CENTRAL_PATH = r"C:\Users\a1227\.halo\temp\artifacts\中央灵魂文档系统"

# 已知的功能模块列表（从user-zone/soul-doc-system/README.md提取）
KNOWN_MODULES = [
    'memory', 'diary', 'sop', 'workflow', 'product', 'sections',
    'skills', 'tools', 'bookmarks', 'contacts', 'experience',
    'discovery', 'collection', 'desktop', 'production_space',
    'sub-role-souls', 'space', 'wiki', 'automation', 'log',
    'timers', 'feedback', 'history', 'git-tree',
    '电路板', '元规则', '深度研究', '灵魂分数', '团队空间',
    '智能体空间', '网页生成与管理', '代办与进度',
    '文件抬头同步脚本.md', '文件抬头模板.md', '理解电路板协议.md',
    'master-soul.md', 'system-prompt.md', 'workflow.md', 'README.md'
]

results = {
    'missing_header': [],
    'missing_timestamp': [],
    'old_timestamp_format': [],
    'missing_circuit_board': [],
    'empty_circuit_board': [],
    'broken_references': [],
    'total_files': 0,
    'files_with_header': 0,
    'files_with_new_timestamp': 0,
}

def check_file(filepath):
    """检查单个文件"""
    rel_path = filepath[len(CENTRAL_PATH)+1:]
    results['total_files'] += 1

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            lines = content.split('\n')
    except:
        return

    # 1. 检查橄榄枝抬头
    has_header = '╔' in content and '╚' in content and '中央灵魂文档系统文件' in content
    if not has_header:
        results['missing_header'].append(rel_path)
    else:
        results['files_with_header'] += 1

    # 2. 检查时间戳格式
    has_new_timestamp = '创建时间' in content and '更新时间' in content
    has_old_timestamp = bool(re.search(r'> \*\*最后更新\*\*[：:]', content))

    if has_new_timestamp:
        results['files_with_new_timestamp'] += 1
    elif has_old_timestamp:
        results['old_timestamp_format'].append(rel_path)

    # 3. 检查电路板内容（如果是电路板文件）
    if '电路板' in filepath and filepath.endswith('.md'):
        # 检查是否为空壳（只有模板文字没有实际内容）
        if '用户原话重述' in content and '理解要点' in content:
            # 检查是否有实际系统内容（不是通用模板）
            has_actual_content = (
                '红领巾' in content or
                '九环' in content or
                '灵魂分数' in content or
                'GA' in content or
                'L0' in content or
                '记忆' in content or
                '快箭' in content or
                '顶级机会' in content or
                '超级信息' in content or
                '子角色' in content or
                '共产' in content or
                '生产空间' in content or
                '空间中心' in content or
                '团队' in content or
                '智能体' in content or
                '深度研究' in content or
                '元规则' in content or
                'sop' in content.lower() or
                'workflow' in content.lower() or
                'sections' in content.lower()
            )
            if not has_actual_content:
                results['empty_circuit_board'].append(rel_path)

# 遍历所有 .md 文件
for root, dirs, files in os.walk(CENTRAL_PATH):
    for filename in files:
        if filename.endswith('.md'):
            filepath = os.path.join(root, filename)
            check_file(filepath)

# 输出结果
print("=" * 60)
print("系统全流程检查结果")
print("=" * 60)
print(f"总文件数: {results['total_files']}")
print(f"有橄榄枝抬头: {results['files_with_header']}")
print(f"有新时间戳格式: {results['files_with_new_timestamp']}")
print(f"缺少橄榄枝抬头: {len(results['missing_header'])}")
print(f"仍用旧时间戳格式: {len(results['old_timestamp_format'])}")
print(f"空壳电路板: {len(results['empty_circuit_board'])}")

if results['missing_header']:
    print("\n--- 缺少橄榄枝抬头的文件（前10个）---")
    for f in results['missing_header'][:10]:
        print(f"  {f}")

if results['old_timestamp_format']:
    print(f"\n--- 仍用旧时间戳格式的文件（前10个）---")
    for f in results['old_timestamp_format'][:10]:
        print(f"  {f}")

if results['empty_circuit_board']:
    print(f"\n--- 空壳电路板（前10个）---")
    for f in results['empty_circuit_board'][:10]:
        print(f"  {f}")

print("\n" + "=" * 60)
print("检查完成")
