---
project: BE
issue_key: BE-964
issue_type: Bug QA
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
jira_url: https://ctil.atlassian.net/browse/BE-964
created: '2024-12-11'
resolved: '2024-12-24'
fix_version: ''
components: []
has_images: true
category: 04_Data_Sync
category_label: 資料同步
quality: partial
title: 'BE-964: [Coach][CRM milestone 2] Send duplicate items to CRM when order issued & voided at the same day'
---
# BE-964: [Coach][CRM milestone 2] Send duplicate items to CRM when order issued & voided at the same day

## 問題描述

[Coach][CRM milestone 2] Send duplicate items to CRM when order issued & voided at the same day

> 📎 **image-20241211-072620.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/c8c57e50-05d8-4f5a-81c9-d3d8805c77c5)（需 Jira 登入）

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/18f7f577-7548-40ba-a1cb-5fe69954fa46)（需 Jira 登入）



## 附件截圖

1. 📎 **image-20241211-072620.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/c8c57e50-05d8-4f5a-81c9-d3d8805c77c5)
2. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/18f7f577-7548-40ba-a1cb-5fe69954fa46)


## Jira Comments

> **Anson Cheung** (2024-12-11):
> Program Release V1.1.6 Release:  \\ds411\public\anson\CRMSanyoPhaseInterface  \CRMSanyoPhaseInterface_v1.1.6.zip Update: group the items in program level instead of using sql distinct to prevent duplicate items sql enhancement: create temp table to filter jouinv_date and remove select distinct  [BE-962 ] support the end of filtered date range by set the new appsettings config "toDate"

> **Sherman tse** (2024-12-17):
> Verified on QA Able to send correct number of items to CRM when order issued & voided at the same day

## 相關資訊

- **Jira:** [BE-964](https://ctil.atlassian.net/browse/BE-964)
- **解決方式:** Done