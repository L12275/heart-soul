#!/usr/bin/env python3
"""文件资产扫描
用法: cd 模型隔离区 && python 中央管理区/资产档案/scan.py
扫描模型隔离区下所有文件夹和文件，输出带时间戳的资产清单。
对比两次扫描结果，即可发现文件增减变化。
"""
import os, sys, datetime

def scan(base_dir, exclude_dirs=None):
    """扫描目录，返回文件树列表"""
    if exclude_dirs is None:
        exclude_dirs = {'.git', '__pycache__', 'node_modules', '.venv', 'venv'}

    entries = []
    for root, dirs, files in os.walk(base_dir):
        # 跳过排除目录
        dirs[:] = [d for d in dirs if d not in exclude_dirs]

        rel_root = os.path.relpath(root, base_dir)
        if rel_root == '.':
            rel_root = ''

        for d in sorted(dirs):
            rel_path = os.path.join(rel_root, d) if rel_root else d
            entries.append(f"[DIR]  {rel_path}/")

        for f in sorted(files):
            rel_path = os.path.join(rel_root, f) if rel_root else f
            full_path = os.path.join(root, f)
            try:
                mtime = os.path.getmtime(full_path)
                ts = datetime.datetime.fromtimestamp(mtime).strftime('%Y%m%d-%H%M')
            except:
                ts = 'unknown'
            entries.append(f"[FILE] {rel_path}  ← {ts}")

    return entries

def main():
    base = sys.argv[1] if len(sys.argv) > 1 else "."
    now = datetime.datetime.now().strftime('%Y%m%d-%H%M')

    entries = scan(base)

    # 输出到 scan.py 所在目录（即资产档案/ 文件夹）
    script_dir = os.path.dirname(os.path.abspath(__file__))
    out_name = f"资产清单-{now}.md"
    out_path = os.path.join(script_dir, out_name)
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(f"# 文件资产清单\n\n")
        f.write(f"> 扫描时间：{now}\n")
        f.write(f"> 扫描范围：{os.path.abspath(base)}\n")
        f.write(f"> 文件总数：{sum(1 for e in entries if e.startswith('[FILE]'))}\n")
        f.write(f"> 文件夹总数：{sum(1 for e in entries if e.startswith('[DIR]'))}\n\n")
        f.write("---\n\n")
        f.write(f"## 完整文件树\n\n```\n")
        f.write("\n".join(entries))
        f.write("\n```\n\n")
        f.write("---\n\n")
        f.write(f"*自动生成于 {now}*\n")

    print(f"Scanned {len(entries)} entries -> {out_name}")

if __name__ == "__main__":
    main()
