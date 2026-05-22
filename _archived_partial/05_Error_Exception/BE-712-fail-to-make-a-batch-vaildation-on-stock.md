---
project: BE
issue_key: BE-712
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
jira_url: https://ctil.atlassian.net/browse/BE-712
created: '2023-01-17'
resolved: '2024-04-27'
fix_version: ''
components: []
has_images: false
category: 05_Error_Exception
category_label: 報錯與異常
quality: partial
title: 'BE-712: Fail to make a batch vaildation on Stock Replenishment (IC5000)'
---
# BE-712: Fail to make a batch vaildation on Stock Replenishment (IC5000)

## 問題描述

Env: [https://172.16.138.101/chainstoreplus/login](https://172.16.138.101/chainstoreplus/login)

ACC: sx1                   PW: sx1

Reproduce steps:

1. To Stock Replenishment (IC5000)

2. Select a batch with items 

3. Click on Batch vaildation

Exisitng result:

Fail to make a batch vaildation & Pop an error as attachment (Ref:image-2023-01-17-10-31-22-444.png)

 

 

Remark:

Same function on Remote control: 101 env works fine



## 相關資訊

- **Jira:** [BE-712](https://ctil.atlassian.net/browse/BE-712)
- **解決方式:** Done