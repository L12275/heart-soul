# Computer Use 原子工具

> 9 个独立脚本，每个实现一种 GUI 操作能力。
> 基于 ljqCtrl.py（Windows）硬件级 Win32API。

---

## 工具列表

| # | 工具 | 用法 |
|---|------|------|
| 1 | screenshot.py | 截图（全屏/窗口/区域/点周围） |
| 2 | click.py | 鼠标点击（带像素验证） |
| 3 | mouse_move.py | 鼠标移动 |
| 4 | mouse_scroll.py | 鼠标滚动 |
| 5 | keyboard_input.py | 键盘输入（文字/快捷键） |
| 6 | window_activate.py | 窗口激活（绕过前台锁） |
| 7 | drag_drop.py | 拖放操作 |
| 8 | window_info.py | 窗口信息查询 |
| 9 | hotkey.py | 快捷键执行 |

## 通用参数

- 所有坐标均为 **物理像素**（= 截图像素坐标）
- 依赖 `ljqCtrl.py`（同目录上级）

## 快速测试

```bash
# 测试鼠标移动到屏幕中心（1920x1080）
python tools/mouse_move.py 960 540

# 测试窗口激活
python tools/window_activate.py "Chrome"

# 测试截图
python tools/screenshot.py -o test.png
```
