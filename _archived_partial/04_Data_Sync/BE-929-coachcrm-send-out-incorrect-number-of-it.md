---
project: BE
issue_key: BE-929
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
jira_url: https://ctil.atlassian.net/browse/BE-929
created: '2024-11-01'
resolved: '2024-11-04'
fix_version: ''
components: []
has_images: false
category: 04_Data_Sync
category_label: 資料同步
quality: partial
title: 'BE-929: [Coach][CRM] Send out incorrect number of items to CRM side by CRMSanyoPhaseInterface'
---
# BE-929: [Coach][CRM] Send out incorrect number of items to CRM side by CRMSanyoPhaseInterface

## 問題描述

Reproduce steps:

1. Upload an order to Backend DB e.g.: OC135MNC0000013 has 1 item

2. Send the order to CRM by CRMSanyoPhaseInterface

3. Check customer history

Existing result:

Send out incorrect number of items to CRM side by CRMSanyoPhaseInterface

1. e.g.: sent OC135MNC0000013  with 2 items to CRM




## Jira Comments

> **Sherman tse** (2024-11-04):
> Verified on QA close case

## 相關資訊

- **Jira:** [BE-929](https://ctil.atlassian.net/browse/BE-929)
- **解決方式:** Done