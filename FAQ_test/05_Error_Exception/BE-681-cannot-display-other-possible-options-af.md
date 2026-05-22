---
project: BE
issue_key: BE-681
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
jira_url: https://ctil.atlassian.net/browse/BE-681
created: '2022-11-08'
resolved: '2023-02-16'
fix_version: ''
components: []
has_images: false
category: 05_Error_Exception
category_label: 報錯與異常
quality: partial
title: 'BE-681: Cannot display other possible options after click ''X'' in Selection list of specific data'
---
# BE-681: Cannot display other possible options after click "X" in Selection list of specific data

## 問題描述

Env: [https://172.16.138.101/chainstoreplus/](https://172.16.138.101/chainstoreplus/)

Location: Selection list of specific data

e.g.: Payment Type Code Maintenance (MF0009)

Reproduce steps:

1. To Payment Type Code Maintenance (MF0009)

2. Click Create

3. Click "..." for location selection

4. Select "P02"

5. Click "..." again for location selection

6. Click "X" in Location code>=

Existing result:

Cannot display other possible options e.g.: display option P01

(Ref: ChainStorePlus _ 99 - ERM Company 99 - Google Chrome 2022-11-08 15-11-52)

 

Remark: Other tabs seems also have same issue



## 相關資訊

- **Jira:** [BE-681](https://ctil.atlassian.net/browse/BE-681)
- **解決方式:** Done