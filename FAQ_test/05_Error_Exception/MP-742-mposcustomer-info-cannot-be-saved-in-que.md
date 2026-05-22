---
project: MP
issue_key: MP-742
issue_type: Bug QA
status: Closed
tags:
- 05_error_exception
- error_exception
- faq
- mp
- mpos
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/MP-742
created: '2025-01-08'
resolved: '2025-02-24'
fix_version: ''
components: []
has_images: true
category: 05_Error_Exception
category_label: 報錯與異常
quality: partial
title: 'MP-742: [MPOS]Customer info cannot be saved in queue busting when order saved with no member'
---
# MP-742: [MPOS]Customer info cannot be saved in queue busting when order saved with no member

## 問題描述

[MPOS]Customer info cannot be saved in queue busting when order saved with no member

Reproduce steps:

1. To sales memo page

2. Add an item

3. Save it to queue busting

4. Retrieve the order from queue busting

5. Add one more item

6. To Save to busket page

Exisitng result:

Customer info cleared in the saved queue busting

> 📎 **image-20250108-023012.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/85dc9b3a-9ab5-4d59-a683-769a2e1b5450)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20250108-023012.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/85dc9b3a-9ab5-4d59-a683-769a2e1b5450)

## 相關資訊

- **Jira:** [MP-742](https://ctil.atlassian.net/browse/MP-742)
- **解決方式:** Done