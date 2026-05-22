---
project: BE
issue_key: BE-1030
issue_type: Bug PRD
status: Closed
faq_score: 5.5
faq_category: 04_Data_Sync
faq_category_label: 資料與同步
tags: [faq, be, data_sync, polling]
jira_url: "https://ctil.atlassian.net/browse/BE-1030"
created: 2025-03-19
resolved: 
resolution: 
has_images: True
---

# BE-1030: [INC2865617] BE UI Polling time display abnormal

> **類型:** Bug PRD | **狀態:** Closed
> **分類:** 資料與同步 | **FAQ 分數:** 5.5
> **負責人:** Jerry Wong
> **組件:** polling

## 問題描述

@@Jerry Wong SOG team callout The BE polling UI display is showing 19/03/202 for 1:10 AM.
When running the job, OC33__1 on 11:15 AM able to run up.
Please help to check what cause the issue and fix?

> 📎 **image-20250319-083825.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/ab00c3fb-3f8b-47a3-998d-fef9e67d691f)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20250319-083825.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/ab00c3fb-3f8b-47a3-998d-fef9e67d691f)


## Jira Comments

> **Tovi Wang** (2025-03-19):
>    03-19 Polling log for your reference.Thanks!

> **Tovi Wang** (2025-03-20):
> 03-20 Polling time恢复正常。怀疑是（03-18）Coach升级DB导致。

## 相關資訊

- **Jira:** [BE-1030](https://ctil.atlassian.net/browse/BE-1030)