#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Argus Paper Reader - HTML Builder Script
========================================
Compiles structured paper JSON data into a standalone, high-aesthetic HTML5 reader.
Zero third-party dependencies (Python standard library only).

Usage:
    python build_html.py --input data.json --output paper.html
    python build_html.py -i data.json -o paper.html --template custom_template.html
"""

import os
import sys
import json
import argparse
from pathlib import Path


def escape_html(text: str) -> str:
    """Escapes HTML special characters, except for already formatted tags."""
    if not text:
        return ""
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
        .replace("'", "&#39;")
    )


def render_sections_nav(sections, synthesis_data=None) -> str:
    """Generates the sticky section navigation bar anchors."""
    nav_items = []
    for idx, sec in enumerate(sections, 1):
        sec_id = sec.get("id", f"sec-{idx}")
        sec_title = sec.get("title", f"Section {idx}")
        nav_items.append(
            f'<a class="nav-anchor-item" href="#{sec_id}">'
            f'<span class="sec-idx">{idx:02d}.</span>{sec_title}'
            f"</a>"
        )

    if synthesis_data:
        nav_items.append(
            '<a class="nav-anchor-item" href="#sec-synthesis">'
            '<span class="sec-idx">✦</span>论证总览 Dashboard'
            "</a>"
        )

    return "\n      ".join(nav_items)


def render_body_content(sections) -> str:
    """Renders all sections and paragraph-pair grids."""
    section_blocks = []

    for s_idx, sec in enumerate(sections, 1):
        sec_id = sec.get("id", f"sec-{s_idx}")
        sec_title = sec.get("title", f"Section {s_idx}")
        sec_desc = sec.get("desc", "")

        rows_html = []
        for p in sec.get("paragraphs", []):
            p_idx = p.get("index", 1)
            dominant_dim = p.get("dominant_dimension", "thesis").lower()
            en_content = p.get("en", "").strip()
            zh_content = p.get("zh", "").strip()
            ann = p.get("annotation", {})

            func_text = ann.get("function", "核心论点阐述")
            role_text = ann.get("logical_role", "承前启后")
            gaze = ann.get("gaze", {})
            tech_text = gaze.get("technique", "精妙的修辞与理论铺陈")
            vuln_text = gaze.get("vulnerability", "审稿人视角下的潜在识别偏差")

            # Paragraph row template
            row = f"""
      <div class="para-row" id="p-{p_idx}">
        <!-- Left Cell: English Original + Chinese Translation -->
        <div class="para-left">
          <div class="para-badge">¶ {int(p_idx):02d}</div>
          <div class="en-content">{en_content}</div>
          <hr class="para-divider">
          <div class="trans-block">
            <div class="trans-header">
              <span>中文学术意译 (Top Journal Style)</span>
              <button class="trans-toggle-pill" type="button">展开译文</button>
            </div>
            <div class="trans-content">{zh_content}</div>
          </div>
        </div>

        <!-- Right Cell: Three-Tier Commentary Card -->
        <div class="para-right">
          <div class="annotation-card" data-dominant="{dominant_dim}">
            <!-- Tier 1: Paragraph Function -->
            <div class="card-tier">
              <div class="tier-header">
                <svg class="tier-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/></svg>
                ① 段落功能
              </div>
              <span class="func-capsule func-{dominant_dim}">
                {func_text}
              </span>
            </div>

            <!-- Tier 2: Logical Role -->
            <div class="card-tier">
              <div class="tier-header">
                <svg class="tier-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg>
                ② 逻辑角色
              </div>
              <div class="role-desc">
                {role_text}
              </div>
            </div>

            <!-- Tier 3: Argus Gaze -->
            <div class="card-tier">
              <div class="tier-header">
                <svg class="tier-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/></svg>
                ③ Argus Gaze（论证技巧与潜在漏洞）
              </div>
              <div class="argus-gaze-box">
                <div class="gaze-subitem gaze-technique">
                  <div class="gaze-subhead">
                    <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
                    论证技巧 / Rhetoric & Design
                  </div>
                  <div class="gaze-text">{tech_text}</div>
                </div>
                <div class="gaze-subitem gaze-vulnerability">
                  <div class="gaze-subhead">
                    <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>
                    潜在漏洞 / Reviewer Vulnerability
                  </div>
                  <div class="gaze-text">{vuln_text}</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
"""
            rows_html.append(row)

        desc_html = f'<div class="section-desc">{sec_desc}</div>' if sec_desc else ""
        section_blocks.append(f"""
    <section class="section-block" id="{sec_id}">
      <div class="section-header">
        <h2 class="section-title">{sec_title}</h2>
        {desc_html}
      </div>
      <div class="section-content">
        {"".join(rows_html)}
      </div>
    </section>
""")

    return "\n".join(section_blocks)


def render_synthesis_dashboard(synthesis) -> str:
    """Renders the Bottom Synthesis Dashboard."""
    if not synthesis:
        return ""

    # 1. Pipeline nodes
    pipeline_items = []
    skeleton = synthesis.get("logic_skeleton", [])
    for idx, node in enumerate(skeleton, 1):
        step = node.get("step", f"Step {idx}")
        title = node.get("title", "")
        desc = node.get("desc", "")
        pipeline_items.append(f"""
        <div class="skeleton-node">
          <div class="skeleton-step-tag">{step}</div>
          <div class="skeleton-node-title">{title}</div>
          <div class="skeleton-node-desc">{desc}</div>
        </div>
""")

    pipeline_html = "".join(pipeline_items)

    # 2. Core thesis
    core_thesis = synthesis.get("core_thesis", "")

    # 3. Strength & Achilles Heel
    strength = synthesis.get("strength", {})
    achilles = synthesis.get("achilles_heel", {})

    str_title = strength.get("title", "论证最强处 / Core Methodological Strength")
    str_content = strength.get("content", "")

    ach_title = achilles.get("title", "阿喀琉斯之踵 / Critical Achilles' Heel")
    ach_content = achilles.get("content", "")

    return f"""
      <div class="dashboard-header">
        <div class="dashboard-title-group">
          <h2 class="dashboard-title">论证结构与批判性复盘 (Synthesis Dashboard)</h2>
          <span class="dashboard-badge">ARGUS PANOPTES REVIEW</span>
        </div>
      </div>

      <!-- Logic Skeleton Pipeline -->
      <div class="skeleton-section">
        <div class="sub-section-title">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 12h-4l-3 9L9 3l-3 9H2"/></svg>
          全文逻辑骨架流 (Logic Pipeline)
        </div>
        <div class="skeleton-pipeline">
          {pipeline_html}
        </div>
      </div>

      <!-- One-Sentence Core Thesis Callout -->
      <div class="thesis-callout-card">
        <div class="thesis-callout-quote-icon">&ldquo;</div>
        <div class="thesis-callout-label">作者核心主张一句话版本 / One-Sentence Core Thesis</div>
        <div class="thesis-callout-text">{core_thesis}</div>
      </div>

      <!-- Strength vs. Achilles' Heel Comparison Grid -->
      <div class="critique-grid">
        <div class="critique-card card-strength">
          <div class="critique-title-row">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="M9 12l2 2 4-4"/></svg>
            <span>{str_title}</span>
          </div>
          <div class="critique-body">
            {str_content}
          </div>
        </div>

        <div class="critique-card card-achilles">
          <div class="critique-title-row">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>
            <span>{ach_title}</span>
          </div>
          <div class="critique-body">
            {ach_content}
          </div>
        </div>
      </div>
"""


def build_argus_html(data_path: Path, output_path: Path, template_path: Path = None):
    """Main compilation routine."""
    if not data_path.exists():
        raise FileNotFoundError(f"Input JSON data file not found: {data_path}")

    # Determine default template location if not supplied
    if template_path is None:
        script_dir = Path(__file__).resolve().parent
        candidate_paths = [
            script_dir.parent / "resources" / "template.html",
            script_dir / "template.html",
            Path.cwd() / ".agents" / "skills" / "argus-paper-reader" / "resources" / "template.html",
            Path.cwd() / "resources" / "template.html"
        ]
        for cp in candidate_paths:
            if cp.exists():
                template_path = cp
                break

    if template_path is None or not template_path.exists():
        raise FileNotFoundError(f"Template file not found. Checked candidate paths.")

    print(f"[Argus] Loading template from: {template_path}")
    template_str = template_path.read_text(encoding="utf-8")

    print(f"[Argus] Loading data from: {data_path}")
    with open(data_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    meta = data.get("meta", {})
    title = meta.get("title", "Academic Paper Analysis")
    authors = meta.get("authors", "Anonymous Authors")
    year = meta.get("year", "")
    venue = meta.get("venue", "")
    year_venue = f"{year} · {venue}" if (year and venue) else (year or venue or "Academic Paper")

    extra_meta_html = ""
    if "doi" in meta:
        doi = meta["doi"]
        extra_meta_html += f'<div class="paper-meta-item"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg><span>DOI: {doi}</span></div>'
    if "url" in meta:
        extra_meta_html += f'<div class="paper-meta-item"><a href="{meta["url"]}" target="_blank" style="color:inherit;text-decoration:underline;">[Paper Link]</a></div>'

    sections = data.get("sections", [])
    synthesis = data.get("synthesis", {})

    # Generate fragments
    nav_html = render_sections_nav(sections, synthesis)
    body_html = render_body_content(sections)
    synthesis_html = render_synthesis_dashboard(synthesis)
    raw_json_str = json.dumps(data, ensure_ascii=False, indent=2)

    # Perform placeholder replacements
    html = template_str
    html = html.replace("<!-- ARGUS_PAGE_TITLE -->", title)
    html = html.replace("<!-- ARGUS_PAPER_TITLE -->", title)
    html = html.replace("<!-- ARGUS_AUTHORS -->", authors)
    html = html.replace("<!-- ARGUS_YEAR_VENUE -->", year_venue)
    html = html.replace("<!-- ARGUS_EXTRA_META -->", extra_meta_html)
    html = html.replace("<!-- ARGUS_SECTIONS_NAV -->", nav_html)
    html = html.replace("<!-- ARGUS_BODY_CONTENT -->", body_html)
    html = html.replace("<!-- ARGUS_SYNTHESIS_DASHBOARD -->", synthesis_html)
    html = html.replace("<!-- ARGUS_RAW_DATA_SCRIPT -->", raw_json_str)

    # Ensure parent output dir exists
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(html, encoding="utf-8")
    print(f"[Argus] Successfully built standalone HTML: {output_path} ({len(html.encode('utf-8'))} bytes)")


def main():
    parser = argparse.ArgumentParser(
        description="Argus Paper Reader: Compile structured academic paper JSON into standalone HTML reader."
    )
    parser.add_argument(
        "-i", "--input",
        required=True,
        type=Path,
        help="Path to the input JSON file containing paper metadata, sections, and annotations."
    )
    parser.add_argument(
        "-o", "--output",
        required=True,
        type=Path,
        help="Path to the output HTML file."
    )
    parser.add_argument(
        "-t", "--template",
        default=None,
        type=Path,
        help="Optional path to custom template.html. Defaults to resources/template.html."
    )

    args = parser.parse_args()
    build_argus_html(args.input, args.output, args.template)


if __name__ == "__main__":
    main()
