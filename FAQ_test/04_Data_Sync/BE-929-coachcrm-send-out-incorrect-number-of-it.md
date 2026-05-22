---
project: BE
issue_key: BE-929
issue_type: Bug QA
status: Closed
faq_score: 7.0
faq_category: 04_Data_Sync
faq_category_label: 資料與同步
tags: [faq, be, data_sync, api]
jira_url: "https://ctil.atlassian.net/browse/BE-929"
created: 2024-11-01
resolved: 2024-11-04
resolution: Done
has_images: False
---

# BE-929: [Coach][CRM] Send out incorrect number of items to CRM side by CRMSanyoPhaseInterface

> **類型:** Bug QA | **狀態:** Closed
> **分類:** 資料與同步 | **FAQ 分數:** 7.0
> **解決日期:** 2024-11-04
> **負責人:** Anson Cheung
> **組件:** API

## 問題描述

Reproduce steps:

1. Upload an order to Backend DB e.g.: OC135MNC0000013 has 1 item

2. Send the order to CRM by CRMSanyoPhaseInterface

3. Check customer history

Existing result:

Send out incorrect number of items to CRM side by CRMSanyoPhaseInterface

1. e.g.: sent OC135MNC0000013  with 2 items to CRM




## Jira Comments

> **Sherman tse** (2024-11-04):
> Verified on QA close case

## 相關資訊

- **Jira:** [BE-929](https://ctil.atlassian.net/browse/BE-929)
- **解決方式:** Done