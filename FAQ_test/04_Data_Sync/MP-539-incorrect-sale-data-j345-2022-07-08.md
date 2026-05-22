---
project: MP
issue_key: MP-539
issue_type: Bug PRD
status: Closed
faq_score: 5.5
faq_category: 04_Data_Sync
faq_category_label: 資料與同步
tags: [faq, mp, data_sync, localiis, mpos-api]
jira_url: "https://ctil.atlassian.net/browse/MP-539"
created: 2022-07-12
resolved: 2024-03-06
resolution: Done
has_images: False
---

# MP-539: Incorrect sale data: J345 2022-07-08

> **類型:** Bug PRD | **狀態:** Closed
> **分類:** 資料與同步 | **FAQ 分數:** 5.5
> **解決日期:** 2024-03-06
> **負責人:** Sang
> **組件:** LocalIIS, MPOS API

## 問題描述

J345-MA005279

2022-07-08

Local IIS 3.14.0




## Jira Comments

> **Joy Li** (2022-07-12):
> \\172.16.183.201\localuser\support\JIRA_DB\MP-539\ IIS Log and dbSSE dbtran and dbhist copied

> **Sang** (2022-07-20):
> [3.19.0] 1.Adding fields back for miscalculations bug fixes (CY Lau: 20220714 Jira  /Jira  / )  1) Product.cs  2) Memos.cs  3) Shared.cs : ConvertSalesItem2Product, ConvertProduct2SalesItem, ConvertProduct2SalesItem,ConvertMemoData2SalesData 2. Write Disc Analysis for Tax Exempted MM Memo Disc Memo Fixed (KTS 220714 v72.02R18, v750.02 )

## 相關資訊

- **Jira:** [MP-539](https://ctil.atlassian.net/browse/MP-539)
- **解決方式:** Done