#!/usr/bin/env python3
"""
工具2：鼠标点击（Mouse Click）
在指定坐标执行鼠标左键点击（硬件级）。

用法：
  python click.py 100 200                    # 点击(100,200)，带像素验证
  python click.py 100 200 --no-check         # 点击但不验证
  python click.py 100 200 --staytime 0.1     # 按下-释放间隔0.1秒

依赖：ljqCtrl.py（同目录）
"""
import sys, os, argparse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ljqCtrl

def main():
    p = argparse.ArgumentParser(description='鼠标点击工具')
    p.add_argument('x', type=int, help='X坐标（物理像素）')
    p.add_argument('y', type=int, help='Y坐标（物理像素）')
    p.add_argument('--no-check', action='store_true', help='禁用像素变化验证')
    p.add_argument('--staytime', type=float, default=0.05, help='按下-释放间隔(秒)')
    args = p.parse_args()

    result = ljqCtrl.Click(args.x, args.y, check=not args.no_check)
    if result is not None:
        diff, _ = result
        print(f'Click({args.x},{args.y}) pixel change: {diff:.1f}%')
        if diff < 0.5:
            print('[WARN] 像素变化≈0%，可能点歪了！')
            sys.exit(1)
    else:
        print(f'Click({args.x},{args.y}) done (no check)')

if __name__ == '__main__':
    main()
