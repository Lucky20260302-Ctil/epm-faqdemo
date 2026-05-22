---
project: BE
issue_key: BE-701
issue_type: Bug PRD
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
jira_url: https://ctil.atlassian.net/browse/BE-701
created: '2022-11-21'
resolved: '2023-01-06'
fix_version: ''
components: []
has_images: false
category: 05_Error_Exception
category_label: 報錯與異常
quality: partial
title: 'BE-701: PO_Invalid Suppliers Error'
---
# BE-701: PO_Invalid Suppliers Error

## 問題描述

Env: Prorunner UAT Backend

ACC: sx1                        PW: sx1

Location: Process > Purchase Order Maintenance (PO3000)

Reproduce steps:

Case 1

1. Purchase Order Information (PO3000) 

2. Create 

3. Header info 

4. Fill PO Date 

5. Fill Supplier (Select Great_Seasons)

6. Currency 

7. Press Validate

8. Invalid Supplier Error 

Case 2

1. Continue as Case 1

2. Press (three dots from suppliers)

3. Invalid Format Error



## 相關資訊

- **Jira:** [BE-701](https://ctil.atlassian.net/browse/BE-701)
- **解決方式:** Done