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




Computer Use（GUI自动化）

> 全控制 Windows 电脑——模型通过屏幕截图 + 鼠标键盘控制实现 Computer Use。
> 基于 GenericAgent 的 `memory/ljqCtrl.py`，不需要安装整个 GA 项目。

**参考文章：[GA实战 | 借助 GenericAgent，Hermes 实现了 Windows 电脑全控制（内附指令）](https://mp.weixin.qq.com/s/UMVDYNGLxKrWNs-_jmS9aQ)**

**核心项目：[GenericAgent](https://github.com/lsdefine/GenericAgent)**
- 用户指令：「去学一下这个项目里的 computer_use，改造一下你自己，剩下的活你来干。」
- 已提取 ljqCtrl.py（177行）和9个原子工具，无需安装整个项目

---

## 文件夹结构

```
computer-use/
├── README.md              ← 本文件（总览）
├── SOP.md                 ← 操作SOP（五步流程+四级探测链+坐标换算）
├── ljqCtrl.py             ← GA 原始 Windows 控制后端（177行，可直接import）
├── 原子工具集.md          ← 9个原子工具的用法+代码（基于真实 ljqCtrl.py）
├── Win32后端参考.md       ← 四个核心技术点详解（DPI/前台锁/像素验证/硬件级）
├── GA-ljqCtrl-SOP.md      ← GA 原始 ljqCtrl 坐标转换 SOP（直接引用）
└── GA-computer_use.md     ← GA 原始 computer_use 策略文档（直接引用）
```

---

## 核心能力

Computer Use = 模型用"眼睛"（截图）看屏幕，用"手"（鼠标键盘）操作电脑。

| 能力 | GA 函数 | 说明 |
|------|---------|------|
| 鼠标左键 | `MouseClick(staytime)` | 硬件级 MOUSEEVENTF_LEFTDOWN + LEFTUP |
| 鼠标双击 | `MouseDClick(staytime)` | 两次 MouseDown/Up |
| 鼠标移动 | `SetCursorPos(z)` | 物理坐标，DPI 自动换算 |
| 点击+验证 | `Click(x, y, check=True)` | 像素变化检测，0%变化=点歪了 |
| 键盘快捷键 | `Press(cmd, staytime)` | 如 'ctrl+v' 'alt+tab' |
| 窗口激活 | `Activate(hwnd)` | 假 Alt-up 绕过前台锁 |
| 前台截图 | `GrabWindow(hwnd)` | 只截客户区，物理像素 |
| 后台截图 | `GrabWindowBg(hwnd)` | WGC，Win10+ |
| 模板匹配 | `FindBlock(fn, wrect)` | 在屏幕上找图，返回物理坐标中心 |

---

## 四条铁律

| 铁律 | 说明 |
|------|------|
| **一律使用物理坐标** | 传给所有工具的坐标必须是物理像素 = 截图像素坐标 |
| **严禁 pyautogui** | pyautogui 会污染 win32api 导致逻辑冲突 |
| **操作前先激活窗口** | 必须 Activate(hwnd) 到前台再操作 |
| **Click 后检查像素变化** | Click(check=True) 返回变化百分比，0%=点歪了，立即停 |

---

## 四级探测链

GA 的核心方法论：**先探测，再操作，先定位，再点击。**

| 级别 | 工具 | 用法 | 适用场景 |
|------|------|------|---------|
| 0 | win32gui 窗口枚举 | 始终先行 | 枚举窗口标题/类名/rect |
| 1 | Python UIA（控件树） | 首选 | 标准控件，免坐标点击 |
| 2 | ui_detect.py + ljqCtrl 截图 | 1无效时用 | OCR+模板匹配 |
| 3 | Vision VLM | 最后手段 | 仅语义理解，不可信坐标 |

---

## 9 个原子工具

每个工具都是独立脚本，直接调用 ljqCtrl.py 底层 API。

```bash
tools/
├── screenshot.py       # 截图（全屏/窗口/区域/点周围）
├── click.py            # 鼠标点击（带像素验证）
├── mouse_move.py       # 鼠标移动
├── mouse_scroll.py     # 鼠标滚动
├── keyboard_input.py   # 键盘输入（文字/快捷键）
├── window_activate.py  # 窗口激活（绕过前台锁）
├── drag_drop.py        # 拖放操作
├── window_info.py      # 窗口信息查询
├── hotkey.py           # 快捷键执行
└── README.md           # 工具列表+快速测试
```

## 快速开始

1. **读取 `SOP.md`** — 了解完整操作流程
2. **读取 `原子工具集.md`** — 学习 9 个原子工具的用法
3. **读取 `Win32后端参考.md`** — 理解四个核心技术点
4. **直接用工具脚本** — 如 `python tools/click.py 100 200`
5. **或 import `ljqCtrl.py`** — 在 Python 代码中直接调用

```python
import ljqCtrl
import win32gui

# 找到窗口
hwnd = win32gui.FindWindow(None, "Chrome")

# 激活 + 截图
ljqCtrl.Activate(hwnd)
img = ljqCtrl.GrabWindow(hwnd)

# 点击 + 输入
ljqCtrl.Click(100, 200)
ljqCtrl.Press('ctrl+v')
```

---

## 与其他工具的关系

- **CLI-Anything**：优先CLI化，Computer Use是CLI化无法覆盖时的补充
- **MCP-Zero**：发现新工具时优先MCP，Computer Use是最后的万能手段
- **脚本**：自动化脚本优先，Computer Use用于脚本无法覆盖的GUI操作

## 安全规则

1. **先确认再操作** — 操作前先截图确认当前状态
2. **不操作敏感区域** — 不碰系统设置、注册表、管理员权限
3. **可逆优先** — 能撤销的操作优先，不能撤销的先确认
4. **记录操作日志** — 每次操作记录做了什么、结果如何
5. **用户知情** — 重要操作前通知用户，获得同意

---

*Computer Use 工具说明 — v4.1 基于真实 GA 代码*
*核心项目：https://github.com/lsdefine/GenericAgent*

---
*更新时间：2026-06-26T21:18*
*每次更新文件，就要同时更新时间戳*
