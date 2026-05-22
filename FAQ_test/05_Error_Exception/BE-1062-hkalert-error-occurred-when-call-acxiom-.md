---
project: BE
issue_key: BE-1062
issue_type: Bug PRD
status: DEV Done
faq_score: 7.0
faq_category: 05_Error_Exception
faq_category_label: 錯誤與異常
tags: [faq, be, error_exception, api]
jira_url: "https://ctil.atlassian.net/browse/BE-1062"
created: 2025-04-28
resolved: 
resolution: 
has_images: True
---

# BE-1062: [HK][Alert] Error occurred when call ACXIOM CRM API: Profile Search

> **類型:** Bug PRD | **狀態:** DEV Done
> **分類:** 錯誤與異常 | **FAQ 分數:** 7.0
> **負責人:** Anson Cheung
> **組件:** API

## 問題描述

**Subject:** [HK][Alert] Error occurred when call ACXIOM CRM API: Profile Search

ACXIOM CRM API return an error response. Please find IT support.

---------------------------------------------------

Endpoint:
v2/cdp/profile/search

Body:
{"pageSize":"100","pageNum":0,"queryCondition":{"operationType":"AND","subQueryConditions":[]}}

Error:
200; Invalid arguments, sub query condition is required

Error occurred time:
0001-01-01 12:00:00

> 📎 **image-20250428-100313.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/e013bef3-a23e-4198-b5e0-09d9993577c0)（需 Jira 登入）

where come from the Error occurred time?

Error occurred time:
0001-01-01 12:00:00



## 附件截圖

1. 📎 **image-20250428-100313.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/e013bef3-a23e-4198-b5e0-09d9993577c0)

## 相關資訊

- **Jira:** [BE-1062](https://ctil.atlassian.net/browse/BE-1062)