---
project: BE
issue_key: BE-1263
issue_type: Bug PRD
status: Test in Progress
tags:
- 05_error_exception
- api
- be
- error_exception
- faq
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/BE-1263
created: '2026-05-05'
resolved: ''
fix_version: ''
components: []
has_images: true
category: 05_Error_Exception
category_label: 報錯與異常
quality: partial
title: 'BE-1263: [INC3572034] COACH AU OCFA221 re-send e-receipt error message pop'
---
# BE-1263: [INC3572034] COACH AU OCFA221 re-send e-receipt error message pop

## 問題描述

Error popped when user re-send e-receipt. (email send but error message popped)

> 📎 **image-20260505-053915.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/3d96e11a-0ca1-41b3-8cfd-28c8eba358c6)（需 Jira 登入）

WA Log:

Send_eReceipt.Error: Arithmetic overflow error converting expression to data type nvarchar.Arithmetic overflow error converting expression to data type nvarchar.The statement has been terminated.The statement has been terminated.

TO -reproduce:

1. iidentity >99999 contain 6 digits

> 📎 **image-20260505-054133.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/a1c30345-9fba-4530-8430-b088c318ec19)（需 Jira 登入）

2. Only popped up when user re-send the e-receipt.



## 附件截圖

1. 📎 **image-20260505-053915.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/3d96e11a-0ca1-41b3-8cfd-28c8eba358c6)
2. 📎 **image-20260505-054133.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/a1c30345-9fba-4530-8430-b088c318ec19)

## 相關資訊

- **Jira:** [BE-1263](https://ctil.atlassian.net/browse/BE-1263)