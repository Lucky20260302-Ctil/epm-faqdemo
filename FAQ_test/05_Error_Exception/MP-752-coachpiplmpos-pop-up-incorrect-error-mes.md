---
project: MP
issue_key: MP-752
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
jira_url: https://ctil.atlassian.net/browse/MP-752
created: '2025-03-03'
resolved: '2025-07-31'
fix_version: ''
components: []
has_images: true
category: 05_Error_Exception
category_label: 報錯與異常
quality: partial
title: 'MP-752: [Coach][PIPL][MPOS] Pop up incorrect error message when searching a member from CN with EXIT_PERMIT = 0/ NULL'
---
# MP-752: [Coach][PIPL][MPOS] Pop up incorrect error message when searching a member from CN with EXIT_PERMIT = 0/ NULL

## 問題描述

[Coach][PIPL][MPOS] Pop up incorrect error message when searching a member from CN with EXIT_PERMIT = 0/ NULL

Testing VM: 172.16.138.180 (HK: 10)

Testing data: 15524552187 mobile phone with EXIT_PERMIT = 0/ NULL

Expected result:

Use  the error message: "This member does not consent to enquire out of border."

> 📎 **image-20250303-092209.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/06f1aad9-b213-4500-9b47-bbf6d2095cd2)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20250303-092209.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/06f1aad9-b213-4500-9b47-bbf6d2095cd2)

## 相關資訊

- **Jira:** [MP-752](https://ctil.atlassian.net/browse/MP-752)
- **解決方式:** Done