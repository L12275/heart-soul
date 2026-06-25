#!/usr/bin/env python3
"""子角色模板同步
用法: cd 模型隔离区 && python soul-doc-system/tools/scripts/sync-sub-role.py
将模板子角色文件夹同步到新的子角色实例。
对比模板和目标，复制缺失文件，更新版本标记。
注意：sub-role-souls/ 已移至 soul-doc-system/ 同级，必须从模型隔离区根目录运行。
"""
import sys, os, shutil, filecmp

def sync(template_dir, target_dir):
    if not os.path.exists(template_dir):
        print(f"template not found: {template_dir}")
        sys.exit(1)
    os.makedirs(target_dir, exist_ok=True)
    count = 0
    for dirpath, _, files in os.walk(template_dir):
        rel = os.path.relpath(dirpath, template_dir)
        target_path = os.path.join(target_dir, rel)
        os.makedirs(target_path, exist_ok=True)
        for f in files:
            src = os.path.join(dirpath, f)
            dst = os.path.join(target_path, f)
            if os.path.exists(dst) and filecmp.cmp(src, dst, shallow=False):
                continue  # skip identical
            shutil.copy2(src, dst)
            count += 1
    print(f"synced {count} files from template → {target_dir}")

if __name__ == "__main__":
    base = sys.argv[1] if len(sys.argv) > 1 else "."
    template = os.path.join(base, "sub-role-souls", "模板子角色-灵魂正分大师")
    sync(template, os.path.join(base, "sub-role-souls", "新子角色"))
