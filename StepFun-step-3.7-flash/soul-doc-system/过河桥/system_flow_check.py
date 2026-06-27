#!/usr/bin/env python3
"""
系统全流程检查脚本 v5 - 使用动态路径查找
"""

import os
import re

CENTRAL_PATH = r"C:\Users\a1227\.halo\temp\artifacts\中央灵魂文档系统\StepFun-step-3.7-flash"
SOUL_DIR = os.path.join(CENTRAL_PATH, "soul-doc-system")

# 动态查找 过河桥 文件夹名（处理中文路径）
CIRCUIT_BOARD_DIR = None
for item in os.listdir(SOUL_DIR):
    if os.path.isdir(os.path.join(SOUL_DIR, item)) and item.encode('utf-8') == b'\xe8\xbf\x87\xe6\xb2\xb3\xe6\xa1\xa5':
        CIRCUIT_BOARD_DIR = item
        break

if not CIRCUIT_BOARD_DIR:
    # fallback
    CIRCUIT_BOARD_DIR = '\u8fc7\u6cb4\u6865'  # 过河桥

class FlowChecker:
    def __init__(self):
        self.errors = []
        self.warnings = []
        self.passed = []

    def check(self, name, condition, detail=""):
        if condition:
            self.passed.append("[OK] " + name)
        else:
            self.errors.append("[ERR] " + name + ": " + detail)

    def warn(self, name, detail=""):
        self.warnings.append("[WARN] " + name + ": " + detail)

    def check_olive_branch_header(self):
        print("=== Step 1: Olive Branch Header ===")
        missing = []
        for root, dirs, files in os.walk(SOUL_DIR):
            for f in files:
                if f.endswith('.md'):
                    fp = os.path.join(root, f)
                    if f in ['README.md', 'SOP.md']:
                        continue
                    try:
                        with open(fp, 'r', encoding='utf-8') as fh:
                            content = fh.read(1200)
                        if '\u2554' not in content or '\u255a' not in content:
                            rel = fp[len(SOUL_DIR)+1:]
                            missing.append(rel)
                    except:
                        pass
        self.check("System files have olive branch header", len(missing) == 0, str(len(missing)) + " missing")
        for f in missing[:5]:
            self.warn("Missing header: " + f)

    def check_timestamps(self):
        print("=== Step 2: Timestamp Format ===")
        old_format = []
        no_timestamp = []
        for root, dirs, files in os.walk(SOUL_DIR):
            for f in files:
                if f.endswith('.md'):
                    fp = os.path.join(root, f)
                    try:
                        with open(fp, 'r', encoding='utf-8') as fh:
                            content = fh.read()
                        has_new = '\u521b\u5efa\u65f6\u95f4' in content and '\u66f4\u65b0\u65f6\u95f4' in content
                        # Only check first 1500 chars for old format (near header/timestamp area)
                        head = content[:1500]
                        has_old = bool(re.search(r'> \*\*\u6700\u540e\u66f4\u65b0\*\*[：:]', head))
                        if has_old:
                            old_format.append(fp[len(SOUL_DIR)+1:])
                        elif not has_new:
                            no_timestamp.append(fp[len(SOUL_DIR)+1:])
                    except:
                        pass
        self.check("Timestamp format unified", len(old_format) == 0 and len(no_timestamp) == 0,
                    str(len(old_format)) + " old, " + str(len(no_timestamp)) + " missing")
        for f in old_format[:5]:
            self.warn("Old format: " + f)

    def check_key_files(self):
        print("=== Step 3: Key Files ===")
        cb_dir = os.path.join(SOUL_DIR, CIRCUIT_BOARD_DIR)
        key_files = {
            "system-prompt.md": os.path.join(SOUL_DIR, "system-prompt.md"),
            "master-soul.md": os.path.join(SOUL_DIR, "master-soul.md"),
            "INITIAL-SEED" + CIRCUIT_BOARD_DIR + ".md": os.path.join(cb_dir, "INITIAL-SEED" + CIRCUIT_BOARD_DIR + ".md"),
            "\u6700\u5f3a\u8111\u5e08\u591a\u5408\u4e00SOP.md": os.path.join(SOUL_DIR, "\u5143\u89c4\u5219", "\u5b9e\u65f6\u52a0\u8f7d", "\u6700\u5f3a\u8111\u5e08\u591a\u5408\u4e00SOP.md"),
        }
        for name, path in key_files.items():
            self.check("Key file: " + name, os.path.exists(path))

    def check_circuit_boards(self):
        print("=== Step 4: Circuit Boards ===")
        cb_dir = os.path.join(SOUL_DIR, CIRCUIT_BOARD_DIR)
        expected_cbs = [
            "CENTRAL_PATH\u89e3\u6790" + CIRCUIT_BOARD_DIR + ".md",
            "INITIAL-SEED" + CIRCUIT_BOARD_DIR + ".md",
            "README" + CIRCUIT_BOARD_DIR + ".md",
            "master-soul" + CIRCUIT_BOARD_DIR + ".md",
            "system-prompt" + CIRCUIT_BOARD_DIR + ".md",
            "workflow" + CIRCUIT_BOARD_DIR + ".md",
            "\u6587\u4ef6\u62ac\u5934\u540c\u6b65\u811a\u672c" + CIRCUIT_BOARD_DIR + ".md",
            "\u6a21\u5757\u540c\u6b65\u7ef4\u62a4\u89c4\u5219" + CIRCUIT_BOARD_DIR + ".md",
            "\u516c\u7f51\u5165\u53e3\u8d70\u6d41\u7a0b\u5168\u7a0b.md",
            "\u6a21\u578b\u540d\u79f0\u547d\u540d" + CIRCUIT_BOARD_DIR + ".md",
            "\u7406\u89e3" + CIRCUIT_BOARD_DIR + "\u534f\u8bae.md",
            CIRCUIT_BOARD_DIR + "\u672c\u8d28\u6df1\u5ea6\u7406\u89e3" + CIRCUIT_BOARD_DIR + ".md",
            "\u4f18\u5316\u65b9\u6848" + CIRCUIT_BOARD_DIR + ".md",
        ]
        for cb in expected_cbs:
            path = os.path.join(cb_dir, cb)
            self.check("System CB: " + cb, os.path.exists(path))

        modules = ["memory", "diary", "sop", "sections", "production_space",
                   "sub-role-souls", "user-zone", "wiki", "tools", "space", "timers",
                   "skills", "desktop", "discovery", "feedback", "git-tree", "history",
                   "collection", "automation", "bookmarks", "contacts",
                   "\u7075\u9b42\u5206\u6570", "\u6df1\u5ea6\u7814\u7a76", "\u56e2\u961f\u7a7a\u95f4", "\u667a\u80fd\u4f53\u7a7a\u95f4", "\u7f51\u9875\u751f\u6210\u4e0e\u7ba1\u7406", "\u529e\u5e38\u4e0e\u8fdb\u5ea6"]
        for mod in modules:
            path = os.path.join(SOUL_DIR, mod, CIRCUIT_BOARD_DIR, mod + CIRCUIT_BOARD_DIR + ".md")
            if os.path.exists(path):
                try:
                    with open(path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    has_content = len(content) > 500
                    self.check("Module CB: " + mod, has_content, "size: " + str(len(content)))
                except:
                    self.check("Module CB: " + mod, False, "read error")

    def check_sop_rename(self):
        print("=== Step 5: Multi-SOP ===")
        multi_files = []
        for root, dirs, files in os.walk(SOUL_DIR):
            for f in files:
                if '\u591a\u5408\u4e00' in f:
                    multi_files.append(os.path.join(root, f))
        self.check("Multi-SOP files", len(multi_files) >= 1, "found " + str(len(multi_files)))

    def check_meta_rules(self):
        print("=== Step 6: Meta Rules ===")
        meta_dir = os.path.join(SOUL_DIR, "\u5143\u89c4\u5219")
        self.check("Meta/real-time/", os.path.exists(os.path.join(meta_dir, "\u5b9e\u65f6\u52a0\u8f7d")))
        self.check("Meta/single/", os.path.exists(os.path.join(meta_dir, "\u5355\u4e2a")))
        self.check("Meta/combo/", os.path.exists(os.path.join(meta_dir, "\u5408\u4f53")))

        rt_dir = os.path.join(meta_dir, "\u5b9e\u65f6\u52a0\u8f7d")
        if os.path.exists(rt_dir):
            rt_files = [f for f in os.listdir(rt_dir) if f.endswith('.md')]
            self.check("Real-time/ files", len(rt_files) > 0, "found " + str(len(rt_files)))

    def run_all(self):
        self.check_olive_branch_header()
        self.check_timestamps()
        self.check_key_files()
        self.check_circuit_boards()
        self.check_sop_rename()
        self.check_meta_rules()

        print("\n" + "=" * 60)
        print("Results")
        print("=" * 60)
        print("[OK] Passed: " + str(len(self.passed)))
        print("[ERR] Errors: " + str(len(self.errors)))
        print("[WARN] Warnings: " + str(len(self.warnings)))

        if self.errors:
            print("\n--- Errors ---")
            for e in self.errors:
                print("  " + e)

        if self.warnings:
            print("\n--- Warnings ---")
            for w in self.warnings:
                print("  " + w)

        if not self.errors:
            print("\n[PASS] All checks passed!")
        else:
            print("\n[FAIL] " + str(len(self.errors)) + " errors to fix")

        return len(self.errors) == 0

if __name__ == '__main__':
    checker = FlowChecker()
    ok = checker.run_all()
    exit(0 if ok else 1)
