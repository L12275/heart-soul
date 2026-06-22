# 子角色灵魂系统索引

> 每个子角色是完全隔离的灵魂文档文件夹。
> 在此总文件夹下按需要自行新增，各子角色之间完全隔离，不能互相污染混淆。

---

## 子角色列表

| 角色名称 | 状态 | 最后更新 | 说明 |
|---------|------|---------|------|
| （暂无） | 待创建 | — | 按需新建 |

---

## 快速创建

1. 在此目录下新建 [角色名称]/ 文件夹
2. 复制标准骨架：
```
[角色名称]/
├── master-soul.md      ← 子角色灵魂主文件
├── genome/             ← 基因库（源头参考）
│   └── README.md
├── sections/           ← 侧文件
│   ├── 01-identity.md          ← 身份定义
│   ├── 02-thinking-patterns.md ← 思维方式
│   ├── 03-knowledge-base.md    ← 知识领域
│   ├── 04-communication.md     ← 沟通风格
│   └── 05-ethics.md            ← 角色道德边界
├── vm/                 ← 虚拟机（运行时临时区域）
│   ├── memory/
│   │   └── context/
│   ├── log/
│   │   ├── archive/            ← 历史归档（年/月/日）
│   │   └── current/            ← 当前会话
│   └── product/                ← 产出物（提前规划分类）
├── experience/         ← 经验（按可信度分级）
│   ├── proven/                 ← 已证实
│   ├── tested/                 ← 测试过
│   ├── Reference/              ← 仅供参考
│   └── suspected-hallucination/ ← 存疑
├── skills/             ← 技能
├── sop/                ← SOP
├── wiki/               ← 参考和历史
└── 灵魂分数/             ← 子角色独立灵魂分
    ├── SCORE.md
    ├── history.md
    ├── ledger.md
    └── penalties.md
```
3. 填写 master-soul.md — 角色身份定义 + 核心行为准则
4. 在此 README 中添加此角色条目

---

## 切换流程

```
检测到需要子角色 → 找到对应文件夹 → 读 master-soul.md + sections/ → 以子角色工作 → 结束回到总灵魂
```

---

## 核心规则

- 各子角色完全隔离，不能互相读取
- 产出物归入各自 vm/product/ 按分类存放
- 经验按可信度分级（proven > tested > Reference > suspected-hallucination）
- 子角色独立灵魂分，不影响总灵魂分数
- 临时协作后恢复干净隔离状态
- 子角色不能挂靠其他模型的灵魂文档
- 不写入其他模型隔离区 = 不污染他人

---

*完整定义：sections/10-sub-role-soul.md*
*创建时间：2026-06-22*
