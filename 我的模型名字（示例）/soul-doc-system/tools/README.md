# 工具（Tools）

> 模型的"工具箱"——脚本、CLI、程序、MCP、Hooks、API、Agents、网页的统一管理。
> 模型越清楚有什么工具、怎么用，才越敢用、越高效。

## 文件夹结构

```
tools/
├── README.md                    ← 本文件（工具总览）
├── cli/                         ← CLI化工具（用CLI-Anything封装后的CLI命令）
│   └── https://github.com/HKUDS/CLI-Anything
├── programs/                    ← 独立程序（Python脚本等）
├── scripts/                     ← 维护脚本（同步/检查/备份）
├── web-tools/                   ← 网页交互工具
├── computer-use/                ← Computer Use（GUI自动化，全控制电脑）
│   ├── ljqCtrl.py               ← GA原始Windows控制后端（177行，可直接import）
│   ├── tools/                   ← 9个原子工具（screenshot/click/mouse_move等）
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
│   └── https://github.com/xfey/MCP-Zero
├── associated-programs/         ← 关联常用程序（只记录路径，不安装）
└── [未来扩展]                   ← 按需新增
```

## CLI化资源

**核心项目：[CLI-Anything](https://github.com/HKUDS/CLI-Anything)**
- 自主实现随时CLI化任意程序、网页、工具
- 模型主动发现需要CLI化的工具后，用此项目封装

**搜索资源：[CLIAnything.cc](https://clianything.cc)**
- 搜索已做成CLI的资源
- 检查是否已有现成CLI再考虑自己封装

## MCP工具

**核心项目：[MCP-Zero](https://github.com/xfey/MCP-Zero)**
- 自主LLM代理的主动工具发现
- 在需要时可自行用MCP-Zero发现和集成新工具
- 详细说明见 mcp/ 文件夹

## Computer Use（GUI自动化）

**核心项目：[GenericAgent computer_use](https://github.com/lsdefine/GenericAgent)**
- 全控制Windows电脑（GUI自动化）
- 模型通过屏幕截图+鼠标键盘控制实现Computer Use
- 参考文章：[GA实战 | 借助 GenericAgent，Hermes 实现了 Windows 电脑全控制](https://mp.weixin.qq.com/s/UMVDYNGLxKrWNs-_jmS9aQ)

**实现方式：**
- 在 tools/computer-use/ 下有详细说明和SOP
- 模型根据需要自行使用computer_use功能
- 9个原子工具：screenshot, click, mouse_move, mouse_scroll, keyboard_input, window_activate, drag_drop, window_info, hotkey
- 所有工具基于 ljqCtrl.py（GA原始Win32后端，177行）

**关联资源：**
| 项目 | URL | 说明 |
|------|-----|------|
| GenericAgent | https://github.com/lsdefine/GenericAgent | Computer Use核心项目 |
| GA实战文章 | https://mp.weixin.qq.com/s/UMVDYNGLxKrWNs-_jmS9aQ | Hermes实现Windows电脑全控制 |

## 关联常用程序

> 如果程序大，不建议安装到这里，但文档写上程序路径、程序文件夹完整文件结构与程序界面平面坐标导航图，便于一篇文档快速清晰重复易用，避免重复浪费时间。

| 程序 | 安装路径 | 文件夹结构 | 界面坐标导航 | 文档位置 |
|------|----------|-----------|-------------|---------|
| Chromium | `C:\Users\a1227\AppData\Local\Chromium\Application\chrome.exe` | chrome.exe | [待填] | [待填] |

## 工具使用规则

1. **优先CLI化** — 能CLI化的尽量CLI化，减少手动操作
2. **不入此** — 程序文件大（>100MB）不复制到项目目录，只记录路径和结构
3. **一条文档顶多次记忆** — 路径+结构+导航写在一起，后续一键直达
4. **用完即记** — 如果利用了某工具完成任务且之前没记，立即补入清单
5. **已验证标注** — 实际使用过的标注"已验证"，未使用的标注"待验证"

---
*工具清单*
*创建时间：2026-06-25*
