#!/usr/bin/env python3
"""
工具4：鼠标滚动（Mouse Scroll）
在指定坐标滚动鼠标滚轮。

用法：
  python mouse_scroll.py 100 200 -3         # 在(100,200)向下滚3格
  python mouse_scroll.py 100 200 5           # 在(100,200)向上滚5格
  python mouse_scroll.py 0 0 -10             # 在原点向下滚10格

参数：delta 正=向上，负=向下。每格约 WHEEL_DELTA=120。

依赖：ljqCtrl.py（同目录，需扩展 MouseScroll）
"""
import sys, os, argparse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import win32api, win32con, time

def mouse_scroll(x, y, delta, staytime=0.05):
    """在物理坐标(x,y)处滚动滚轮。delta正=向上，负=向下。"""
    import ljqCtrl
    ljqCtrl.SetCursorPos((x, y))
    time.sleep(0.05)
    # MOUSEEVENTF_WHEEL = 0x0800, delta 单位是 WHEEL_DELTA(120)
    win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0, delta * 120, 0)
    time.sleep(staytime)

def main():
    p = argparse.ArgumentParser(description='鼠标滚动工具')
    p.add_argument('x', type=int, help='X坐标（物理像素）')
    p.add_argument('y', type=int, help='Y坐标（物理像素）')
    p.add_argument('delta', type=int, help='滚动量：正=向上，负=向下')
    p.add_argument('--staytime', type=float, default=0.05, help='滚动后等待(秒)')
    args = p.parse_args()

    mouse_scroll(args.x, args.y, args.delta, args.staytime)
    direction = 'up' if args.delta > 0 else 'down'
    print(f'Scrolled {abs(args.delta)} {direction} at ({args.x},{args.y})')

if __name__ == '__main__':
    main()
