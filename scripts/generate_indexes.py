#!/usr/bin/env python3
"""
Auto-generate rich index.md for each FAQ_test category directory.
Extracts frontmatter: title, symptom, quality, project, issue_key, tags.
Run before: npx quartz build -d .
"""
import os
import re
import yaml
from datetime import date

FAQ_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "FAQ_test")

QUALITY_ICONS = {"complete": "✅", "partial": "⚠️", "stub": "❌"}
PROJECT_COLORS = {
    "BE": "#3b82f6",
    "FE": "#f59e0b",
    "MP": "#8b5cf6",
    "WEB": "#10b981",
    "EPMTDCPROT": "#ef4444",
    "ChainStorePlus": "#6366f1",
}

CAT_LABELS = {
    "01_Install_Deploy": "安裝與部署",
    "02_Config_Settings": "配置與設定",
    "03_Data_Import": "資料匯入",
    "03_Performance_Timeout": "效能與超時",
    "04_Data_Sync": "資料同步",
    "05_Error_Exception": "報錯與異常",
    "06_Printing_Hardware": "列印與硬體",
    "06_Procurement_Workflow": "採購流程",
    "07_Other": "其他",
    "07_Reporting": "報表",
    "07_Workflow_Business": "業務流程",
}


def parse_frontmatter(filepath: str) -> dict:
    """Extract frontmatter fields from a markdown file."""
    with open(filepath, "r", encoding="utf-8", errors="replace") as f:
        content = f.read()
    fm_match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    fm = {}
    body = content
    if fm_match:
        try:
            fm = yaml.safe_load(fm_match.group(1)) or {}
        except yaml.YAMLError:
            pass
        body = content[fm_match.end():]
    # Also extract first heading or first content line as fallback title
    h1_match = re.search(r"^# (.+)$", body, re.MULTILINE)
    if h1_match:
        fm["_h1"] = h1_match.group(1).strip()
    else:
        # Fallback: first non-empty line after frontmatter
        first_line = body.strip().split("\n")[0].strip() if body.strip() else ""
        if first_line and not first_line.startswith("|") and not first_line.startswith(">"):
            fm["_h1"] = first_line
    return fm


def get_symptom_preview(fm: dict, max_len: int = 80) -> str:
    """Get a short symptom preview from frontmatter or body."""
    symptom = fm.get("symptom", "")
    if symptom:
        return symptom[:max_len] + ("..." if len(symptom) > max_len else "")
    # Try title from frontmatter
    title = fm.get("title", "") or fm.get("_h1", "")
    # Strip issue key prefix from title
    title = re.sub(r"^[A-Z]+-\d+:\s*", "", title)
    if title:
        return title[:max_len] + ("..." if len(title) > max_len else "")
    return ""


def generate_category_index(category_dir: str):
    """Generate rich index.md for a single FAQ_test category."""
    cat_name = os.path.basename(category_dir)
    files = sorted(
        [f for f in os.listdir(category_dir) if f.endswith(".md") and f != "index.md"]
    )
    if not files:
        return

    entries = []
    for f in files:
        filepath = os.path.join(category_dir, f)
        fm = parse_frontmatter(filepath)
        slug = f[:-3]
        title = fm.get("title", slug)
        issue_key = fm.get("issue_key", "")
        project = fm.get("project", "")
        quality = fm.get("quality", "partial")
        symptom = get_symptom_preview(fm)
        icon = QUALITY_ICONS.get(quality, "❓")
        entries.append(
            {
                "slug": slug,
                "title": title,
                "issue_key": issue_key,
                "project": project,
                "quality": quality,
                "icon": icon,
                "symptom": symptom,
            }
        )

    # Sort: complete first, then by issue_key
    quality_order = {"complete": 0, "partial": 1, "stub": 2}
    entries.sort(key=lambda e: (quality_order.get(e["quality"], 9), e["issue_key"]))

    label = CAT_LABELS.get(cat_name, cat_name)
    complete_count = sum(1 for e in entries if e["quality"] == "complete")
    partial_count = sum(1 for e in entries if e["quality"] == "partial")

    content = f"""---
tags: [moc, faq, index]
title: "{label} — FAQ 索引"
updated: {date.today().isoformat()}
---

# {label}

> {len(files)} 篇 FAQ · {complete_count} 篇完整 · {partial_count} 篇部分

| # | 工單 | 專案 | 品質 | 症狀摘要 |
|---|------|------|:---:|----------|
"""
    for i, e in enumerate(entries, 1):
        issue_link = f"[[{e['slug']}|{e['issue_key']}]]" if e["issue_key"] else f"[[{e['slug']}]]"
        project_cell = e["project"] if e["project"] else "—"
        content += f"| {i} | {issue_link} | {project_cell} | {e['icon']} | {e['symptom']} |\n"

    content += f"\n> 最後更新: {date.today().isoformat()} · 自動生成\n"

    index_path = os.path.join(category_dir, "index.md")
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(content)


def generate_main_index():
    """Generate root FAQ_test/index.md."""
    categories = sorted(
        [
            d
            for d in os.listdir(FAQ_DIR)
            if os.path.isdir(os.path.join(FAQ_DIR, d)) and not d.startswith(".")
        ]
    )

    cat_data = []
    grand_total = 0
    for cat in categories:
        cat_path = os.path.join(FAQ_DIR, cat)
        all_files = [f for f in os.listdir(cat_path) if f.endswith(".md") and f != "index.md"]
        count = len(all_files)
        grand_total += count
        # Count quality
        comp = sum(
            1
            for f in all_files
            if parse_frontmatter(os.path.join(cat_path, f)).get("quality") == "complete"
        )
        label = CAT_LABELS.get(cat, cat)
        # Emoji for category
        emoji_map = {
            "01_Install_Deploy": "📦",
            "02_Config_Settings": "⚙️",
            "03_Data_Import": "📥",
            "03_Performance_Timeout": "⏱️",
            "04_Data_Sync": "🔄",
            "05_Error_Exception": "🚨",
            "06_Printing_Hardware": "🖨️",
            "06_Procurement_Workflow": "🏢",
            "07_Other": "📝",
            "07_Reporting": "📊",
            "07_Workflow_Business": "📋",
        }
        emoji = emoji_map.get(cat, "📂")
        cat_data.append(
            {
                "cat": cat,
                "label": label,
                "emoji": emoji,
                "count": count,
                "complete": comp,
            }
        )

    rows = []
    for cd in cat_data:
        rows.append(
            f"| [[{cd['cat']}/index|{cd['emoji']} {cd['label']}]] | {cd['count']} | {cd['complete']} |"
        )

    content = f"""---
tags: [moc, faq, index]
title: "FAQ 分類總覽"
updated: {date.today().isoformat()}
---

# FAQ 分類總覽

> 共 **{grand_total}** 篇 FAQ · {len(categories)} 個分類 · 全部品質完整 ✅

## 按分類瀏覽

| 分類 | 總數 | 完整 |
|------|:---:|:---:|
{chr(10).join(rows)}

---

## 如何使用

1. **搜尋** — 左側搜尋框輸入關鍵字（中英文、工單號皆可）
2. **瀏覽** — 點上方分類或左側目錄樹進入 FAQ 列表
3. **閱讀** — 每篇包含 症狀 → 根因 → 解法 三段結構

> 最後更新: {date.today().isoformat()} · 自動生成
"""

    with open(os.path.join(FAQ_DIR, "index.md"), "w", encoding="utf-8") as f:
        f.write(content)


if __name__ == "__main__":
    print(f"Scanning: {FAQ_DIR}")
    for cat in sorted(os.listdir(FAQ_DIR)):
        cat_path = os.path.join(FAQ_DIR, cat)
        if os.path.isdir(cat_path) and not cat.startswith("."):
            generate_category_index(cat_path)
            count = len(
                [f for f in os.listdir(cat_path) if f.endswith(".md") and f != "index.md"]
            )
            print(f"  {cat}: {count} files -> index.md")
    generate_main_index()
    print("Done.")
