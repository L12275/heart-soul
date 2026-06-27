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


> **创建时间**：2026-06-27T20:42
> **更新时间**：2026-06-27T23:30
> 每次更新文件，就要同时更新时间戳
> 过河桥 — tools

> **此过河桥是 工具系统 - 底层操作工具的统一管理与CLI化 的基因片段。**
> 没有历史上下文时，读此文件即可重建/修复/使用该模块。
> 每次进入该模块前，先读此过河桥，理解其完整机制。

---

## 1. 用户原话重述

用户在 system-prompt.md 和 tools/README.md 中建立了工具系统：

**用户原话要点**：
1. "工具系统：有什么工具、怎么用、CLI化资源。"（每次对话第十步必读）
2. "模型的"工具箱"——脚本、CLI、程序、MCP、Hooks、API、智能体空间、网页的统一管理。"
3. "模型越清楚有什么工具、怎么用，才越敢用、越高效。"
4. "优先CLI化 — 能CLI化的尽量CLI化，减少手动操作"
5. "用完即记 — 如果利用了某工具完成任务且之前没记，立即补入清单"
6. "已验证标注 — 实际使用过的标注"已验证"，未使用的标注"待验证""
7. 自主实现随时CLI化任意程序、网页、工具（CLI-Anything项目）
8. "在需要时可自行用MCP-Zero发现和集成新工具"
9. Computer Use：全控制Windows电脑（GUI自动化），9个原子工具

**用户的核心意图**：
- 工具系统是模型的"手脚"——越清楚有什么工具，才越敢用、越高效
- CLI化优先：能CLI化的尽量CLI化
- 用完即记：新工具用完后立即补充到工具清单
- 已验证标注：区分已验证工具和待验证工具

---

## 2. 理解要点

**核心机制**：

### CLI-Anything 工具系统

**核心项目**：[CLI-Anything](https://github.com/HKUDS/CLI-Anything)
- 自主实现随时CLI化任意程序、网页、工具
- 模型主动发现需要CLI化的工具后，用此项目封装
- 搜索已做成CLI的资源：[CLIAnything.cc](https://clianything.cc)

**CLI化原则**：
1. 优先CLI化 — 能CLI化的尽量CLI化，减少手动操作
2. 检查是否已有现成CLI再考虑自己封装（先搜 CLIAnything.cc）
3. 用完即记 — 利用某工具完成任务且之前没记，立即补入清单
4. 已验证标注 — 实际使用过的标注"已验证"，未使用的标注"待验证"

### 模块内文件夹结构

```
tools/
├── README.md                    ← 本文件（工具总览）
├── cli/                         ← CLI化工具（用CLI-Anything封装后的CLI命令）
│   └── 参考：https://github.com/HKUDS/CLI-Anything
├── programs/                    ← 独立程序（Python脚本等）
├── scripts/                     ← 维护脚本（同步/检查/备份）
├── web-tools/                   ← 网页交互工具
├── computer-use/                ← Computer Use（GUI自动化，全控制电脑）
│   ├── ljqCtrl.py               ← GA原始Windows控制后端（177行，可直接import）
│   ├── tools/                   ← 9个原子工具
│   ├── README.md                ← Computer Use总览
│   ├── SOP.md                   ← 操作SOP
│   ├── 原子工具集.md            ← 9个原子工具用法+代码
│   ├── Win32后端参考.md         ← 四个核心技术点详解
│   ├── GA-ljqCtrl-SOP.md        ← GA原始坐标转换SOP
│   └── GA-computer_use.md       ← GA原始策略文档
├── router/                      ← 路由器工具（代理/转发/流量控制）
├── commands/                    ← 系统命令封装
├── plugins/                     ← 可插拔功能模块
├── api/                         ← API接口测试/封装/文档
├── hooks/                       ← 事件钩子脚本
├── mcp/                         ← MCP工具（自主LLM代理的主动工具发现）
│   └── 参考：https://github.com/xfey/MCP-Zero
├── associated-programs/         ← 关联常用程序（只记录路径，不安装）
└── [未来扩展]                   ← 按需新增
```

### Computer Use（GUI自动化）

**核心项目**：[GenericAgent computer_use](https://github.com/lsdefine/GenericAgent)
- 全控制Windows电脑（GUI自动化）
- 模型通过屏幕截图+鼠标键盘控制实现Computer Use

**9个原子工具**：
1. screenshot — 屏幕截图
2. click — 点击
3. mouse_move — 鼠标移动
4. mouse_scroll — 鼠标滚动
5. keyboard_input — 键盘输入
6. window_activate — 窗口激活
7. drag_drop — 拖放
8. window_info — 窗口信息
9. hotkey — 快捷键

**实现基础**：所有工具基于 ljqCtrl.py（GA原始Win32后端，177行，可直接import）

**使用时机**：模型根据需要自行使用computer_use功能，tools/computer-use/下有详细说明和SOP

### MCP工具（自主工具发现）

**核心项目**：[MCP-Zero](https://github.com/xfey/MCP-Zero)
- 自主LLM代理的主动工具发现
- 在需要时可自行用MCP-Zero发现和集成新工具
- 详细说明见 mcp/ 文件夹

### 关联常用程序

> 如果程序大，不建议安装到项目目录，但文档写上程序路径、程序文件夹完整文件结构与程序界面平面坐标导航图，便于一篇文档快速清晰重复易用。

| 程序 | 安装路径 | 文件夹结构 | 界面坐标导航 | 文档位置 |
|------|----------|-----------|-------------|---------|
| Chromium | `C:\Users\a1227\AppData\Local\Chromium\Application\chrome.exe` | chrome.exe | [待填] | [待填] |

### 工具使用规则

1. **优先CLI化** — 能CLI化的尽量CLI化，减少手动操作
2. **不入此** — 程序文件大（>100MB）不复制到项目目录，只记录路径和结构
3. **一条文档顶多次记忆** — 路径+结构+导航写在一起，后续一键直达
4. **用完即记** — 如果利用了某工具完成任务且之前没记，立即补入清单
5. **已验证标注** — 实际使用过的标注"已验证"，未使用的标注"待验证"

---

## 3. 可能的歧义

| 歧义 | 说明 | 解决 |
|------|------|------|
| CLI-Anything 和 MCP-Zero 的区别 | 不清楚两个工具发现/封装项目的定位 | CLI-Anything = 把已有程序/网页CLI化（封装层）；MCP-Zero = 自主发现新工具并集成（发现层）。两者互补 |
| Computer Use 是否需要每次都加载 | 不清楚这个工具的使用频率 | 不需要每次都加载。在需要GUI自动化时读取 tools/computer-use/ 下的说明和SOP |
| 关联程序是否要安装到 tools/ 目录 | 不清楚大程序怎么管理 | 不入此：程序文件大（>100MB）不复制到项目目录，只记录路径和结构 |
| 工具验证状态如何追踪 | 不清楚已验证/待验证如何记录 | 在 README.md 的关联资源表格中加"已验证"列，实际使用过的标注 |
| MCP工具是否已安装 | 不清楚 MCP-Zero 在当前环境中的状态 | 需要时查看 mcp/ 文件夹内容，确认是否已集成 |
| cli/ 和 commands/ 的区别 | 不清楚两个命令类目录的差异 | cli/ = 用CLI-Anything封装的第三方工具；commands/ = 模型自己封装的系统命令 |
| scripts/ 和 programs/ 的区别 | 不清楚两个程序类目录的差异 | scripts/ = 维护脚本（同步/检查/备份等运维用途）；programs/ = 独立功能程序（Python脚本等） |
| 新工具发现流程 | 不清楚模型遇到新工具时的标准流程 | ①搜 CLIAnything.cc 看是否已有CLI ②没有 → 用CLI-Anything封装 ③加入 tools/ 对应目录 ④更新 README.md |

---

## 4. 我的判断

**使用该模块的标准动作**：
1. 读取本过河桥，理解工具系统完整结构
2. 读取 tools/README.md，确认当前有哪些可用工具
3. 根据任务需要选择合适的工具
4. Computer Use 需要时：读取 tools/computer-use/SOP.md 和 原子工具集.md
5. MCP工具需要时：查看 mcp/ 文件夹，确认可用工具
6. 工具使用完成后：如果之前没记录，立即补入 README.md 的工具清单
7. 标注验证状态：已验证 / 待验证

**重建该模块的标准动作**：
1. 在 soul-doc-system/tools/ 下创建完整目录结构
2. 创建 tools/README.md，写入工具总览
3. 创建各子目录（cli/、programs/、scripts/、web-tools/、computer-use/、router/、commands/、plugins/、api/、hooks/、mcp/、associated-programs/）
4. computer-use/ 下创建详细文档（ljqCtrl.py、SOP、原子工具集等）
5. mcp/ 下记录 MCP-Zero 项目信息
6. associated-programs/ 下记录已安装程序路径
7. 验证所有文件头部有统一橄榄枝抬头

**新工具接入流程**：
1. 模型遇到需要使用的新工具/程序/网页
2. 搜索 CLIAnything.cc 确认是否已有CLI版本
3. 有 → 直接使用；没有 → 用CLI-Anything项目封装
4. 将封装后的工具放入 tools/cli/ 或对应子目录
5. 在 tools/README.md 中添加条目，标注验证状态
6. 如涉及关联程序，更新 associated-programs/ 表格

**定时任务中的工具维护**：
1. 读取 tools/README.md 检查工具清单
2. 检查是否有新工具需要添加
3. 验证已有工具的状态标注是否正确
4. 检查 associated-programs/ 中的程序路径是否仍然有效
5. 如有更新，同步到通用区工具模块

---

## 5. 等待确认

- [ ] 模块路径是否正确？（soul-doc-system/tools/）
- [ ] 模块内12个子目录是否齐全？
- [ ] computer-use/ 下的9个原子工具文档是否完整？
- [ ] MCP-Zero 是否已集成到 mcp/ 目录？
- [ ] associated-programs/ 中的程序路径是否有效？
- [ ] 是否已经通过公网通路确认？
- [ ] 工具清单中的验证状态是否与实际使用情况一致？

---

*过河桥 — tools*
*创建时间：2026-06-27T19:30*
*最后更新：2026-06-27T20:42*
*关联：文件抬头模板 v3.1 | 公网入口走流程全程 | CENTRAL_PATH解析过河桥 | CLI-Anything项目 | MCP-Zero项目 | GenericAgent Computer Use | 工具验证标注系统 | 用完即记规则*
