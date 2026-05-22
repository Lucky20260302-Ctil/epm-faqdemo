---
project: BE
issue_key: BE-774
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
jira_url: https://ctil.atlassian.net/browse/BE-774
created: '2023-06-21'
resolved: '2023-06-23'
fix_version: ''
components: []
has_images: true
category: 05_Error_Exception
category_label: 報錯與異常
quality: partial
title: 'BE-774: Fail to process batch vaildation on Stock Receive (TF6000)'
---
# BE-774: Fail to process batch vaildation on Stock Receive (TF6000)

## 問題描述

Reproduce steps:

1. Go to Stock Receive (TF6000)

2. Create a new batch

3. Put item into the batch

4. Make a batch vaildation

Existing reuslt:

Pop up error (screenshot as below) & Fail to make a batch vaildation

Testing Env: [https://172.16.138.55/ChainStorePlus_LandsD_QA](https://172.16.138.55/ChainStorePlus_LandsD_QA)

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/c3c19a0b-37bc-4af2-a50a-3c7d329813e4)（需 Jira 登入）


## 附件截圖

1. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/c3c19a0b-37bc-4af2-a50a-3c7d329813e4)

## 相關資訊

- **Jira:** [BE-774](https://ctil.atlassian.net/browse/BE-774)
- **解決方式:** Done