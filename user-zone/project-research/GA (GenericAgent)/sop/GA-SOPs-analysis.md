# GA SOP 系统分析 — 可借鉴复用的设计

> 来源：https://github.com/lsdefine/GenericAgent
> 分析时间：2026-06-22

---

## GA 的 SOP 自动沉淀流程

```
同一场景3次 → 提炼SOP候选 → 验证1次 → 标记validated
validated SOP积累 → 触发merge到更高层级
```

**关键：** GA 不预先设计 SOP，而是从实际工作中自动结晶。

**9个原子工具 = 9个最小SOP：**
- code_run → 执行代码的标准流程
- file_read/write/patch → 文件操作SOP
- web_scan → 网页扫描SOP
- web_execute_js → 浏览器控制SOP
- update_working_checkpoint → 短期记忆写入SOP
- start_long_term_update → 长期记忆蒸馏SOP

## morphling_sop.md（项目级能力吸收）

核心三元组：目标 + 测例 + 行为（调用/重写/舍弃）

可复用到子角色：当子角色需要学习新领域的知识时，用 morphling 方法吸收。

---

*GA SOP分析*
*创建时间：2026-06-22*
