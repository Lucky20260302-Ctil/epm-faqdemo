---
project: FE
issue_key: FE-1843
issue_type: Bug DEV
status: Selected for Development (migrated)
faq_score: 5.0
faq_category: 04_Data_Sync
faq_category_label: 資料與同步
tags: [faq, fe, data_sync, front-end-v750.01r01a]
jira_url: "https://ctil.atlassian.net/browse/FE-1843"
created: 2026-01-05
resolved: 
resolution: 
has_images: True
---

# FE-1843: miss sales memo

> **類型:** Bug DEV | **狀態:** Selected for Development (migrated)
> **分類:** 資料與同步 | **FAQ 分數:** 5.0
> **負責人:** Sang
> **組件:** Front End v750.01R01A

## 問題描述

[INC3374986][INC3373375][INC3371843] AWS JP region J717till1, Pos version75.004.1305.0001

missing sales memo for 3 days in a row, those sales memos not created in PCD file.

> 📎 **image-20260105-092548.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/9e58a060-9aa0-49c0-a2a4-ad89028c5726)（需 Jira 登入）

> 📎 **image-20260105-092603.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/b838c34b-12f3-4b09-ae0f-166cecf156ad)（需 Jira 登入）

> 📎 **image-20260105-092626.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/9cf1d341-6169-40a2-a409-ec565c1f3b35)（需 Jira 登入）

> 📎 **image-20260105-123912.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/ce1588c8-8c23-4f23-b6e2-41dce2e8188e)（需 Jira 登入）

> 📎 **image-20260105-123951.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/4c8ca27e-e968-4e39-a290-0df7226ce540)（需 Jira 登入）

> 📎 **image-20260105-124024.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/399c625e-9011-4066-9295-9308e8b583ff)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20260105-092548.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/9e58a060-9aa0-49c0-a2a4-ad89028c5726)
2. 📎 **image-20260105-092603.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/b838c34b-12f3-4b09-ae0f-166cecf156ad)
3. 📎 **image-20260105-092626.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/9cf1d341-6169-40a2-a409-ec565c1f3b35)
4. 📎 **image-20260105-123912.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/ce1588c8-8c23-4f23-b6e2-41dce2e8188e)
5. 📎 **image-20260105-123951.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/4c8ca27e-e968-4e39-a290-0df7226ce540)
6. 📎 **image-20260105-124024.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/399c625e-9011-4066-9295-9308e8b583ff)


## Jira Comments

> **Automation for Jira** (2026-01-06):
> Issue has been created since Days since: 0 Week since : 0 Issue due date difference Days since :  Weeks since: 

> **Sang** (2026-01-06):
>        Problem due to ‘ Internal error: Cannot open the shared memory region.’

> **Sang** (2026-01-06):
>        Please stop csplus.exe, use POSSupp.exe ‘-clonesdf dbtrans’ command to clone a new dbtran.sdf and monitor the result. 

> **pierre.shi** (2026-01-06):
>  let me try. thanks

> **pierre.shi** (2026-01-12):
> Hi  I have clone dbtrans on SG OCF61till0 several days before, but still miss sales memo in pc file. 

> **Sang** (2026-01-13):
>      Any suggestion?

> **pierre.shi** (2026-02-03):
>       any suggestion about this issue? This issue still occurs occasionally.

## 相關資訊

- **Jira:** [FE-1843](https://ctil.atlassian.net/browse/FE-1843)