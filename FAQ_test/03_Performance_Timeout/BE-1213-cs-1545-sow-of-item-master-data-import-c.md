---
project: BE
issue_key: BE-1213
issue_type: SOW
status: Closed
faq_score: 8.0
faq_category: 03_Performance_Timeout
faq_category_label: 效能與逾時
tags: [faq, be, performance_timeout, backend-(chainstoreplus-7.0)]
jira_url: "https://ctil.atlassian.net/browse/BE-1213"
created: 2025-11-14
resolved: 2026-01-08
resolution: Done
has_images: True
---

# BE-1213: [CS-1545] SOW of Item Master Data Import Customization

> **類型:** SOW | **狀態:** Closed
> **分類:** 效能與逾時 | **FAQ 分數:** 8.0
> **解決日期:** 2026-01-08
> **負責人:** Jerry Wong
> **組件:** Backend (ChainStorePlus 7.0)

## 問題描述


> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/753cac9a-b871-4290-96bb-9de42b60a82e)（需 Jira 登入）
Due to requirements from the legal team, we need to prevent unexpected item description updates that could impact compliance. The standard SAP item master interface (itemmaster import) can inadvertently override product descriptions, Free Gift settings, and the Discount Control flag during data synchronization, potentially leading to unintended changes in item properties.

 

This customization allows users to lock item descriptions, Free Gift and Discount Control settings against update-mode imports, the system will help preserve original product description, Free Gift and Discount Control settings against accidental changes by the interface file.

** **

**NOTE: This change will apply to all regions and brands.**



## 附件截圖

1. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/753cac9a-b871-4290-96bb-9de42b60a82e)

## 相關資訊

- **Jira:** [BE-1213](https://ctil.atlassian.net/browse/BE-1213)
- **解決方式:** Done
- **標籤:** datainterface