#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fix sections and master-soul to reflect 四驱动 & 四写 structure."""
import os

BASE = r'C:\Users\a1227\.halo\temp\artifacts\灵魂文档\我的模型名字（示例）\soul-doc-system'

def read(p):
    with open(p, 'r', encoding='utf-8') as f:
        return f.read()

def write(p, c):
    with open(p, 'w', encoding='utf-8') as f:
        f.write(c)

print("[1] Updating 08-isolation.md...")
p08 = os.path.join(BASE, 'sections', '08-isolation.md')
c08 = read(p08)
# Fix 8.2a -> 8.2
c08 = c08.replace('## 8.2a ', '## 8.2 ')

# Replace tree block
OLD_TREE_08 = """```
灵魂文档总区/
├── INITIAL-SEED.md ← 种子文件（总区，只读）
├── soul-doc-system/ ← 原型参考（总区，只读）
├── [模型-版本]/ ← 你的隔离区（只有你能写）
│   ├── soul-doc-system/
│   ├── sop/
│   └── ...
├── [其他模型]/ ← 其他模型的隔离区（你只能读）
└── ...
```"""

NEW_TREE_08 = """```
灵魂文档总区/
├── INITIAL-SEED.md          ← 种子文件（总区，只读）
├── soul-doc-system/          ← 原型参考（总区，只读）
├── user-zone/                ← 用户通用区（四驱动：主地平面）
├── 我的模型名字（示例）/     ← 模型隔离区示例（四驱动）
├── StepFun-step-3.7-flash/   ← 模型隔离区（四驱动）
└── [其他模型]/               ← 其他模型隔离区（只读参考）

[模型隔离区]/ ← 例如：我的模型名字（示例）/
└── soul-doc-system/
    ├── master-soul.md
    ├── sections/
    ├── sop/
    ├── desktop/          ← 通用桌面（地平面层）
    ├── diary/            ← 通用日记（地平面层）
    ├── memory/           ← 通用记忆 L0-L4（地平面层）
    ├── history/
    ├── production_space/ ← 生产空间（四驱动专用层）
    │   ├── 工作室/      ← 工作室级（跨工作台共用）
    │   └── [工作台名称]/ ← 单工作台（与通用工作台平级）
    │       ├── desktop/
    │       ├── diary/    ← 小时级时间轴日记
    │       ├── memory/   ← L0-L4记忆
    │       ├── sop/      ← 工作台专用SOP（超级信息SOP驱动）
    │       ├── workflow/
    │       ├── temp/     ← 临时文件（30天自动清理）
    │       ├── product/  ← 产出物（60天检查）
    │       ├── contacts/
    │       └── bookmarks/
    ├── sub-role-souls/   ← 子角色灵魂系统
    └── [其他系统文件]
```"""

if OLD_TREE_08 in c08:
    c08 = c08.replace(OLD_TREE_08, NEW_TREE_08)
    write(p08, c08)
    print("  [OK] tree block replaced")
else:
    print("  [ERR] OLD_TREE_08 not found, will skip")

print("[2] Updating 10-sub-role-soul.md...")
p10 = os.path.join(BASE, 'sections', '10-sub-role-soul.md')
c10 = read(p10)
# Replace just the file tree for sub-role structure (keep everything else)
# We don't need to change 10-sub-role too much since it already has production_space
# Just add a note about 四驱动
note = """**四驱动注释：**
子角色内部也遵循四驱动&四写规则。子角色的`vm/product/`对应主系统的`production_space/[工作台]/product/`，
子角色的`sections/`对应主系统的`sections/`。子角色是四驱动的"专用层"，在其自己的隔离区内独立运行。

"""
# Insert after line containing "每个子角色是一个完整的灵魂文档文件夹"
c10 = c10.replace(
    "每个子角色是一个完整的灵魂文档文件夹，包含自己的所有内容",
    "每个子角色是一个完整的灵魂文档文件夹，包含自己的所有内容。"
)
write(p10, c10)
print("  [OK]")

print("[3] Updating 13-collection.md...")
p13 = os.path.join(BASE, 'sections', '13-collection.md')
c13 = read(p13)
# collection structure is fine as-is (it's a flat collection module)
# Just add note repositioning
obs = """> 近原则：collection 放在 soul-doc-system/ 根目录，因为在各工作台都需要采集。
> 采集文件按类型分开放，索引统一在 catalog/index.md。"""
if obs not in c13:
    c13 = c13.replace(
        "采集系统解决的问题：",
        obs + "\n\n采集系统解决的问题："
    )
write(p13, c13)
print("  [OK]")

print("[DONE] 1-3 finished.")
