# Git 合流（Git Tree Convergence）

> 多模型、多分支的 git 历史管理与远程仓库推送。
> 合流 = 多个分支的精华汇总到主分支。

---

## 文件夹结构

```
git-tree/
├── convergence/ ← 合流记录（哪些分支合并了什么）
├── history/ ← git 提交历史
└── remotes/ ← 远程仓库信息
```

---

## 推送规则

| 操作 | 规则 |
|------|------|
| 模型推送 | 只推送自己隔离区的稳定版 |
| 中央内容 | 由维护者决定是否推送 |
| 其他模型 | 不管，他们自己推 |
| 不稳定版 | 不推送，避免污染 |

## 远程仓库

- GitHub: https://github.com/L12275/heart-soul
- Gitee: https://gitee.com/L12275/heart-soul

*使用说明：如果克隆仓库自用，可把远程仓库地址改成你自己的。*

---

*git-tree：soul-doc-system/git-tree/README.md*
*创建时间：2026-06-23*
