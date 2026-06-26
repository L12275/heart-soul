# GA (GenericAgent) 参考资料索引

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
*最后更新：2026-06-26 21:18*
