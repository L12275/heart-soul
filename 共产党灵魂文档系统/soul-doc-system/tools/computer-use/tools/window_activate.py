#!/usr/bin/env python3
"""
工具6：窗口激活（Window Activate）
将指定窗口带到前台。

用法：
  python window_activate.py "Chrome"             # 按标题子串激活
  python window_activate.py "记事本"               # 中文标题
  python window_activate.py 0x123456              # 按句柄激活

技术：假 Alt-up 绕过 Windows 前台锁。

依赖：ljqCtrl.py（同目录）、win32gui
"""
import sys, os, argparse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import win32gui
import ljqCtrl

def main():
    p = argparse.ArgumentParser(description='窗口激活工具')
    p.add_argument('target', help='窗口标题子串或句柄(0x...)')
    args = p.parse_args()

    target = args.target
    if target.startswith('0x') or target.isdigit():
        hwnd = int(target, 0)
    else:
        hwnd = win32gui.FindWindow(None, target)
        if not hwnd:
            # 尝试枚举找包含该子串的窗口
            results = []
            def cb(h, _):
                if win32gui.IsWindowVisible(h):
                    title = win32gui.GetWindowText(h)
                    if target.lower() in title.lower():
                        results.append((h, title))
                return True
            win32gui.EnumWindows(cb, None)
            if not results:
                print(f'窗口未找到: {target}')
                sys.exit(1)
            hwnd = results[0][0]
            print(f'找到窗口: {results[0][1]} (hwnd={hwnd})')

    title = win32gui.GetWindowText(hwnd)
    ljqCtrl.Activate(hwnd)
    print(f'窗口已激活: "{title}" (hwnd={hwnd})')

if __name__ == '__main__':
    main()
