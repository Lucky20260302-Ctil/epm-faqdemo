---
project: FE
issue_key: FE-1255
issue_type: Bug QA
status: Closed
faq_score: 5.5
faq_category: 04_Data_Sync
faq_category_label: 資料與同步
tags: [faq, fe, data_sync, front-end-v760.02]
jira_url: "https://ctil.atlassian.net/browse/FE-1255"
created: 2023-06-05
resolved: 2023-07-27
resolution: Done
has_images: True
---

# FE-1255: [Lands] Quatation No. display incorrect number of digits

> **類型:** Bug QA | **狀態:** Closed
> **分類:** 資料與同步 | **FAQ 分數:** 5.5
> **解決日期:** 2023-07-27
> **負責人:** Sang
> **組件:** front end v760.02

## 問題描述

Existing result:

Quatation No. used 8 digits

Expected reuslt:

Quatation No. would use 9 digits ( format: "TillNo" + "Q" + YY + ##### )

Related screenshot as below:

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/038bc0cb-5185-4702-8e19-18d9fb5f1a44)（需 Jira 登入）


## 附件截圖

1. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/038bc0cb-5185-4702-8e19-18d9fb5f1a44)

## 相關資訊

- **Jira:** [FE-1255](https://ctil.atlassian.net/browse/FE-1255)
- **解決方式:** Done