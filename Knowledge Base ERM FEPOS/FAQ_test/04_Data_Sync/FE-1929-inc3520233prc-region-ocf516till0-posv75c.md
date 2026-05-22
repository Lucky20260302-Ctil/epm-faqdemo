---
project: FE
issue_key: FE-1929
issue_type: Bug DEV
status: Open
faq_score: 4.5
faq_category: 04_Data_Sync
faq_category_label: 資料與同步
tags: [faq, fe, data_sync, cs2kconnect]
jira_url: "https://ctil.atlassian.net/browse/FE-1929"
created: 2026-04-16
resolved: 
resolution: 
has_images: True
---

# FE-1929: [INC3520233]PRC region OCF516till0 POSv75,cs2kconnect can't generate acp file in time.

> **類型:** Bug DEV | **狀態:** Open
> **分類:** 資料與同步 | **FAQ 分數:** 4.5
> **負責人:** Cy Lau
> **組件:** CS2kconnect

## 問題描述

only this till has this issue, always can’t generate acp file im time.

get the logs from till0 on 12th Apr.

had 2 memos that day:

00002748 created at 15:43

00002749 created at 16:50

> 📎 **image-20260416-024825.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/aa213473-2f2d-473d-b0d3-30d10ce5c2c9)（需 Jira 登入）
but no acp file generated that time.

> 📎 **image-20260416-024856.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/18444d54-7fdb-4f0c-9360-f008fedfe8f2)（需 Jira 登入）

> 📎 **image-20260416-024916.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/5c579120-b946-49ab-befd-fdfe40fb3cb4)（需 Jira 登入）
but the acp file was generated at 17:50, the two sales memos both included:

> 📎 **image-20260416-025018.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/ded61f41-2c91-42c9-a68b-301655b8ded4)（需 Jira 登入）

> 📎 **image-20260416-025039.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/430921e2-545f-41c9-afa6-105467ac3580)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20260416-024825.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/aa213473-2f2d-473d-b0d3-30d10ce5c2c9)
2. 📎 **image-20260416-024856.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/18444d54-7fdb-4f0c-9360-f008fedfe8f2)
3. 📎 **image-20260416-024916.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/5c579120-b946-49ab-befd-fdfe40fb3cb4)
4. 📎 **image-20260416-025018.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/ded61f41-2c91-42c9-a68b-301655b8ded4)
5. 📎 **image-20260416-025039.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/430921e2-545f-41c9-afa6-105467ac3580)

## 相關資訊

- **Jira:** [FE-1929](https://ctil.atlassian.net/browse/FE-1929)