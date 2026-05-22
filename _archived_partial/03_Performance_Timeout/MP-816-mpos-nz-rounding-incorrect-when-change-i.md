---
project: MP
issue_key: MP-816
issue_type: Bug QA
status: Open
tags:
- 03_performance_timeout
- faq
- mp
- mpos
- performance_timeout
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/MP-816
created: '2026-03-04'
resolved: ''
fix_version: ''
components: []
has_images: true
category: 03_Performance_Timeout
category_label: 效能與超時
quality: partial
title: 'MP-816: MPOS NZ Rounding incorrect when change is ending in 6¢'
---
# MP-816: MPOS NZ Rounding incorrect when change is ending in 6¢

## 問題描述

MPOS: When the price is 738.34 and the cash is 739. the original change should be 0.66, after rounding, it should be 0.70

> 📎 **image-20260304-092851.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/e6b89d98-7e7e-4b3a-bca6-bd9ffdb3b3d0)（需 Jira 登入）

Here is the same case in POS:

> 📎 **image-20260304-093048.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/33aa9fb9-63e2-499e-bd11-d590ed00eaa2)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20260304-092851.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/e6b89d98-7e7e-4b3a-bca6-bd9ffdb3b3d0)
2. 📎 **image-20260304-093048.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/33aa9fb9-63e2-499e-bd11-d590ed00eaa2)

## 相關資訊

- **Jira:** [MP-816](https://ctil.atlassian.net/browse/MP-816)