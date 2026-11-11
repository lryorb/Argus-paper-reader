# Argus-paper-reader (阿耳戈斯学术论文双栏双语逻辑精读器)

<p align="center">
  <img src="https://img.shields.io/badge/Argus-Panoptes%20v1.0-0f1e36?style=for-the-badge&logoColor=white" alt="Argus Version" />
  <img src="https://img.shields.io/badge/Compatibility-Google%20Antigravity%20%7C%20Claude%20Code-0284c7?style=for-the-badge" alt="Compatibility" />
  <img src="https://img.shields.io/badge/Standard-Agent%20Skill%20%26%20Standalone%20HTML5-16a34a?style=for-the-badge" alt="Standard" />
  <img src="https://img.shields.io/badge/License-MIT-d97706?style=for-the-badge" alt="License" />
</p>

<p align="center">
  <strong>百眼全视，洞察学术论文的论证骨架与逻辑漏洞</strong><br>
  <em>All-Seeing Insight into Argumentative Skeletons and Methodological Vulnerabilities</em>
</p>

---

## 📖 项目简介 (Introduction)

**`Argus-paper-reader`** 是一款专为学术研究人员、研究生与审稿人设计的 AI Agent Skill。项目名称源自古希腊神话中拥有百只眼睛的“全视巨人”**阿耳戈斯（Argus Panoptes）**——在神话中，他睡眠时仅闭上数只眼，余者时刻警惕地洞察四周。

在学术文献研读中，**Argus 象征着一种永不闭合的审稿人（Referee）洞察力**：不仅带你精读论文的表面文字，更能穿透修辞迷雾，解构论文深层的因果推断骨架、理论机制假说，并从顶级期刊匿名审稿人的挑剔视角，一针见血地指出其潜在的内生性疑虑、遗漏变量与外部有效性局限。

本项目兼容 **Google Antigravity (`.agents/skills/`)** 以及 **Claude Code / Codex** 规范，具备零外部 Python 依赖的渲染打包工具链，一键输出单文件自包含、高审美期刊级排版的交互式 HTML 精读报告。

---

## ✨ 核心特性 (Key Features)

### 1. 顶级学术期刊审美与交互系统 (Editorial Academic Design)
- **色调与排版**：深海军蓝（`#0f1e36`）顶部控制台 + 暖米白纸张底色（`#faf8f5`）+ 浮雕米色卡片，还原经典《美国经济评论》(AER) 等期刊纸质质感。
- **字体与排版**：正文采用经典衬线体 `Lora`（1.05rem / 1.78 行高），中文采用思源宋体 `Noto Serif SC`，UI 采用 `IBM Plex Sans`。
- **公式支持**：原生集成 **KaTeX CDN** 引擎，完美支持复杂行内与块级数学公式自动排版（`$...$` 与 `$$...$$`）。
- **顶栏交互功能**：
  - **阅读进度条 (Reading Progress Bar)**：实时跟随滚动感知全局阅读位置。
  - **五维透镜聚光灯 (Five-Lens Spotlight Filter)**：支持一键聚焦高亮特定维度，其余维度自动降低透明度（0.22 灰度降噪）。
  - **多视图模式 (View Switcher)**：一键切换 `双语对照`、`仅看英文` 与 `折叠译文（支持逐段单独展开）`。
  - **吸顶章节锚点导航 (Sticky Section Nav)**：结合 `IntersectionObserver` 自动高亮当前所在章节。

### 2. Argus Five-Lens（五维高亮标注体系）
在左栏英文正文中使用精准的 `<mark>` 胶囊高亮，悬浮即可触发交互微标签：

| 维度 ID (`data-dim`) | 视觉色彩 | 语义类别 | 识别对象与触发判定 |
| :--- | :--- | :--- | :--- |
| **`thesis`** | 琥珀金黄 (`#fef3c7` / `#d97706`) | 核心论点 (Thesis) | 中心假说、核心因果命题、重大学术发现与理论贡献 |
| **`concept`** | 绯红玫瑰 (`#ffe4e6` / `#e11d48`) | 关键概念 (Concept) | 核心理论构念、操作化变量界定、中介与调节机制定义 |
| **`evidence`** | 湖水湛蓝 (`#e0f2fe` / `#0284c7`) | 实证证据 (Evidence) | 计量回归估计系数、统计显著性 ($p$ 值、标准误)、效应量 |
| **`rebuttal`** | 翡翠草绿 (`#dcfce7` / `#16a34a`) | 让步反驳 (Rebuttal) | 排除备选解释、前置让步、适用边界条件、稳健性检验 |
| **`method`** | 罗兰紫罗 (`#f3e8ff` / `#9333ea`) | 方法论 (Methodology) | 因果识别策略 (DID / IV / RDD)、计量模型设定、数据反事实构建 |

### 3. 按段落严格对齐的左右双栏布局 (Paragraph-Pair Grid)
- **严禁独立长列导致的阅读错位**：全篇以自然段为基本单元，每个自然段为一个独立的 `.para-row` 容器（桌面端 `7fr : 5fr`，移动端自适应堆叠）。
- **左单元格（英中双语对照）**：
  - 上半部：英文原文 + 五维透镜高亮。
  - 分隔线：`1px solid #e2ddd3` 极细分隔线。
  - 下半部：**学术级中文意译**（采用《经济研究》、《管理世界》发表标准，彻底剔除机翻腔，中文块保持干净无彩色高亮）。
- **右单元格（三层批判性学术批注卡片）**：
  1. `① 段落功能`：胶囊徽章标识（如：引出核心问题、计量模型设定、让步与异议排除等）。
  2. `② 逻辑角色`：说明该段在整体论证链条中的承上启下位置。
  3. `③ Argus Gaze（百眼凝视：论证技巧与潜在漏洞）`：
     - **论证技巧 (Technique & Rhetoric)**：解构作者高超的叙事修辞、外生性铺垫或识别设计。
     - **潜在漏洞 (Vulnerability & Critique)**：从资深审稿人视角指出识别假设、排他性约束、测量误差或外推局限。

### 4. 底部论证全局复盘仪表盘 (Bottom Synthesis Dashboard)
- **全文逻辑骨架流 (Logic Pipeline)**：可视化 6 阶段论证链条：
  $$\text{问题 (Question)} \rightarrow \text{论点 (Thesis)} \rightarrow \text{方法 (Method)} \rightarrow \text{证据 (Evidence)} \rightarrow \text{反驳 (Rebuttal)} \rightarrow \text{结论 (Conclusion)}$$
- **作者核心主张一句话版本 (One-Sentence Core Thesis)**：引文卡片提炼核心因果命题。
- **论证最强处 vs. 阿喀琉斯之踵 (Strength vs. Achilles' Heel)**：左右对称对比卡片，提炼论文最具穿透力的学术贡献与最脆弱的致命软肋。

---

## 📂 仓库目录结构 (Repository Structure)

```text
Argus-paper-reader/
├── .agents/
│   └── skills/
│       └── argus-paper-reader/
│           ├── SKILL.md                     # Skill 核心定义文件 (含 YAML frontmatter 与执行规范)
│           ├── resources/
│           │   ├── template.html            # 高审美、自包含的 HTML5 视图模板 (内置 CSS/JS)
│           │   └── annotation-rubric.md     # 五维透镜规范、学术意译与三层批注标准
│           └── scripts/
│               └── build_html.py            # Python 单文件构建脚本 (零第三方外部依赖)
├── examples/
│   ├── demo_data.json                       # 经典论文 (AJR 2001) 实证片段结构化数据
│   └── argus_demo_paper.html                # 编译生成的演示 HTML 文件 (开箱即看)
├── LICENSE                                  # MIT 开源许可证
└── README.md                                # 中英双语项目说明文档
```

---

## 🚀 安装与配置 (Installation & Setup)

### 方式一：在 Google Antigravity 中使用
将本技能克隆或复制到当前工作区或全局 Agent 技能目录中：
```bash
# 复制至当前项目的工作区技能目录：
mkdir -p .agents/skills/argus-paper-reader
cp -r path/to/Argus-paper-reader/.agents/skills/argus-paper-reader/* .agents/skills/argus-paper-reader/

# 或放入全局配置目录：
# ~/.gemini/antigravity/skills/argus-paper-reader/
```
Antigravity 会自动发现并索引 `argus-paper-reader`。当您对 Antigravity 说：
> *“请用 Argus 阅读器帮我精读这篇 PDF/论文”* 或 *“帮我生成这篇文章的双栏双语逻辑精读 HTML”*

系统将自动触发该 Skill 工作流。

### 方式二：在 Claude Code / Codex 中使用
将 Skill 目录链接或复制到 Claude Code 的技能配置中：
```bash
mkdir -p ~/.claude/skills/argus-paper-reader
cp -r .agents/skills/argus-paper-reader/* ~/.claude/skills/argus-paper-reader/
```

---

## 🛠️ 使用与构建指南 (Usage Workflow)

### 1. 结构化 JSON 数据格式
您可以直接提供符合如下规范的 JSON 文件（例如 `examples/demo_data.json`）：

```json
{
  "meta": {
    "title": "论文标题 (Paper Title)",
    "authors": "作者列表",
    "year": "发表年份",
    "venue": "发表期刊或会议",
    "doi": "10.xxxx/xxxxx",
    "url": "https://..."
  },
  "sections": [
    {
      "id": "sec-1",
      "title": "1. 章节名称",
      "paragraphs": [
        {
          "index": 1,
          "dominant_dimension": "thesis",
          "en": "English text with <mark class=\"hl hl-thesis\" data-dim=\"thesis\" data-label=\"核心假说\">...</mark> and LaTeX $formula$",
          "zh": "中文学术意译...",
          "annotation": {
            "function": "引出核心问题与假说",
            "logical_role": "确立全篇因果检验的逻辑起点...",
            "gaze": {
              "technique": "通过历史因果故事与反事实对照建立直觉...",
              "vulnerability": "遗漏时变混杂因素的风险..."
            }
          }
        }
      ]
    }
  ],
  "synthesis": {
    "core_thesis": "作者核心主张一句话版本...",
    "logic_skeleton": [
      {"step": "问题 (Question)", "title": "...", "desc": "..."},
      {"step": "论点 (Thesis)", "title": "...", "desc": "..."},
      {"step": "方法 (Method)", "title": "...", "desc": "..."},
      {"step": "证据 (Evidence)", "title": "...", "desc": "..."},
      {"step": "反驳 (Rebuttal)", "title": "...", "desc": "..."},
      {"step": "结论 (Conclusion)", "title": "...", "desc": "..."}
    ],
    "strength": {
      "title": "论证最强处",
      "content": "..."
    },
    "achilles_heel": {
      "title": "阿喀琉斯之踵（最脆弱处）",
      "content": "..."
    }
  }
}
```

### 2. 命令行渲染打包 (Build CLI)
内置的 `build_html.py` 仅使用 Python 标准库，**无需 `pip install` 任何第三方包**：
```bash
python .agents/skills/argus-paper-reader/scripts/build_html.py \
  --input examples/demo_data.json \
  --output examples/argus_demo_paper.html
```
生成的 `.html` 文件是**完全自包含的单文件**，双击即可在任何浏览器（Chrome, Safari, Edge, Firefox）中离线或在线畅读，支持打印排版优化（`Ctrl+P`）。

---

## 📊 经典演示案例 (Demo Preview)

在 `examples/` 目录下提供了经典计量经济学文献的精读演示：
- **演示文献**：Acemoglu, Johnson, & Robinson (2001, *American Economic Review*), *"The Colonial Origins of Comparative Development: An Empirical Investigation"*
- **演示页面**：[examples/argus_demo_paper.html](file:///./examples/argus_demo_paper.html)
- **涵盖内容**：
  - 核心命题与历史工具变量（殖民者死亡率）的理论动机
  - 新欧洲型包容制度 vs. 掠夺型制度的二元机制
  - 2SLS 两阶段结构计量模型与数学公式设定（KaTeX）
  - 基准回归系数 $\hat{\alpha}=0.94$、弱工具变量排除与地理生态竞争假说的反驳
  - 审稿人视角下的排他性约束破缺疑虑与数据拼接问题

---

## 🤝 贡献与开源协议 (Contributing & License)

欢迎学术研究者、LLM 开发者提交 Issue 和 Pull Request，共同扩充更多学科维度的批注规则模板与渲染主题！

本项目基于 [MIT License](LICENSE) 开源发布。
