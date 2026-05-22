---
project: FE
issue_key: FE-1468
issue_type: Change Request
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
jira_url: https://ctil.atlassian.net/browse/FE-1468
created: '2024-07-21'
resolved: '2024-09-04'
fix_version: ''
components: []
has_images: true
category: 04_Data_Sync
category_label: 資料同步
quality: partial
title: 'FE-1468: JC REMS SQ0343-126 – Opted out customer still able to fetch profile.'
---
# FE-1468: JC REMS SQ0343-126 – Opted out customer still able to fetch profile.

## 問題描述

1. 
> 📎 **image-20240721-105524.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/b87937be-f1bc-4032-af6f-e4854f35f4e0)（需 Jira 登入）



## 附件截圖

1. 📎 **image-20240721-105524.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/b87937be-f1bc-4032-af6f-e4854f35f4e0)


## Jira Comments

> **Sang** (2024-07-21):
> Check the QR Code JWT Token Expiry (exp - Unix DateTime) - block expired customer (SQ0343-126) (KTS 240721 Jira FE-1468 'v750.01R02N) Block QRcode/API Profile IsOptIn=False (SQ0343-126) (KTS 240721 Jira FE-1468 'v750.01R02N) Offline Search Member No found - show "invalid Loyalty Programme Account" (KTS 240721 Jira FE-1468 'v750.01R02N)

> **Andrew_Au** (2024-09-04):
>  Please update the ticket status

## 相關資訊

- **Jira:** [FE-1468](https://ctil.atlassian.net/browse/FE-1468)
- **解決方式:** Done