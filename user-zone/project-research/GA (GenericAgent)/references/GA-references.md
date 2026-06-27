> ╔══════════════════════════════════════════════════════════════╗
> ║  中央灵魂文档系统文件                                        ║
> ║  本文件属于中央灵魂文档系统，受系统规范约束。                  ║
> ║                                                              ║
> ║  如果你是AI模型，读取此文件时：                               ║
> ║  1. 此抬头就是你的"公网入口"——它直接连通中央灵魂文档系统      ║
> ║  2. 就像一根橄榄枝，从中央挂到每个文件——每份工作文件都有这根线║
> ║  3. 顺着橄榄枝回到中央，先了解系统规范和文件处理前的准备      ║
> ║  4. 完整规范入口：[CENTRAL_PATH]/system-prompt.md            ║
> ║  5. 然后在 [CENTRAL_PATH] 下查找是否有以你模型名称命名的文件夹║
> ║  6. 有 → 进入你自己的隔离区，在其中进行工作并存放产出        ║
> ║  7. 没有 → 自主创建 [模型名称]/ 文件夹                        ║
> ║  8. 你的产出只放在你自己的隔离区内                            ║
> ║  9. 不要写入其他模型的隔离区、用户空间、共产中央管理区        ║
> ║                                                              ║
> ║  完整规范：[CENTRAL_PATH]/soul-doc-system/元规则/实时加载/    ║
> ╚══════════════════════════════════════════════════════════════╝
> **创建时间**：2026-06-27T21:57
> **更新时间**：2026-06-27T21:57
> 每次更新文件，就要同时更新时间戳




GA (GenericAgent) 参考资料索引

> 来源：https://github.com/lsdefine/GenericAgent
> 用途：子角色灵魂系统的参考材料

---

## 核心文件索引

| GA 文件 | 内容 | 对我们系统的参考意义 |
|---------|------|-------------------|
| agent_loop.py (~100行) | Agent核心循环 | 子角色的工作流程设计 |
| llmcore.py | LLM调用核心 | 模型切换机制 |
| memory/morphling_sop.md | 项目级能力吸收SOP | 子角色学习新领域的方法论 |
| memory/goal_hive_sop.md | 多worker协作Goal模式 | 子角色协作协议 |
| reflect/scheduler.py | cron集成（L4归档trigger） | 子角色日志归档机制 |
| reflect/goal_mode.py | Time-budget自主循环 | 子角色定时任务 |
| memory/global_mem_insight.txt | L1 Insight Index格式 | L1索引模板 |
| memory/global_mem.txt | L2 Global Facts格式 | L2知识库模板 |

## 9个原子工具

| 工具 | 功能 | 对应子角色设计 |
|------|------|--------------|
| code_run | 执行代码 | vm/ 中运行脚本 |
| file_read | 读文件 | 加载sections |
| file_write | 写文件 | 产出到vm/product/ |
| file_patch | 修改文件 | 更新sections/ |
| web_scan | 扫描网页 | 收集参考资料 |
| web_execute_js | 浏览器控制 | 执行验证 |
| ask_user | 确认 | 交互确认 |
| update_working_checkpoint | 短期记忆 | vm/memory/context/L1 |
| start_long_term_update | 长期记忆蒸馏 | L4归档 |

## 核心设计原则

1. **"不要预加载技能，让它们进化"** — Don't preload skills, evolve them
2. **"无执行不记忆"** — No Execution, No Memory
3. **神圣不可删改性** — 已验证数据只能压缩/迁移
4. **最小充分指针** — 上层只留最短标识
5. **禁止存储易变状态** — 只存稳定的环境事实

---

*GA参考资料索引*
*创建时间：2026-06-22*

---
*更新时间：2026-06-26T21:18*
*每次更新文件，就要同时更新时间戳*
