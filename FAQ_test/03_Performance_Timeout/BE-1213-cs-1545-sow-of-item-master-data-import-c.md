---
project: BE
issue_key: BE-1213
issue_type: SOW
status: Closed
tags:
- 03_performance_timeout
- backend-(chainstoreplus-7.0)
- be
- faq
- performance_timeout
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/BE-1213
created: '2025-11-14'
resolved: '2026-01-08'
fix_version: ''
components: []
has_images: true
category: 03_Performance_Timeout
category_label: 效能與超時
quality: partial
title: 'BE-1213: [CS-1545] SOW of Item Master Data Import Customization'
---
# BE-1213: [CS-1545] SOW of Item Master Data Import Customization

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