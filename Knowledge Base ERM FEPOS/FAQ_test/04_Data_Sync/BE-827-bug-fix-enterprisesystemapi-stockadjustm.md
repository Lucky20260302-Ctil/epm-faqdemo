---
project: BE
issue_key: BE-827
issue_type: Bug DEV
status: Closed
faq_score: 4.5
faq_category: 04_Data_Sync
faq_category_label: 資料與同步
tags: [faq, be, data_sync, data-interface]
jira_url: "https://ctil.atlassian.net/browse/BE-827"
created: 2023-11-01
resolved: 2023-11-10
resolution: Done
has_images: True
---

# BE-827: bug fix EnterpriseSystemAPI StockAdjustment overwrite the origin value by accident

> **類型:** Bug DEV | **狀態:** Closed
> **分類:** 資料與同步 | **FAQ 分數:** 4.5
> **解決日期:** 2023-11-10
> **負責人:** Sherman tse
> **組件:** Data Interface

## 問題描述

incorrect:

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/7c7a2b39-cbf1-4e42-a1a1-9804027ed618)（需 Jira 登入）
 

correct:

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/ff482ede-7cc6-452e-b06a-6f75f0e26f73)（需 Jira 登入）
 



## 附件截圖

1. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/7c7a2b39-cbf1-4e42-a1a1-9804027ed618)
2. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/ff482ede-7cc6-452e-b06a-6f75f0e26f73)


## Jira Comments

> **Sherman tse** (2023-11-01):
> Verified on QA env 

> **Sherman tse** (2023-11-10):
> Verified on UAT env

## 相關資訊

- **Jira:** [BE-827](https://ctil.atlassian.net/browse/BE-827)
- **解決方式:** Done