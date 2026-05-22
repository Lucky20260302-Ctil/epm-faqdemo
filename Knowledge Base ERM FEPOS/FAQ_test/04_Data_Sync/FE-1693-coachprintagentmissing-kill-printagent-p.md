---
project: FE
issue_key: FE-1693
issue_type: Bug QA
status: Closed
faq_score: 6.0
faq_category: 04_Data_Sync
faq_category_label: 資料與同步
tags: [faq, fe, data_sync, front-end]
jira_url: "https://ctil.atlassian.net/browse/FE-1693"
created: 2025-05-12
resolved: 2025-09-10
resolution: Done
has_images: True
---

# FE-1693: [Coach][PrintAgent]Missing kill PrintAgent process causing PrintAgent still exist after POS dayend

> **類型:** Bug QA | **狀態:** Closed
> **分類:** 資料與同步 | **FAQ 分數:** 6.0
> **解決日期:** 2025-09-10
> **負責人:** Cy Lau
> **組件:** Front End

## 問題描述

[Coach][PrintAgent]Missing kill PrintAgent process causing PrintAgent still exist after POS dayend

Reproduce steps:

1. Open POS (PrintAgent keep running)

2. Process DayEnd

3. Wait for Dayend completed

4. Check the background task

> 📎 **image-20250512-055400.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/d9a334f9-77e4-46a0-a81e-44dc4c1d5d2b)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20250512-055400.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/d9a334f9-77e4-46a0-a81e-44dc4c1d5d2b)

## 相關資訊

- **Jira:** [FE-1693](https://ctil.atlassian.net/browse/FE-1693)
- **解決方式:** Done