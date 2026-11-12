# Security Policy / 安全策略

## 🔒 隐私与架构安全声明 (Privacy & Architecture Security)

**`Argus-paper-reader`** 深知学术界对**未发表手稿（Unpublished Manuscripts）**、**工作论文（Working Papers）**及**盲审稿件（Confidential Peer-Review Drafts）**的极端隐私诉求，因此本项目的架构从底层遵循「零服务器数据留存」原则：

1. **纯静态本地单文件输出**：
   - 本工具渲染生成的 `.html` 阅读器为**完全本地化、纯静态的单文件（Standalone Single-File HTML5）**。
   - **零后端请求、零分析遥测（Telemetry）**：页面内部不包含任何统计追踪脚本、第三方上报接口或外部 API 调用，绝不会将您的任何文献文本、译文或批注笔记上传至远程服务器。
   - **受控且带完整性校验的外部资源**：仅在页面渲染时通过 HTTPS 加载字体库（Google Fonts）以及官方 **KaTeX v0.16.9 CDN**（且全部 `<link>` 与 `<script>` 均配置了严格的 **SRI Subresource Integrity 哈希校验** `integrity="sha384-..."` 与 `crossorigin="anonymous"`，防止供应链篡改）；即使在完全断网的离线环境下打开，核心文本、双语对照与交互逻辑依然可正常运行。

2. **构建脚本安全 (`scripts/build_html.py`)**：
   - **零第三方依赖**：`scripts/build_html.py` 仅使用 Python 官方标准库（`os`、`re`、`sys`、`json`、`argparse`、`pathlib`），不依赖任何外部 PyPI 包，彻底杜绝第三方依赖投毒与供应链风险。
   - **XSS 注入防御**：在将结构化论文 JSON 数据嵌入 `<script id="argus-raw-data" type="application/json">` 时，脚本会自动对 `</` 序列进行安全转义（替换为 `<\/`），防止论文原文中的特殊字符或恶意构造内容提前闭合 `<script>` 标签引发 DOM XSS 漏洞。

---

## 🚨 支持的版本 (Supported Versions)

| 版本 (Version) | 安全维护状态 (Supported) |
| :--- | :--- |
| `main` (v1.x) | :white_check_mark: 持续维护中 |

---

## 📬 漏洞反馈渠道 (Reporting a Vulnerability)

如果您在使用过程中发现任何安全隐患（例如 HTML/JSON 注入绕过、XSS 漏洞或模板逻辑缺陷），**请勿在公开 Issue 中直接披露未修复的漏洞利用细节**。

请通过 GitHub 官方加密安全通道向项目维护者私密报告：
- **GitHub Security Advisories**: [https://github.com/lryorb/Argus-paper-reader/security/advisories](https://github.com/lryorb/Argus-paper-reader/security/advisories)

我们将在收到报告后的 **48 小时内**予以响应与确认，并在验证修复后发布安全更新公告及致谢。
