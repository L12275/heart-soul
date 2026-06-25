#!/usr/bin/env python3
"""
工具1：截图（Screenshot）
截取当前屏幕、指定窗口或指定区域。

用法：
  python screenshot.py                          # 全屏截图
  python screenshot.py --window "窗口标题"       # 窗口截图
  python screenshot.py --window 0x123456         # 按句柄截图
  python screenshot.py --region 0 0 800 600     # 区域截图
  python screenshot.py --at 100 200 --radius 50 # 某点周围截图

输出：保存为 PNG，路径打印到 stdout。
依赖：ljqCtrl.py（同目录）、Pillow、numpy、opencv-python
"""
import sys, os, argparse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ljqCtrl
from PIL import ImageGrab

def main():
    p = argparse.ArgumentParser(description='截图工具')
    p.add_argument('--window', help='窗口标题子串或句柄(0x...)')
    p.add_argument('--region', nargs=4, type=int, metavar=('L','T','R','B'), help='屏幕区域（物理像素）')
    p.add_argument('--at', nargs=2, type=int, metavar=('X','Y'), help='以(x,y)为中心')
    p.add_argument('--radius', type=int, default=100, help='--at 模式的半径(px)，默认100')
    p.add_argument('--output', '-o', default='screenshot.png', help='输出路径')
    args = p.parse_args()

    img = None
    if args.window:
        img = ljqCtrl.GrabWindow(args.window)
    elif args.at:
        img = ljqCtrl.ScreenCapAt(args.at[0], args.at[1], args.radius)
    elif args.region:
        l, t, r, b = args.region
        img = ImageGrab.grab((l, t, r, b))
    else:
        img = ImageGrab.grab()

    img.save(args.output)
    print(f'Screenshot saved: {args.output} ({img.size[0]}x{img.size[1]})')

if __name__ == '__main__':
    main()
