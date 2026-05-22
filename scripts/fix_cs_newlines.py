#!/usr/bin/env python3
"""
Fix literal escape sequences in ChainStoreplus markdown files.
- Converts literal \\n to actual newlines
- Converts literal \\t to actual tabs
- Fixes other escape sequence issues
"""
import re
from pathlib import Path

CS_DIR = Path("ChainStoreplus")


def fix_file(filepath: Path) -> bool:
    content = filepath.read_text(encoding="utf-8")
    original = content

    # Parse frontmatter
    fm_match = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
    if not fm_match:
        return False

    fm_text = fm_match.group(1)
    body = content[fm_match.end():]

    # Fix literal \n -> actual newlines (but not in markdown tables or code)
    # Pattern: literal backslash-n that's not inside a markdown code block or table
    body = body.replace("\\n\\n", "\n\n")
    body = body.replace("\\n", "\n")

    # Fix literal \t -> spaces (tabs don't render well in markdown)
    body = body.replace("\\t", "    ")

    # Fix escaped quotes
    body = body.replace('\\"', '"')
    body = body.replace("\\'", "'")

    # Fix escaped backslashes (but not already-fixed ones)
    body = body.replace("\\\\", "\\")

    # Clean up: remove excessive blank lines (more than 2)
    body = re.sub(r"\n{3,}", "\n\n", body)

    # Rebuild
    new_content = f"---\n{fm_text}\n---\n\n{body.strip()}\n"

    if new_content != original:
        filepath.write_text(new_content, encoding="utf-8")
        return True
    return False


def main():
    count = 0
    for md_file in sorted(CS_DIR.rglob("*.md")):
        if md_file.name == "index.md" or md_file.name.startswith("."):
            continue
        if fix_file(md_file):
            count += 1
            print(f"  Fixed: {md_file.relative_to(CS_DIR)}")

    print(f"\nFixed {count} files.")


if __name__ == "__main__":
    main()
