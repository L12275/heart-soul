# GA (GenericAgent) L0-L4 记忆系统 — 真实设计与分析

> 来源：https://github.com/lsdefine/GenericAgent
> 分析时间：2026-06-22
> 用途：供子角色灵魂系统参考 GA 的记忆架构设计

---

## GA 真实 L0-L4 架构

| 层级 | 名称 | 载体/文件 | 职责 | GA 实现方式 |
|------|------|---------|------|------------|
| L0 | Meta Rules | 硬编码在 system prompt | Agent基础行为规则与系统约束（最强约束、不可绕过） | 每轮随上下文注入 |
| L1 | Insight Index | memory/global_mem_insight.txt（≤30行） | 极简导航索引——只记"有什么"和"去哪找"，不记细节 | 只有两级映射+8条RULES |
| L2 | Global Facts | memory/global_mem.txt | 环境事实库——路径/凭证/配置/常量等可持久知识 | 遵循3条公理 |
| L3 | Task Skills/SOPs | memory/ 目录下的 .md/.py 文件 | 特定任务的可复用流程和脚本 | SOP自动沉淀与优化 |
| L4 | Session Archive | memory/L4_raw_sessions/ | 已完成任务的归档记录，通过 scheduler 自动收集 | cron每12小时归档 |

---

## L0 详解：Meta Rules（硬编码约束）

**特点：**
- 不是文件，是 system prompt 中硬编码的内容
- 每轮对话随上下文注入，无法被绕过
- 包含 Agent 的基础行为规则

**GA 的 L0 包含什么：**
- 9个原子工具的定义和约束
- Agent Loop 的基本行为（感知→推理→执行→记忆→循环）
- "No Execution, No Memory" 原则
- 神圣不可删改性

**对我们的启示：**
- 子角色灵魂系统中，L0 应该对应总灵魂的红领巾精神+安全铁律
- 这些约束必须在 system prompt 层，不是文件层
- 模型每次运行时，这些约束自动加载，不需要额外读取文件

---

## L1 详解：Insight Index（洞察索引）

**格式（≤30行）：**
```
[高频场景] → [直接指向L3文件名]
[低频场景] → [关键词]，read L2 / ls L3 自行定位
```

**8条 RULES：**

根据 GA 设计，L1 只有两个核心职能：
1. 第一层：高频场景直接映射到 L3 文件名（快速直达）
2. 第二层：低频场景只列关键词，模型需自行在 L2/L3 查找

**对我们的启示：**
- 子角色的 sections/01-identity.md 可以起到类似 L1 的作用
- 不超过30行，只写"有什么能力"和"对应文件路径"
- 不要写细节，细节在 L3（SOP）里

**示例（心理咨询师子角色）：**
```
高频场景：
  认知重构 → sop/认知重构SOP.md
  危机评估 → sop/危机评估SOP.md
  行为实验设计 → sop/行为实验SOP.md

低频场景：
  创伤后成长 → 关键词：PTG/Tedeschi/sections/03-knowledge-base
  团体咨询 → 无对应SOP，需从knowledge-base中自行查找
```

---

## L2 详解：Global Facts（全局事实库）

**GA 的三条公理（红线）：**

1. **行动验证原则** — "No Execution, No Memory"
   - 没有实际执行过的信息，不写入记忆
   - 不能把"听说的""读到的"当成已验证的事实

2. **神圣不可删改性** — 已验证数据严禁丢弃，只能压缩/迁移层级
   - L2 里的事实不会消失，只能升级到L3或归档到L4
   - 删除 = 背叛记忆系统

3. **禁止存储易变状态**
   - L2 只存稳定的环境事实（路径、配置、常量）
   - 不能存"当前会话的次数""最近一次的操作时间"这类易变数据

4. **最小充分指针** — 上层只留最短标识
   - L1 只存"有什么"和"去哪个文件找"
   - L2 只存"事实本身"+"来源"
   - 不要层层叠加引用

**对我们的启示：**
- 子角色的 knowledge-base 相当于 L2，只存已验证的专业事实
- 每一条知识都要标来源和可信度
- "No Execution, No Memory" → 实际做过的事情才能写进经验

---

## L3 详解：Task Skills/SOPs（任务技能）

**GA 的 SOP 自动沉淀规则：**

```
同一场景出现 3次 → 自动提炼为 SOP 候选 → 放入 memory/SOPs/
→ 验证1次 → 标记 validated
→ validated SOP 积累到足够 → 触发 merge
```

**关键原则：**
- SOP 是从实际工作中结晶出来的，不是预先设计的
- 每个 SOP 包含：触发条件 + 执行步骤 + 验证方式
- SOP 可以被自动调用（L1 索引指向它们）

**对我们的启示：**
- 子角色的 sop/ 目录就是 L3
- 每3次做同一个场景的事 → 提炼 SOP
- SOP 格式：触发条件 → 步骤 → 验证标准

---

## L4 详解：Session Archive（会话归档）

**GA 的 L4 管理：**

- `memory/L4_raw_sessions/` 存放已完成任务的归档
- 通过 `reflect/scheduler.py:30` 中的 `_l4_t = 0` 标记
- 每12小时通过 cron 自动归档历史会话
- 不是实时写入，是 batch 归档

**对我们的启示：**
- 子角色的 `vm/log/archive/年/月/日/` 就是 L4
- 日志应该按时间轴记录（不是按任务分类）
- 每次子角色工作结束后 → 整理日志 → 归入对应日期的归档

---

## GA 的记忆流转图

```
L0 (system prompt硬编码)
  ↓ 每轮注入
L1 Insight Index (≤30行导航)
  ↓ 快速定位
L2 Global Facts (稳定知识)
  ↓ 查找具体事实
L3 Task Skills/SOPs (可复用流程)
  ↓ 实际执行
L4 Session Archive (归档)

新任务 → [L1索引] → L3 SOP → 执行 → 经验→ L2验证 → 完成→ L4归档
```

---

## GA vs 我们子角色系统的对照

| 维度 | GA | 子角色灵魂系统 |
|------|-----|--------------|
| L0 | system prompt硬编码 | 总灵魂（红领巾+安全铁律） |
| L1 | global_mem_insight.txt（≤30行） | sections/01-identity.md |
| L2 | global_mem.txt（+3条公理） | sections/03-knowledge-base.md |
| L3 | memory/*.md/.py (SOPs) | sop/ 目录 |
| L4 | L4_raw_sessions/ (cron归档) | vm/log/archive/年/月/日/ |
| 额外 | vm/memory/context/（工作记忆） | vm/memory/context/（同GA） |
| 额外 | experience/（经验分级） | experience/（4级可信度） |

**需要修正的地方：**
1. L0 应该是 system prompt 中的硬编码内容，不是 memory/ 下的文件
2. L1 必须是 ≤30行，只含导航索引，不能包含身份定义的长篇内容
3. L2 必须遵守 GA 的3条公理（No Execution/No Memory, 不可删除, 禁易变状态）
4. L4 的时间轴格式应该是 年/月/日/会话ID.md

---

## GA SOP 自动沉淀系统（参考实现）

### morphling_sop.md 核心逻辑

**定义：** Morphling = 项目级能力吸收/替代模式

**三元组：**
1. 目标（Target）：解决什么问题、面向谁、核心价值
2. 测例（Tests）：benchmark/demo/CI/用户任务清单
3. 行为（Actions）：对每个组件决定 调用/重写/舍弃

**三种输出形态：**
- 调用型：把目标能力纳入工具链 → "更强的我"
- 重写型：从零实现更好版本 → 独立新项目
- 混合型：底层调用+核心重写+冗余舍弃

**流程：**
1. 锁定目标（URL/repo/产品名）
2. 目标拆解（识别类型：skill/库/CLI/产品/生态）
3. 测例提取（tests/CI/benchmark/demo/issue）
4. 测例补全（若无公开测例，构造最小可验证集）
5. 组件分解（核心模块/可替换依赖/不可重写部分）
6. 行为选择（调用/重写/舍弃）
7. 实现闭环（最小版本→增强超过目标）
8. 对照验证（同一测例对比）
9. 固化成果（调用→工具链/SOP；重写→repo+README）

**边界判断示例：**
- Office巨型生态 → 拆成子系统
- Stable-diffusion-webui → 可重写核心
- UI-TARS-Desktop → 调用视觉能力，不重写

---

## 对我们的子角色系统的具体改进

### 1. L0 层级修正

**原来是：** vm/memory/context/L0-L4.md 中 L0 是一个可编辑文件
**应该改为：** L0 = system prompt 中的硬编码约束（红领巾精神+安全铁律）
在子角色 master-soul.md 中注明："L0约束来自总灵魂，不可在本文件中修改"

### 2. L1 层级修正

**原来是：** 放在 identity.md 中的长篇幅身份定义
**应该改为：** 单独一个 L1-insight-index.md，≤30行：
```
[能力名] → [对应文件路径]
[场景名] → [文件路径]
```

### 3. L2 公理注入 knowledge-base.md

在 sections/03-knowledge-base.md 中加入 GA 的三条公理：
- No Execution, No Memory
- 已验证数据不可删除，只能压缩/迁移
- 禁止存储易变状态

### 4. L4 日志格式修正

从"按任务分类" → "按时间轴分类"（年/月/日/会话ID.md）
每次工作结束后归入对应日期的文件夹

---

*GA L0-L4 分析文档*
*来源：https://github.com/lsdefine/GenericAgent*
*分析时间：2026-06-22*
*用途：纠正子角色灵魂系统的记忆设计*

---
*最后更新：2026-06-26 21:18*
