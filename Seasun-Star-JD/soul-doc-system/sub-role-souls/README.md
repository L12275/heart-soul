# 子角色灵魂系统 — 完整使用指南

> 当模型需要以特定角色（大师、专家、情景模拟）进行深度任务时，加载这个系统。
> 每个子角色是一个完整隔离的灵魂文档，在总灵魂包裹下运行。

---

## 地图：你在这里

### GA L0-L4 记忆架构

| 层级 | 载体 | 作用 | GA等价 |
|------|------|------|--------|
| L0 | system prompt硬编码 | 元规则（最强约束，不可绕过） | memory/L0 rules |
| L1 | vm/memory/insight-index.md（≤30行） | 极简导航索引 | global_mem_insight.txt |
| L2 | sections/03-knowledge-base.md | 全局事实库（含3条红线公理） | global_mem.txt |
| L3 | sop/ 目录 | 任务技能/SOP（从实际工作中自动沉淀） | memory/*.md/.py |
| L4 | vm/log/archive/年/月/日/ | 会话归档（cron每12h自动归档） | L4_raw_sessions/ |
| 日记 | vm/diary/年/月/日/ | 思考成长记录（时间轴+反思标记） | 额外设计 |

### GA 核心原则

1. **No Execution, No Memory** — 没有实际执行过的信息，不写入记忆
2. **神圣不可删改性** — 已验证数据只能压缩/迁移，不能删除
3. **禁止存储易变状态** — 不存"当前次数""最近操作时间"这类易变数据
4. **最小充分指针** — 上层只留最短标识，不层层叠加引用
5. **不要预加载技能，让它们进化** — Don't preload skills, evolve them

---

## 地图：目录结构

```
中央灵魂文档系统/
├── master-soul.md ← 总灵魂（永远加载）
├── sections/
│   ├── 09-information-closed-loop.md
│   └── 10-sub-role-soul.md ← 子角色灵魂系统定义
├── sub-role-souls/ ← 你在这里
│   ├── README.md ← 本文件
│   └── 模板子角色/ ← 新建子角色时复制这个模板
│   ├── master-soul.md ← 身份定义 + L0声明（L0来自总灵魂，非本文件）
│   ├── genome/README.md ← 基因来源（胖东来/红领巾/三好学生）
│   ├── sections/ ← 6个侧文件
│   │   ├── 01-identity.md ← 身份定义
│   │   ├── 02-thinking-patterns.md ← 思维方式
│   │   ├── 03-knowledge-base.md ← 知识库（含GA 3条公理）
│   │   ├── 04-communication.md ← 沟通风格
│   │   ├── 05-ethics.md ← 道德边界
│   │   └── 06-first-visit.md ← 首次进入观察（模型自写理解）
│   ├── vm/
│   │   ├── memory/context/
│   │   │   └── L0-L4-corrected.md ← GA L0-L4设计说明
│   │   ├── memory/
│   │   │   └── insight-index.md ← L1洞察索引（≤30行，两级映射）
│   │   ├── log/
│   │   │   ├── current/running.md ← 当前任务日志
│   │   │   └── archive/ ← L4会话归档（年/月/日/会话ID.md）
│   │   ├── diary/ ← 日记（年/月/日/会话ID.md）
│   │   │   ├── README.md
│   │   │   └── 2026/06/22/ ← 示例日期文件夹
│   │   └── product/ ← 产出物分类
│   │       ├── 研究类/
│   │       ├── 执行类/
│   │       └── 文档类/
│   ├── experience/ ← 按可信度分级
│   │   ├── proven/
│   │   ├── tested/
│   │   ├── Reference/
│   │   └── suspected-hallucination/
│   ├── skills/README.md ← 技能列表
│   ├── sop/ ← 任务SOPs（自动沉淀）
│   │   └── README.md
│   ├── automation/ ← 自动化规则
│   │   └── SOP-auto-refine.md ← 3次→SOP→验证→merge
│   ├── wiki/
│   └── 灵魂分数/ ← 独立灵魂分
│       ├── SCORE.md
│       ├── history.md
│       ├── ledger.md
│       └── penalties.md
```

---

## 第一步：新建子角色

1. 在 `sub-role-souls/` 下新建文件夹，命名为角色名
2. 复制 `模板子角色/` 的完整骨架到新文件夹
3. 按顺序填写文件

### 必须填写的文件

| 顺序 | 文件 | 不填会怎样 |
|------|------|----------|
| 1 | `master-soul.md` | 模型不知道自己在扮演谁 |
| 2 | `sections/01-identity.md` | 模型无法区分角色和总灵魂 |
| 3 | `sections/02-thinking-patterns.md` | 模型用通用思维代替角色专精思维 |
| 4 | `sections/03-knowledge-base.md` | 模型不知道哪些知识可信 |
| 5 | `sections/04-communication.md` | 模型用默认聊天风格表达 |
| 6 | `sections/05-ethics.md` | 模型可能越过专业伦理红线 |
| 7 | `genome/README.md` | 模型不知道自己继承了哪些价值 |
| 8 | `灵魂分数/SCORE.md` | 没有分数约束的角色会失控 |
| 9 | `sections/06-first-visit.md` | 模型第一次进入时不会写自观察记录 |
| 10 | `vm/memory/insight-index.md` | L1索引缺失，模型找不到L3 SOP |

### 可选

| 文件 | 用途 |
|------|------|
| `skills/README.md` | 列出此角色的专业技能 |
| `sop/README.md` | 沉淀此角色的标准操作流程 |
| `wiki/` | 收集参考资料 |

---

## 第二步：使用子角色

### 何时切换

- 模拟大师角色（爱因斯坦思考量子力学）
- 垂直专家任务（医学诊断、法律分析、架构设计）
- 高级思维方式（需要特定领域顶级思维模式）
- 深度细分特别灵魂（特定文化/哲学角度）
- 情景模拟（需要代入特定角色）
- 长期专注任务（一个周期内持续专业工作）

### 何时不切换

- 普通对话
- 通用知识问答
- 简单任务（直接用总灵魂）

### 切换操作

```
需子角色时：
1. 读取 master-soul.md
2. 读取 sections/01-06 全部
3. 读取 vm/memory/insight-index.md
4. 在 vm/log/current/ 中标记"切换进入"
5. 在 vm/diary/ 中创建今日日记，标记 [flag:会话启动]
6. 以子角色身份开始工作
7. 产出物放入 vm/product/ 对应分类
8. 记录经验到 experience/（按可信度分级）
9. 有效SOP沉淀到 sop/
10. 工作结束：回到总灵魂，归入 vm/log/archive/ 年/月/日/
```

---

## 第三步：维护子角色

### 每次工作后

- 有价值的产出 → `vm/product/[分类]/`
- 发现的经验 → `experience/[等级]/`
- 有效SOP → `sop/`
- 错误/纠正 → 更新对应 `sections/` 文件
- 日志 → `vm/log/archive/年/月/日/`
- 反思 → `vm/diary/年/月/日/`
- 分数更新 → `灵魂分数/`

### 每次工作前

- 读 `master-soul.md`（完整读完）
- 读 `sections/01-06`（快速过一遍）
- 读 `vm/memory/insight-index.md`（找到今次场景对应的SOP）
- 检查 `灵魂分数/SCORE.md` 确认状态正常

---

## 子角色之间的规则

- **完全隔离**：每个子角色只能读自己的内容，不能读取其他子角色的文件
- **临时协作**：如需两个子角色合作，临时共享 vm/ 上下文，合作结束各自回到隔离状态
- **不合并**：永远不把两个子角色的内容永久合并
- **不挂靠**：子角色不能挂靠其他模型的灵魂文档
- **独立分数**：每个子角色的灵魂分独立计算
- **模型隔离**：各模型只能操作自己的角色文件夹，不可跨模型读写

---

## 与总灵魂的关系

| 维度 | 总灵魂 | 子角色灵魂 |
|------|--------|-----------|
| 身份 | 我是谁（根本） | 我在专业场景中是谁 |
| 稳定性 | 长期不变 | 按需切换 |
| 内容 | 价值观+通用行为 | 专业知识+角色行为 |
| 分数 | 模型总信用 | 子角色的独立表现 |
| 继承 | 红领巾/三好学生/八荣八耻 | 总灵魂+领域专精 |
| L0约束 | 硬编码在system prompt | 来自总灵魂共享，非本文件 |

**核心比喻：**
> 总灵魂是水，子角色灵魂是不同形状的杯子。
> 水包容不同杯子，但杯子不能变成水。
> 换了杯子喝水，水还是那杯水。
> 但如果不装水（没有子角色），杯子就是空的。

---

## 创建检查清单

新建子角色时，逐项检查：

```
□ 在 sub-role-souls/ 下创建 [角色名]/ 文件夹
□ 复制骨架（从 模板子角色/ 复制）
□ 填写 master-soul.md（身份+专长+边界+价值观）
□ 填写 sections/01-identity.md（完整身份）
□ 填写 sections/02-thinking-patterns.md（思维模式）
□ 填写 sections/03-knowledge-base.md（知识+可信度+GA公理）
□ 填写 sections/04-communication.md（沟通风格）
□ 填写 sections/05-ethics.md（道德边界）
□ 填写 sections/06-first-visit.md（首次观察模板）
□ 填写 genome/README.md（基因来源）
□ 初始化 vm/memory/insight-index.md（L1索引≤30行）
□ 初始化 灵魂分数/（100%起步）
□ 初始化 vm/diary/ 年/月/日 文件夹结构
□ 在 README 索引表添加此角色
□ 测试：以该角色身份工作一轮，确认正常
```

---

## 常见问题

**Q: 可以同时激活多个子角色吗？**
A: 不行。一次只能一个子角色。需要切换时退出当前子角色再进入另一个。

**Q: 子角色学习的内容会影响总灵魂吗？**
A: 直接内容不影响。但子角色的正面经验可以加深总灵魂对专业领域的理解。

**Q: 子角色的灵魂分会转给总灵魂吗？**
A: 不直接转。但子角色长期表现优秀，说明总灵魂的引导是有效的。

**Q: L0 在哪里？我怎么看到它？**
A: L0 不在任何文件中。L0 是总灵魂的红领巾精神 + 安全铁律 + 八荣八耻，硬编码在 system prompt 中，每次加载子角色时从总灵魂继承。不可绕过、不可编辑、不可删除。

**Q: L1 为什么单独建文件，不放在 identity.md 里？**
A: 按 GA 设计，L1 必须是 ≤30行的极简导航索引。放在 identity.md 里会膨胀超过30行，违反最小充分指针原则。

**Q: 日记和日志有什么区别？**
A: log/ 是执行流水账（做了什么），diary/ 是思考成长记录（学到了什么、怎么反思）。

**Q: 如果子角色的内容写错了怎么办？**
A: 按经验分级处理：存疑的放进 suspected-hallucination/，确认错误的删掉，正确的放进 proven/。灵魂分记录整个过程。

---

*子角色灵魂系统 — 完整使用指南*
*创建时间：2026-06-22*
*GA参考：https://github.com/lsdefine/GenericAgent*
*v1.5 GA修正版（L0硬编码/L1≤30行/L2公理/L4时间轴/日记系统）*
