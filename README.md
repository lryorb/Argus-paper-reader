<div align="center">

# 👁️ Argus-paper-reader

**阿耳戈斯学术论文双栏双语逻辑精读器**  
*All-Seeing Academic Paper Logic Reader & Dual-Column Bilingual Annotator Skill*

[![License: MIT](https://img.shields.io/badge/License-MIT-0f1e36?style=for-the-badge)](https://github.com/lryorb/Argus-paper-reader/blob/main/LICENSE-MIT)
[![Content: CC0-1.0](https://img.shields.io/badge/Content-CC0--1.0-c59b27?style=for-the-badge)](https://github.com/lryorb/Argus-paper-reader/blob/main/LICENSE-CC0)
[![Compatible: Antigravity | Claude Code | Codex](https://img.shields.io/badge/Compatible-Antigravity%20%7C%20Claude%20Code%20%7C%20Codex-0284c7?style=for-the-badge)](https://github.com/lryorb/Argus-paper-reader)
[![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-16a34a?style=for-the-badge)](https://github.com/lryorb/Argus-paper-reader/blob/main/CONTRIBUTING.md)

<p>
  <strong>百眼全视，洞察学术论文的论证骨架与逻辑漏洞</strong><br>
  <em>Transforming linear literature reading into spatialized argumentative mapping with five-lens spotlighting and referee-grade critique.</em>
</p>

[在线示例 Demo](examples/argus_demo_paper.html) • [安装指南 Installation](#-安装指南--installation) • [五维透镜 Five-Lens](#-核心特性--key-features) • [贡献指南 Contributing](CONTRIBUTING.md) • [安全策略 Security](SECURITY.md)

</div>

---

## 🏛️ 项目缘起 / The Myth of Argus Panoptes

在古希腊神话中，**阿耳戈斯（Argus Panoptes）** 是拥有一百只眼睛的“全视巨人”——即使在沉睡时，也永远睁着数十只眼睛警惕地洞察四方。

传统的 PDF 线性精读往往让人陷入“只见词句、不见骨架”的泥淖，极易忽略作者隐蔽的内生性前提或修辞陷阱。**`Argus-paper-reader`** 将百眼巨人的全视隐喻注入 AI 科研工作流，把传统的线性阅读重构为**“五维透镜高亮 + 逐段中英精译 + 审稿人视角三层解剖”**的空间化论证映射（Spatialized Argumentative Mapping），帮助研究者在几分钟内看穿一篇顶刊论文的逻辑铁律与「阿喀琉斯之踵」。

> In Greek mythology, **Argus Panoptes** is the all-seeing hundred-eyed giant who never closes all his eyes at once. `Argus-paper-reader` brings this unblinking referee gaze into modern academic workflows—transforming dense empirical and theoretical papers into **Five-Lens Highlighting + Idiomatic Bilingual Paraphrasing + Three-Tier Referee Critique** in a single standalone, print-ready HTML5 reader.

---

## ✨ 核心特性 / Key Features

### 🏛️ Editorial Journal Masthead（顶级期刊刊头质感）
- 汲取 *American Economic Review (AER)* 与 *The Economist* 刊头灵感：深海军蓝（`#0f1e36`）品牌刊头 + 暖米白纸张底色（`#faf8f5`）+ 浮雕米色卡片。
- 英文正文采用 `Lora` 衬线体（`1.05rem` / `1.78` 行高），中文采用思源宋体 `Noto Serif SC`，标点严格遵从学术书卷风格（直角引号 `「...」` / 标准中文双引号 `“...”`），杜绝单引号与杂乱标签噪音。
- 配备一体化毛玻璃吸顶工具栏（Unified Sticky Glass Toolbar），单行防挤压保护，长文章节横向滚轮顺滑穿梭，锚点跳转自带 `scroll-margin-top` 防遮挡。

### 🔬 Argus Five-Lens Spotlight（五维聚光灯联动 + 快捷键 `0-5`）
点击工具栏图例或按下键盘数字键 **`0`–`5`**，即可激活**左右双栏聚光灯联动（Cross-Column Spotlight）**：命中段落的高亮文本与右栏对应批注卡片同步外发光呼应，非相关段落自动淡出降噪（Opacity 降至 `0.42`，悬停恢复 `0.9`）。

| 快捷键 | 维度 ID (`data-dim`) | 视觉色彩 | 语义类别 | 判定标准与双栏联动机制 |
| :---: | :--- | :--- | :--- | :--- |
| **`0`** | `all` | 海军蓝 (`#0f1e36`) | 全部维度 (Show All) | 解除聚光灯过滤，恢复全文全部五维高亮与双栏全亮态 |
| **`1`** | **`thesis`** | 琥珀金黄 (`#fef3c7` / `#d97706`) | 核心论点 (Thesis) | 中心因果假说、主要理论发现、贡献声明；联动命中右栏金边发光卡片 |
| **`2`** | **`concept`** | 绯红玫瑰 (`#ffe4e6` / `#e11d48`) | 关键概念 (Concept) | 专属理论构念、操作化变量界定、中介/调节构念；联动命中右栏绯红卡片 |
| **`3`** | **`evidence`** | 湖水湛蓝 (`#e0f2fe` / `#0284c7`) | 实证证据 (Evidence) | 回归估计系数、统计显著性（$p$ 值、标准误）、基准事实；联动命中右栏湛蓝卡片 |
| **`4`** | **`rebuttal`** | 翡翠草绿 (`#dcfce7` / `#16a34a`) | 让步反驳 (Rebuttal) | 排除备选解释、前置让步、排他性约束边界讨论；联动命中右栏翠绿卡片 |
| **`5`** | **`method`** | 罗兰紫罗 (`#f3e8ff` / `#9333ea`) | 方法论 (Methodology) | 因果识别策略（DID / IV / RDD）、计量方程设定、反事实构造；联动命中右栏紫罗卡片 |

### 📐 Paragraph-Pair Grid & KaTeX Native（严格逐段对齐与原生公式高亮）
- **永不漂移的段落矩阵**：严禁左右独立长列造成的错位。每一自然段构成一个独立的 `.para-row`（桌面端 `7fr : 5fr`，移动端自适应单栏堆叠）。
- **KaTeX 块级公式自适应卡片**：原生集成带 SRI 哈希校验的 KaTeX CDN，行内（`$...$`）与块级（`$$...$$`）公式自动渲染。当块级公式嵌套在 `<mark>` 高亮标签中时，自动升格为 `.hl-block` 独立色边公式卡片，悬浮维度微标精准停靠右上角，彻底杜绝底边断裂与文字遮挡。
- **右栏三层解剖卡片**：
  1. `① 段落功能`：胶囊徽章提炼段落核心修辞动作；
  2. `② 逻辑角色`：精准定位该段在全文论证骨架中的承上启下作用；
  3. `③ 论证解剖 (Argus Gaze)`：拆解为 **✦ 论证设计与修辞** 与 **⚑ 潜在漏洞与审稿质疑** 双面透镜。

### 🔄 Three-Mode View Switcher（三模态阅读视图切换）
- **`双语对照`**：英文原文（含五维高亮）+ 极细分隔线 + 顶级中文期刊水准意译（干净无彩色干扰）。
- **`仅看英文`**：一键隐藏中文块，专注原汁原味英文精读与右栏批注思考。
- **`折叠译文`**：隐藏多余分隔线，将译文收起为整条可点击展开的浅米色热区（点击任意位置即可展开，展开后仅点击左上角收起按钮折叠，不影响划词复制）。

### 🧭 Bottom Synthesis Dashboard（底部全局复盘仪表盘）
- **全文逻辑骨架**：横向 6 阶段箭头流程图呈现 $\text{问题 (Question)} \rightarrow \text{论点 (Thesis)} \rightarrow \text{方法 (Method)} \rightarrow \text{证据 (Evidence)} \rightarrow \text{反驳 (Rebuttal)} \rightarrow \text{结论 (Conclusion)}$。
- **核心主张（Core Thesis）**：大字号引文卡片提炼作者最本质的命题。
- **核心方法论优势 vs. 阿喀琉斯之踵（识别软肋）**：左右对称对比卡片，凝练全篇最坚实的设计支柱与最易遭拒稿的底层隐患。

---

## 📊 在线预览与示例 / Live Demo

仓库在 `examples/` 目录下内置了实证经济学里程碑文献的完整精读演示：
- **示例文献**：Daron Acemoglu, Simon Johnson, & James A. Robinson (2001), *"The Colonial Origins of Comparative Development: An Empirical Investigation"*, *American Economic Review*, 91(5), 1369–1401.
- **演示文件**：[`examples/argus_demo_paper.html`](examples/argus_demo_paper.html)（对应结构化数据：[`examples/demo_data.json`](examples/demo_data.json)）
- **直接体验**：克隆或下载本仓库后，用任意现代浏览器（Chrome / Safari / Edge / Firefox）双击打开 `examples/argus_demo_paper.html` 即可离线体验全套交互、KaTeX 公式高亮卡片与键盘快捷键 `0`–`5`。

---

## 🚀 安装指南 / Installation

### 1. 克隆仓库 / Clone Repository
```bash
git clone https://github.com/lryorb/Argus-paper-reader.git
cd Argus-paper-reader
```

### 2. 在 Google Antigravity 中加载 / Load in Google Antigravity
将本 Skill 文件夹复制或软链接至当前工作区的 `.agents/skills/` 目录（或全局技能目录 `~/.gemini/antigravity/skills/`）：
```bash
# 工作区级加载（推荐）
mkdir -p /path/to/your-workspace/.agents/skills/argus-paper-reader
cp -r .agents/skills/argus-paper-reader/* /path/to/your-workspace/.agents/skills/argus-paper-reader/
```
加载后，只需在对话中向 Antigravity 下达指令：
> *“请用 Argus 阅读器精读这篇论文 PDF，并生成双栏双语逻辑批注 HTML”*

### 3. 在 Claude Code / Codex 中加载 / Load in Claude Code & Codex
本项目遵循标准 Agent Skill（`SKILL.md` YAML frontmatter + `resources/` + `scripts/`）规范，可直接复制到 Claude Code 或 Codex 的全局技能目录：
```bash
# Claude Code 全局安装示例
mkdir -p ~/.claude/skills/argus-paper-reader
cp -r .agents/skills/argus-paper-reader/* ~/.claude/skills/argus-paper-reader/
```

### 4. 手动命令行构建 / Manual CLI Build
内置构建脚本 [`scripts/build_html.py`](.agents/skills/argus-paper-reader/scripts/build_html.py) **零第三方 Python 依赖**（仅使用标准库）：
```bash
python3 .agents/skills/argus-paper-reader/scripts/build_html.py \
  --input examples/demo_data.json \
  --output output_paper.html
```

---

## 📂 仓库结构 / Repository Structure

```text
Argus-paper-reader/
├── .agents/skills/argus-paper-reader/
│   ├── SKILL.md                      # Skill 核心规范与工作流定义 (YAML frontmatter)
│   ├── resources/
│   │   ├── template.html             # 自包含 HTML5/CSS/JS 单文件渲染模板
│   │   └── annotation-rubric.md      # Argus 五维透镜、意译与三层批注分析准则
│   └── scripts/
│       └── build_html.py             # 零依赖 Python 构建与公式/标点安全处理脚本
├── examples/
│   ├── demo_data.json                # AJR (2001, AER) 示范结构化 JSON 数据
│   └── argus_demo_paper.html         # 完整编译的独立 HTML5 演示文件
├── CODE_OF_CONDUCT.md                # Contributor Covenant 行为准则
├── CONTRIBUTING.md                   # 学科拓展与 PR 贡献指南
├── LICENSE                           # MIT 主开源协议 (Copyright 2026 lryorb)
├── LICENSE-MIT                       # MIT 开源协议文本（代码与工具链）
├── LICENSE-CC0                       # CC0 1.0 公共领域奉献协议（规范与输出物）
├── SECURITY.md                       # 隐私架构与安全漏洞响应策略
├── .gitignore                        # Git 忽略配置
└── README.md                         # 中英双语说明文档
```

---

## ⚖️ 双协议声明 / Dual License Notice

本项目采取**代码与学术内容分离的双轨开源协议（Dual Licensing）**，以最大限度保障开发复用与学术共享自由：

- **代码与构建工具链遵循 [`MIT License`](LICENSE-MIT)**（`Copyright (c) 2026 lryorb`）：适用于 `scripts/build_html.py`、`resources/template.html` 中的前端交互 JavaScript/CSS 以及所有工程脚本。
- **学术标注规范与输出成果遵循 [`CC0 1.0 Universal`](LICENSE-CC0)**：适用于 `resources/annotation-rubric.md`、JSON 数据模式以及您使用本工具生成的全部 HTML 精读笔记与批注文档——任何学者均可零限制地将其用于课堂研讨、组会分享、科研笔记或公开发表，无需额外署名负担。

> **Summary**: Software & build scripts are licensed under **[MIT](LICENSE-MIT)**; annotation rubrics, JSON schemas, and user-generated HTML outputs are dedicated to the public domain under **[CC0-1.0](LICENSE-CC0)** for unrestricted academic use.
