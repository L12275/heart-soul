#!/usr/bin/env python3
"""
工具5：键盘输入（Keyboard Input）
模拟键盘按键和文本输入。

用法：
  python keyboard_input.py "hello world"           # 输入文字
  python keyboard_input.py ctrl+v                   # 快捷键
  python keyboard_input.py ctrl+shift+esc           # 组合键
  python keyboard_input.py "hello" --click 100 200  # 先点击再输入

依赖：ljqCtrl.py（同目录）、pyperclip（用于剪贴板粘贴）
"""
import sys, os, argparse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ljqCtrl

def main():
    p = argparse.ArgumentParser(description='键盘输入工具')
    p.add_argument('keys', help='按键或文字，如 "ctrl+v" 或 "hello"')
    p.add_argument('--click', nargs=2, type=int, metavar=('X','Y'), help='先点击此坐标再输入')
    p.add_argument('--delay', type=float, default=0.03, help='每字符间隔(秒)')
    p.add_argument('--staytime', type=float, default=0, help='按键按下保持(秒)')
    args = p.parse_args()

    if args.click:
        ljqCtrl.Click(args.click[0], args.click[1])

    keys = args.keys
    if '+' in keys:
        # 组合键
        ljqCtrl.Press(keys, staytime=args.staytime)
        print(f'Hotkey pressed: {keys}')
    else:
        # 文本输入：通过剪贴板粘贴（最可靠）
        try:
            import pyperclip
            pyperclip.copy(keys)
            ljqCtrl.Press('ctrl+v')
            print(f'Text pasted: "{keys}" ({len(keys)} chars)')
        except ImportError:
            # 无 pyperclip 时逐字符模拟（可靠性较低）
            for ch in keys:
                vk = ord(ch)
                ljqCtrl.Press(ch)
                time.sleep(args.delay)
            print(f'Text typed: "{keys}" ({len(keys)} chars, char by char)')

if __name__ == '__main__':
    main()
