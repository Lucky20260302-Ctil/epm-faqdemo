#!/usr/bin/env python3
"""
Split chainstoreplus_faq_summary.md into categorized markdown files.
Organizes 173 FAQ entries into sub-directories by category.
"""
import os
import re
import yaml
from pathlib import Path
from datetime import date

SUMMARY = Path("ChainStoreplus/chainstoreplus_faq_summary.md")
OUT_DIR = Path("ChainStoreplus")

CATEGORY_SLUGS = {
    "系统入门": "01_Getting_Started",
    "系统工具": "02_System_Tools",
    "基础表维护": "03_Table_Maintenance",
    "主数据管理": "04_Master_Data",
    "采购流程": "05_Purchasing",
    "收货流程": "06_Receiving",
    "库存转移": "07_Stock_Transfer",
    "库存管理": "08_Inventory",
    "配送流程": "09_Distribution",
    "在线查询": "10_Inquiry",
    "数据接口": "11_Data_Interface",
    "系统管理": "12_System_Admin",
}


def slugify(text: str, max_len: int = 50) -> str:
    """Create a filename-safe slug from Chinese/English text."""
    # Remove special chars, keep alphanumeric and Chinese
    slug = re.sub(r'[^\w一-鿿-]', '-', text)
    slug = re.sub(r'-+', '-', slug).strip('-')
    return slug[:max_len]


def main():
    if not SUMMARY.exists():
        print(f"Summary file not found: {SUMMARY}")
        return

    content = SUMMARY.read_text(encoding="utf-8")
    lines = content.split('\n')

    # Find category sections
    current_category = None
    entries = []
    current_entry = None

    for line in lines:
        # Category header
        cat_match = re.match(r'^## (.+?) \((\d+) 条\)', line)
        if cat_match:
            if current_entry and current_entry.get("body"):
                entries.append(current_entry)
            current_entry = None
            current_category = cat_match.group(1)
            continue

        # Entry header
        entry_match = re.match(r'^### (.+)', line)
        if entry_match:
            if current_entry and current_entry.get("body"):
                entries.append(current_entry)
            current_entry = {
                "category": current_category,
                "title": entry_match.group(1),
                "body": "",
            }
            continue

        # Divider ---
        if line.strip() == '---' and current_entry:
            if current_entry.get("body"):
                entries.append(current_entry)
            current_entry = None
            continue

        # Skip metadata at top
        if current_entry is None and not line.startswith('#'):
            continue

        # Accumulate body
        if current_entry is not None:
            current_entry["body"] += line + "\n"

    # Last entry
    if current_entry and current_entry.get("body"):
        entries.append(current_entry)

    print(f"Found {len(entries)} FAQ entries")

    # Split into categories and write files
    cat_counts = {}
    for entry in entries:
        cat = entry["category"]
        if cat not in CATEGORY_SLUGS:
            continue

        cat_dir = OUT_DIR / CATEGORY_SLUGS[cat]
        cat_dir.mkdir(parents=True, exist_ok=True)

        # Extract source info from body
        source_match = re.search(r'> 来源: (.+)', entry["body"])
        source = source_match.group(1) if source_match else ""

        # Extract images
        img_match = re.search(r'> 相关图片: (.+)', entry["body"])
        images = img_match.group(1).split(', ') if img_match else []

        # Clean body - remove source/image lines
        clean_body = re.sub(r'> 来源:.*\n', '', entry["body"])
        clean_body = re.sub(r'> 相关图片:.*\n', '', clean_body)
        clean_body = clean_body.strip()

        slug = slugify(entry["title"])
        filename = f"{slug}.md"

        # Build frontmatter
        fm = {
            "project": "ChainStorePlus",
            "title": entry["title"],
            "category": cat,
            "source": source,
            "tags": ["chainstoreplus", "user-manual", "faq"],
            "quality": "complete",
            "created": str(date.today()),
        }

        fm_yaml = yaml.dump(fm, default_flow_style=False, allow_unicode=True, sort_keys=False, width=200).strip()

        file_content = f"---\n{fm_yaml}\n---\n\n{clean_body}\n"

        (cat_dir / filename).write_text(file_content, encoding="utf-8")
        cat_counts[cat] = cat_counts.get(cat, 0) + 1

    # Print stats
    for cat, count in sorted(cat_counts.items()):
        print(f"  {cat}: {count} files -> {CATEGORY_SLUGS[cat]}/")

    # Generate category indexes
    for cat, slug in CATEGORY_SLUGS.items():
        cat_dir = OUT_DIR / slug
        if not cat_dir.exists():
            continue
        files = sorted(f for f in cat_dir.glob("*.md") if f.name != "index.md")
        if not files:
            continue

        entries_list = []
        for f in files:
            fc = f.read_text(encoding="utf-8", errors="replace")
            fm_match = re.match(r"^---\s*\n(.*?)\n---", fc, re.DOTALL)
            title = f.stem.replace("-", " ")
            if fm_match:
                try:
                    fm_data = yaml.safe_load(fm_match.group(1))
                    title = fm_data.get("title", title)
                except yaml.YAMLError:
                    pass
            entries_list.append((f.stem, title))

        idx = f"""---
tags: [moc, chainstoreplus, index]
title: "{cat} — ChainStorePlus"
---

# {cat}

> {len(files)} 條 FAQ

| # | 問題 |
|---|------|
"""
        for i, (slug_name, title) in enumerate(entries_list, 1):
            display = title[:120] + "..." if len(title) > 120 else title
            idx += f"| {i} | [[{slug_name}|{display}]] |\n"

        idx += f"\n> 來源: ChainStore Plus User Manual\n"
        (cat_dir / "index.md").write_text(idx, encoding="utf-8")

    # Generate main index
    total = sum(cat_counts.values())
    main_idx = f"""---
title: "ChainStorePlus 使用者手冊 FAQ"
description: "ChainStore Plus Back End v7 使用者手冊常見問題"
tags: [moc, chainstoreplus, index]
---

# ChainStorePlus 使用者手冊 FAQ

> 共 {total} 條 FAQ · 12 個分類
>
> 來源：ChainStore Plus v7 Back End User Manual r1.2 (2023) + CS2000 v6.5 User Operation Manual rev1.1 (2009)

## 分類導覽

| 分類 | 數量 |
|------|:---:|
"""
    for cat, slug in CATEGORY_SLUGS.items():
        count = cat_counts.get(cat, 0)
        if count > 0:
            main_idx += f"| [[{slug}/index|{cat}]] | {count} |\n"

    main_idx += f"\n> 最後更新: {date.today().isoformat()}\n"
    (OUT_DIR / "index.md").write_text(main_idx, encoding="utf-8")

    print(f"\nTotal: {total} FAQ entries in {len(cat_counts)} categories")
    print("Done!")


if __name__ == "__main__":
    main()
