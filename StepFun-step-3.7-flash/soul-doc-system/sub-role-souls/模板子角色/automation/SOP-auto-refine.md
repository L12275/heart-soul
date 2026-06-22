# SOP自动沉淀与优化系统

> 参考 GA (GenericAgent) 的 SOP 自动沉淀与优化系统。
> 此脚本/流程让模型自动把经验转化为可复用的 SOP。

---

## 自动沉淀规则

同一场景出现 **3次** → 自动提炼为 SOP 候选

## SOP 进化流程

```
工作产出 → 发现有效模式 → 记录到 experience/
→ 出现3次 → 提炼为 SOP 候选 → 放入 sop/README.md
→ 验证1次 → 标记 validated
→ validated SOP 积累3个 → 触发 merge 到 sections/
```

## 优化规则

- 每次使用 SOP 后记录效果
- 效果不好 → 更新 SOP（修改步骤或触发条件）
- 效果持续好 → 升级熟练度
- 发现更好的做法 → 重写 SOP

---

*自动化系统：automation/SOP-auto-refine.md*
*创建时间：2026-06-22*
