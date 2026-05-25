#!/usr/bin/env python3
"""Fix EPRO notes in-place: split numbered sections, clean smart quotes."""
import os, re

BASE = r'D:\ObsidianDB\FAQTest\FAQ_test'
EPRO_DIRS = ['08_EPRO_System', '09_EPRO_PreTender', '10_EPRO_TenderStage',
             '11_EPRO_PostTender', '12_EPRO_Supplier', '13_EPRO_Reports', '14_EPRO_Others']

def split_numbered_sections(text):
    """Convert flat numbered paragraphs into markdown nested lists."""
    lines = text.split('\n')
    result = []
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        # Match "3.3.1. Some text" or "3.4. Some text" or "3.4.1. Text"
        m = re.match(r'^(\d+\.\d+(?:\.\d+)?)[.\s]+(.+)$', stripped)
        if m and len(m.group(1).split('.')) <= 3:
            num = m.group(1)
            content = m.group(2).strip()
            depth = len(num.split('.'))
            if depth == 2:
                # Collect continuation lines for this item
                full_content = [content]
                j = i + 1
                while j < len(lines):
                    next_line = lines[j].strip()
                    if re.match(r'^\d+\.\d+(?:\.\d+)?[.\s]+', next_line):
                        break
                    if next_line:
                        full_content.append(next_line)
                    j += 1
                joined = ' '.join(full_content)
                result.append(f'- **{num}** {joined}')
                i = j - 1
            elif depth >= 3:
                result.append(f'    - **{num}** {content}')
        else:
            result.append(line)
        i += 1
    return '\n'.join(result)

def clean_smart_quotes(text):
    for old, new in [('“','"'), ('”','"'), ('‘',"'"), ('’',"'"),
                     ('–','-'), ('—','--'), (' ',' '), ('…','...')]:
        text = text.replace(old, new)
    return text

def fix_single_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # Clean smart quotes everywhere
    content = clean_smart_quotes(content)

    # Find and fix the description section
    desc_match = re.search(r'(## 需求描述\n\n)(.+?)(?=\n## |\Z)', content, re.DOTALL)
    if desc_match:
        header = desc_match.group(1)
        desc = desc_match.group(2)
        fixed_desc = split_numbered_sections(desc)
        content = content[:desc_match.start()] + header + fixed_desc + content[desc_match.end():]

    # Find and fix table sections too
    table_match = re.search(r'(## 相關資料表\n\n)(.+?)(?=\Z)', content, re.DOTALL)
    if table_match:
        header = table_match.group(1)
        tables = table_match.group(2)
        fixed_tables = clean_smart_quotes(tables)
        content = content[:table_match.start()] + header + fixed_tables + content[table_match.end():]

    if content != original:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def remove_low_quality():
    """Remove notes with essentially no content."""
    removed = 0
    for ep_dir in EPRO_DIRS:
        d = os.path.join(BASE, ep_dir)
        if not os.path.exists(d): continue
        for f in sorted(os.listdir(d)):
            if not f.endswith('.md') or f == 'index.md': continue
            path = os.path.join(d, f)
            with open(path, 'r', encoding='utf-8') as fh:
                content = fh.read()
            # Extract description text
            desc_match = re.search(r'## 需求描述\n\n(.+?)(?=\n## |\Z)', content, re.DOTALL)
            if desc_match:
                desc = desc_match.group(1).strip()
                # Filter out empty or near-empty
                meaningful = re.sub(r'Requirement ID:.*?Requirement Type:.*?\n', '', desc)
                meaningful = re.sub(r'Parent Requirement #:.*?\n', '', meaningful)
                meaningful = re.sub(r'(None|Description:|Rationale:|Acceptance.*?:|Dependencies:|Tailoring.*?:|Change History:).*?\n', '', meaningful)
                meaningful = meaningful.strip()
                # Only remove if truly empty (all key fields are "None" or empty)
                all_none = all(
                    v.strip() in ('None', '')
                    for v in re.findall(r'(?:Description|Rationale|Acceptance[^:]*|Dependencies|Tailoring[^:]*|Change[^:]*):\s*(.+?)$', desc, re.MULTILINE)
                )
                if all_none and len(meaningful) < 20:
                    os.remove(path)
                    removed += 1
                    print(f'  Removed (empty): {ep_dir}/{f}')
    return removed

def main():
    # Step 1: Fix formatting
    fixed = 0
    for ep_dir in EPRO_DIRS:
        d = os.path.join(BASE, ep_dir)
        if not os.path.exists(d): continue
        for f in sorted(os.listdir(d)):
            if not f.endswith('.md') or f == 'index.md': continue
            if fix_single_file(os.path.join(d, f)):
                fixed += 1
    print(f'Fixed formatting: {fixed} notes')

    # Step 2: Remove low quality
    removed = remove_low_quality()
    print(f'Removed low quality: {removed} notes')

    # Step 3: Count remaining
    remaining = 0
    for ep_dir in EPRO_DIRS:
        d = os.path.join(BASE, ep_dir)
        if os.path.exists(d):
            count = len([f for f in os.listdir(d) if f.endswith('.md') and f != 'index.md'])
            print(f'  {ep_dir}: {count} notes')
            remaining += count
    print(f'Total remaining: {remaining} EPRO notes')

if __name__ == '__main__':
    main()
