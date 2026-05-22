---
project: FE
issue_key: FE-1539
issue_type: Bug QA
status: Closed
tags:
- 04_data_sync
- data_sync
- faq
- fe
- front-end
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/FE-1539
created: '2024-10-24'
resolved: '2024-10-28'
fix_version: ''
components: []
has_images: true
category: 04_Data_Sync
category_label: 資料同步
quality: partial
title: 'FE-1539: Coach MY BDO - TMU mode printout missing footer'
---
# FE-1539: Coach MY BDO - TMU mode printout missing footer

## 問題描述

mpos printout in TMU mode
mpos ereceipt in TMU mode
mpos printout zebra
POS ereceipt in TMU mode
POS printout in TMU mode

all these printout/ereceipt is missing [📎附件](https://ctil.atlassian.net/rest/api/3/attachment/content/bd0f024e-f2bd-4c4e-b809-ae7ea5e6bc8d) 

as per the SOW:

> 📎 **image-20241024-013530.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/13dc8bc9-b7db-4c69-8424-6d0b44ace438)（需 Jira 登入）
current TMU and zebra:

> 📎 **signal-2024-10-24-093659.jpeg** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/61803a54-8edc-442a-a138-3eceb4ab52f6)（需 Jira 登入）
current POS ereceipt when printing is set to TMU:
 [📎附件](https://ctil.atlassian.net/rest/api/3/attachment/content/cba3938a-2a8f-459f-af5d-991e09c89e63) 

current MPOS ereceipt when printing is set to TMU:

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/130c1015-02e5-4bbd-97cb-ef8ad7d81981)（需 Jira 登入）



## 附件截圖

1. 📎 **image-20241024-013530.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/13dc8bc9-b7db-4c69-8424-6d0b44ace438)
2. 📎 **signal-2024-10-24-093659.jpeg** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/61803a54-8edc-442a-a138-3eceb4ab52f6)
3. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/130c1015-02e5-4bbd-97cb-ef8ad7d81981)


## Jira Comments

> **Andy Ko** (2024-10-24):
> 

> **Sang** (2024-10-24):
> Coach TMU Print Out - Footer file Config Sales/Deposit Settle - tblconfig.FOOTERFILENAMENORMAL Sales Exchange - tblconfig.FOOTERFILENAMEEXCHANGE Sales Return/Void/VoidDeposit Settle - tblconfig.FOOTERFILENAMERETURN Void Sales Return / Void Sales Exchange - tblconfig.FOOTERFILENAMERETURN

> **Sang** (2024-10-24):
> Please check file 

## 相關資訊

- **Jira:** [FE-1539](https://ctil.atlassian.net/browse/FE-1539)
- **解決方式:** Done