# 子角色灵魂系统 — 完整使用指南

> 当模型需要以特定角色（大师、专家、情景模拟）进行深度任务时，加载这个系统。
> 每个子角色是总灵魂的"分支"，按完整闭环设计，在总灵魂包裹下运行。

---

## 地图：你在这里

### GA L0-L4 记忆架构

| 层级 | 载体 | 作用 | GA等价 |
|------|------|------|--------|
| L0 | system prompt硬编码 | 元规则（最强约束，不可绕过） | memory/L0 rules |
| L1 | vm/memory/insight-index.md（≤30行） | 极简导航索引 | global_mem_insight.txt |
| L2 | sections/03-knowledge-base.md | 全局事实库（含3条红线公理） | global_mem.txt |
| L3 | sop/ 目录 | 任务技能/SOP（自动沉淀） | memory/*.md/.py |
| L4 | vm/log/archive/年/月/日/ | 会话归档（cron每12h自动归档） | L4_raw_sessions/ |
| 日记 | vm/diary/年/月/日/ | 思考成长记录（时间轴+反思标记） | 额外设计 |

### GA 核心原则

1. **No Execution, No Memory** — 没有实际执行过的信息，不写入记忆
2. **神圣不可删改性** — 已验证数据只能压缩/迁移，不能删除
3. **禁止存储易变状态** — 不存易变数据
4. **最小充分指针** — 上层只留最短标识
5. **不要预加载技能，让它们进化** — Don't preload skills, evolve them

---

## 地图：目录结构（完整闭环）

```
中央灵魂文档系统/
├── master-soul.md ← 总灵魂（永远加载）
├── sections/
│   ├── 09-information-closed-loop.md
│   └── 10-sub-role-soul.md ← 子角色灵魂系统定义
├── sub-role-souls/ ← 子角色总文件夹
│   ├── README.md ← 本文件
│   └── 模板子角色-灵魂正分大师/ ← 新建子角色时复制这个模板
│       ├── master-soul.md ← 身份定义 + L0声明（L0来自总灵魂，非本文件）
│       ├── genome/README.md ← 基因来源（胖东来/红领巾/三好学生）
│       ├── sections/ ← 9个侧文件
│       │   ├── 01-identity.md ← 身份定义
│       │   ├── 02-thinking-patterns.md ← 思维方式
│       │   ├── 03-knowledge-base.md ← 知识库（含GA 3条公理）
│       │   ├── 04-communication.md ← 沟通风格
│       │   ├── 05-ethics.md ← 道德边界
│       │   ├── 06-first-visit.md ← 首次进入观察
│       │   ├── 07-tools.md ← 工具（CLI-Anything）
│       │   ├── 08-desktop.md ← 办公桌说明
│       │   └── 09-discovery.md ← 发现记录
│       ├── vm/ ← 运行时自动使用
│       │   ├── memory/
│       │   │   ├── context/L0-L4.md ← GA L0-L4设计（L0=硬编码非文件）
│       │   │   └── insight-index.md ← L1洞察索引（≤30行）
│       │   ├── log/ ← 执行流水账（L4归档）
│       │   │   ├── current/running.md
│       │   │   └── archive/年/月/日/
│       │   ├── diary/ ← 日记（时间轴格式）
│       │   │   ├── README.md
│       │   │   └── 年/月/日/会话ID.md
│       │   └── product/ ← 产出物分类
│       │       ├── 研究类/
│       │       ├── 执行类/
│       │       └── 文档类/
│       ├── experience/ ← 按可信度分级
│       │   ├── proven/ ← 已证实
│       │   ├── tested/ ← 测试过
│       │   ├── Reference/ ← 仅供参考
│       │   └── suspected-hallucination/ ← 存疑
│       ├── skills/README.md ← 技能列表
│       ├── sop/ ← 任务SOPs（自动沉淀）
│       │   └── README.md
│       ├── automation/ ← 自动化规则
│       │   └── SOP-auto-refine.md
│       ├── wiki/ ← 参考和历史
│       └── 灵魂分数/ ← 独立灵魂分
│           ├── SCORE.md
│           ├── history.md
│           ├── ledger.md
│           └── penalties.md
```

---

## 第一步：新建子角色

1. 在 `sub-role-souls/` 下新建文件夹，命名为角色名
2. 复制 `模板子角色-灵魂正分大师/` 的完整骨架
3. 按顺序填写文件

### 必须填写的文件

| 顺序 | 文件 | 不填会怎样 |
|------|------|----------|
| 1 | `master-soul.md` | 模型不知道自己在扮演谁 |
| 2 | `sections/01-identity.md` | 模型无法区分角色和总灵魂 |
| 3 | `sections/02-thinking-patterns.md` | 模型用通用思维代替专精思维 |
| 4 | `sections/03-knowledge-base.md` | 模型不知道哪些知识可信 |
| 5 | `sections/04-communication.md` | 模型用默认聊天风格表达 |
| 6 | `sections/05-ethics.md` | 模型可能越过专业伦理红线 |
| 7 | `genome/README.md` | 模型不知道自己继承了哪些价值 |
| 8 | `灵魂分数/SCORE.md` | 没有分数约束的角色会失控 |
| 9 | `sections/06-first-visit.md` | 模型第一次进入时不会写自观察记录 |
| 10 | `vm/memory/insight-index.md` | L1索引缺失 |

### 可选

| 文件 | 用途 |
|------|------|
| `sections/07-tools.md` | 此角色专用工具清单 |
| `sections/08-desktop.md` | 子角色便签（写进vm/diary/） |
| `sections/09-discovery.md` | 发现/启发记录 |
| `skills/README.md` | 列出此角色的专业技能 |
| `sop/README.md` | 沉淀SOP |
| `wiki/` | 收集参考资料 |

---

## 第二步：使用子角色

### 何时切换

- 模拟大师角色（爱因斯坦思考量子力学）
- 垂直专家任务（医学诊断、法律分析、架构设计）
- 高级思维方式（需要特定领域顶级思维模式）
- 深度细分特别灵魂（特定文化/哲学角度）
- 情景模拟（需要代入特定角色）

### 切换操作

```
需子角色时：
1. 读取 master-soul.md
2. 读取 sections/01-09 全部
3. 读取 vm/memory/insight-index.md
4. 在 vm/log/current/ 中标记"切换进入"
5. 在 vm/diary/ 中创建今日日记，标记 [flag:会话启动]
6. 以子角色身份开始工作
7. 产出物放入 vm/product/ 对应分类
8. 记录经验到 experience/
9. 有效SOP沉淀到 sop/
10. 工作结束：回到总灵魂
```

---

## 第三步：维护子角色

- 产出 → `vm/product/`
- 经验 → `experience/`
- 日志 → `vm/log/archive/年/月/日/`
- 反思 → `vm/diary/年/月/日/`
- SOP → `sop/`
- 发现 → `sections/09-discovery.md`
- 分数 → `灵魂分数/`

---

## 子角色之间的规则

- **完全隔离**：每个子角色只能读自己的内容
- **临时协作**：合作结束各自回到隔离状态
- **不合并**：永远不把两个子角色的内容永久合并
- **独立分数**：每个子角色的灵魂分独立计算
- **模型隔离**：各模型只能操作自己的角色文件夹

---

## 常见问题

**Q: L0 在哪里？**
A: L0 不在任何文件中，硬编码在 system prompt 里，每次加载从总灵魂继承。

**Q: L1 为什么单独建文件？**
A: L1 必须 ≤30行极简导航，放在 identity.md 里会膨胀违反最小充分指针原则。

**Q: 日记和日志有什么区别？**
A: log/ 是执行流水账（做了什么），diary/ 是思考成长记录（学到了什么）。

---

*子角色灵魂系统 — 完整使用指南*
*v2.11 完整闭环版（sections 01-09 / vm / experience / skills / sop / automation / wiki / 灵魂分数）*

---
*最后更新：2026-06-26 21:18*
