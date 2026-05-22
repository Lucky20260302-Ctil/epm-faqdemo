---
project: FE
issue_key: FE-1819
issue_type: Bug PRD
status: Selected for Development (migrated)
tags:
- 04_data_sync
- data_sync
- faq
- fe
- front-end
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/FE-1819
created: '2025-11-25'
resolved: ''
fix_version: ''
components: []
has_images: true
category: 04_Data_Sync
category_label: 資料同步
quality: partial
title: 'FE-1819: incomplete log purging in frontend Retdata6/history'
---
# FE-1819: incomplete log purging in frontend Retdata6/history

## 問題描述

in CSplus v75, the history log will be zipped into retdata6/history and should be purged periodically based on configutation DELETEHISTORYPERIOD.

However, it is found that in Coach CN Prod frontend, the zipped NPOS, UploadPCD and WA logs have not been purged even passed the house keeping period.

Hence require modifying the frontend to include those logs into housekeeping cycle.

> 📎 **image-20251125-100245.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/1688463b-c696-4432-91cf-bb1c8af11f1a)（需 Jira 登入）

> 📎 **image-20251125-100230.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/a345128e-0518-4e6b-bf8e-4c8ebb6e5300)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20251125-100245.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/1688463b-c696-4432-91cf-bb1c8af11f1a)
2. 📎 **image-20251125-100230.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/a345128e-0518-4e6b-bf8e-4c8ebb6e5300)


## Jira Comments

> **Automation for Jira** (2025-12-29):
> Issue has been created since Days since: 33 Week since : 4 Issue due date difference Days since :  Weeks since: 

## 相關資訊

- **Jira:** [FE-1819](https://ctil.atlassian.net/browse/FE-1819)