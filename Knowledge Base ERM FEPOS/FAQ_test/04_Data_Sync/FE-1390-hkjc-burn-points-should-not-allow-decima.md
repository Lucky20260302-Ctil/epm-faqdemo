---
project: FE
issue_key: FE-1390
issue_type: Bug QA
status: Closed
faq_score: 5.5
faq_category: 04_Data_Sync
faq_category_label: 資料與同步
tags: [faq, fe, data_sync, front-end]
jira_url: "https://ctil.atlassian.net/browse/FE-1390"
created: 2024-05-16
resolved: 2024-06-12
resolution: Done
has_images: True
---

# FE-1390: HKJC burn points should not allow decimals

> **類型:** Bug QA | **狀態:** Closed
> **分類:** 資料與同步 | **FAQ 分數:** 5.5
> **解決日期:** 2024-06-12
> **負責人:** Andy Ko
> **組件:** Front End

## 問題描述

When inputting amount for burn points, the lowest value should be 1, but currently the system allows decimal:

> 📎 **image-20240516-092229.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/06dfb621-1831-4361-a820-6c261e9303c0)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20240516-092229.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/06dfb621-1831-4361-a820-6c261e9303c0)


## Jira Comments

> **Andy Ko** (2024-05-21):
>  I tested inputting 1.50 for BP amount , and it rounded to 2. Is this based on the rounding flag in config?

> **Sang** (2024-05-23):
> Burn Point not accept decimal, auto round down to dollar  (KTS 240516 Jira FE-1390 v750.01R02A)

## 相關資訊

- **Jira:** [FE-1390](https://ctil.atlassian.net/browse/FE-1390)
- **解決方式:** Done