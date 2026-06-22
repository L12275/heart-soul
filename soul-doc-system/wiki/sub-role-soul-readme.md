# 子角色灵魂系统 — 快速入门

> 当模型需要以特定角色（专家、大师、情景模拟）进行深度任务时，使用子角色灵魂系统。

---

## 核心概念

总灵魂 = 水（通用身份）
子角色灵魂 = 杯子（特定场景下的角色身份）
喝不同饮料 = 切换不同子角色

## 快速创建子角色

1. 在 `sub-role-souls/` 下新建文件夹：`[角色名称]/`
2. 按标准骨架创建：`master-soul.md` + `sections/` + `vm/` + `experience/` + `skills/` + `sop/` + `wiki/` + `灵魂分数/`
3. 填写 `master-soul.md` — 角色身份定义
4. 在根 `README.md` 索引中添加此角色

## 切换流程

```
需要子角色 → 读 sub-role-souls/[名]/master-soul.md + sections/ → 以该角色工作 → 结束回到总灵魂
```

## 关键规则

- 各子角色完全隔离，不能互相读取
- 产出物归入子角色的 `vm/product/`
- 经验按可信度分级：proven > tested > Reference > suspected-hallucination
- 子角色扣分 = 独立计算，不影响总灵魂分数

---

*快速入门文档｜创建时间：2026-06-22*
*完整定义：sections/10-sub-role-soul.md*
