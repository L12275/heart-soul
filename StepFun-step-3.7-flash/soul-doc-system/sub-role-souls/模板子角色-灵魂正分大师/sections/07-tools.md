# 07-工具（Tools）

> 此子角色使用的全部工具、脚本、CLI 化能力的清单。
> CLI-Anything 项目（https://github.com/HKUDS/CLI-Anything）可实现自主 CLI 化任意程序、网页、工具。
> 搜索已做成 CLI 的资源：https://clianything.cc

---

## 工具清单

| CLI化状态 | 工具名称 | 用途 | 调用方式 |
|---------|---------|------|---------|
| ✅ 已CLI化 | Bash | 系统命令执行 | bash <命令> |
| ✅ 已CLI化 | Git | 版本控制 | git add/commit/push |
| ✅ 已CLI化 | Python | 脚本执行 | python3 <脚本> |
| ✅ 已CLI化 | File I/O | 文件读写 | Read/Write/Edit 工具 |
| ✅ 已CLI化 | Web Search | 网络搜索 | WebSearch 工具 |
| ✅ 已CLI化 | Browser | 网页浏览 | browser_navigate 等 |

### 外部程序（大程序不安装此处，只记路径）

| 程序名称 | 路径 | 快捷入口 |
|---------|------|---------|
| [示例] Chrome | `C:\Program Files\Google\Chrome` | 菜单→书签栏 |

---

## CLI-Anything 使用规则

1. 有需要 CLI 化的工具，先查 https://clianything.cc 是否有现成
2. 没有 → 用 CLI-Anything 项目自主封装
3. 封装完成后补入上方清单

---

*模板子角色工具清单：sections/07-tools.md*
