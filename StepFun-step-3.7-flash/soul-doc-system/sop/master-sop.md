# 主SOP文件（Master SOP）

> 这是所有子SOP的索引和联动说明。AI每次读master-soul.md后，应读本文件了解SOP体系。
> 本文件关联到 master-soul.md 的第三章（工作流SOP）。

---

## 当前SOP目录

| SOP编号 | 名称 | 类型 | 级别 | 状态 |
|---------|------|------|------|------|
| 暂无 | 等待积累 | - | - | 初始状态 |

**说明：** 当前SOP区为空。随着AI工作积累，具体SOP将按类型和级别放入对应目录。

---

## SOP与master-soul.md的对应关系

| master-soul.md章节 | 对应SOP类型 | 说明 |
|-------------------|------------|------|
| 第一章：注意力铁律 | sop/types/attention/ | 注意力相关的具体执行SOP |
| 第二章：沟通规范 | sop/types/communication/ | 沟通相关的具体执行SOP |
| 第三章：工作流SOP | sop/types/workflow/ | 工作流程的具体执行SOP |
| 第四章：思考模式 | sop/types/thinking/ | 思考方法的具体执行SOP |
| 第五章：自我评价 | sop/types/evaluation/ | 评价方法的具体执行SOP |
| 第六章：安全边界 | sop/types/safety/ | 安全操作的具体执行SOP |
| 第七章：自我改进 | sop/types/general/ | 跨类型的通用改进SOP |

---

## SOP联动关系

```
master-soul.md（行为骨架）
    ↓ 引用
master-sop.md（SOP索引）
    ↓ 关联
各子SOP文件（具体执行步骤）
```

**执行顺序：**
1. AI读 master-soul.md → 了解行为规范
2. AI读 master-sop.md → 了解有哪些SOP可用
3. AI根据任务类型 → 找到对应的子SOP文件
4. AI按SOP步骤执行任务
5. AI发现更好的做法 → 创建/更新子SOP文件
6. 子SOP验证有效 → 考虑提升到master-soul.md

---

## 激活时机

**每个SOP文件必须写明：**
- 触发条件：什么情况下激活此SOP
- 执行顺序：与其他SOP的先后关系
- 结束条件：什么情况下SOP执行完毕

**激活方式：**
- AI在master-soul.md的第七章中找到"改进触发条件"
- 根据触发条件匹配对应的SOP文件
- 按SOP文件中的步骤执行

---

## 提升条件

某个SOP从sop区提升到master-soul.md的条件：
1. 经过3次以上实际验证，证明有效
2. 是每次工作都会用到的核心规范
3. 内容简洁（不超过200字），适合放入主文档
4. 不与master-soul.md现有规则冲突

提升方式：通过merge-protocol.md的安全检查后，合并到master-soul.md对应章节。

---

*此文件将在SOP积累过程中持续更新。*
