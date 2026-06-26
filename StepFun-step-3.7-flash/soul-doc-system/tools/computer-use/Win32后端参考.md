# Win32 后端参考 — 基于 GA ljqCtrl.py 真实代码

> GA 的 ljqCtrl.py 就是完整的 Win32 后端实现。
> 不用看伪代码，直接看 GA 仓库里的真实代码：`memory/ljqCtrl.py`
> 参考：https://github.com/lsdefine/GenericAgent

---

## 完整代码：ljqCtrl.py

文件已复制到本目录：`ljqCtrl.py`（177 行，可直接 import 使用）

```python
"""
CRITICAL: 严禁在此工具链中 import pyautogui (会污染 win32api 导致逻辑冲突)。
ljqCtrl Quick Reference:
- dpi_scale: float (Logical = Physical * dpi_scale)
- Click(x, y, check=True): Use Physical Coordinates. check=True → 自动比前后像素变化，返回周边图像
- SetCursorPos(z): Use Physical Coordinates z=(x, y)
- Press(cmd, staytime=0): Keyboard shortcuts (e.g. 'ctrl+v')
- FindBlock(fn, wrect=None, threshold=0.8) -> (obj_center_phys, is_found)
- MouseDClick(staytime=0.05), MouseClick(staytime=0.05)
- GrabWindow(hwnd) -> PIL Image: DPI-safe window screenshot (needs foreground)
- GrabWindowBg(hwnd_or_name) -> PIL Image: WGC background capture (Win10+, pip install windows-capture)
"""
import os, sys, time, random, math, win32api, win32con, win32gui, ctypes
import numpy as np

print('[TIPS] always use physical coordinates!')

dpi_scale = 1
try:
    from PIL import ImageGrab, Image, ImageEnhance, ImageFilter, ImageDraw
    import cv2
except: pass

# ========== DPI 感知（启动时自动初始化） ==========
ctypes.windll.user32.SetProcessDPIAware()

_hdc = ctypes.windll.user32.GetDC(0)
swidth = ctypes.windll.gdi32.GetDeviceCaps(_hdc, 118)   # DESKTOPHORZRES (物理)
sheight = ctypes.windll.gdi32.GetDeviceCaps(_hdc, 117)   # DESKTOPVERTRES
ctypes.windll.user32.ReleaseDC(0, _hdc)
cwidth = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)  # 逻辑
cheight = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
dpi_scale = cwidth / swidth
print('Screen width & height:', swidth, sheight)
print('dpi_scale:', dpi_scale)

# ========== 鼠标工具 ==========

def MouseDown():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)

def MouseUp():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def MouseClick(staytime=0.05):
    """硬件级左键点击"""
    MouseDown()
    time.sleep(staytime)
    MouseUp()
    time.sleep(0.05)

def MouseDClick(staytime=0.05):
    """硬件级双击"""
    MouseDown()
    MouseUp()
    MouseDown()
    MouseUp()
    time.sleep(0.05)

def SetCursorPos(z):
    """移动鼠标到物理坐标 z=(x, y)。自动换算逻辑坐标。"""
    z = tuple(map(lambda v: int(v * dpi_scale), z))
    win32api.SetCursorPos(z)
    time.sleep(0.05)

def Click(x, y=None, check=True):
    """点击+像素验证。check=True 返回变化百分比。0%=点歪了。"""
    if type(x) is type(tuple()):
        x, y = int(x[0]), int(x[1])
    if check:
        before, fg_before = ScreenCapAt(x, y), win32gui.GetForegroundWindow()
    SetCursorPos((x, y))
    MouseClick()
    if check:
        time.sleep(0.5)
        after = ScreenCapAt(x, y)
        b, a = np.array(before), np.array(after)
        diff = np.sum(np.any(b != a, axis=2))
        total = b.shape[0] * b.shape[1]
        fg_after = win32gui.GetForegroundWindow()
        fg_title = win32gui.GetWindowText(fg_after)
        fg_changed = fg_before != fg_after
        print(f'[Click check] {diff}/{total} px changed ({diff/total*100:.1f}%) | fg: "{fg_title}" {"CHANGED" if fg_changed else ""}')
        return after
click = Click

# ========== 键盘工具 ==========

VK_CODE = {
    'backspace': 0x08, 'tab': 0x09, 'enter': 0x0D, 'shift': 0x10,
    'ctrl': 0x11, 'alt': 0x12, 'pause': 0x13, 'caps_lock': 0x14,
    'esc': 0x1B, 'space': 0x20, 'page_up': 0x21, 'page_down': 0x22,
    'end': 0x23, 'home': 0x24,
    'left_arrow': 0x25, 'up_arrow': 0x26, 'right_arrow': 0x27, 'down_arrow': 0x28,
    '0': 0x30, '1': 0x31, '2': 0x32, '3': 0x33, '4': 0x34,
    '5': 0x35, '6': 0x36, '7': 0x37, '8': 0x38, '9': 0x39,
    'a': 0x41, 'b': 0x42, 'c': 0x43, 'd': 0x44, 'e': 0x45,
    'f': 0x46, 'g': 0x47, 'h': 0x48, 'i': 0x49, 'j': 0x4A,
    'k': 0x4B, 'l': 0x4C, 'm': 0x4D, 'n': 0x4E, 'o': 0x4F,
    'p': 0x50, 'q': 0x51, 'r': 0x52, 's': 0x53, 't': 0x54,
    'u': 0x55, 'v': 0x56, 'w': 0x57, 'x': 0x58, 'y': 0x59, 'z': 0x5A,
    'F1': 0x70, 'F2': 0x71, 'F3': 0x72, 'F4': 0x73, 'F5': 0x74,
    'F6': 0x75, 'F7': 0x76, 'F8': 0x77, 'F9': 0x78, 'F10': 0x79,
    'F11': 0x7A, 'F12': 0x7B,
    'num_lock': 0x90, 'scroll_lock': 0x91,
    'left_shift': 0xA0, 'right_shift': 0xA1,
    'left_control': 0xA2, 'right_control': 0xA3,
    'left_menu': 0xA4, 'right_menu': 0xA5,
    '+': 0xBB, ',': 0xBC, '-': 0xBD, '.': 0xBE, '/': 0xBF,
    '`': 0xC0, ';': 0xBA, '[': 0xDB, '\\': 0xDC, ']': 0xDD, "'": 0xDE,
}
VK_CODE = {k.lower(): v for k, v in VK_CODE.items()}

def Press(cmd, staytime=0):
    """快捷键。如 'ctrl+v' 'alt+tab' 'ctrl+shift+esc'"""
    cmds = cmd.lower().split('+')
    for z in cmds:
        win32api.keybd_event(VK_CODE[z], 0, 0, 0)
        time.sleep(staytime)
    for z in reversed(cmds):
        time.sleep(staytime)
        win32api.keybd_event(VK_CODE[z], 0, win32con.KEYEVENTF_KEYUP, 0)
press = Press

# ========== 窗口工具 ==========

def Activate(hwnd):
    """激活窗口。假 Alt-up 绕过前台锁。"""
    if ctypes.windll.user32.IsIconic(hwnd):
        ctypes.windll.user32.ShowWindow(hwnd, 9)  # SW_RESTORE
    ctypes.windll.user32.keybd_event(0x12, 0, 2, 0)  # 假 Alt-up
    time.sleep(0.02)
    try:
        win32gui.SetForegroundWindow(hwnd)
    except Exception:
        ctypes.windll.user32.BringWindowToTop(hwnd)
        ctypes.windll.user32.SetFocus(hwnd)
    time.sleep(0.15)
activate = Activate

# ========== 截图工具 ==========

def GrabWindow(hwnd):
    """前台窗口截图（只截客户区，物理像素）"""
    if isinstance(hwnd, str):
        hwnd = win32gui.FindWindow(None, hwnd)
        assert hwnd, f'窗口未找到: {hwnd}'
    Activate(hwnd)
    time.sleep(0.25)
    l, t = win32gui.ClientToScreen(hwnd, (0, 0))
    cr = win32gui.GetClientRect(hwnd)
    bbox = (l, t, l + cr[2], t + cr[3])
    bbox = tuple(int(v / dpi_scale) for v in bbox)
    return ImageGrab.grab(bbox)

def GrabWindowBg(hwnd_or_name, timeout=5):
    """WGC 后台截图（Win10+）"""
    import threading, tempfile
    from windows_capture import WindowsCapture, Frame, CaptureControl
    tmp = tempfile.mktemp(suffix='.png')
    done = threading.Event()
    kw = {'window_hwnd': hwnd_or_name} if isinstance(hwnd_or_name, int) else {'window_name': hwnd_or_name}
    cap = WindowsCapture(cursor_capture=False, draw_border=False, **kw)
    @cap.event
    def on_frame_arrived(frame, capture_control):
        frame.save_as_image(tmp)
        capture_control.stop()
        done.set()
    @cap.event
    def on_closed():
        done.set()
    cap.start_free_threaded()
    done.wait(timeout=timeout)
    if os.path.exists(tmp):
        img = Image.open(tmp)
        img.load()
        os.remove(tmp)
        return img

def ScreenCapAt(x, y, r=100):
    """物理坐标(x,y)为中心 ±r 的屏幕截图 → PIL Image"""
    return ImageGrab.grab((x - r, y - r, x + r, y + r))

# ========== 模板匹配 ==========

def GetWRect(sr):
    """快捷区域名 → 物理像素 [l,u,r,b]。如 'left2'=左半屏"""
    num = int(sr[-1])
    l, u, r, b = 0, 0, swidth, sheight
    if 'left' in sr: r = swidth // num
    if 'right' in sr: l = swidth * (num - 1) // num
    if 'top' in sr: b = sheight // num
    if 'bottom' in sr: u = sheight * (num - 1) // num
    return [l, u, r, b]

def FindBlock(fn, wrect=None, verbose=0, threshold=0.8):
    """在屏幕(或wrect区域)内找模板图。返回 ((center_x, center_y), is_found)"""
    tic = time.process_time()
    if wrect is not None and isinstance(wrect, Image.Image):
        scr, wrect = wrect, None
    else:
        if isinstance(wrect, str):
            wrect = GetWRect(wrect)
        scr = ImageGrab.grab(wrect)
    blc = Image.open(fn) if isinstance(fn, str) else fn
    T = cv2.cvtColor(np.array(blc), cv2.COLOR_RGB2BGR)
    B = cv2.cvtColor(np.array(scr), cv2.COLOR_RGB2BGR)
    tsh, tsw = T.shape[:2]
    res = cv2.matchTemplate(B, T, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(res)
    oj, oi = max_loc
    if wrect is None:
        wrect = [0, 0, scr.size[0], scr.size[1]]
    obj = (oj + wrect[0] + tsw // 2, oi + wrect[1] + tsh // 2)
    if verbose:
        print(f'Max match: {max_val:.4f} at ({oj}, {oi}) cost: {time.process_time() - tic:.3f}s')
    return obj, max_val > threshold
```

---

## 四个核心技术点

### 1. 硬件级 Win32API（非 PostMessage）

| 方式 | 代码 | 效果 |
|------|------|------|
| PostMessage | `win32gui.PostMessage(hwnd, WM_LBUTTONDOWN, ...)` | 只发消息，Chrome/Electron 拦截 |
| 硬件级 | `win32api.mouse_event(MOUSEEVENTF_LEFTDOWN, ...)` | 模拟真实硬件事件，无法拦截 |

**为什么硬件级更好：**
- Chrome/Electron 等现代应用使用低层级钩子检测输入
- PostMessage 只到消息队列，被这些应用拦截
- 硬件级 event 绕过应用层检测

### 2. 前台锁绕过

```python
def Activate(hwnd):
    # 发假 Alt-up 骗过前台锁
    ctypes.windll.user32.keybd_event(0x12, 0, 2, 0)
    time.sleep(0.02)
    win32gui.SetForegroundWindow(hwnd)
```

Windows 有前台锁机制（防止程序 stealing focus）：
- 先发送虚拟 Alt 键释放事件
- 系统认为用户正在按 Alt 键，解除限制
- `SetForegroundWindow` 就能成功

### 3. DPI 感知

```python
ctypes.windll.user32.SetProcessDPIAware()  # 启动时调用
_hdc = ctypes.windll.user32.GetDC(0)
swidth = ctypes.windll.gdi32.GetDeviceCaps(_hdc, 118)   # 物理像素宽
sheight = ctypes.windll.gdi32.GetDeviceCaps(_hdc, 117)   # 物理像素高
cwidth = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)  # 逻辑宽
dpi_scale = cwidth / swidth
```

- `dpi_scale = 逻辑 / 物理`（150%缩放下 = 1.5）
- 所有坐标统一用物理像素
- SetCursorPos 时乘以 dpi_scale 转为逻辑坐标

### 4. Click 像素验证（GA 独有）

```python
def Click(x, y, check=True):
    before = ScreenCapAt(x, y)       # 点击前截图
    SetCursorPos((x, y))
    MouseClick()
    time.sleep(0.5)
    after = ScreenCapAt(x, y)        # 点击后截图
    diff = np.sum(np.any(before != after, axis=2))
    total = before.shape[0] * before.shape[1]
    print(f'{diff}/{total} px changed ({diff/total*100:.1f}%)')
```

- 点击前后各截一张小图（±100px）
- 计算像素差异百分比
- **0% = 点歪了**，立即停下来诊断
- 同时检查前台窗口是否切换

---

## 与 macOS 版的对应

| 功能 | Windows (ljqCtrl.py) | macOS (macljqCtrl.py) |
|------|---------------------|----------------------|
| 鼠标 | `win32api.mouse_event` | `Quartz.CGEventPost` |
| 键盘 | `win32api.keybd_event` | `Quartz.CGEventCreateKeyboardEvent` |
| 窗口枚举 | `win32gui.FindWindow/EnumWindows` | `Quartz.CGWindowListCopyWindowInfo` |
| 窗口激活 | `SetForegroundWindow` + 假 Alt-up | `NSRunningApplication.activateWithOptions_` |
| 截图 | `ImageGrab.grab` | `/usr/sbin/screencapture` |
| 坐标 | 物理像素（DPI 自动换算） | 物理像素（Retina 下 scale=0.5） |
| UIA | Python UIA / ui_detect | AX辅助功能 API (AXElements/AXPress) |

GA 的跨平台设计：`import macljqCtrl as ljqCtrl` 即可无缝切换。

---

## 依赖安装

```bash
# 必选
pip install pywin32  # win32api, win32con, win32gui

# 截图增强（可选）
pip install Pillow numpy opencv-python

# 后台截图（可选，Win10+）
pip install windows-capture
```

---

*Win32 后端参考 — 基于 GA ljqCtrl.py 真实代码*
*来源：https://github.com/lsdefine/GenericAgent*

---
*最后更新：2026-06-26 21:18*
