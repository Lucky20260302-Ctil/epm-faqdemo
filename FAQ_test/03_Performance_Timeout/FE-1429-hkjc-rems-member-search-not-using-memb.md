---
project: FE
issue_key: FE-1429
issue_type: Bug QA
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
jira_url: https://ctil.atlassian.net/browse/FE-1429
created: '2024-06-26'
resolved: '2024-06-27'
fix_version: ''
components: []
has_images: false
category: 03_Performance_Timeout
category_label: 效能與超時
quality: partial
title: 'FE-1429: [HKJC] REMS - Member search not using member discount from member type'
---
# FE-1429: [HKJC] REMS - Member search not using member discount from member type

## 問題描述

after scanning/inputting QR code, the returned member has a type that should include member discount. However, after inputting the member, there is no member discount applied.

findings:

1. the member that has no member discount has a vip number in the tblvipmas. 

2. the record in tblvipmas has a different type from the API response. 

3. the type in local DB does not have member discount.

4. after changing the vip number in local DB, the API response will give the correct member discount.



## 相關資訊

- **Jira:** [FE-1429](https://ctil.atlassian.net/browse/FE-1429)
- **解決方式:** Done