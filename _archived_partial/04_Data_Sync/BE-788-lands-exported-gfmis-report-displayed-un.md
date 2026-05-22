---
project: BE
issue_key: BE-788
issue_type: Bug QA
status: Closed
tags:
- 04_data_sync
- backend-(web)
- be
- data_sync
- faq
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/BE-788
created: '2023-08-14'
resolved: '2023-09-01'
fix_version: ''
components: []
has_images: true
category: 04_Data_Sync
category_label: 資料同步
quality: partial
title: 'BE-788: [Lands] Exported GFMIS report displayed unnecessary store records'
---
# BE-788: [Lands] Exported GFMIS report displayed unnecessary store records

## 問題描述

Reporduce steps:

1. To GFMIS Report export a report (e.g.: select store is LHQ)

Existing result:

Exported GFMIS report displayed unnecessary store records (not only LHQ captured screen as below)

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/bff37e62-3448-40e7-a0e2-6eba66a6b93c)（需 Jira 登入）


## 附件截圖

1. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/bff37e62-3448-40e7-a0e2-6eba66a6b93c)


## Jira Comments

> **Hans Wong** (2023-08-18):
>   Latest web frontend and API update fixing Jira issues   and  . CSBN_API-v1.5.1-2023-08-16.zip ChainStorePlus-v1.7.1-2023-08-16.zip [\\ds411\csms70\delivery\lands\UAT\Backend (Web)\2023-08-16]   172.16.138.65 is already updated.   Please test in QA environment, the above Jira issues address problem of no. 9 and 30-6 in below UAT report. UAT Cycle 1_v1.1

> **Sherman tse** (2023-09-01):
> Verified on UAT 10.77.227.28 UAT

## 相關資訊

- **Jira:** [BE-788](https://ctil.atlassian.net/browse/BE-788)
- **解決方式:** Done