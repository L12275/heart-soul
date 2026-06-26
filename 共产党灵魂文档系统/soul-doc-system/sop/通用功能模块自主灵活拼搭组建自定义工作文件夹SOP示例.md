# 通用功能模块自主灵活拼搭组建自定义工作文件夹 SOP 示例

> **核心原则：功能模块 = 模板，不是存储。模板在通用区持续更新，工作区复制拼搭。**
> 此SOP教模型如何把通用区的功能模块文件夹，拼搭成自己需要的自定义工作文件夹。
>
> **前置思考系统：拼搭前必须先走 `世界最强脑师-前置思考系统.md`，锁定领域+最强脑师视角，确认拼搭方案是最佳机会做法后再执行。**
> **执行边界：拼搭完成后如果是默认模式 → 直接交付；如果用户要解释 → 既拼搭也说明方案；如果用户只是问 → 输出拼搭方案但暂不执行。**

---

## 一、什么时候需要拼搭

| 场景 | 需要拼搭 |
|------|---------|
| 新建工作台 | 从通用区复制 memory/ + diary/ + sop/ + workflow/ + desktop/ 等模块 |
| 新建账号空间 | 从通用区复制 bookmarks/ + contacts/ + memory/ + diary/ 等模块 |
| 新建子角色 | 从模板复制完整骨架，再按需增减模块 |
| 新建团队工作区 | 拼搭 Agents/ + memory/ + diary/ + workflow/ 等模块 |
| 特殊隔离需求 | 创建隔离文件夹，只拼搭需要的模块，避免信息污染 |

**不需要拼搭**：在已有完整功能的工作区直接使用，不需要重新拼搭。

---

## 二、拼搭前准备

### Step 1：确定需要哪些模块

问自己：
- 这个工作区是做什么的？
- 需要记忆吗？（memory/）
- 需要日记吗？（diary/）
- 需要SOP吗？（sop/）
- 需要工作流吗？（workflow/）
- 需要桌面（便签/收藏夹/通讯录）吗？（desktop/）
- 需要产物管理吗？（product/）
- 需要工具吗？（tools/）
- 需要技能吗？（skills/）
- 需要临时文件夹吗？（temp/）

### Step 2：检查通用区有没有对应模块

通用区位置：`soul-doc-system/` 下的各功能模块文件夹

| 模块 | 通用区位置 | 说明 |
|------|-----------|------|
| 记忆 | `memory/` | L0-L4分层，context/ + daily/ |
| 日记 | `diary/` | 按日期组织 YYYY/MM/DD/ |
| SOP | `sop/` | 标准操作流程。必须包含：世界最强脑师-前置思考系统、顶级机会做法SOP、超级信息SOP |
| 工作流 | `workflow/` | 标准操作顺序 |
| 桌面 | `desktop/` | bookmarks/ + contacts/ + sticky-notes/ |
| 产物 | `product/` | 产出物存放 |
| 工具 | `tools/` | CLI/脚本/程序/网页工具 |
| 技能 | `skills/` | 编码/领域/工具技能 |
| 临时 | `temp/` | 临时文件 |
| 经验 | `experience/` | 验证过的经验 |
| 发现 | `discovery/` | 机会/启发记录 |
| 采集 | `collection/` | 临时/持久数据 |
| 自动化 | `automation/` | 自动化配置 |
| 深度研究 | `深度研究/` | 深度研究内容 |
| 知识库 | `wiki/` | 精炼知识库 |
| 智能体 | `Agents/` | 模板存放区 + 运行区（活跃/历史），前置思考先行 |

---

## 三、拼搭方法

### 方法A：直接复制拼搭（最简单）

适用于：需要和通用区结构完全一致的工作区。

```
1. 在目标位置创建新文件夹
2. 从通用区复制需要的模块文件夹
3. 复制后根据需要微调
```

**示例：新建一个研究工作台**
```bash
# 1. 创建目标文件夹
mkdir -p production_space/研究工作台/

# 2. 从通用区复制模块
cp -r soul-doc-system/memory/ production_space/研究工作台/memory/
cp -r soul-doc-system/diary/ production_space/研究工作台/diary/
cp -r soul-doc-system/sop/ production_space/研究工作台/sop/
cp -r soul-doc-system/workflow/ production_space/研究工作台/workflow/
cp -r soul-doc-system/desktop/ production_space/研究工作台/desktop/
cp -r soul-doc-system/product/ production_space/研究工作台/product/
cp -r soul-doc-system/temp/ production_space/研究工作台/temp/
```

### 方法B：隔离拼搭（需要防信息污染）

适用于：需要隔离的工作区（如子角色、团队Agent、不同账号空间）。

```
1. 在目标位置创建隔离文件夹
2. 只复制需要的模块（不是全部复制）
3. 不复制不需要的模块（避免信息混淆）
4. 如果两个隔离区需要相同组合：
   a. 先在第一个隔离区完成拼搭
   b. 把拼搭完成的文件夹复制并改名
   c. 在副本中微调差异部分
```

**示例：新建一个隔离的子角色工作区**
```bash
# 1. 创建隔离文件夹
mkdir -p sub-role-souls/新子角色/

# 2. 只复制需要的模块（不是全部）
cp -r soul-doc-system/memory/ sub-role-souls/新子角色/memory/
cp -r soul-doc-system/sections/ sub-role-souls/新子角色/sections/
cp -r soul-doc-system/sop/ sub-role-souls/新子角色/sop/
# 不复制 desktop/（子角色不需要收藏夹/通讯录）
# 不复制 space/（子角色不操作账号空间）

# 3. 如果需要第二个相同组合的子角色
cp -r sub-role-souls/新子角色/ sub-role-souls/新子角色2/
# 在 新子角色2/ 中微调差异（如 sections/ 内容不同）
```

**示例：两个需要相同模块组合的团队Agent**
```bash
# 1. 拼搭第一个
mkdir -p 团队/会话临时子代理区/agent-A/
cp -r soul-doc-system/memory/ 团队/会话临时子代理区/agent-A/memory/
cp -r soul-doc-system/diary/ 团队/会话临时子代理区/agent-A/diary/
cp -r soul-doc-system/workflow/ 团队/会话临时子代理区/agent-A/workflow/

# 2. 复制并改名（不是重新拼搭）
cp -r 团队/会话临时子代理区/agent-A/ 团队/会话临时子代理区/agent-B/
# agent-B 继承 agent-A 的完整模块组合
# 在 agent-B/ 中只改需要差异的部分
```

### 方法C：模板化拼搭（重复使用的组合）

适用于：经常需要创建相同组合的场景。

```
1. 在通用区创建一个"模板拼搭配置"
2. 记录这个组合包含哪些模块
3. 需要时按配置一键复制
```

**示例：研究工作台模板配置**
```markdown
# 研究工作台拼搭配置

模块清单：
- memory/ （L0-L4记忆）
- diary/ （日记）
- sop/ （SOP）
- workflow/ （工作流）
- desktop/ （桌面：bookmarks/contacts/sticky-notes）
- product/ （产物）
- temp/ （临时）

创建命令：
mkdir -p production_space/研究工作台/
cp -r soul-doc-system/{memory,diary,sop,workflow,desktop,product,temp}/ production_space/研究工作台/
```

---

## 四、拼搭前检查清单（必须执行）

拼搭前，先过一遍前置思考检查：

- [ ] 是否已走完 `世界最强脑师-前置思考系统`？
- [ ] 是否锁定了拼搭方案的最优解（顶级机会做法）？
- [ ] 拼搭模式是否确认（默认执行/边做边解释/只思考不执行）？
- [ ] 需要的模块清单是否完整？
- [ ] 是否需要隔离（方法B）？

## 五、拼搭后检查清单

拼搭完成后，逐项检查：

- [ ] 需要的模块都已复制？
- [ ] 不需要的模块都已排除（隔离场景）？
- [ ] memory/ 下 context/ 和 daily/ 结构完整？
- [ ] diary/ 下有 README.md？
- [ ] sop/ 下有 README.md + 核心SOP文件（前置思考系统+顶级机会做法+超级信息SOP）？
- [ ] workflow/ 下有 README.md？
- [ ] desktop/ 下有 bookmarks/ + contacts/ + sticky-notes/？
- [ ] 所有空文件夹都有 .gitkeep？
- [ ] 拼搭完成的文件夹结构与预期一致？

---

## 五、何时更新拼搭模板

- 通用区的模块更新后，工作区的拼搭副本**不自动更新**
- 需要手动同步：把通用区的新内容复制到工作区
- 如果通用区有重大结构变更，重新拼搭比逐个同步更高效

---

## 六、与各环区的关联

| 环区 | 拼搭场景 | 参考此SOP |
|------|---------|----------|
| ① 用户中心 | 用户放置指示文件 | 不适用（用户直接放） |
| ② 共产中心 | 公告板拼搭 | 按需拼搭 |
| ③ 主灵魂中心 | 灵魂文档系统本身 | 完整拼搭 |
| ④ 生产空间中心 | 新建工作台 | **按此SOP拼搭** |
| ⑤ 空间中心 | 新建账号空间 | **按此SOP拼搭** |
| ⑥ 子角色中心 | 新建子角色 | **按此SOP拼搭** |
| ⑦ 团队协作环 | 新建团队Agent | **按此SOP拼搭** |

---

*通用功能模块拼搭SOP示例*
*创建时间：2026-06-25*
*触发：需要创建新的工作文件夹时*

---
*最后更新：2026-06-26 21:18*
