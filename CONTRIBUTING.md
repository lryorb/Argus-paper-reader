# Contributing to Argus-paper-reader

首先感谢您关注并考虑为 **`Argus-paper-reader`** 贡献力量！无论您是经济学家、计算机学者、生物医学研究员，还是前端/Agent 工程师，都欢迎通过 Issue 与 Pull Request 共同打造更锐利的学术文献解析体验。

---

## 🐛 报告 Bug (Reporting Bugs)

在提交 [GitHub Issue](https://github.com/lryorb/Argus-paper-reader/issues) 时，请尽量附上复现所需的最小上下文，尤其是以下高频场景：

1. **特殊 LaTeX 宏包与公式渲染异常**：
   - 本阅读器前端采用原生 **KaTeX**（v0.16.9）渲染 `$...$` 与 `$$...$$`。若遇到自定义宏（如 `\mathbbm{1}`、`\argmax`、复杂 `align*` 或 TikZ 图表环境）报错或 `<mark>` 嵌套错位：
   - 请附上原始 LaTeX 文本片段、`demo.json` 对应字段及浏览器控制台错误截图。
2. **长文献分块与自然段切分问题**：
   - 若遇到跨页表格、脚注或长篇文献被 Agent 误合并、漏段的情况，请说明 PDF 解析来源及触发 Prompt。
3. **标点清理冲突**：
   - 若在极端多语混排或化学式/代码片段中发生标点规范化误伤，请直接提供触发字符串。

---

## 📚 为不同学科扩充标注规范 (`annotation-rubric.md`)

`Argus Five-Lens` 默认对实证经济学、金融学与社会科学进行了深度优化，我们非常欢迎为其他学科贡献专属 `annotation-rubric` 变体或补充规则：

- **计量经济学 / 因果推断**：细化 DID（平行趋势检验、交错 DID 异质性处理效应）、IV（排他性约束、LATE 解释）、RDD（局部随机化、操纵检验）的批注提示词库。
- **计算机科学 / AI & Systems**：
  - `method` $\rightarrow$ 模型架构（Transformer 变体、损失函数、系统瓶颈优化）
  - `evidence` $\rightarrow$ Ablation Study（消融实验）、Scaling Law 指标、Latency/Throughput 基准对比
  - `rebuttal` $\rightarrow$ 计算复杂度局限、超参敏感性、潜在数据泄露风险
- **生物医学 / 临床试验**：
  - `method` $\rightarrow$ RCT 随机对照分组、盲法设计、样本量效能计算、多组学测序管线
  - `evidence` $\rightarrow$ 风险比（HR）、置信区间（CI）、Kaplan-Meier 曲线、$p$-value 校正
  - `rebuttal` $\rightarrow$ 混杂因素（Confounders）、失访偏误（Attrition Bias）、体外到体内外推局限

> 修改时请直接编辑 `.agents/skills/argus-paper-reader/resources/annotation-rubric.md` 或在 `resources/` 下提供学科参考模块，并在 `SKILL.md` 中说明触发条件。

---

## 🎨 调整 CSS 主题与视觉样式 (`template.html`)

所有的视觉色调、字体栈与五维透镜颜色均集中声明在 `.agents/skills/argus-paper-reader/resources/template.html` 顶部的 `:root` CSS 变量中：

- **期刊基础色板**：`--color-navy` (`#0f1e36`)、`--color-paper` (`#faf8f5`)、`--color-trans-bg` (`#f0ece2`)
- **五维透镜变量**：`--lens-{dim}-bg`、`--lens-{dim}-border`、`--lens-{dim}-text`
- **自定义建议**：如果您想贡献“暗黑模式（Dark Editorial Mode）”、“极简打印模式”或针对移动端的折叠优化，请在修改 `template.html` 后，务必重新编译 `examples/argus_demo_paper.html` 验证公式与交互是否完整工作。

---

## 🔀 标准提交流程 (Fork -> Branch -> PR)

1. **Fork 本仓库**：点击右上角 Fork 至您的 GitHub 账号。
2. **创建特性分支**：
   ```bash
   git checkout -b feat/your-feature-name
   # 或修复类分支：
   git checkout -b fix/issue-description
   ```
3. **本地开发与自测**：
   - 运行构建脚本验证更改无报错且零外部依赖：
     ```bash
     python3 .agents/skills/argus-paper-reader/scripts/build_html.py \
       --input examples/demo_data.json \
       --output examples/argus_demo_paper.html
     ```
   - 在浏览器中检查双栏对齐、KaTeX 公式、快捷键 `0`–`5` 聚光灯联动及“折叠译文”交互。
4. **提交 Commit**（建议遵循 Conventional Commits 规范）：
   ```bash
   git add .
   git commit -m "feat(rubric): add biomedical RCT critique guidelines"
   ```
5. **推送并发起 Pull Request**：
   ```bash
   git push origin feat/your-feature-name
   ```
   随后在 GitHub 上开启 Pull Request，简要说明修改动机与测试结果。

---

## ⚖️ 协议约定

提交代码贡献即代表您同意：工程脚本与前端代码采用 **[MIT License](LICENSE-MIT)** 发布，标注规范与示例数据采用 **[CC0-1.0](LICENSE-CC0)** 奉献至公共领域。
