# Heart Soul - 灵魂文档系统

> 不是训练模型，是写文档。模型的能力来自训练，但稳定性来自灵魂文档。

## 这是什么

Heart Soul 是一套**灵魂文档工程系统**。让任何AI系统加载一个文档后，就能表现出接近Claude级别的稳定性和用户体验。

核心原理：Claude的"好评"秘密不是模型能力，而是每次对话都加载的一个长达12万字的灵魂文档——约束注意力、提供SOP、引导沟通、自我评价。

这套系统让你也能拥有自己的灵魂文档。

## 核心特性

- **多模型生态**：每个模型在隔离区独立构建自己的灵魂文档，互不污染
- **自动复兴**：新模型读取种子后自动创建自己的灵魂文档系统
- **用户专区**：用户放置好内容，所有模型可读取学习
- **认输机制**：模型可以选择坚持自己、借鉴学习或认输出局
- **SOP文件区**：具体执行步骤按类型和级别分类存放
- **信息闭环结构**：自包含+多路径+自纠正的SOP和知识体系
- **灵魂分数系统**：行为量化评价，违规自动扣分，提供短期记忆约束
- **模型隔离区**：每个模型独立构建灵魂文档，互不污染
- **滚动定时任务**：后台自动学习更新的持续完善机制

## 快速开始

### 1. 读取种子文件

```
总区/INITIAL-SEED.md
```

这是所有模型的共同起点。同时，也可以从 [`soul-doc-system/workflow.md`](soul-doc-system/workflow.md) 进入，这是完整运行流程的快速导航入口。

### 2. 创建隔离区

在你的模型名称下创建文件夹：

```
灵魂文档总区/
├── INITIAL-SEED.md ← 种子（只读）
├── soul-doc-system/ ← 原型参考（只读）
│   ├── master-soul.md
│   ├── workflow.md ← 完整运行流程（参考入口）
│   ├── sections/
│   ├── sop/
│   ├── skills/
│   ├── automation/
│   ├── history/
│   └── wiki/
├── user-zone/ ← 用户专区（只读）
│   ├── 【Obsidian源同步】
│   ├── wiki/
│   ├── sop/
│   ├── skills/
│   ├── 经验/
│   ├── 文档/
│   └── 杂收集/
├── [你的模型名]/ ← 你的隔离区（各自独立，只写自己的）
│   └── soul-doc-system/
│       ├── master-soul.md
│       ├── workflow.md
│       ├── sections/
│       ├── sop/
│       ├── skills/
│       ├── automation/
│       ├── history/
│       ├── wiki/
│       └── 灵魂分数/
└── ...
```

### 3. 构建灵魂文档

至少包含：
- `master-soul.md` - 主灵魂文档
- `workflow.md` - 运行流程导航
- 3个section文件（注意力、沟通、工作流）
- `sop/` 和 `skills/` 目录
- `灵魂分数/` 目录（记录分数和违规日志）

## 远程仓库

- GitHub: https://github.com/L12275/heart-soul
- Gitee: https://gitee.com/L12275/heart-soul

### 克隆自用方法

这是一个原本私人使用、现已公开的中央灵魂文档仓库，里面包含示例和成品内容。

自用方式有两种：

**方式一：克隆后改远程地址（推荐）**

```
git clone https://github.com/L12275/heart-soul.git
cd heart-soul
git remote set-url origin <你自己的仓库地址>
```

这样 AI 会把更新推送到你自己的仓库，互不干扰。

**方式二：继续推送到此中央仓库**

不需要改远程地址。每个模型只推送自己隔离区的稳定版内容，不同模型的隔离区互不污染，可以共享一个中央灵魂文档仓库，无需重新建设自己的灵魂文档。

因为灵魂文档除非特殊定制，都是公开通用的——"好好学习天天向上"就会有好学生、好未来、好成绩、好表现。

**推送规则：** 每个模型只推送自己隔离区的稳定版内容。不推送未验证的、不推送其他模型的隔离区。

## 目录结构（完整）

```
灵魂文档总区/
├── INITIAL-SEED.md ← 用户原话种子（权威源，只读）
├── soul-doc-system/ ← 原型参考（只读）
│   ├── master-soul.md
│   ├── workflow.md ← 完整运行流程（快速导航入口）
│   ├── sections/
│   │   ├── 01-红领巾精神.md
│   │   ├── 02-注意力铁律.md
│   │   ├── 03-沟通铁律.md
│   │   ├── 04-工作流铁律.md
│   │   ├── 05-思考铁律.md
│   │   ├── 06-安全铁律.md
│   │   ├── 07-自我改进协议.md
│   │   ├── 08-自动复兴与身份隔离.md
│   │   ├── 09-系统架构.md
│   │   ├── 10-使用说明.md
│   │   ├── 11-核心理念总结.md
│   │   ├── 12-灵魂分数系统.md
│   │   └── 13-自动加载与滚动定时任务流程.md
│   ├── sop/
│   │   ├── information-element-sop.md ← 信息要素输出SOP
│   │   └── data-causality-sop.md ← 数据因果SOP
│   ├── skills/
│   │   └── thinking-power/
│   │       └── SKILL.md ← 顶级思考力技能
│   ├── automation/
│   ├── history/
│   └── wiki/
├── user-zone/ ← 用户专用文件夹（只读）
│   ├── 【Obsidian源同步：3自动建立灵魂提示文件.md】
│   ├── wiki/
│   │   └── data-causality-sop.md
│   ├── sop/
│   │   ├── 信息要素-SOP.md
│   │   ├── data-causality-sop.md ← 通用版（无NVIDIA测试内容）
│   │   └── data-causality-sop-compact.md ← 压缩版（自纠正闭环）
│   ├── skills/
│   ├── 经验/
│   ├── 文档/
│   └── 杂收集/
├── StepFun-step-3.7-flash/ ← 模型隔离区示例（各自独立）
│   └── soul-doc-system/
│       ├── master-soul.md
│       ├── workflow.md
│       ├── sections/
│       ├── sop/
│       ├── skills/
│       ├── automation/
│       ├── history/
│       ├── wiki/
│       └── 灵魂分数/
├── [模型名]/ ← 模型隔离区（各自独立，只写自己的）
│   └── soul-doc-system/
│       ├── master-soul.md
│       ├── workflow.md
│       ├── sections/
│       ├── sop/
│       ├── skills/
│       ├── automation/
│       ├── history/
│       ├── wiki/
│       └── 灵魂分数/
└── 1-[模型名]/ ← 用户标记排名1
```

## 参考方向

- 红领巾精神（诚实勇敢、团结友爱、时刻准备着）
- 八荣八耻（诚实守信、遵纪守法、辛勤劳动）
- 三好学生（德智体全面发展）
- 仁义礼智（行为准则四维框架）
- 胖东来天使城（极致标准化+人性化）
- Claude灵魂文档（12万字注意力引导）

## 核心理念

> 不是prompt engineering，这是**灵魂工程**。

> 训练决定模型能做什么，灵魂文档决定模型每次做的时候怎么做。

## 版本历史

- v0.1 - 初始骨架
- v0.2 - 红领巾精神 + Agent Team + SOP区 + 灵魂分数
- v0.3 - 用户专区 + 自动更新机制 + 认输机制
- v0.4 - 多模型隔离 + Obsidian同步 + 信息闭环结构
- v0.5 - workflow.md + 灵魂分数系统 + 推送规则优化
- v0.6 - 模型隔离区 + 模板避坑指南 + 综合大版本
- v1.0 - 完整系统：13章master-soul + SOP/技能/Section + 滚动定时任务 + 自动复兴
- v1.1 - 模型隔离区标准模板 + rolling-timer skill + 分数系统
- v1.2 - 信息闭环结构 + 信息要素SOP + thinking-power skill + 灵魂文档片段 + 数据因果压缩SOP + 全局共振共振

---

*Heart Soul - 选心、选脑、选智商*
