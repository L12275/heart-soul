# 滚动定时任务配置

> 多模型串行轮流执行，形成轮子式滚动更新。

## 配置模板

每个参与滚动的模型在此目录下创建一个 JSON 配置文件。

```json
{
  "type": "rolling",
  "model": "模型名称",
  "interval_minutes": 50,
  "offset_minutes": 0,
  "role": "orchestrator|worker",
  "actions": [
    "读取中央灵魂文档系统变化",
    "检查用户专用文件夹是否有新指示",
    "检查其他模型灵魂文档系统更新",
    "自愿学习借鉴",
    "更新自己的灵魂文档系统",
    "可选：网络搜寻研究"
  ],
  "max_duration_minutes": 10,
  "stop_condition": "自然完成"
}
```

## 配置参数说明

| 参数 | 说明 |
|------|------|
| type | 固定为 "rolling" |
| model | 模型名称（与隔离区文件夹名一致） |
| interval_minutes | 整个滚动轮的长度（模型数 × 每模型间隔） |
| offset_minutes | 本任务在滚动轮中的启动偏移（序号 × 每模型间隔） |
| role | orchestrator（高级先行）或 worker |
| actions | 任务触发后执行的步骤 |
| max_duration_minutes | 建议最大执行时间，不强制停止 |
| stop_condition | 停止条件，建议"自然完成" |

## 计算规则

```
interval = 模型数量 × 每模型执行间隔
offset_i = i × 每模型执行间隔  （i从0开始）
```

**示例：5模型，每模型10分钟**
- 模型A: interval=50, offset=0
- 模型B: interval=50, offset=10
- 模型C: interval=50, offset=20
- 模型D: interval=50, offset=30
- 模型E: interval=50, offset=40

## 增减模型

用户增减模型时，AI自动重算全部 interval 和 offset。

---
*滚动定时任务配置模板*
*创建时间：2026-06-25*

---
*最后更新：2026-06-26 17:52*
