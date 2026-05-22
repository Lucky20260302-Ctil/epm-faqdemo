---
project: FE
issue_key: FE-1900
issue_type: Bug QA
status: Closed
tags:
- 04_data_sync
- data_sync
- dtutil
- faq
- fe
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/FE-1900
created: '2026-03-13'
resolved: '2026-03-17'
fix_version: ''
components: []
has_images: true
category: 04_Data_Sync
category_label: 資料同步
quality: partial
title: 'FE-1900: [Dtutil] Transafer Delivery note printed as veritical, it shoule be landscape'
---
# FE-1900: [Dtutil] Transafer Delivery note printed as veritical, it shoule be landscape

## 問題描述

[Dtutil] Transafer Delivery note printed as veritical, it shoule be landscape

Applied with v4.27 KOS.LPrinter.dll
VM: 172.16.138.131
.\sxd
Yan20201104@

C:\DTUTIL2

> 📎 **image-20260313-103416.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/2e22c37d-8dfe-4a9e-8bd8-820518d750ad)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20260313-103416.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/2e22c37d-8dfe-4a9e-8bd8-820518d750ad)


## Jira Comments

> **Automation for Jira** (2026-03-16):
> Issue has been created since Days since: 2 Week since : 0 Issue due date difference Days since :  Weeks since: 

> **Sang** (2026-03-16):
>  Please try updated program KOS.Lprinter.exe , uploaded to \\ds411\share\POS_FE_Release\20260316 DTUT Print DN

> **Sang** (2026-03-16):
>    Upgrade SanyoPos.Report.dll to v720.02R28 Change DN report layout to Portrait. Program uploaded to \\ds411\share\POS_FE_Release\20260316 DTUT Print DN

> **Sherman tse** (2026-03-17):
> Verified OK on QA Print out using vertical mode finally

> **Sherman tse** (2026-03-17):
>  

## 相關資訊

- **Jira:** [FE-1900](https://ctil.atlassian.net/browse/FE-1900)
- **解決方式:** Done