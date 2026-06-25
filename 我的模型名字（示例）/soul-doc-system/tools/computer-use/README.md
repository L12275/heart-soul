# Computer Use（GUI自动化）

> 全控制Windows电脑——模型通过屏幕截图+鼠标键盘控制实现Computer Use。
> 基于：[GenericAgent computer_use](https://github.com/lsdefine/GenericAgent)

---

## 核心项目

**GenericAgent** — https://github.com/lsdefine/GenericAgent

- 实现了Computer Use功能：模型可以截图、点击、输入、滚动
- 全控制Windows电脑：文件管理、网页浏览、程序操作
- 参考文章：[GA实战 | 借助 GenericAgent，Hermes 实现了 Windows 电脑全控制](https://mp.weixin.qq.com/s/UMVDYNGLxKrWNs-_jmS9aQ)

## 功能概述

Computer Use = 模型用"眼睛"（截图）看屏幕，用"手"（鼠标键盘）操作电脑。

| 能力 | 说明 | 典型场景 |
|------|------|---------|
| 截图 | 截取当前屏幕或窗口 | 看到当前界面状态 |
| 鼠标 | 移动、点击、双击、右键 | 点击按钮、选择菜单 |
| 键盘 | 输入文字、快捷键 | 打字、Ctrl+C、Alt+Tab |
| 滚动 | 页面上下滚动 | 浏览长页面 |
| 拖放 | 拖动文件或元素 | 移动文件、排序 |

## 使用场景

- 用户不在电脑前，需要模型代为操作
- 需要操作GUI程序（无CLI接口）
- 需要浏览网页并执行复杂操作
- 需要批量处理文件（拖放、复制等）
- 需要演示操作流程

## 安全规则

1. **先确认再操作** — 操作前先截图确认当前状态
2. **不操作敏感区域** — 不碰系统设置、注册表、管理员权限
3. **可逆优先** — 能撤销的操作优先，不能撤销的先确认
4. **记录操作日志** — 每次操作记录做了什么、结果如何
5. **用户知情** — 重要操作前通知用户，获得同意

## 与其他工具的关系

- **CLI-Anything**：优先CLI化，Computer Use是CLI化无法覆盖时的补充
- **MCP-Zero**：发现新工具时优先MCP，Computer Use是最后的万能手段
- **脚本**：自动化脚本优先，Computer Use用于脚本无法覆盖的GUI操作

## 快速开始

1. 确保GenericAgent已安装并配置
2. 读取 `SOP.md` 了解操作流程
3. 根据任务类型选择操作策略
4. 每次操作前先截图确认
5. 操作后验证结果

---

*Computer Use 工具说明*
*创建时间：2026-06-25*
*核心项目：https://github.com/lsdefine/GenericAgent*
