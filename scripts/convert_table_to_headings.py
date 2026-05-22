#!/usr/bin/env python3
"""
Convert table-format FAQ sections to heading format.

From:
  | 問題
  content...

  | 根因
  content...

  | 解法
  content...

To:
  ## 症狀
  content...

  ## 根因
  content...

  ## 解法
  content...
"""
import re
from pathlib import Path

FAQ_DIR = Path("FAQ_test")

SECTION_MAP = {
    "問題": "症狀",
    "問題描述": "症狀",
    "症状": "症狀",
    "症狀": "症狀",
    "symptom": "symptom",
    "Problem": "symptom",
    "根因": "根因",
    "根因分析": "根因",
    "root cause": "root-cause",
    "root_cause": "root-cause",
    "解法": "解法",
    "解決方案": "解法",
    "solution": "solution",
    "fix": "solution",
    "相關資訊": "相關資訊",
    "相关资讯": "相關資訊",
}


def convert_file(filepath: Path) -> bool:
    """Convert a single file from table format to heading format."""
    content = filepath.read_text(encoding="utf-8")

    # Check if it uses table format
    if not re.search(r"^\|\s*(問題|根因|解法)", content, re.MULTILINE):
        return False

    # Parse frontmatter
    fm_match = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
    if not fm_match:
        return False

    fm_text = fm_match.group(1)
    body = content[fm_match.end():]

    # Split by table section markers
    # Pattern: | SectionName\ncontent...
    lines = body.split("\n")
    new_lines = []
    current_section = None

    for line in lines:
        section_match = re.match(r"^\|\s*(.+?)\s*$", line)
        if section_match:
            section_name = section_match.group(1).strip()
            mapped = SECTION_MAP.get(section_name, section_name)
            # Skip the first line if it's the title (no | prefix)
            if current_section is not None and new_lines and new_lines[-1] == "":
                new_lines.pop()  # Remove trailing blank
            new_lines.append("")
            new_lines.append(f"## {mapped}")
            new_lines.append("")
            current_section = section_name
        else:
            new_lines.append(line)

    new_body = "\n".join(new_lines).strip() + "\n"

    # Remove extra blank lines (more than 2 consecutive)
    new_body = re.sub(r"\n{3,}", "\n\n", new_body)

    # Extract first non-empty line as title if frontmatter doesn't have one
    if "title:" not in fm_text:
        body_stripped = new_body.strip()
        first_line_match = re.match(r"^([A-Z]+-\d+.*?)$", body_stripped, re.MULTILINE)
        if first_line_match:
            extracted_title = first_line_match.group(1).strip()
            # Insert title into frontmatter before the closing ---
            fm_text = fm_text.rstrip() + f"\ntitle: '{extracted_title}'\n"
            # Remove the first line from body
            new_body = re.sub(r"^[A-Z]+-\d+.*?\n", "", new_body, count=1)
            new_body = new_body.strip() + "\n"

    # Rebuild file
    new_content = f"---\n{fm_text}\n---\n\n{new_body}"
    filepath.write_text(new_content, encoding="utf-8")
    return True


def main():
    converted = 0
    for md_file in sorted(FAQ_DIR.rglob("*.md")):
        if md_file.name == "index.md" or md_file.name.startswith("."):
            continue
        if convert_file(md_file):
            converted += 1
            print(f"  Converted: {md_file.relative_to(FAQ_DIR)}")

    print(f"\nConverted {converted} files from table format to heading format.")


if __name__ == "__main__":
    main()
