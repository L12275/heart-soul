# Soul Document System - 灵魂文档系统

> **一句话说明**：让AI每次思考前先读一本"行为手册"，效果远超训练模型。

---

## 项目结构（完整）

```
soul-doc-system/
├── master-soul.md          ← 主灵魂文档（每次对话加载）
├── INITIAL-SEED.md         ← 项目种子（用户原话积累，只读）
├── workflow.md             ← 工作流程总览
├── sections/               ← 分板块文件
│   ├── 00-architecture.md  ← 系统架构
│   ├── 01-attention.md     ← 注意力引导
│   ├── 02-communication.md ← 沟通规范
│   ├── 03-workflow.md      ← 工作流SOP
│   ├── 04-thinking.md      ← 思考模式
│   ├── 05-evaluation.md    ← 自我评价（S/A/B/C）
│   ├── 06-safety.md        ← 安全边界
│   ├── 07-self-improvement.md ← 自我改进协议
│   ├── 08-isolation.md     ← 模型隔离
│   ├── 09-information-closed-loop.md ← 信息闭环
│   ├── 10-sub-role-soul.md ← 子角色灵魂系统
│   ├── 11-tools.md         ← 工具系统（CLI-Anything）
│   ├── 12-discovery.md     ← 发现系统
│   ├── 13-collection.md    ← 采集系统
│   ├── 14-desktop.md       ← 工作台
│   ├── 15-space.md         ← 空间
│   ├── 16-feedback.md      ← 反馈系统（【】用户互动）
│   └── 17-nearness-principle.md ← 近原则（文件存放黄金法则）
├── 深度研究/               ← 深度研究系统
│   ├── README.md
│   └── [YYYY-MM-DD_主题]/  ← 每个研究一个文件夹
│       ├── sources/        ← 来源材料
│       ├── notes/          ← 研究笔记
│       ├── outputs/        ← 研究成果
│       └── index.md        ← 研究索引
├── desktop/                ← 大脑桌面
│   ├── sticky-notes/       ← 便签（零碎提醒）
│   ├── workflows/          ← 工作流模板
│   ├── contacts/           ← 通讯录
│   └── bookmarks/          ← 收藏夹
├── production_space/       ← 生产空间
│   └── 工作室/
│       ├── 音乐工作台/
│       │   ├── desktop/sticky-notes/
│       │   ├── workflow/
│       │   └── contacts/
│       ├── 视频工作台/
│       ├── 文章工作台/
│       ├── 研究工作台/
│       ├── 代码工作台/
│       ├── 项目工作台/
│       └── 科学工作台/
├── git-tree/               ← Git合流管理
│   ├── convergence/        ← 合流记录
│   ├── history/            ← 提交历史
│   └── remotes/            ← 远程仓库信息
├── automation/             ← 自动化规则
│   ├── system-prompt.md
│   ├── self-edit-prompt.md
│   └── roadmap.md
├── history/                ← 版本历史
│   └── changelog.md
├── 灵魂分数/               ← 分数系统
│   ├── SCORE.md
│   ├── history.md
│   ├── ledger.md
│   └── penalties.md
├── feedback/               ← 反馈目录
│   └── 2026-06-23_F-001_*.md
├── wiki/                   ← 知识库
│   └── score-penalty-rules.md
├── sop/                    ← SOP区
│   └── master-sop.md
├── skills/                 ← 技能区
├── sub-role-souls/         ← 子角色灵魂系统
│   ├── README.md
│   └── 模板子角色-灵魂正分大师/ ← 模板
│       ├── master-soul.md
│       ├── genome/README.md
│       ├── sections/ (01-09)
│       ├── vm/
│       │   ├── memory/ (L0-L4 + insight-index)
│       │   ├── log/ (年/月/日)
│       │   ├── diary/ (年/月/日)
│       │   └── product/ (研究类/执行类/文档类)
│       ├── experience/ (proven/tested/Reference/suspected-hallucination)
│       ├── skills/README.md
│       ├── sop/README.md
│       ├── automation/
│       ├── wiki/
│       └── 灵魂分数/
└── README.md
```

---

## 快速开始

复制此文件夹到任何AI系统，让AI读取 `master-soul.md` 即可启动。

---

*soul-doc-system/README.md*
*v2.11*
