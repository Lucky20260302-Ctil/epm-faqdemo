---
project: FE
issue_key: FE-1248
issue_type: Bug PRD
status: Closed
tags:
- 03_performance_timeout
- faq
- fe
- front-end
- performance_timeout
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/FE-1248
created: '2023-05-19'
resolved: '2024-09-23'
fix_version: ''
components: []
has_images: true
category: 03_Performance_Timeout
category_label: 效能與超時
quality: partial
title: 'FE-1248: Add UPC validation while color size change'
---
# FE-1248: Add UPC validation while color size change

## 問題描述

OCF95-10025549

Refer to log, we found that user selected CI059 Col='UYP' & size='9   B' by Barcode scan.

Then change the size code to '8.5B' manually. Since CI059 'UYP' '8.5B' is valid item color size but no UPC. 

We do NOT have UPC validation while color size change.

>> I will checking with development team if we can add  UPC validation while color size change.

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/d8874080-9316-49ab-bd72-230e2d4d7fa3)（需 Jira 登入）


## 附件截圖

1. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/d8874080-9316-49ab-bd72-230e2d4d7fa3)

## 相關資訊

- **Jira:** [FE-1248](https://ctil.atlassian.net/browse/FE-1248)
- **解決方式:** Done