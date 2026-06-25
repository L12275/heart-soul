#!/usr/bin/env python3
"""
工具3：鼠标移动（Mouse Move）
将鼠标移动到指定坐标。

用法：
  python mouse_move.py 100 200        # 移动到(100,200)
  python mouse_move.py 100 200 --no-wait  # 不等待

依赖：ljqCtrl.py（同目录）
"""
import sys, os, argparse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ljqCtrl

def main():
    p = argparse.ArgumentParser(description='鼠标移动工具')
    p.add_argument('x', type=int, help='X坐标（物理像素）')
    p.add_argument('y', type=int, help='Y坐标（物理像素）')
    p.add_argument('--no-wait', action='store_true', help='移动后不等待')
    args = p.parse_args()

    ljqCtrl.SetCursorPos((args.x, args.y))
    print(f'Mouse moved to ({args.x}, {args.y})')

if __name__ == '__main__':
    main()
