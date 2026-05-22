---
project: FE
title: "FE-1656: IMX refresh transfer receive record everytime when user enter the transfer receive page on FE"
issue_key: FE-1656
issue_type: Bug PRD
status: Test in Progress
faq_score: 6.0
faq_category: 04_Data_Sync
faq_category_label: 資料與同步
tags: [faq, fe, data_sync, front-end]
jira_url: "https://ctil.atlassian.net/browse/FE-1656"
created: 2025-03-20
resolved: 
resolution: 
has_images: True
---

# FE-1656: IMX refresh transfer receive record everytime when user enter the transfer receive page on FE

## 問題描述

FE user can receive a transfer when it was already received in BE.
@@Sang  Please help to add a config to control user can refresh the transfer status to avoid this issue.

**FE Record** – Received on 2025/03/03 at 17:29

 

> 📎 **image-20250320-084742.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/3badf50c-648f-41a7-b3f3-07ae9ffaf476)（需 Jira 登入）

Be Record – receive on 2025/03/03  15:50 by user 230324

> 📎 **image-20250320-084751.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/f4683849-5d0c-4205-a73d-4b7558c5081a)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20250320-084742.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/3badf50c-648f-41a7-b3f3-07ae9ffaf476)
2. 📎 **image-20250320-084751.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/f4683849-5d0c-4205-a73d-4b7558c5081a)


## Jira Comments

> **Sang** (2025-03-31):
>   Patch uploaded to \\ds411\share\POS_FE_Release\20250331 MX V710.02R14ZY Patch 'v710.02R14ZY Add tblconfig.TfxRecRefreshFullUpdate Y- Full Update, N-Delta Update (Default) (KTS 250331  Jira FE-1656 'v710.02R14ZY), v75.05

> **Andrew_Au** (2025-08-28):
>     Please arrange some test the bug fix. Still not release to IMX

> **Andrew_Au** (2025-09-30):
>  

> **Andrew_Au** (2025-10-03):
>  Please update status

## 相關資訊

- **Jira:** [FE-1656](https://ctil.atlassian.net/browse/FE-1656)