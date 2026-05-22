---
project: FE
issue_key: FE-1920
issue_type: Bug QA
status: Test in Progress
tags:
- 04_data_sync
- data_sync
- faq
- fe
- front-end
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/FE-1920
created: '2026-04-09'
resolved: ''
fix_version: ''
components: []
has_images: true
category: 04_Data_Sync
category_label: 資料同步
quality: partial
title: 'FE-1920: deposit can''t modify ticket'
---
# FE-1920: deposit can't modify ticket 

## 問題描述

deposit can't modify ticket

Reported by BASH

Reproduce step: *Suggest to use dbhist data directly

1. Deposit settle the deposit

2. Select Amend

Existing result:

Pop up 'Object reference not set to an instance of an object'

Dbtrans n Dbhist from BASH:

\\172.16.183.201\localuser\support\20260409\10S01010

> 📎 **image-20260409-021708.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/bad63de7-03d6-4f29-8b75-7431610fbc31)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20260409-021708.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/bad63de7-03d6-4f29-8b75-7431610fbc31)


## Jira Comments

> **Automation for Jira** (2026-04-10):
> Issue has been created since Days since: 0 Week since : 0 Issue due date difference Days since :  Weeks since: 

> **Sang** (2026-04-10):
> Problem due to amend deposit no.'s vip no. is not available in member database.

> **Sang** (2026-04-10):
> Handle while settle member deposit with amendment - but cannot find member no. - popup message allow sa to select option (KTS 250410 FE-1920 v750.04R12)  Option 1: Cancel settlement  Option 2: Settle by remove invalid member, SA can input other member no.

> **Andrew_Au** (2026-04-16):
> Please update the ticket status

## 相關資訊

- **Jira:** [FE-1920](https://ctil.atlassian.net/browse/FE-1920)