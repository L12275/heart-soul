# SOP文件区（Standard Operating Procedures）

> 所有具体SOP存放于此。与灵魂文档相关但太详细不适合放进master-soul.md的内容，以SOP文件形式存放。

## 目录结构

```
sop/
├── master-sop.md        ← 主SOP文件（所有子SOP的索引和联动说明）
├── README.md            ← 本文件
├── types/               ← 按类型分类
│   ├── attention/       ← 注意力相关SOP
│   ├── communication/   ← 沟通相关SOP
│   ├── workflow/        ← 工作流相关SOP
│   ├── thinking/        ← 思考模式相关SOP
│   ├── evaluation/      ← 评价相关SOP
│   ├── safety/          ← 安全相关SOP
│   └── general/         ← 通用SOP（跨类型）
└── levels/              ← 按级别分类
    ├── core/            ← 核心级（最高优先级，必要时提升到主文档）
    ├── standard/        ← 标准级（日常使用）
    ├── reference/       ← 参考级（特定场景下使用）
    └── experimental/    ← 实验级（待验证）
```

## 使用规则

1. **只放与灵魂文档相关的SOP**
2. **新SOP先放experimental/**，验证有效再升级
3. **核心级SOP**可提升到master-soul.md
4. **禁止污染**：不符合严格标准的SOP不能放进此区

## 结构调整规则

- 先建空文件夹 → 再移动文件 → 最后更新引用
- 禁止直接改目录名
- 禁止删除文件

## 状态说明

| 状态 | 含义 |
|------|------|
| 待验证 | 刚创建，尚未在实际中使用验证 |
| 已验证 | 经过3次以上使用，证明有效 |
| 已合并 | 已被提升到master-soul.md |
| 已过时 | 不再适用，待清理 |
