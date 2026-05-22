---
project: BE
issue_key: BE-708
issue_type: Bug QA
status: Closed
tags:
- 05_error_exception
- backend-(web)
- be
- error_exception
- faq
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/BE-708
created: '2022-11-29'
resolved: '2023-03-03'
fix_version: ''
components: []
has_images: false
category: 05_Error_Exception
category_label: 報錯與異常
quality: partial
title: 'BE-708: Cannot edit existing records successfully in VAT Tax Rate'
---
# BE-708: Cannot edit existing records successfully in VAT Tax Rate

## 問題描述

Env: [https://172.16.138.55/ChainStorePlus_AIGLE/mx2000](https://172.16.138.55/ChainStorePlus_AIGLE/mx2000)

Location: VAT Tax Rate Information (MX2000)

Reproduce steps:

1. Click into one of the records

2. Edit a field e.g.: Description

3. Click on Save

Exisitng result:

Pop en error: Effective Date Overlapped & cannot save successfully (ref: image-2022-11-29-15-42-56-215.png)



## 相關資訊

- **Jira:** [BE-708](https://ctil.atlassian.net/browse/BE-708)
- **解決方式:** Done