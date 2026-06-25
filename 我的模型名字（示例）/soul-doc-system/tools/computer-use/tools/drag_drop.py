#!/usr/bin/env python3
"""
工具7：拖放（Drag & Drop）
从源位置拖动元素到目标位置。

用法：
  python drag_drop.py 100 200 300 400       # 从(100,200)拖到(300,400)
  python drag_drop.py 100 200 300 400 --staytime 0.1  # 长按拖放

依赖：ljqCtrl.py（同目录）
"""
import sys, os, argparse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ljqCtrl

def main():
    p = argparse.ArgumentParser(description='拖放工具')
    p.add_argument('sx', type=int, help='起始X（物理像素）')
    p.add_argument('sy', type=int, help='起始Y（物理像素）')
    p.add_argument('ex', type=int, help='目标X（物理像素）')
    p.add_argument('ey', type=int, help='目标Y（物理像素）')
    p.add_argument('--staytime', type=float, default=0.05, help='按下-释放间隔(秒)')
    args = p.parse_args()

    ljqCtrl.SetCursorPos((args.sx, args.sy))
    ljqCtrl.MouseDown()
    ljqCtrl.SetCursorPos((args.ex, args.ey))
    time.sleep(args.staytime)
    ljqCtrl.MouseUp()
    print(f'DragDrop: ({args.sx},{args.sy}) -> ({args.ex},{args.ey})')

if __name__ == '__main__':
    import time
    main()
