---
project: BE
issue_key: BE-1263
issue_type: Bug PRD
status: Test in Progress
faq_score: 7.0
faq_category: 05_Error_Exception
faq_category_label: 錯誤與異常
tags: [faq, be, error_exception, api]
jira_url: "https://ctil.atlassian.net/browse/BE-1263"
created: 2026-05-05
resolved: 
resolution: 
has_images: True
---

# BE-1263: [INC3572034] COACH AU OCFA221 re-send e-receipt error message pop

> **類型:** Bug PRD | **狀態:** Test in Progress
> **分類:** 錯誤與異常 | **FAQ 分數:** 7.0
> **負責人:** Sherman tse
> **組件:** API

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