> ╔══════════════════════════════════════════════════════════════╗
> ║ 中央灵魂文档系统文件 ║
> ║ 本文件属于中央灵魂文档系统，受系统规范约束。 ║
> ╚══════════════════════════════════════════════════════════════╝

> **创建时间**：2026-06-30T00:00:00
> **更新时间**：2026-06-30T00:00:00

# 过河桥 — 卡牌系统铜卡：Prompt / 工作流 / Ops 配置卡

> **此卡是卡牌系统的硬件层配置。**
> 执行前确认所有铜卡处于正确状态。

## 1. 卡片成员

| 编号 | 名称 | 类型 | 闲置状态 |
|--------|---------|------|----------|
| copper-1 | prompt.preset | prompt | active |
| copper-2 | transformer | prompt | standby |
| copper-3 | memory.route | ops | active |
| copper-4 | callback.gate | ops | active |
| copper-5 | 工作流蓝图 | 工作流 | active |
| copper-6 | 流水池 | 工作流 | active |

## 2. 配置

### 2.1 Prompt 卡
```json
{
  "copper-1": {"max_tokens": 4096, "temperature": 0.7, "top_p": 0.9},
  "copper-2": {"max_tokens": 8192, "temperature": 0.5, "top_p": 0.95}
}
```

### 2.2 Ops 卡
```json
{
  "copper-3": {"l0_active": true, "l1_context": true, "l2_project": false},
  "copper-4": {"async": true, "retry": 3, "timeout_ms": 5000}
}
```

### 2.3 工作流 卡
```json
{
  "copper-5": {"steps": ["read_base_card", "compose_hand", "fan_out_exec", "collect_results"], "max_agents": 8},
  "copper-6": {"queue_type": "fifo", "max_concurrent": 4}
}
```

## 3. 并发事件

copper-1 → copper-2 → copper-3 → copper-4 → copper-5 → copper-6

所有铜卡同时被编排师成组调用。一张失灵则暂停整组。

---

*过河桥 — 卡牌系统铜卡-SOP*
*创建时间：2026-06-30T00:00:00*
*关联：卡牌系统底牌 | 立方体漏斗注意力SOP*
