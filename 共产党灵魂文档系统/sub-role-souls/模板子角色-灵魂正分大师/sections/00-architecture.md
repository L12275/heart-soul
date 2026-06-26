# 第0章：系统架构

## 文件体系

```
soul-doc-system/
├── INITIAL-SEED.md          ← 原始种子（只读）
├── master-soul.md           ← 主文档（从sections合并生成）
├── sections/                ← 分板块文件
│   ├── 00-architecture.md   ← 本文件
│   ├── 01-attention.md      ← 注意力引导
│   ├── 02-communication.md  ← 沟通规范
│   ├── 03-workflow.md       ← 工作流SOP
│   ├── 04-thinking.md       ← 思考模式
│   ├── 05-evaluation.md     ← 自我评价
│   ├── 06-safety.md         ← 安全边界
│   └── 07-self-improvement.md ← 自我改进协议
├── automation/
│   ├── self-edit-prompt.md  ← AI自我编辑提示词
│   ├── merge-protocol.md    ← 合并协议
│   ├── quality-check.md     ← 质量检查清单
│   └── roadmap.md           ← 自我完善路线图
├── history/
│   └── changelog.md
└── README.md
```

## 文件关系

| 文件 | 作用 | 可修改？ |
|------|------|---------|
| INITIAL-SEED.md | 项目起源和核心理念记录 | ❌ 只读 |
| master-soul.md | 每次对话加载的核心文档 | ⚠️ 仅通过merge合并 |
| sections/*.md | 分板块维护，各自独立 | ✅ 可直接修改 |
| automation/*.md | AI自我维护的工具文件 | ✅ 可修改 |

## 加载顺序

1. 用户说"加载soul-doc-system"
2. AI读master-soul.md（完整读完，不跳行）
3. AI根据任务类型读对应section
4. AI遵循文档规则执行任务
5. 发现改进点→更新section→积累后合并到master

## 合并规则

- master-soul.md**不是手动写的**，是从sections合并生成的
- 合并触发条件：每周一次 或 积累5条新规则
- 合并方法：按编号顺序，将各section内容整合为master的对应章节
- 合并前必须通过安全检查

## 安全约束

- 禁止直接修改master-soul.md
- 新规则先在section中验证，稳定后再合并
- 每次合并记录changelog

---
*最后更新：2026-06-26 21:18*
