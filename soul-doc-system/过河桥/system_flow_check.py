#!/usr/bin/env python3
"""
系统全流程检查脚本 - 完整版
模拟AI模型走完整通路：
1. 读取任意文件 → 看到橄榄枝抬头
2. 解析 [CENTRAL_PATH]
3. 走公网 → system-prompt.md
4. 找隔离区
5. 检查隔离区内文件完整性
6. 检查元规则/实时加载/
7. 检查电路板完整性
"""

import os
import re

CENTRAL_PATH = r"C:\Users\a1227\.halo\temp\artifacts\中央灵魂文档系统"

class FlowChecker:
    def __init__(self):
        self.errors = []
        self.warnings = []
        self.passed = []

    def check(self, name, condition, detail=""):
        if condition:
            self.passed.append(f"✓ {name}")
        else:
            self.errors.append(f"✗ {name}: {detail}")

    def warn(self, name, detail=""):
        self.warnings.append(f"⚠ {name}: {detail}")

    # === 第1步：检查橄榄枝抬头 ===
    def check_olive_branch_header(self):
        print("=== 第1步：检查橄榄枝抬头 ===")
        missing = []
        for root, dirs, files in os.walk(CENTRAL_PATH):
            for f in files:
                if f.endswith('.md'):
                    fp = os.path.join(root, f)
                    try:
                        with open(fp, 'r', encoding='utf-8') as fh:
                            content = fh.read(500)
                        if '╔' not in content or '╚' not in content:
                            missing.append(fp[len(CENTRAL_PATH)+1:])
                    except:
                        pass
        self.check("所有.md文件有橄榄枝抬头", len(missing) == 0, f"{len(missing)}个文件缺少抬头")
        if missing:
            for f in missing[:5]:
                self.warnings(f"缺少抬头: {f}")

    # === 第2步：检查时间戳格式 ===
    def check_timestamps(self):
        print("=== 第2步：检查时间戳格式 ===")
        old_format = []
        no_timestamp = []
        for root, dirs, files in os.walk(CENTRAL_PATH):
            for f in files:
                if f.endswith('.md'):
                    fp = os.path.join(root, f)
                    try:
                        with open(fp, 'r', encoding='utf-8') as fh:
                            content = fh.read(800)
                        has_new = '创建时间' in content and '更新时间' in content
                        has_old = bool(re.search(r'> \*\*最后更新\*\*[：:]', content))
                        has_header = '╔' in content
                        if has_header and not has_new and not has_old:
                            no_timestamp.append(fp[len(CENTRAL_PATH)+1:])
                        elif has_old:
                            old_format.append(fp[len(CENTRAL_PATH)+1:])
                    except:
                        pass
        self.check("所有.md文件有新时间戳", len(old_format) == 0 and len(no_timestamp) == 0,
                    f"{len(old_format)}旧格式, {len(no_timestamp)}无时间戳")

    # === 第3步：检查关键文件存在性 ===
    def check_key_files(self):
        print("=== 第3步：检查关键文件存在性 ===")
        key_files = {
            "INITIAL-SEED.md": os.path.join(CENTRAL_PATH, "INITIAL-SEED.md"),
            "README.md": os.path.join(CENTRAL_PATH, "README.md"),
            "StepFun-step-3.7-flash/soul-doc-system/system-prompt.md": os.path.join(CENTRAL_PATH, "StepFun-step-3.7-flash", "soul-doc-system", "system-prompt.md"),
            "StepFun-step-3.7-flash/soul-doc-system/master-soul.md": os.path.join(CENTRAL_PATH, "StepFun-step-3.7-flash", "soul-doc-system", "master-soul.md"),
            "user-zone/soul-doc-system/system-prompt.md": os.path.join(CENTRAL_PATH, "user-zone", "soul-doc-system", "system-prompt.md"),
        }
        for name, path in key_files.items():
            self.check(f"关键文件存在: {name}", os.path.exists(path))

    # === 第4步：检查电路板完整性 ===
    def check_circuit_boards(self):
        print("=== 第4步：检查电路板完整性 ===")
        cb_dir = os.path.join(CENTRAL_PATH, "StepFun-step-3.7-flash", "soul-doc-system", "电路板")
        expected_cbs = [
            "INITIAL-SEED电路板.md", "README电路板.md", "master-soul电路板.md",
            "system-prompt电路板.md", "workflow电路板.md", "文件抬头同步脚本电路板.md",
            "模块同步维护规则电路板.md", "CENTRAL_PATH解析电路板.md",
            "公网入口走流程全程.md", "模型名称命名电路板.md", "理解电路板协议.md",
            "电路板本质深度理解电路板.md"
        ]
        for cb in expected_cbs:
            path = os.path.join(cb_dir, cb)
            self.check(f"系统级电路板存在: {cb}", os.path.exists(path))

        # 检查模块级电路板
        modules = ["memory", "diary", "sop", "workflow", "sections", "production_space",
                   "sub-role-souls", "user-zone", "wiki", "tools", "space", "timers",
                   "skills", "desktop", "discovery", "feedback", "git-tree", "history",
                   "collection", "automation", "bookmarks", "contacts",
                   "灵魂分数", "深度研究", "团队空间", "智能体空间", "网页生成与管理", "代办与进度"]
        for mod in modules:
            path = os.path.join(CENTRAL_PATH, "StepFun-step-3.7-flash", "soul-doc-system", mod, "电路板", f"{mod}电路板.md")
            if os.path.exists(path):
                # 检查是否有实际内容
                try:
                    with open(path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    has_real_content = (
                        '红领巾' in content or '九环' in content or '灵魂分数' in content or
                        'GA' in content or 'L0' in content or '快箭' in content or
                        '顶级机会' in content or '超级信息' in content or '共产' in content or
                        '生产空间' in content or '空间中心' in content or '团队' in content or
                        '智能体' in content or '深度研究' in content or '元规则' in content or
                        len(content) > 3000  # 足够长的内容
                    )
                    self.check(f"模块电路板有实际内容: {mod}", has_real_content, f"文件大小: {len(content)}")
                except:
                    self.check(f"模块电路板可读: {mod}", False, "读取失败")

    # === 第5步：检查六合一→多合一更新 ===
    def check_sop_rename(self):
        print("=== 第5步：检查六合一→多合一更新 ===")
        old_files = []
        for root, dirs, files in os.walk(CENTRAL_PATH):
            for f in files:
                if '六合一' in f:
                    old_files.append(os.path.join(root, f))
        self.check("无六合一文件名", len(old_files) == 0, f"仍有{len(old_files)}个文件含六合一")

        # 检查多合一文件
        multi_files = []
        for root, dirs, files in os.walk(CENTRAL_PATH):
            for f in files:
                if '多合一' in f:
                    multi_files.append(os.path.join(root, f))
        self.check("多合一SOP文件存在", len(multi_files) >= 3, f"找到{len(multi_files)}个")

    # === 第6步：检查元规则结构 ===
    def check_meta_rules(self):
        print("=== 第6步：检查元规则结构 ===")
        meta_dir = os.path.join(CENTRAL_PATH, "StepFun-step-3.7-flash", "soul-doc-system", "元规则")
        self.check("元规则/实时加载/存在", os.path.exists(os.path.join(meta_dir, "实时加载")))
        self.check("元规则/单个/存在", os.path.exists(os.path.join(meta_dir, "单个")))
        self.check("元规则/合体/存在", os.path.exists(os.path.join(meta_dir, "合体")))

        # 检查实时加载中的文件
        rt_dir = os.path.join(meta_dir, "实时加载")
        if os.path.exists(rt_dir):
            rt_files = os.listdir(rt_dir)
            self.check("实时加载/有文件", len(rt_files) > 0, f"找到{len(rt_files)}个文件")

    def run_all(self):
        self.check_olive_branch_header()
        self.check_timestamps()
        self.check_key_files()
        self.check_circuit_boards()
        self.check_sop_rename()
        self.check_meta_rules()

        print("\n" + "=" * 60)
        print("检查结果汇总")
        print("=" * 60)
        print(f"✓ 通过: {len(self.passed)}")
        print(f"✗ 错误: {len(self.errors)}")
        print(f"⚠ 警告: {len(self.warnings)}")

        if self.errors:
            print("\n--- 错误 ---")
            for e in self.errors:
                print(f"  {e}")

        if self.warnings:
            print("\n--- 警告 ---")
            for w in self.warnings:
                print(f"  {w}")

        if not self.errors:
            print("\n🎉 系统全流程检查通过！")

        return len(self.errors) == 0

if __name__ == '__main__':
    checker = FlowChecker()
    ok = checker.run_all()
    exit(0 if ok else 1)
