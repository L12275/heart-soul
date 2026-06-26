# 网页生成与管理 — 通用功能模块模板

> **网页项目的设计、开发、部署全流程管理。**
> 当六环/多驱动区需要网页生产功能时，复制本文件夹到目标位置拼搭使用。

## 文件夹结构

```
网页生成与管理/
├── README.md          ← 本文件
├── templates/         ← 网页模板（HTML/CSS/JS骨架）
├── projects/          ← 进行中的网页项目
├── assets/            ← 共享资源（图片/字体/样式库）
├── deploy/            ← 部署配置和脚本
└── 工具链.md          ← 推荐工具链（构建/部署/托管）
```

## templates/ — 网页模板

预定义的网页骨架，按类型分类：

| 类型 | 用途 | 技术栈 |
|------|------|--------|
| landing/ | 落地页 | HTML+CSS |
| dashboard/ | 数据面板 | HTML+JS+Chart |
| blog/ | 博客/文章 | Markdown→HTML |
| docs/ | 文档站 | Markdown→HTML |
| app/ | 单页应用 | HTML+JS+CSS |

## projects/ — 进行中的项目

每个项目独立文件夹：

```
projects/
└── [项目名]/
    ├── src/          ← 源代码
    ├── config/       ← 配置文件
    ├── output/       ← 输出文件（部署用）
    ├── notes.md      ← 项目笔记
    └── status.md     ← 当前状态
```

## assets/ — 共享资源

```
assets/
├── images/           ← 图片资源
├── fonts/            ← 字体文件
├── styles/           ← CSS框架和主题
└── libs/             ← JS库（jQuery/React/Vue等）
```

## deploy/ — 部署配置

```
deploy/
├── config.json       ← 部署配置（目标URL/认证/环境变量）
├── deploy.sh         ← 部署脚本
└── rollback.sh       ← 回滚脚本
```

## 工具链

### 开发工具
- **HTML/CSS**: 原生或 Tailwind CSS
- **JS**: 原生或按需引入框架
- **构建**: 根据项目复杂度选择（简单项目无需构建）

### 部署选项
- **静态托管**: GitHub Pages / Gitee Pages / Vercel / Netlify
- **FTP**: 传统服务器部署
- **Git Push**: 自动触发部署

### 推荐流程
1. 在 `templates/` 选择最接近的模板
2. 在 `projects/` 下创建项目文件夹
3. 基于模板开发，使用 `assets/` 中的共享资源
4. 完成在 `output/` 中生成最终文件
5. 通过 `deploy/` 中的脚本部署

---
*网页生成与管理 功能模块*
*创建时间：2026-06-25*

---
*最后更新：2026-06-26 17:52*
