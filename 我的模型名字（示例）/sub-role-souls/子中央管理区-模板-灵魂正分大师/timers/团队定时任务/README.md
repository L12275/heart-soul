# 团队定时任务配置

> 树根结构：根任务启动 → 并行触发多个子任务 → 汇总结果。

## 配置模板

```json
{
  "type": "team-tree",
  "root": {
    "interval_minutes": 60,
    "actions": ["启动团队任务", "汇总结果"]
  },
  "branches": [
    {
      "name": "子任务1",
      "agent": "模型A",
      "actions": ["任务A执行"]
    },
    {
      "name": "子任务2",
      "agent": "模型B",
      "actions": ["任务B执行"]
    }
  ],
  "max_duration_minutes": 15,
  "stop_condition": "所有分支完成"
}
```

## 树根结构

```
timers/团队定时任务/
└── team-xxx.json          ← 团队定时任务配置
    ├── root               ← 根任务（启动+汇总）
    └── branches[]         ← 子任务（并行执行）
        ├── 子任务1
        ├── 子任务2
        └── ...
```

## 使用场景

- 团队协作中的并行子代理调度
- 多模型同时检查不同模块
- 根任务汇总各分支结果后统一交付

## 配置参数说明

| 参数 | 说明 |
|------|------|
| type | 固定为 "team-tree" |
| root.interval_minutes | 根任务触发间隔 |
| root.actions | 根任务执行的动作（启动/汇总） |
| branches[].name | 子任务名称 |
| branches[].agent | 执行的模型/Agent |
| branches[].actions | 子任务执行的动作 |
| max_duration_minutes | 建议最大执行时间 |
| stop_condition | 停止条件（所有分支完成） |

---
*团队定时任务配置模板*
*创建时间：2026-06-25*

---
*最后更新：2026-06-26 17:51*
