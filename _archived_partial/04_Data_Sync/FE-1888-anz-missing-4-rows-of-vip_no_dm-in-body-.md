---
project: FE
issue_key: FE-1888
issue_type: Bug QA
status: DEV Done
tags:
- 04_data_sync
- data_sync
- faq
- fe
- front-end
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/FE-1888
created: '2026-02-13'
resolved: ''
fix_version: ''
components: []
has_images: true
category: 04_Data_Sync
category_label: 資料同步
quality: partial
title: 'FE-1888: [ANZ] Missing 4 rows of vip_no_dm in body of  Dayend upsert member from [dbTrans].[dbo].[NEW VIP]'
---
# FE-1888: [ANZ] Missing 4 rows of vip_no_dm in body of  Dayend upsert member from [dbTrans].[dbo].[NEW VIP]

## 問題描述

[ANZ] Missing 4 rows of vip_no_dm in body of  Dayend upsert member from [dbTrans].[dbo].[NEW VIP]

body of  Dayend upsert member from [dbTrans].[dbo].[NEW VIP]:

{ "vip_no":"OC602MBS0000001", "vip_last_name":"TSEEES", "vip_first_name":"TESTERRRR", "vip_title":"", "vip_type":"C", "vip_issue_date":"2025/10/24", "vip_issue_loc":"OC602", "vip_expiry_date":"2026/10/23", "vip_birth_iyy":"1999", "vip_birth_imm":"09", "vip_birth_idd":"09", "vip_tel_1":"2728383894", "vip_tel_2":"6850123400", "vip_sex":"M", "vip_addr_1":" ", "vip_addr_2":" ", "vip_addr_3":" ", "vip_addr_4":" ", "vip_postal":" ", "[vip_email":"TESTER123246@GMAIL.COM](mailto:vip_email%22:%22TESTER123246@GMAIL.COM)", "update_timestamp":"2026/02/13 08:00:00", "vip_type_start_date":"2025/10/24", "vip_create_date":"2025/10/24", "vip_kana_first_name":"", "vip_kana_last_name":""}

Please refer to WA for details.

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/9e15a071-f27b-48ec-bedf-63ee6b25fe88)（需 Jira 登入）

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/f2a1cfc2-baf8-465f-81ce-e44c8c346ce6)（需 Jira 登入）



## 附件截圖

1. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/9e15a071-f27b-48ec-bedf-63ee6b25fe88)
2. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/f2a1cfc2-baf8-465f-81ce-e44c8c346ce6)


## Jira Comments

> **Automation for Jira** (2026-02-16):
> Issue has been created since Days since: 2 Week since : 0 Issue due date difference Days since :  Weeks since: 

> **Sang** (2026-02-16):
>  MPOS have not fill in data of Member communication channel, so upsert member  have not such row.

> **Andrew_Au** (2026-05-05):
>  Please update the ticket status

## 相關資訊

- **Jira:** [FE-1888](https://ctil.atlassian.net/browse/FE-1888)