# Agents/memory — 说明

> **本目录不直接存储内容。**
> Agent 运行记忆使用通用区的记忆模块和日记模块，按需拼搭。

## 使用方式

1. Agent 运行时，在目标工作文件夹下创建 `memory/` 和 `diary/`
2. 从通用区 `memory/`（soul-doc-system/memory/）复制需要的模块文件
3. 从通用区 `diary/` 复制需要的模板文件
4. Agent 在自身工作区的 memory/ 和 diary/ 中维护运行记忆

## 拼搭示例

```
目标工作文件夹/
├── memory/
│   ├── context/
│   │   ├── L0.md    ← 从通用区 memory/context/L0.md 复制
│   │   ├── L1.md    ← 从通用区 memory/context/L1.md 复制
│   │   └── ...
│   └── daily/
│       └── YYYY/MM/DD/  ← 按日期创建
├── diary/
│   ├── README.md    ← 从通用区 diary/README.md 复制
│   └── YYYY/MM/DD/  ← 按日期创建
```

**完整拼搭SOP**：见 `../../../../../../sop/通用功能模块自主灵活拼搭组建自定义工作文件夹SOP示例.md`

---
*Agents/memory 说明*
*创建时间：2026-06-25*

---
*最后更新：2026-06-26 21:18*
