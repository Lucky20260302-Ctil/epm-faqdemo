---
project: BE
issue_key: BE-1059
issue_type: Bug PRD
status: Closed
tags:
- 04_data_sync
- api
- be
- data_sync
- faq
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/BE-1059
created: '2025-04-28'
resolved: '2025-07-04'
fix_version: ''
components: []
has_images: true
category: 04_Data_Sync
category_label: 資料同步
quality: partial
title: 'BE-1059: [CS-1413]Issue_P type in CS2000'
---
# BE-1059: [CS-1413]Issue_P type in CS2000

## 問題描述

Issue_Detail:

when API return a P type member，CS2000 should convert “P” to "C". but CS2000 didn't convert to this member to "C" and send "P" to Car 

> 📎 **image-20250428-004323.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/762d1d78-52ca-4310-aad2-17af5b8934ae)（需 Jira 登入）

Induced by Async insertion workflow

The data was directly passed to FEPOS 



## 附件截圖

1. 📎 **image-20250428-004323.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/762d1d78-52ca-4310-aad2-17af5b8934ae)


## Jira Comments

> **Cy Lau** (2025-04-28):
> 20240424 1749 Program Release V1.07.18(Acxiom CRM)   Release: \\ds411\public\samuel\beapi\v1.7.18_20250424 Api_gateway (build 9c92a27)  Beapi (build 8a3b49d) Update   Notes:     Release notes:   Api_gateway  BEAPI  [FE-1678 ] fix member type P did not convert to C when upsert is done by background service       Source code: Api_gateway: http://172.16.138.42:3000/ERM/BEGW   BEAPI: http://172.16.138.42:3000/ERM/BEAPI.git  (acxiom_crm)

> **Andrew_Au** (2025-06-05):
>   Please update the ticket status

> **Joy Li** (2025-07-04):
> released on 2025-04-26 BE-V70R3.101

## 相關資訊

- **Jira:** [BE-1059](https://ctil.atlassian.net/browse/BE-1059)
- **解決方式:** Done