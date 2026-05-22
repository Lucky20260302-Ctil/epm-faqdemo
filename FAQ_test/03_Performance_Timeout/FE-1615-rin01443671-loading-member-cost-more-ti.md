---
project: FE
issue_key: FE-1615
issue_type: Bug DEV
status: Closed
tags:
- 03_performance_timeout
- faq
- fe
- front-end-v750.01r01a
- performance_timeout
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/FE-1615
created: '2025-01-24'
resolved: ''
fix_version: ''
components: []
has_images: false
category: 03_Performance_Timeout
category_label: 效能與超時
quality: partial
title: 'FE-1615: RIN01443671- loading member cost more time in V75'
---
# FE-1615: RIN01443671- loading member cost more time in V75

## 問題描述

OCF120C00054040
1.From "input vip data in POS" to "CRM response vip data",spend31 s.
2.from "Start upsert CRM member" to "API response member data to POS" ,spend 9 s

Total spend about 40 s.



## 相關資訊

- **Jira:** [FE-1615](https://ctil.atlassian.net/browse/FE-1615)