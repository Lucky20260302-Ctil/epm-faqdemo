---
project: BE
issue_key: BE-1192
issue_type: SOW
status: Open
faq_score: 6.5
faq_category: 05_Error_Exception
faq_category_label: 錯誤與異常
tags: [faq, be, error_exception, data-interface]
jira_url: "https://ctil.atlassian.net/browse/BE-1192"
created: 2025-10-24
resolved: 
resolution: 
has_images: False
---

# BE-1192: [CS-1787] New Sales Export Interface for Resorts World Sentosa

> **類型:** SOW | **狀態:** Open
> **分類:** 錯誤與異常 | **FAQ 分數:** 6.5
> **負責人:** Ken Wang
> **組件:** Data Interface

## 問題描述

New Request from Lein that new Sales Interface is required to export Dayend Sales or Hourly Sales (fallback in dayend data not available) to Tangent System (teant sales management system of Sentosa.)

Please note that <u>**RWS requires two API integration formats to be implemented concurrently**</u>, each serving a specific purpose:

 

1. End-of-Day API – Provides the final and accurate sales data to be used for reconciliation purposes.

2. Hourly API – Serves as a fallback mechanism. In the event the End-of-Day sales data is not available (e.g., if the cashier fails to perform settlement), the system will automatically retrieve the hourly sales data (24 hourly entries) as a substitute.

 

This dual integration approach ensures data accuracy while maintaining operational reliability in the event of incomplete daily closures.



## 相關資訊

- **Jira:** [BE-1192](https://ctil.atlassian.net/browse/BE-1192)
- **標籤:** LL_Sales_Interface