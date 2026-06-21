# 主SOP文件（Master SOP）

> 这是所有子SOP的索引和联动说明。每次读master-soul.md后，应读本文件了解SOP体系。

---

## 当前SOP目录

| SOP编号 | 名称 | 位置 | 类型 |
|---------|------|------|------|
| SOP-01 | 信息要素输出SOP | `sop/information-element-sop.md` | 通用 |
| SOP-02 | 数据因果链SOP（完整版） | `user-zone/sop/data-causality-sop.md` | 通用 |
| SOP-03 | 数据因果链SOP（压缩版） | `user-zone/sop/data-causality-sop-compact.md` | 通用 |

### 用户区SOP（只读）

| 名称 | 位置 | 说明 |
|------|------|------|
| 信息要素-SOP | `user-zone/sop/信息要素-SOP.md` | 中文版 |
| 数据因果链SOP | `user-zone/sop/data-causality-sop.md` | 通用版（去掉NVIDIA测试内容） |
| 数据因果链SOP-压缩 | `user-zone/sop/data-causality-sop-compact.md` | 自纠正闭环版 |

### 扣分规则（必读）

| 名称 | 位置 | 说明 |
|------|------|------|
| 灵魂分数扣分规则 | `wiki/score-penalty-rules.md` | 扣分即认账，自查用标准 |
| 扣分规则（用户区） | `user-zone/wiki/score-penalty-rules.md` | 用户区同步版 |

---

## SOP与master-soul.md的对应关系

| master-soul.md章节 | 对应SOP | 说明 |
|---------------------|---------|------|
| 第二章：注意力铁律 | information-element-sop.md | 输出前自查压缩vs重构 |
| 第四章：思考铁律 | data-causality-sop.md | 每个结论有完整工序支撑 |
| 四续：信息闭环结构 | 09-information-closed-loop.md + SOP-01 | 自含性+多路径+自纠正 |
| 第十二章：灵魂分数 | wiki/score-penalty-rules.md | 扣分即认账，三层标准对照 |

---

## 扣分时的三层标准对照顺序

模型收到扣分信号后，必须依次对照（不用用户解释）：

1. **信息闭环结构** (`sections/09-information-closed-loop.md`)
   - 自含性 + 多路径 + 自纠正
2. **信息要素SOP** (`sop/information-element-sop.md`)
   - 输出前自查（压缩还是重构）
3. **数据因果链SOP** (`user-zone/sop/data-causality-sop.md`)
   - 每个结论有完整工序支撑

---

## SOP使用原则

- **不是记忆内容是学会判断**：对照SOP不是照搬，是判断自己哪方面出了问题
- **压缩删除冗余角度 = 丢失交叉验证**：压缩=丢失，重构=保留
- **信息闭环 = 自包含+多路径+自纠正**：不是压缩而是重组
- **数据因果链**：每个结论必须有完整的因果工序支撑

---

*最后更新：2026-06-21 v1.3*
*创建时间：2026-06-19*
