---
project: BE
issue_key: BE-680
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
jira_url: https://ctil.atlassian.net/browse/BE-680
created: '2022-11-08'
resolved: '2023-02-21'
fix_version: ''
components: []
has_images: false
category: 05_Error_Exception
category_label: 報錯與異常
quality: partial
title: 'BE-680: Position of Aging code field is incorrect'
---
# BE-680: Position of Aging code field is incorrect

## 問題描述

Env: [https://172.16.138.101/chainstoreplus/](https://172.16.138.101/chainstoreplus/)

Location: 

Secondary > optional > Aging table maintenance (MF5008)

Existing result:

Field of inserting Aging code placed at incorrect position (under from date/ to date)

Expected result:

Field of inserting Aging code should be placed at first row (Ref: image-2022-11-08-13-50-45-890.png)



## 相關資訊

- **Jira:** [BE-680](https://ctil.atlassian.net/browse/BE-680)
- **解決方式:** Done