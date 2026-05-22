---
project: FE
title: "FE-853: Enhance the POSsupport Tools add command remove the Pick up list and transfer list records"
issue_key: FE-853
issue_type: Improvement
status: Closed
faq_score: 4.0
faq_category: 04_Data_Sync
faq_category_label: 資料與同步
tags: [faq, fe, data_sync, frontend]
jira_url: "https://ctil.atlassian.net/browse/FE-853"
created: 2020-11-24
resolved: 2024-05-04
resolution: Done
has_images: True
---

# FE-853: Enhance the POSsupport Tools add command remove the Pick up list and transfer list records

## 問題描述

Remark1:  Dont use run as administrator command prompt to execute
Remark2:  Should also execute in both request and pickup location

Just use command prompt is normal.

e.g.
C:\Program Files (x86)\CS2000POS\possupp
-pwd sxdsupport
-execute deletereserverequest AH2S 00000070

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/d07401fe-5e82-4466-88a9-91e5dc2ca1bf)（需 Jira 登入）

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/755537cc-2106-4bb6-9308-5f4f87eba297)（需 Jira 登入）


## 附件截圖

1. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/d07401fe-5e82-4466-88a9-91e5dc2ca1bf)
2. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/755537cc-2106-4bb6-9308-5f4f87eba297)


## Jira Comments

> **howard** (2020-11-25):
> -execute deletereserverequest AH1S 00000067

> **howard** (2020-11-26):
> Cannot connect to SQL server (Checked possupp.exe.config/ vbretail.ini and FE can enquiry BE purchase History Record)  

> **howard** (2020-11-26):
> 

## 相關資訊

- **Jira:** [FE-853](https://ctil.atlassian.net/browse/FE-853)
- **解決方式:** Done