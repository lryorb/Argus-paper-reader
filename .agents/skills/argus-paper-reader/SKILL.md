---
name: argus-paper-reader
description: 阿耳戈斯学术论文双栏双语逻辑精读器 (Argus Paper Reader)。当用户需要精读实证或理论学术论文、解构论证骨架与潜在逻辑漏洞、生成按段落严格对齐的英中双语对照 HTML、五维透镜高亮（Thesis/Concept/Evidence/Rebuttal/Method）及三层批判性学术批注时触发此技能。
---

# Argus Paper Reader (阿耳戈斯学术论文双栏双语逻辑精读器)

> **设计哲学**：取名自古希腊神话中的百眼巨人**阿耳戈斯 (Argus Panoptes)**，其拥有一百只眼睛，睡眠时仅闭上数只，余者洞察四方。在学术研究中，Argus 象征着**以审稿人（Referee）的严苛与全视视角，透视学术论文的论证骨架、修辞策略、因果识别设计与底层逻辑漏洞**。

---

## 适用场景 (Trigger Scenarios)
- 研读中英文学术论文（尤其是经济学、金融学、管理学、实证社会科学、因果推断等实证类文献）。
- 组会研读、学术文献报告（Reading Report）、博士生文献精读与文献综述。
- 审稿人（Peer Review）同行评审推演、论文答辩与论证缺陷审判。
- 用户要求：“请帮我把这篇论文生成双语对照网页”、“深度解析这篇论文的论证逻辑”、“帮我用 Argus 精读这篇文献”。

---

## 核心分析体系

### 1. Argus Five-Lens (五维高亮标注体系)
在左栏英文正文中使用 HTML `<mark>` 标签注入五维透镜：
```html
<mark class="hl hl-{dim}" data-dim="{dim}" data-label="{label}">English Text</mark>
```
- **`thesis` (核心论点, 琥珀金黄)**：中心假说、核心因果命题、重大学术发现与理论贡献。
- **`concept` (关键概念, 绯红玫瑰)**：新提出的理论构念、操作化核心变量定义、中介/调节概念。
- **`evidence` (实证证据, 湖水湛蓝)**：关键计量回归系数、统计检验 $p$ 值、效应量大小、样本基准事实。
- **`rebuttal` (让步反驳, 翡翠草绿)**：作者的主动让步、对备选解释（Alternative Explanations）的排除、适用边界。
- **`method` (方法论, 罗兰紫罗)**：识别策略（DID / IV / RDD / PSM）、计量模型设定、数据筛选与反事实构造。

### 2. 顶级期刊排版与学术级中文意译
- **刊头与工具栏**：采用庄重的学术期刊刊头（Journal Masthead）布局，搭配一体化毛玻璃吸顶工具栏（Unified Sticky Glass Toolbar），随页面滚动自由切换五维透镜与阅读视图。
- **纯净双语对照**：左栏下半部的中文翻译达到《经济研究》、《管理世界》、《中国社会科学》等顶级期刊发表标准；中文译文与批注中的专有名词统一采用直角引号 `「...」` 或中文双引号 `“...”`，严禁单引号。默认模式下直接呈现干净译文（无生硬标签行扰乱视线），在“折叠译文”模式下提供整条点击热区与 `▸ 展开中文译文` 按钮。
- **数学公式增强**：针对块级公式 `$$...$$` 嵌套于 `<mark>` 标签的场景，自动识别并升格为公式高亮卡片（`.hl-block`），确保紫色/金黄等高亮边框和悬浮标签（停靠右上角）完美呈现。

### 3. 右栏逐段三层批判性批注 (Three-Tier Critical Commentary)
每个自然段右侧必须配置结构化评注卡片：
1. **① 段落功能 (Paragraph Function)**：胶囊徽章标示（如：`引出核心问题`、`构建理论假说`、`计量模型设定`、`基准实证发现`、`让步与异议排除` 等）。
2. **② 逻辑角色 (Logical Role)**：阐释该段在全文逻辑骨架中的空间定位与承上启下连接作用。
3. **③ 论证解剖 (Argus Gaze)**：
   - **✦ 论证设计与修辞**：解构作者巧妙的修辞策略、外生性铺陈或直觉构建。
   - **⚑ 潜在漏洞与审稿质疑**：从资深审稿人视角的致命挑刺（遗漏变量、反向因果、弱工具变量、排他性约束破缺、样本选择偏差、外部有效性局限）。

### 4. 底部论证全局复盘仪表盘 (Synthesis Dashboard)
- **全文逻辑骨架**：横向 6 阶段可视化链条：`问题 (Question) → 论点 (Thesis) → 方法 (Method) → 证据 (Evidence) → 反驳 (Rebuttal) → 结论 (Conclusion)`。
- **核心主张（Core Thesis）**：醒目提炼全篇最具穿透力的核心因果命题。
- **核心方法论优势 vs. 阿喀琉斯之踵（识别软肋）**：左右对称对比卡片。

---

## 严格执行工作流 (Standard Workflow)

### 步骤 1：文本解析与段落切分 (Strict Paragraph Alignment)
- **严禁遗漏或合并任何自然段**！每一个自然段都必须独立作为一个 `.para-row` 处理。
- 保留原文中的数学公式，规范为标准 KaTeX 格式（行内 `$x_i$`，块级 `$$y_i = \beta x_i + \varepsilon_i$$`）。

### 步骤 2：五维透镜标注与学术意译
- 依据 `resources/annotation-rubric.md` 进行英文正文 `<mark>` 高亮注入。
- 输出高质量学术级中文意译。

### 步骤 3：构建逐段批注与全局复盘
- 撰写每段的三层批注卡片（段落功能、逻辑角色、Argus Gaze 技巧与漏洞）。
- 撰写底部仪表盘数据（6步骨架流、一句话论点、最强处与最弱处）。

### 步骤 4：编译生成独立自包含 HTML 页面
优先生成符合结构的中间 JSON 文件，并运行内置打包脚本：
```bash
python3 .agents/skills/argus-paper-reader/scripts/build_html.py --input <data.json> --output <paper.html>
```

#### JSON 数据契约格式：
```json
{
  "meta": {
    "title": "论文完整英文标题",
    "authors": "作者列表 (如: Daron Acemoglu, Simon Johnson, James A. Robinson)",
    "year": "发表年份 (如: 2001)",
    "venue": "发表期刊/会议 (如: American Economic Review)",
    "doi": "可选 DOI",
    "url": "可选原文链接"
  },
  "sections": [
    {
      "id": "sec-1",
      "title": "1. 章节标题",
      "desc": "可选简短章节概述",
      "paragraphs": [
        {
          "index": 1,
          "dominant_dimension": "thesis",
          "en": "英文正文，内含 <mark class=\"hl hl-thesis\" data-dim=\"thesis\" data-label=\"核心假说\">...</mark> 标签及 LaTeX 公式",
          "zh": "中文学术意译...",
          "annotation": {
            "function": "引出核心问题与假说",
            "logical_role": "确立全篇因果检验的逻辑起点...",
            "gaze": {
              "technique": "通过历史因果故事与反事实对照建立经济学直觉...",
              "vulnerability": "早期殖民者定居死亡率数据的历史测量误差可能传导至第二阶段估计..."
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
      "title": "论证最强处 / Core Methodological Strength",
      "content": "..."
    },
    "achilles_heel": {
      "title": "阿喀琉斯之踵 / Critical Achilles' Heel",
      "content": "..."
    }
  }
}
```

> **无 Python 环境降级策略**：若运行环境不支持 Python，直接读取 `resources/template.html`，将各区块替换为生成的 HTML 结构后直接输出为单文件 HTML。

---

## 资源索引
- [标注与分析规范指南 (annotation-rubric.md)](file:///./resources/annotation-rubric.md)
- [HTML5 高级视图模板 (template.html)](file:///./resources/template.html)
- [Python 渲染构建脚本 (build_html.py)](file:///./scripts/build_html.py)
