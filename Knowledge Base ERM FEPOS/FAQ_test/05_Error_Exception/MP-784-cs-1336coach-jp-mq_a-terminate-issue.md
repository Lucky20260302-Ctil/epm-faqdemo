---
project: MP
issue_key: MP-784
issue_type: Bug PRD
status: Closed
faq_score: 7.0
faq_category: 05_Error_Exception
faq_category_label: 錯誤與異常
tags: [faq, mp, error_exception, backend]
jira_url: "https://ctil.atlassian.net/browse/MP-784"
created: 2025-06-30
resolved: 
resolution: 
has_images: True
---

# MP-784: [CS-1336]Coach JP MQ_A terminate issue

> **類型:** Bug PRD | **狀態:** Closed
> **分類:** 錯誤與異常 | **FAQ 分數:** 7.0
> **負責人:** Tovi Wang
> **組件:** Backend

## 問題描述

1.ACP2025062910224698.J450_M file里的 J450-MB002294 data 导致了posting terminate.

Posting error:

ACP2025062910224698.J450_M Start Processing

[TERMINATE(3)]/ExecuteReader requires the command to have a transaction when the connection assigned to the command is in a pending local transaction.  The Transaction property of the command has not 

What’s mean this error?                                                                                                                                                         

> 📎 **image-20250630-092041.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/fd54419f-2947-4b75-88ef-45c272a55e63)（需 Jira 登入）
2.查询PCD file里面此memo的data，发现有一个24 code这行数据。其它没有发现明显异常。

> 📎 **image-20250701-015003.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/7fd02dce-94fb-41da-9c14-5cad1ba21cd1)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20250630-092041.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/fd54419f-2947-4b75-88ef-45c272a55e63)
2. 📎 **image-20250701-015003.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/7fd02dce-94fb-41da-9c14-5cad1ba21cd1)

## 相關資訊

- **Jira:** [MP-784](https://ctil.atlassian.net/browse/MP-784)