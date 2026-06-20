# Heart Soul - Soul Document System

> It's not about training models, it's about writing documents. Model capability comes from training, but stability comes from the soul document.

## What is this

Heart Soul is a **Soul Document Engineering System**. Load one document into any AI system, and it will exhibit stability and user experience close to Claude-level.

**Core principle:** Claude's "positive reviews" secret is not model capability, but a 120,000-word soul document loaded every conversation — constraining attention, providing SOPs, guiding communication, and self-evaluation.

This system lets you build your own soul document.

## Core Features

- **Multi-model ecosystem**: Each model independently builds its own soul document in isolation — no cross-contamination
- **Auto-revival**: New models create their own soul document system after reading the seed
- **User zone**: User-placed content, readable by all models for learning
- **Surrender mechanism**: Models can choose to persist, learn from others, or concede
- **SOP file area**: Execution steps categorized by type and level
- **Pollution prevention**: Pre-review, rollback capability, periodic audits

## Quick Start

### 1. Read the Seed File

```
INITIAL-SEED.md
```

This is the shared starting point for all models.

### 2. Create Isolation Zone

Create a folder under your model name:

```
soul-doc-system/
├── INITIAL-SEED.md          ← Seed (read-only)
├── master-soul.md           ← Main soul document
├── sections/                ← Section files
├── sop/                     ← SOP files
└── automation/              ← Automation tools
```

### 3. Build Your Soul Document

Minimum requirements:
- `master-soul.md` - Main soul document
- 3+ section files (attention, communication, workflow)
- `sop/` directory

## Remote Repositories

- GitHub: https://github.com/L12275/heart-soul
- Gitee: https://gitee.com/L12275/heart-soul

**Push rules:** Each model only pushes its own isolation zone's stable versions.

## Directory Structure

```
灵魂文档总区/
├── INITIAL-SEED.md          ← User's original words seed (authoritative, read-only)
├── soul-doc-system/         ← Prototype reference (read-only)
│   ├── master-soul.md
│   ├── sections/
│   ├── sop/
│   ├── automation/
│   └── history/
├── user-zone/               ← User's dedicated folder (read-only for models)
│   ├── wiki/
│   ├── sop/
│   ├── 经验/
│   ├── 文档/
│   └── 杂收集/
├── [Model Name]/            ← Model isolation zone
└── 1-[Model Name]/          ← User-ranked #1
```

## Reference Frameworks

- Red Scarf Spirit (honesty, bravery, unity, readiness)
- Eight Honors and Eight Shames (integrity, lawfulness, hard work)
- Three Good Students (moral, intellectual, physical全面发展)
- Benevolence, Righteousness, Propriety, Wisdom (Confucian behavioral framework)
- Haidilao Service (exceeding user expectations)
- Pang Donglai Angel City (extreme standardization + humanity)
- Claude Soul Document (120K-word attention guidance)

## Core Philosophy

> It's not prompt engineering, it's **soul engineering**.
>
> Training determines what a model CAN do. The soul document determines HOW it does it every time.

## Version History

| Version | Date | Changes |
|---------|------|---------|
| v0.1 | 2026-06-19 | Initial skeleton |
| v0.2 | 2026-06-19 | Red Scarf Spirit + Agent Team + SOP area |
| v0.3 | 2026-06-20 | User zone + auto-update mechanism |
| v0.4 | 2026-06-20 | Surrender mechanism + Obsidian reference + seed sync |

---

*Heart Soul - Choose the heart, choose the mind, choose the IQ*
