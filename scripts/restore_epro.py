#!/usr/bin/env python3
"""
Restore EPRO files from archive, fix formatting, move to top-level EPRO_System/.
- Fixes duplicate "FR-XXX-001: FR-XXX-001:" titles
- Converts raw tab-separated requirement format to clean Markdown
- Removes duplicate H1 (ArticleTitle component handles display)
- Creates proper category structure with clean names
- Generates EPRO index page
"""
import os
import re
import shutil
import yaml
from pathlib import Path
from datetime import date

ARCHIVE_DIR = Path("_archived_stubs")
EPRO_DIR = Path("EPRO_System")

CATEGORY_MAP = {
    "08_EPRO_System": ("01_General_Requirements", "General Requirements"),
    "09_EPRO_PreTender": ("02_PreTender", "Pre-Tender"),
    "10_EPRO_TenderStage": ("03_TenderStage", "Tender Stage"),
    "11_EPRO_PostTender": ("04_PostTender", "Post-Tender"),
    "12_EPRO_Supplier": ("05_Supplier", "Supplier"),
    "13_EPRO_Reports": ("06_Reports", "Reports"),
    "14_EPRO_Others": ("07_Others", "Others"),
}


def parse_raw_requirement(body: str) -> dict:
    """Parse the raw tab-separated requirement format into structured fields."""
    fields = {
        "description": "",
        "rationale": "",
        "acceptance": "",
        "dependencies": "",
        "tailoring": "",
        "change_history": "",
    }

    all_boundaries = [
        "Rationale:",
        "Acceptance / Fit Criteria:",
        "Acceptance/Fit Criteria:",
        "Dependencies:",
        "Tailoring Guidelines:",
        "Change History:",
    ]

    def find_section_end(text, exclude_boundaries=None):
        """Find the end of a section by looking for the next section boundary."""
        end_pos = len(text)
        for boundary in all_boundaries:
            if exclude_boundaries and boundary in exclude_boundaries:
                continue
            pos = text.find("\n" + boundary)
            if 0 <= pos < end_pos:
                end_pos = pos
        return text[:end_pos].strip()

    # Description
    desc_start = body.find("Description:")
    if desc_start >= 0:
        fields["description"] = find_section_end(body[desc_start + len("Description:"):])

    # Rationale
    ratio_start = body.find("Rationale:")
    if ratio_start >= 0:
        val = find_section_end(body[ratio_start + len("Rationale:"):],
                              exclude_boundaries=["Rationale:"])
        if val and val.lower() != "none":
            fields["rationale"] = val

    # Acceptance / Fit Criteria
    for marker in ["Acceptance / Fit Criteria:", "Acceptance/Fit Criteria:"]:
        acc_start = body.find(marker)
        if acc_start >= 0:
            val = find_section_end(body[acc_start + len(marker):],
                                  exclude_boundaries=["Acceptance / Fit Criteria:", "Acceptance/Fit Criteria:", "Rationale:"])
            if val:
                fields["acceptance"] = val
            break

    # Dependencies
    deps_start = body.find("Dependencies:")
    if deps_start >= 0:
        val = find_section_end(body[deps_start + len("Dependencies:"):],
                              exclude_boundaries=["Dependencies:", "Rationale:", "Acceptance / Fit Criteria:", "Acceptance/Fit Criteria:"])
        if val and val.lower() != "none":
            fields["dependencies"] = val

    # Tailoring
    tail_start = body.find("Tailoring Guidelines:")
    if tail_start >= 0:
        val = find_section_end(body[tail_start + len("Tailoring Guidelines:"):],
                              exclude_boundaries=["Tailoring Guidelines:", "Rationale:", "Acceptance / Fit Criteria:", "Acceptance/Fit Criteria:", "Dependencies:"])
        if val and val.lower() != "none":
            fields["tailoring"] = val

    # Change History
    ch_start = body.find("Change History:")
    if ch_start >= 0:
        val = body[ch_start + len("Change History:"):].strip()
        if val and val.lower() != "none":
            fields["change_history"] = val

    return fields


def fix_title(title: str) -> str:
    """Fix duplicate issue key in title: 'FR-GR-001: FR-GR-001: ...' -> 'FR-GR-001: ...'"""
    if not title:
        return title
    # Match pattern like "FR-GR-001: FR-GR-001: Rest of title" or "FR-GR-001:FR-GR-001:..."
    match = re.match(r"^([A-Z]+-[A-Z]+-\d+):\s*\1:\s*(.*)", title)
    if match:
        return f"{match.group(1)}: {match.group(2)}"
    # Also handle "ABC-123: ABC-123: ..." format
    match = re.match(r"^([A-Z]+-\d+):\s*\1:\s*(.*)", title)
    if match:
        return f"{match.group(1)}: {match.group(2)}"
    return title


def rebuild_epro_file(src_path: Path, dest_path: Path, category_label: str):
    """Read, fix, and write an EPRO file."""
    content = src_path.read_text(encoding="utf-8", errors="replace")

    # Parse frontmatter
    fm_match = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
    if not fm_match:
        return False

    try:
        fm = yaml.safe_load(fm_match.group(1)) or {}
    except yaml.YAMLError:
        fm = {}

    body = content[fm_match.end():]

    # Fix title
    old_title = fm.get("title", "")
    new_title = fix_title(str(old_title))

    # Extract issue key from title
    key_match = re.match(r"^([A-Z]+-\d+):", new_title)
    issue_key = key_match.group(1) if key_match else ""

    # Parse raw requirement format
    req_fields = parse_raw_requirement(body)

    # Build clean body
    clean_body = ""

    # Description
    if req_fields["description"]:
        clean_body += f"## 需求描述\n\n{req_fields['description']}\n\n"

    # Rationale
    if req_fields["rationale"]:
        clean_body += f"## 需求理由\n\n{req_fields['rationale']}\n\n"

    # Acceptance criteria
    if req_fields["acceptance"]:
        clean_body += f"## 驗收標準\n\n{req_fields['acceptance']}\n\n"

    # Dependencies
    if req_fields["dependencies"]:
        clean_body += f"## 依賴項\n\n{req_fields['dependencies']}\n\n"

    # Tailoring
    if req_fields["tailoring"]:
        clean_body += f"## 裁剪指南\n\n{req_fields['tailoring']}\n\n"

    if not clean_body:
        # Fallback: keep the original body minus the raw header
        clean_body = body.strip()

    # Build new frontmatter
    new_fm = {
        "project": "EPRO",
        "issue_key": issue_key,
        "issue_type": "Functional Requirement",
        "status": "Specified",
        "tags": ["epro", "functional-requirement", "spec"],
        "title": new_title,
        "quality": "complete",
        "category_label": category_label,
        "created": str(date.today()),
    }

    new_fm_yaml = yaml.dump(new_fm, default_flow_style=False, allow_unicode=True, sort_keys=False, width=200).strip()
    new_content = f"---\n{new_fm_yaml}\n---\n\n{clean_body}\n"

    dest_path.parent.mkdir(parents=True, exist_ok=True)
    dest_path.write_text(new_content, encoding="utf-8")
    return True


def generate_epro_index():
    """Generate EPRO_System/index.md."""
    categories = sorted(
        [d for d in EPRO_DIR.iterdir() if d.is_dir() and not d.name.startswith(".")]
    )

    rows = []
    total = 0
    for cat_dir in categories:
        files = [f for f in cat_dir.glob("*.md") if f.name != "index.md"]
        count = len(files)
        total += count
        # Get display name from the first file's frontmatter
        label = cat_dir.name
        rows.append(f"| [[{cat_dir.name}/index|{label}]] | {count} |")

    content = f"""---
title: "EPRO e-Procurement System"
description: "e-Procurement Platform Functional Requirements — 124 functional specifications"
tags: [moc, epro, index]
---

# EPRO e-Procurement System

> e-Procurement Platform (ProSmart) 功能需求規格 · {total} 條需求

## 分類

| 分類 | 需求數量 |
|------|:---:|
{chr(10).join(rows)}

---

## 說明

本區包含 e-Procurement Platform 的功能需求規格，涵蓋從系統基礎架構到各採購階段的完整功能定義。

每條需求包含：需求描述 → 需求理由 → 驗收標準
"""
    (EPRO_DIR / "index.md").write_text(content, encoding="utf-8")


def generate_category_indexes():
    """Generate index.md for each EPRO category."""
    for cat_dir in sorted(EPRO_DIR.iterdir()):
        if not cat_dir.is_dir() or cat_dir.name.startswith("."):
            continue
        files = sorted(
            [f for f in cat_dir.glob("*.md") if f.name != "index.md"]
        )
        if not files:
            continue

        entries = []
        for f in files:
            content = f.read_text(encoding="utf-8", errors="replace")
            fm_match = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
            title = f.stem
            issue_key = ""
            if fm_match:
                try:
                    fm = yaml.safe_load(fm_match.group(1))
                    title = fm.get("title", f.stem)
                    issue_key = fm.get("issue_key", "")
                except yaml.YAMLError:
                    pass
            entries.append({"slug": f.stem, "title": title, "key": issue_key})

        label = cat_dir.name
        content = f"""---
tags: [moc, epro, index]
title: "{label} — EPRO"
---

# {label}

> {len(files)} 條功能需求

| # | 需求 ID | 標題 |
|---|---------|------|
"""
        for i, e in enumerate(entries, 1):
            display = e["title"]
            if len(display) > 100:
                display = display[:97] + "..."
            content += "| " + str(i) + " | " + e["key"] + " | [[" + e["slug"] + "|" + display + "]] |\n"

        content += f"\n> 自動生成 · {date.today().isoformat()}\n"
        (cat_dir / "index.md").write_text(content, encoding="utf-8")


def main():
    print("Restoring EPRO files from archive...")
    if not ARCHIVE_DIR.exists():
        print(f"Archive directory {ARCHIVE_DIR} not found!")
        return

    # Clean destination
    if EPRO_DIR.exists():
        shutil.rmtree(EPRO_DIR)

    moved = 0
    for old_cat, (new_cat, label) in CATEGORY_MAP.items():
        src_dir = ARCHIVE_DIR / old_cat
        if not src_dir.exists():
            print(f"  {old_cat}: not found, skipping")
            continue

        files = [f for f in src_dir.glob("*.md") if f.name != "index.md"]
        for f in sorted(files):
            dest_name = f.name
            dest_path = EPRO_DIR / new_cat / dest_name
            if rebuild_epro_file(f, dest_path, label):
                moved += 1

        print(f"  {old_cat} -> {new_cat}: {len(files)} files")

    print(f"\nRestored {moved} EPRO files to {EPRO_DIR}/")

    # Generate indexes
    generate_epro_index()
    generate_category_indexes()
    print("Generated EPRO index pages")

    print("\nDone! Run 'npm run build' to regenerate the site.")


if __name__ == "__main__":
    main()
