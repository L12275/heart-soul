#!/usr/bin/env python3
"""
工具8：获取窗口信息（Get Window Info）
获取指定窗口的位置、大小、标题等信息。

用法：
  python window_info.py "Chrome"               # 按标题子串查找
  python window_info.py --all                  # 列出所有可见窗口
  python window_info.py 0x123456               # 按句柄查询

输出：JSON 格式（标题、句柄、位置、大小、是否前台）。

依赖：ljqCtrl.py（同目录）、win32gui
"""
import sys, os, json, argparse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import win32gui
import ljqCtrl

def get_window_info(hwnd):
    title = win32gui.GetWindowText(hwnd)
    cls = win32gui.GetClassName(hwnd)
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    fg = win32gui.GetForegroundWindow() == hwnd
    visible = win32gui.IsWindowVisible(hwnd)
    return {
        'hwnd': hwnd,
        'title': title,
        'class': cls,
        'left': left, 'top': top, 'right': right, 'bottom': bottom,
        'width': right - left, 'height': bottom - top,
        'foreground': fg,
        'visible': visible
    }

def main():
    p = argparse.ArgumentParser(description='窗口信息工具')
    p.add_argument('target', nargs='?', help='窗口标题子串或句柄(0x...)')
    p.add_argument('--all', action='store_true', help='列出所有可见窗口')
    args = p.parse_args()

    if args.all:
        windows = []
        def cb(hwnd, _):
            if win32gui.IsWindowVisible(hwnd):
                windows.append(get_window_info(hwnd))
            return True
        win32gui.EnumWindows(cb, None)
        print(json.dumps(windows, ensure_ascii=False, indent=2))
        return

    if not args.target:
        # 默认列出前台窗口
        fg = win32gui.GetForegroundWindow()
        print(json.dumps(get_window_info(fg), ensure_ascii=False, indent=2))
        return

    target = args.target
    if target.startswith('0x') or target.isdigit():
        hwnd = int(target, 0)
    else:
        hwnd = win32gui.FindWindow(None, target)
        if not hwnd:
            results = []
            def cb(h, _):
                if win32gui.IsWindowVisible(h):
                    title = win32gui.GetWindowText(h)
                    if target.lower() in title.lower():
                        results.append((h, title))
                return True
            win32gui.EnumWindows(cb, None)
            if not results:
                print(json.dumps({'error': f'窗口未找到: {target}'}, ensure_ascii=False))
                sys.exit(1)
            hwnd = results[0][0]

    print(json.dumps(get_window_info(hwnd), ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
