---
project: FE
issue_key: FE-1906
issue_type: Bug QA
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
jira_url: https://ctil.atlassian.net/browse/FE-1906
created: '2026-03-26'
resolved: ''
fix_version: ''
components: []
has_images: true
category: 04_Data_Sync
category_label: 資料同步
quality: partial
title: 'FE-1906: [DTUT] Edit module pop up ''Could not find file C:/redata6/BatchData.Mdb'''
---
# FE-1906: [DTUT] Edit module pop up 'Could not find file C:\redata6\BatchData.Mdb'

## 問題描述


> 📎 **image-20260326-015621.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/09c38216-afeb-4d31-9e19-46c067fb11b0)（需 Jira 登入）

Issue can be reproduced in dtutil2_v8348_260312b1454.exe , seems still has .mdb issue in edit function

1.  Click on tab of 2. Stock Transfer

2. Select a batch file

3. Click on Edit

Existing result:

Pop up Could not find file C:\redata6\BatchData.Mdb

*Need enhancement to support use batchData,accdb



## 附件截圖

1. 📎 **image-20260326-015621.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/09c38216-afeb-4d31-9e19-46c067fb11b0)


## Jira Comments

> **Automation for Jira** (2026-03-26):
> Issue has been created since Days since: 0 Week since : 0 Issue due date difference Days since :  Weeks since: 

> **Sang** (2026-03-26):
>  REVISED PROGRAM UPLOADED TO \\ds411\share\POS_FE_Release\20260326 DTUT Edit - v72 DALNC  DTUT Edit - Support BatchData.accdb (KTS 260326 FE-1906  v720.2R28D, v750.04R22, v750.05R11) use local DBMas to validate SKU

## 相關資訊

- **Jira:** [FE-1906](https://ctil.atlassian.net/browse/FE-1906)