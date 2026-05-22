#!/usr/bin/env python3
"""
FAQ Frontmatter Normalization Script
=====================================
Walks all .md files in FAQ_test/, parses frontmatter, normalizes to unified schema,
and assigns quality scores based on content completeness.

Unified frontmatter schema:
  - project: BE | FE | MP | WEB | EPMTDCPROT | ChainStorePlus
  - issue_key: ticket key (e.g. BE-1020)
  - issue_type: Bug PRD | Bug QA | Task | Improvement | SOW | Change Request
  - status: Closed | HOLD | Resolved | In Progress
  - tags: [faq, <project_lower>, <category_tag>, ...]
  - symptom: 1-sentence symptom description
  - root_cause: root cause in 1-2 sentences (empty if unknown)
  - solution: solution in 1-2 sentences (empty if unknown)
  - quality: complete | partial | stub
  - jira_url: Jira issue URL
  - created: YYYY-MM-DD
  - resolved: YYYY-MM-DD (empty if not resolved)
  - fix_version: version string
  - components: [list of affected components]
  - has_images: true | false
  - category: folder name (e.g. 05_Error_Exception)
  - category_label: Chinese label (e.g. 錯誤與異常)
"""

import os
import re
import yaml
import json
from pathlib import Path
from datetime import datetime
from collections import Counter

FAQ_DIR = Path("FAQ_test")
DRY_RUN = True  # Set to False to actually write changes
REPORT_FILE = Path("scripts/normalization_report.json")

# Category mapping
CATEGORY_MAP = {
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

PROJECT_FROM_KEY = {
    "BE": "BE", "FE": "FE", "MP": "MP", "WEB": "WEB",
    "EPMTDCPROT": "EPMTDCPROT",
    "CS": "ChainStorePlus",
}

SECTION_PATTERNS = {
    "problem": re.compile(
        r"^#{1,3}\s*(問題描述|問題|症状|症狀|symptom|Problem|Issue)",
        re.IGNORECASE | re.MULTILINE,
    ),
    "root_cause": re.compile(
        r"^#{1,3}\s*(根因|根因分析|根本原因|root.?cause|Root Cause)",
        re.IGNORECASE | re.MULTILINE,
    ),
    "solution": re.compile(
        r"^#{1,3}\s*(解法|解決方案|解决方案|solution|fix|Solution|Fix|Resolution)",
        re.IGNORECASE | re.MULTILINE,
    ),
}

TABLE_SECTION = re.compile(
    r"^\|\s*(問題|根因|解法|症状|症狀|solution|root.cause|problem)",
    re.IGNORECASE | re.MULTILINE,
)


def detect_category(file_path: Path) -> tuple[str, str]:
    """Detect category from file path."""
    parts = file_path.parts
    for i, part in enumerate(parts):
        if part in CATEGORY_MAP:
            return part, CATEGORY_MAP[part]
    return "", ""


def detect_project_from_key(issue_key: str) -> str:
    """Detect project from issue key prefix."""
    if not issue_key:
        return ""
    for prefix, project in PROJECT_FROM_KEY.items():
        if issue_key.upper().startswith(prefix):
            return project
    return ""


def extract_symptom_from_frontmatter(fm: dict) -> str:
    """Extract symptom from frontmatter if present."""
    for key in ["symptom", "symptom_description", "problem", "problem_description"]:
        if fm.get(key):
            return str(fm[key]).strip()
    return ""


def extract_root_cause_from_frontmatter(fm: dict) -> str:
    """Extract root cause from frontmatter if present."""
    for key in ["root_cause", "root-cause", "rootCause", "cause"]:
        if fm.get(key):
            return str(fm[key]).strip()
    return ""


def extract_solution_from_frontmatter(fm: dict) -> str:
    """Extract solution from frontmatter if present."""
    for key in ["solution", "fix", "resolution", "workaround"]:
        if fm.get(key):
            return str(fm[key]).strip()
    return ""


def analyze_content_quality(body: str, fm: dict) -> str:
    """Determine quality: complete | partial | stub."""
    # Check both heading and table format
    has_problem = bool(SECTION_PATTERNS["problem"].search(body)) or bool(
        TABLE_SECTION.search(body)
    )
    # For root cause and solution, also check for simple text patterns in body
    has_root_cause = (
        bool(SECTION_PATTERNS["root_cause"].search(body))
        or bool(re.search(r"^\|\s*根因", body, re.MULTILINE))
        or bool(re.search(r"根因", body))
    )
    has_solution = (
        bool(SECTION_PATTERNS["solution"].search(body))
        or bool(re.search(r"^\|\s*解法", body, re.MULTILINE))
        or bool(re.search(r"解法", body))
    )

    problem_text = body_section_text(body, SECTION_PATTERNS["problem"], TABLE_SECTION)
    root_cause_text = body_section_text(body, SECTION_PATTERNS["root_cause"], None)
    solution_text = body_section_text(body, SECTION_PATTERNS["solution"], None)

    # Check for "None" or empty problem
    problem_empty = not problem_text or problem_text.strip().lower() in ("none", "n/a", "")
    root_empty = not root_cause_text or root_cause_text.strip().lower() in ("none", "n/a", "")
    solution_empty = not solution_text or solution_text.strip().lower() in ("none", "n/a", "")

    if problem_empty:
        return "stub"
    if has_root_cause and has_solution and has_problem:
        return "complete"
    if has_problem and not problem_empty:
        return "partial"
    return "stub"


def body_section_text(body: str, heading_pattern, table_pattern) -> str:
    """Extract text content of a section."""
    # Try heading-based first
    match = heading_pattern.search(body)
    if match:
        start = match.end()
        next_section = re.search(r"^#{1,3}\s", body[start:], re.MULTILINE)
        end = start + next_section.start() if next_section else len(body)
        return body[start:end].strip()
    # Try table-based
    if table_pattern:
        match = table_pattern.search(body)
        if match:
            return body[match.start():].split("\n\n")[0] if body[match.start():] else ""
    return ""


def normalize_file(file_path: Path) -> dict:
    """Normalize a single markdown file and return its report entry."""
    result = {
        "path": str(file_path),
        "action": "unchanged",
        "quality": "unknown",
        "issues": [],
    }

    try:
        content = file_path.read_text(encoding="utf-8")
    except Exception as e:
        result["action"] = "error"
        result["issues"].append(f"Read error: {e}")
        return result

    # Parse frontmatter
    fm_match = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
    if not fm_match:
        result["action"] = "error"
        result["issues"].append("No frontmatter found")
        return result

    try:
        fm = yaml.safe_load(fm_match.group(1))
    except yaml.YAMLError as e:
        result["action"] = "error"
        result["issues"].append(f"YAML error: {e}")
        return result

    if not isinstance(fm, dict):
        result["action"] = "error"
        result["issues"].append("Frontmatter is not a dict")
        return result

    body = content[fm_match.end():]

    # Determine category from path
    category, category_label = detect_category(file_path)
    if not category:
        result["issues"].append("Could not detect category from path")

    # Normalize project
    old_project = fm.get("project", "")
    issue_key = fm.get("issue_key", fm.get("jira", ""))
    if not old_project and issue_key:
        old_project = detect_project_from_key(issue_key)
    # Preserve original casing for known projects
    project_upper = old_project.upper() if old_project else ""
    known_projects = {"BE", "FE", "MP", "WEB", "EPMTDCPROT", "CHAINSTOREPLUS", "CHAINSTORE"}
    if project_upper in known_projects:
        # Use title case for display names
        if project_upper == "CHAINSTOREPLUS":
            project = "ChainStorePlus"
        elif project_upper == "CHAINSTORE":
            project = "ChainStore"
        elif project_upper == "EPMTDCPROT":
            project = "EPMTDCPROT"
        else:
            project = project_upper
    else:
        project = old_project

    # Normalize issue_key
    if not issue_key:
        for k in ["jira", "ticket", "key"]:
            if fm.get(k):
                issue_key = str(fm[k])
                break

    # Build normalized frontmatter
    new_fm = {
        "project": project or "",
        "issue_key": issue_key or "",
        "issue_type": fm.get("issue_type", fm.get("type", "")),
        "status": fm.get("status", ""),
        "tags": normalize_tags(fm, project, category),
        "symptom": fm.get("symptom", extract_symptom_from_frontmatter(fm)),
        "root_cause": fm.get("root_cause", extract_root_cause_from_frontmatter(fm)),
        "solution": fm.get("solution", extract_solution_from_frontmatter(fm)),
        "jira_url": fm.get("jira_url", ""),
        "created": normalize_date(fm.get("created", "")),
        "resolved": normalize_date(fm.get("resolved", "")),
        "fix_version": str(fm.get("fix_version", fm.get("fixVersion", ""))),
        "components": fm.get("components", fm.get("component", [])),
        "has_images": bool(fm.get("has_images", False)),
        "category": category,
        "category_label": category_label,
    }

    # Determine quality
    quality = analyze_content_quality(body, fm)
    new_fm["quality"] = quality

    # Remove old non-standard fields
    old_keys = set(fm.keys())
    new_keys = set(new_fm.keys())
    removed_keys = old_keys - new_keys - {
        "title", "date", "updated", "aliases", "cssclasses",
        "publish", "description", "related", "faq_score",
        "faq_category", "faq_category_label", "resolution",
    }
    if removed_keys:
        result["issues"].append(f"Removed keys: {removed_keys}")

    # Check if changes needed
    needs_update = False
    for key, value in new_fm.items():
        if key not in fm or fm[key] != value:
            needs_update = True
            break

    if quality != fm.get("quality", ""):
        needs_update = True

    if not needs_update:
        result["action"] = "unchanged"
        result["quality"] = quality
        return result

    result["action"] = "updated"
    result["quality"] = quality

    if not DRY_RUN:
        # Keep title if present
        if fm.get("title"):
            new_fm["title"] = fm["title"]

        # Strip duplicate H1 from body if it matches the title
        body = strip_duplicate_h1(body, new_fm.get("title", ""))

        # Rebuild file
        new_frontmatter = yaml.dump(
            new_fm,
            default_flow_style=False,
            allow_unicode=True,
            sort_keys=False,
            width=200,
        ).strip()
        new_content = f"---\n{new_frontmatter}\n---\n{body}"
        file_path.write_text(new_content, encoding="utf-8")

    return result


def strip_duplicate_h1(body: str, title: str) -> str:
    """Remove leading H1 from body if it duplicates the frontmatter title."""
    if not title or not body:
        return body
    # Match both `# Title` and `# Title` with anchor ID from Quartz
    h1_match = re.match(r"^# (.+?)(?:\s*\{[^}]*\})?\s*\n", body)
    if h1_match:
        h1_text = h1_match.group(1).strip()
        # Normalize both for comparison (strip issue keys, whitespace)
        title_norm = title.strip()
        h1_norm = h1_text.strip()
        if title_norm == h1_norm or h1_norm.startswith(title_norm) or title_norm.startswith(h1_norm):
            return body[h1_match.end():]
    return body


def normalize_tags(fm: dict, project: str, category: str) -> list:
    """Build normalized tag list."""
    tags = set()
    tags.add("faq")

    if project:
        tags.add(project.lower())

    if category:
        tags.add(category.lower())

    # Keep existing useful tags
    existing = fm.get("tags", [])
    if isinstance(existing, list):
        for tag in existing:
            tag_lower = str(tag).lower().strip("#")
            if tag_lower in ("faq", "moc", "index", "welcome"):
                continue
            if tag_lower in ("be", "fe", "mp", "web"):
                continue
            tags.add(tag_lower)
    elif isinstance(existing, str):
        tags.add(existing.lower().strip("#"))

    return sorted(tags)


def normalize_date(date_val) -> str:
    """Normalize date to YYYY-MM-DD."""
    if not date_val:
        return ""
    if isinstance(date_val, datetime):
        return date_val.strftime("%Y-%m-%d")
    date_str = str(date_val).strip()
    # Try common formats
    for fmt in ["%Y-%m-%d", "%Y/%m/%d", "%d/%m/%Y", "%d-%m-%Y", "%Y%m%d"]:
        try:
            return datetime.strptime(date_str, fmt).strftime("%Y-%m-%d")
        except ValueError:
            continue
    return date_str


def main():
    global DRY_RUN
    import sys

    if "--apply" in sys.argv:
        DRY_RUN = False
        print("[APPLY] APPLY MODE - Files will be modified")
    else:
        print("[DRY RUN] - No files will be modified (use --apply to write changes)")

    print(f"Scanning {FAQ_DIR}...\n")

    all_results = []
    stats = Counter()

    for md_file in sorted(FAQ_DIR.rglob("*.md")):
        if md_file.name.startswith("."):
            continue
        result = normalize_file(md_file)
        all_results.append(result)
        stats[result["action"]] += 1
        stats[f"quality_{result['quality']}"] += 1

    # Print summary
    print(f"\n{'='*60}")
    print(f"SUMMARY")
    print(f"{'='*60}")
    print(f"Total files scanned: {len(all_results)}")
    print(f"  Updated: {stats['updated']}")
    print(f"  Unchanged: {stats['unchanged']}")
    print(f"  Errors: {stats['error']}")
    print(f"\nQuality distribution:")
    print(f"  Complete: {stats['quality_complete']}")
    print(f"  Partial: {stats['quality_partial']}")
    print(f"  Stub: {stats['quality_stub']}")

    # List stub files
    stubs = [r for r in all_results if r["quality"] == "stub"]
    if stubs:
        print(f"\n{'-'*60}")
        print(f"STUB FILES (content is empty or 'None'): {len(stubs)}")
        print(f"{'-'*60}")
        for s in stubs:
            print(f"  {s['path']}")

    # List files with issues
    issues = [r for r in all_results if r["issues"]]
    if issues:
        print(f"\n{'-'*60}")
        print(f"FILES WITH ISSUES: {len(issues)}")
        print(f"{'-'*60}")
        for i in issues:
            print(f"  {i['path']}")
            for issue in i["issues"]:
                print(f"    -> {issue}")

    # Save report
    report = {
        "run_at": datetime.now().isoformat(),
        "dry_run": DRY_RUN,
        "stats": dict(stats),
        "results": all_results,
    }
    REPORT_FILE.parent.mkdir(parents=True, exist_ok=True)
    REPORT_FILE.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nReport saved to {REPORT_FILE}")


if __name__ == "__main__":
    main()
