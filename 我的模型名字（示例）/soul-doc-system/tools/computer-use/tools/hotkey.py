#!/usr/bin/env python3
"""
工具9：快捷键（Hotkey / Key Combination）
执行组合键操作。

用法：
  python hotkey.py ctrl+v                    # Ctrl+V
  python hotkey.py alt+tab                   # Alt+Tab
  python hotkey.py ctrl+shift+esc            # Ctrl+Shift+Esc
  python hotkey.py win+d                     # Win+D
  python hotkey.py ctrl+alt+delete           # Ctrl+Alt+Delete

支持的单键：ctrl, alt, shift, win, 以及所有 VK_CODE 中的键。
GA 的 ljqCtrl.Press 底层实现。

依赖：ljqCtrl.py（同目录）
"""
import sys, os, argparse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ljqCtrl

def main():
    p = argparse.ArgumentParser(description='快捷键工具')
    p.add_argument('combo', help='组合键，如 "ctrl+v" "alt+tab" "win+d"')
    p.add_argument('--staytime', type=float, default=0, help='按键保持时间(秒)')
    args = p.parse_args()

    try:
        ljqCtrl.Press(args.combo, staytime=args.staytime)
        print(f'Hotkey executed: {args.combo}')
    except KeyError as e:
        print(f'错误：未知按键 {e}。支持的按键：{", ".join(sorted(ljqCtrl.VK_CODE.keys()))}')
        sys.exit(1)

if __name__ == '__main__':
    main()
