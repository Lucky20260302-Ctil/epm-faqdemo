---
project: BE
issue_key: BE-1219
issue_type: SOW
status: Open
faq_score: 5.5
faq_category: 04_Data_Sync
faq_category_label: 資料與同步
tags: [faq, be, data_sync, data-interface]
jira_url: "https://ctil.atlassian.net/browse/BE-1219"
created: 2025-12-03
resolved: 
resolution: 
has_images: False
---

# BE-1219: New Sales Export Interface for Mayang Mall 

> **類型:** SOW | **狀態:** Open
> **分類:** 資料與同步 | **FAQ 分數:** 5.5
> **組件:** Data Interface

## 問題描述

New Request from Lein that new Sales Interface is required to export Hourly Sales to Tangent System (tenant sales management system of Mayang.)

The API integration will be implemented for below purpose:

 

1. Sales Hourly API 

1. retrieve the hourly sales data (24 hourly entries) and export to Tangent once per day.

2. need to export sales data for the past 7 days.

 




## Jira Comments

> **Ken Wang** (2025-12-03):
> Attached is the API Documentation POS Sales Hourly to submit and integrate via Web API. Please send hourly sales via API to the test URL  Here is the Staging phase url :    User ID:      postestapimy Password:  @APITest1234 Machine ID:  50100902   URL GET TOKEN: https://staging.synthesis.bz/posmy/v1/api/token   URL POST Sales Data:  https://staging.synthesis.bz/posmy/v1/api/SalesHourly

> **Ken Wang** (2025-12-03):
> Attached the specification from Landlord and SOW for review.

> **Sherman tse** (2026-01-08):
>   Can we close this ticket?

> **Andrew_Au** (2026-04-16):
>   Can we update the ticket status to 'Closed'?

## 相關資訊

- **Jira:** [BE-1219](https://ctil.atlassian.net/browse/BE-1219)
- **標籤:** LL_Sales_Interface