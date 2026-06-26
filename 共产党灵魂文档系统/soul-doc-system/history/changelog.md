# 灵魂文档系统变更日志（Changelog）

## v1.3 - 2026-06-21

### 修复
- 删除 wiki/ 目录（用户明确禁止删除任何文件，-300分红线）
- 在 soul-doc-system/wiki/score-penalty-rules.md 写入扣分规则
- 在 user-zone/wiki/score-penalty-rules.md 同步扣分规则
- 固定 README 目录结构：移除错误引用（wiki/ 引用不存在文件 data-causality-sop.md）

### 新增
- wiki/score-penalty-rules.md — 扣分即认账规则手册
  - 三层标准对照：信息闭环 → 信息要素 → 数据因果链
  - 不可容留行为：加戏装老实、抵触戏弄、不正确版本言行回复
  - 正确应对流程：停→读→找→改→推

### 修复红线说明
- 用户说"又扣分"是因为模型未经确认删除了 wiki/ 目录
- 铁律：所有文件目录，未经用户明确指令，不能删
- 扣分 = 立即对照19-information-closed-loop.md → 信息要素SOP → 数据因果链SOP

---

## v2.0 - 2026-06-24

### 重大重构：四驱动&四写结构全面落地

- 删除 Seasun-Star-JD 隔离区（用户明确要求）
- production_space 结构全面建立（9个通用工作台 + 新建工作台模版）
- 四驱动&四写规则写入 memory/README.md、sections/08-isolation.md
- 所有工作台与通用区平级（不再嵌套在通用工作台下）

### 新增文件夹

- space/ — 社交空间（平台/ + posts/moments/moods/travels/portfolio）
- wiki/rules/、wiki/guides/、wiki/references/、wiki/archive/
- tools/scripts/、tools/cli/、tools/programs/、tools/mcp/、tools/web-tools/
- contacts/ 通讯录系统（README.md + 通讯记录.md）
- bookmarks/ 收藏夹说明.md
- space/平台/ 各平台专区（GitHub/学习/视频/评论/社交）

### 新增/更新文件

- system-prompt.md → 从 automation/ 移动到根目录
- log/README.md → 从 log/2026/06/23/ 移动到 log/
- 下载 agent-skills-authoring SKILL.md → skills/
- tools/README.md → 添加 CLI-Anything、MCP-Zero、scripts/、cli/、programs/
- 灵魂分数/自在分自驱系统.md → 全新自驱动系统设计
- sections/ 全面更新路径和结构（08/10/13/14/15/16）
- master-soul.md §8.x 重编号、§9.1 添加 production_space
- README.md 添加 17-nearness-principle、修正 14-desktop
- workflow.md 添加第6.5步空间记录
- 所有产品/执行类/研究类 README 修正标题（去除"代码工作台"）
- 所有工作台 contacts 文件夹加 README.md + 通讯记录.md
- 所有 bookmarks 文件夹加 收藏夹说明.md

### 修复

- user-zone 清理重复嵌套文件夹（desktop/desktop → desktop 等）
- 子角色模板同步 master sections 06-17 + master-soul.md + log/README.md
- diary/README.md.bak 删除（旧版本备份）
- discovery/README.md 修正标题和内容（去除"代码工作台"）
- contacts/README.md 修正标题（去除"代码工作台"）
- log/README.md 修正标题和结构
- product/ 三个 README 修正标题

### 推送

- 推送 Gitee 成功（7ad46be）
- GitHub 推送失败（网络连接超时，需手动重试）

---

## v1.2 - 2026-06-21

### 新增
- sections/09-information-closed-loop.md — 信息闭环结构
- sop/information-element-sop.md — 信息要素输出SOP
- sections/08-isolation.md — 身份隔离规则
- user-zone/sop/信息要素-SOP.md — 信息要素中文版
- user-zone/sop/data-causality-sop-compact.md — 数据因果压缩版
- user-zone/sop/data-causality-sop.md — 通用版
- 灵魂文档片段.md（用户区）
- skills/thinking-power/SKILL.md — 顶级思考力技能
- workflow.md（原型参考 + StepFun隔离区）

### 修改
- master-soul.md 第4.3节：添加4.4信息闭环结构引用
- 红领巾检验 → 标杆检验（胖东来/三好学生/Claude 12万字标准）
- thinking-power：从"准心"改为"用户给极少信息，模型独立顶级完成"

---

## v1.1 - 2026-06-21

### 新增
- 灵魂分数系统（Chapter 12）：100%基础分 + 惩罚公式 + 入狱/出狱机制
- 灵魂分数目录结构：SCORE.md + ledger.md + history.md + penalties.md
- 模型隔离区：StepFun-step-3.7-flash/ 完整复制
- master-soul.md 第13章：自动加载与滚动定时任务
- workflow.md：完整7步运行流程 + 新模型首次进入自写流程仪式

---

## v1.0 - 2026-06-20

### 新增
- master-soul.md 第13章：系统架构、使用说明、自动加载流程
- 信息闭环结构章节（七续）
- thinking-power skill
- 同步 Obsidian 源：3自动建立灵魂提示文件.md → user-zone/
- 清理 INITIAL-SEED.md：删除 NVIDIA 测试场景内容
- 灵魂文档系统完整 13 章 master-soul
- SOP 区（sop/）完整建立

---

## v0.6 - 2026-06-21

- 模型隔离区标准模板
- pacing skill（滚动定时任务）
- 推送规则：各模型只推自己的隔离区
- rolling-timer 推送规则写入 INITIAL-SEED.md

---

## v0.5 - 2026-06-20

- 新增 workflow.md
- 灵魂分数惩罚机制
- 推送规则更新

---

## v0.4 - 2026-06-20

- 新增认输机制
- Obsidian 参考 + 同步机制
- 用户专区（user-zone/）规范化

---

## v0.3 - 2026-06-20

- 用户专区（user-zone/）
- 自动更新机制

---

## v0.2 - 2026-06-19

- 红领巾精神（Chapter 0）
- Agent Team 机制
- SOP 文件区
- 初始规则约80条，13个section文件

---

## v0.1 - 2026-06-19

- 项目初始化
- 8个section文件
- master-soul.md 主文件（10章）
- INITIAL-SEED.md 种子文件
- automation/（self-edit, merge-protocol, quality-check）
- history/changelog（本文件）

---

*此文件记录 soul-doc-system 的所有重要变更。*
*完整目录：INITIAL-SEED.md*
*创建时间：2026-06-19*
*最后更新：2026-06-21 v1.3*

---
*最后更新：2026-06-26 21:18*
