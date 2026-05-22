#!/usr/bin/env python3
"""
Auto-generate index.md for each FAQ_test category directory.
Scans all .md files, extracts frontmatter titles, generates index.
Run before: npx quartz build -d .
"""
import os, re, yaml
from datetime import date

FAQ_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'FAQ_test')

def get_title(filepath):
    """Extract title from frontmatter or H1 of a markdown file."""
    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
    # Try frontmatter title
    fm_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if fm_match:
        try:
            fm = yaml.safe_load(fm_match.group(1))
            if fm and isinstance(fm, dict) and 'title' in fm:
                return fm['title']
        except:
            pass
    # Fallback: H1
    h1_match = re.search(r'^# (.+)$', content, re.MULTILINE)
    if h1_match:
        return h1_match.group(1).strip()
    return os.path.basename(filepath)[:-3]

def generate_category_index(category_dir):
    """Generate index.md for a single FAQ_test category."""
    cat_name = os.path.basename(category_dir)
    files = sorted([f for f in os.listdir(category_dir)
                   if f.endswith('.md') and f != 'index.md'])

    if not files:
        return

    # Extract titles
    entries = []
    for f in files:
        title = get_title(os.path.join(category_dir, f))
        slug = f[:-3]
        entries.append((slug, title))

    # Category display name mapping
    cat_labels = {
        '01_Install_Deploy': '安裝與部署',
        '02_Config_Settings': '配置與設定',
        '03_Data_Import': '資料匯入',
        '03_Performance_Timeout': '效能與超時',
        '04_Data_Sync': '資料同步',
        '05_Error_Exception': '報錯與異常',
        '06_Printing_Hardware': '列印與硬體',
        '06_Procurement_Workflow': '採購流程',
        '07_Other': '其他',
        '07_Reporting': '報表',
        '07_Workflow_Business': '業務流程',
    }
    label = cat_labels.get(cat_name, cat_name)

    content = f'''---
tags: [moc, faq, index]
title: "{label} — FAQ 索引"
updated: {date.today().isoformat()}
---

# {label}

> 自動生成索引 · {len(files)} 篇 FAQ

| # | 問題 |
|---|------|
'''
    for i, (slug, title) in enumerate(entries, 1):
        content += '| ' + str(i) + ' | [[' + slug + '|' + title + ']] |\n'

    content += f'\n> 最後更新: {date.today().isoformat()}\n'

    index_path = os.path.join(category_dir, 'index.md')
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)

def generate_main_index():
    """Generate root FAQ_test/index.md."""
    categories = sorted([d for d in os.listdir(FAQ_DIR)
                        if os.path.isdir(os.path.join(FAQ_DIR, d)) and not d.startswith('.')])

    cat_labels = {
        '01_Install_Deploy': '安裝與部署',
        '02_Config_Settings': '配置與設定',
        '03_Data_Import': '資料匯入',
        '03_Performance_Timeout': '效能與超時',
        '04_Data_Sync': '資料同步',
        '05_Error_Exception': '報錯與異常',
        '06_Printing_Hardware': '列印與硬體',
        '06_Procurement_Workflow': '採購流程',
        '07_Other': '其他',
        '07_Reporting': '報表',
        '07_Workflow_Business': '業務流程',
    }

    cat_rows = []
    total = 0
    for cat in categories:
        count = len([f for f in os.listdir(os.path.join(FAQ_DIR, cat))
                    if f.endswith('.md') and f != 'index.md'])
        total += count
        label = cat_labels.get(cat, cat)
        cat_rows.append('| [[' + cat + '/index|' + label + ']] | ' + str(count) + ' |')

    content = f'''---
tags: [moc, faq, index]
title: "ERM FAQ 知識庫"
updated: {date.today().isoformat()}
---

# ERM FAQ 知識庫

> 自動生成索引 · {total} 篇 FAQ · {len(categories)} 個分類

## 分類導航

| 分類 | 數量 |
|------|------|
{chr(10).join(cat_rows)}

---

## 如何使用

1. **搜尋**：使用左側搜尋框輸入關鍵字（支援中英文、工單號）
2. **瀏覽**：點擊上方分類進入對應 FAQ 列表
3. **每篇包含**：症狀描述 → 根本原因 → 解決方案

> 最後更新: {date.today().isoformat()}
'''

    with open(os.path.join(FAQ_DIR, 'index.md'), 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    print(f'Scanning: {FAQ_DIR}')
    for cat in sorted(os.listdir(FAQ_DIR)):
        cat_path = os.path.join(FAQ_DIR, cat)
        if os.path.isdir(cat_path) and not cat.startswith('.'):
            generate_category_index(cat_path)
            count = len([f for f in os.listdir(cat_path) if f.endswith('.md') and f != 'index.md'])
            print(f'  {cat}: {count} files -> index.md')
    generate_main_index()
    print('Done.')
