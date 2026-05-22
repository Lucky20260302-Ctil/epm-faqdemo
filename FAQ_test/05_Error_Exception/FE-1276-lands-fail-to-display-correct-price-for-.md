---
project: FE
issue_key: FE-1276
issue_type: Bug QA
status: Closed
tags:
- 05_error_exception
- error_exception
- faq
- fe
- front-end
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/FE-1276
created: '2023-07-24'
resolved: '2023-11-16'
fix_version: ''
components: []
has_images: true
category: 05_Error_Exception
category_label: 報錯與異常
quality: partial
title: 'FE-1276: [Lands] Fail to display correct price for the item that runs more than 1 event at the same time'
---
# FE-1276: [Lands] Fail to display correct price for the item that runs more than 1 event at the same time

## 問題描述

Data from bookfair:

\\ds411\share\Sherman\data of bookfair

Reproduce step:

1. POS search item e.g.: 178683

2. Display 3 same items with same price

Existing result:

Fail to display correct price for the item that runs more than 1 event at the same time

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/cee240e6-2cd0-4756-a224-068829b46911)（需 Jira 登入）


## 附件截圖

1. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/cee240e6-2cd0-4756-a224-068829b46911)

## 相關資訊

- **Jira:** [FE-1276](https://ctil.atlassian.net/browse/FE-1276)
- **解決方式:** Done