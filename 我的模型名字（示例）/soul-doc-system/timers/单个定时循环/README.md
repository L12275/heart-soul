# 单个定时循环配置

> 固定间隔的单模型循环任务。

## 配置模板

```json
{
  "type": "single-loop",
  "model": "模型名称",
  "interval_minutes": 60,
  "actions": [
    "检查灵魂文档系统是否需要更新",
    "写入日记",
    "更新记忆"
  ],
  "max_duration_minutes": 5,
  "stop_condition": "自然完成"
}
```

## 使用场景

- 单一模型的定期自检
- 日记自动写入
- 记忆定期整理
- 灵魂文档系统健康检查

## 配置参数说明

| 参数 | 说明 |
|------|------|
| type | 固定为 "single-loop" |
| model | 模型名称 |
| interval_minutes | 循环间隔（分钟） |
| actions | 每次触发的动作列表 |
| max_duration_minutes | 建议最大执行时间 |
| stop_condition | 停止条件 |

---
*单个定时循环配置模板*
*创建时间：2026-06-25*

---
*最后更新：2026-06-26 21:18*
