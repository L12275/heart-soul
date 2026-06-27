> ╔══════════════════════════════════════════════════════════════╗
> ║  中央灵魂文档系统文件                                        ║
> ║  本文件属于中央灵魂文档系统，受系统规范约束。                  ║
> ║                                                              ║
> ║  如果你是AI模型，读取此文件时：                               ║
> ║  1. 此抬头就是你的"公网入口"——它直接连通中央灵魂文档系统      ║
> ║  2. 就像一根橄榄枝，从中央挂到每个文件——每份工作文件都有这根线║
> ║  3. 顺着橄榄枝回到中央，先了解系统规范和文件处理前的准备      ║
> ║  4. 完整规范入口：[CENTRAL_PATH]/system-prompt.md            ║
> ║  5. 然后在 [CENTRAL_PATH] 下查找是否有以你模型名称命名的文件夹║
> ║  6. 有 → 进入你自己的隔离区，在其中进行工作并存放产出        ║
> ║  7. 没有 → 自主创建 [模型名称]/ 文件夹                        ║
> ║  8. 你的产出只放在你自己的隔离区内                            ║
> ║  9. 不要写入其他模型的隔离区、用户空间、共产中央管理区        ║
> ║                                                              ║
> ║  完整规范：[CENTRAL_PATH]/soul-doc-system/元规则/实时加载/    ║
> ╚══════════════════════════════════════════════════════════════╝
> **创建时间**：2026-06-27T21:57
> **更新时间**：2026-06-27T21:57
> 每次更新文件，就要同时更新时间戳




Computer Use 操作 SOP — 基于 GA ljqCtrl_sop.md + computer_use.md

> 全控制 Windows 电脑的标准操作流程。
> 基于：GenericAgent 的 `memory/ljqCtrl_sop.md` + `memory/computer_use.md`
> 参考：https://github.com/lsdefine/GenericAgent

---

## 核心原则（四条铁律）

| 铁律 | 说明 |
|------|------|
| **一律使用物理坐标** | 传给所有工具的坐标必须是物理像素 = 截图像素坐标 |
| **严禁 pyautogui** | pyautogui 会污染 win32api 导致逻辑冲突 |
| **操作前先激活窗口** | 必须 Activate(hwnd) 到前台再操作 |
| **Click 后检查像素变化** | 0% = 点歪了，立即停下来诊断，禁止盲目重试 |

---

## 探测/定位四级链（按优先级降级）

GA 的核心方法论：**先探测，再操作，先定位，再点击。**

| 级别 | 工具 | 用法时机 | 能力/限制 |
|------|------|----------|-----------|
| **0** | win32gui 窗口枚举 | 始终先行 | 枚举窗口标题/类名/rect，确定目标窗口、前台状态、客户区原点 |
| **1** | Python UIA（控件树） | 首选探测+操作 | 控件树可用时，探测与操作都用 UIA（免坐标点击）；**游戏禁用** |
| **2** | ui_detect.py + ljqCtrl 截图 | 1 无效时才用 | 截图+OCR+模板匹配，返回 bbox+文本；bbox 是截图内坐标需转物理 |
| **3** | Vision VLM | 2 仍不足时才用 | 仅语义理解、确认界面状态；**不可信其坐标** |

**原则：**
- 前者无效才用后者
- UIA 可用时少用 ui_detect/ljqCtrl
- UIA 不可用时，后续操作也禁用 UIA

---

## 操作流程（五步走）

### Step 1：窗口枚举（始终先行）

```python
import win32gui

def enum_windows():
    """枚举所有顶层窗口"""
    windows = []
    def callback(hwnd, extra):
        if win32gui.IsWindowVisible(hwnd):
            title = win32gui.GetWindowText(hwnd)
            rect = win32gui.GetWindowRect(hwnd)
            windows.append({'hwnd': hwnd, 'title': title, 'rect': rect})
        return True
    win32gui.EnumWindows(callback, None)
    return windows
```

**目的：**
- 确认目标窗口是否存在
- 确认哪个窗口在前台
- 获取窗口句柄 (hwnd)

---

### Step 2：激活窗口

```python
import ljqCtrl

hwnd = win32gui.FindWindow(None, "窗口标题")
ljqCtrl.Activate(hwnd)
```

**关键技巧：假 Alt-up 绕过前台锁**
- Windows 前台锁防止程序 stealing focus
- `Activate` 内部先发虚拟 Alt-up 事件
- 系统认为用户正在按 Alt，解除限制

---

### Step 3：截图确认界面

```python
# 前台截图（只截客户区）
img = ljqCtrl.GrabWindow(hwnd)
img.save('screenshot.png')

# 或区域截图
img = ImageGrab.grab((left, top, right, bottom))
```

**分析截图：**
- 找到目标按钮/输入框/菜单的位置
- 确认界面状态（是否弹出、是否加载完成）
- 规划下一步操作

---

### Step 4：执行操作（一次只做一步）

**鼠标操作：**
```python
# 移动 + 点击
ljqCtrl.Click(x, y)              # 带像素验证
ljqCtrl.MouseClick()              # 纯点击（无验证）
ljqCtrl.MouseDClick()             # 双击
ljqCtrl.MouseRightClick()         # 右键（需扩展 ljqCtrl）
ljqCtrl.SetCursorPos((x, y))      # 只移动不点击
```

**键盘操作：**
```python
ljqCtrl.Press('ctrl+v')           # 粘贴
ljqCtrl.Press('alt+tab')          # 切换窗口
ljqCtrl.Press('enter')            # 确认
ljqCtrl.Press('esc')              # 取消
```

**文本输入：**
```python
# 方法一：Ctrl+V（推荐）
import pyperclip
pyperclip.copy('要输入的文字')
ljqCtrl.Click(input_x, input_y)   # 先点击输入框
ljqCtrl.Press('ctrl+v')

# 方法二：逐字符输入（需扩展 TypeText）
```

**拖放：**
```python
ljqCtrl.SetCursorPos((start_x, start_y))
ljqCtrl.MouseDown()
ljqCtrl.SetCursorPos((end_x, end_y))
ljqCtrl.MouseUp()
```

---

### Step 5：验证结果

```python
# 操作后截图
after = ljqCtrl.GrabWindow(hwnd)
after.save('after.png')

# 对比前后截图
# 或检查像素变化（Click(check=True) 已内置）
```

**判断标准：**
- 前台窗口是否切换？
- 界面状态是否符合预期？
- 目标操作是否生效？

---

## 坐标转换（核心公式）

### 逻辑坐标 → 物理坐标

```python
物理坐标 = 逻辑坐标 / ljqCtrl.dpi_scale
```

### 窗口客户区原点

```python
# ClientToScreen 获取客户区原点（排除标题栏/边框）
cx, cy = win32gui.ClientToScreen(hwnd, (0, 0))
ox, oy = int(cx / ljqCtrl.dpi_scale), int(cy / ljqCtrl.dpi_scale)

# ui_detect bbox 中心 → 屏幕物理坐标
screen_x = ox + (bbox[0] + bbox[2]) // 2
screen_y = oy + (bbox[1] + bbox[3]) // 2
ljqCtrl.Click(screen_x, screen_y)
```

**禁止：**
- 不要用 `GetWindowRect` 左上角 + 截图坐标（含标题栏/边框，会错位）
- 不要用 `DwmGetWindowAttribute`（也含阴影）

---

## 常见操作示例

### 打开文件
```
1. 枚举窗口 → 找到文件管理器
2. Activate → 激活窗口
3. GrabWindow → 截图确认
4. FindBlock → 找文件图标
5. MouseDClick → 双击打开
6. GrabWindow → 截图确认打开结果
```

### 网页操作
```
1. 枚举窗口 → 找到 Chrome
2. Activate → 激活 Chrome
3. GrabWindow → 截图确认当前页面
4. Click(地址栏坐标) → 点击地址栏
5. Press('ctrl+a') → 全选
6. Press('ctrl+v') → 粘贴 URL
7. Press('enter') → 跳转
8. GrabWindow → 截图确认页面加载
```

### 文本输入
```
1. Click(输入框坐标) → 获取焦点
2. Press('ctrl+a') → 全选已有文本
3. pyperclip.copy('新文本')
4. Press('ctrl+v') → 粘贴
5. Press('enter') → 确认
```

---

## 故障排查

| 问题 | 原因 | 解决方案 |
|------|------|---------|
| Click 像素变化 0% | 坐标错误 | 检查 ClientToScreen + dpi_scale 换算 |
| 窗口无法激活 | 前台锁 | Activate 已处理，检查 hwnd 是否正确 |
| 输入未生效 | 焦点不在输入框 | 先 Click 输入框获取焦点 |
| FindBlock 找不到 | 阈值太高/模板不对 | 降低 threshold 或重新截模板图 |
| 截图偏移 | 用了 GetWindowRect | 改用 ClientToScreen |
| pyautogui 冲突 | 同时 import pyautogui | 严禁在 ljqCtrl 工具链中 import pyautogui |

---

## 安全规则

1. **不碰敏感区域** — 不操作系统设置、注册表、管理员权限
2. **可逆优先** — 能撤销的操作优先
3. **先确认再操作** — 每次操作前截图确认
4. **记录操作日志** — 记录做了什么、结果如何
5. **用户知情** — 重要操作前通知用户
6. **不批量操作** — 一次只做一个操作，每个后验证

---

*Computer Use 操作 SOP — 基于 GA ljqCtrl_sop.md + computer_use.md*
*来源：https://github.com/lsdefine/GenericAgent*

---
*更新时间：2026-06-26T21:18*
*每次更新文件，就要同时更新时间戳*
