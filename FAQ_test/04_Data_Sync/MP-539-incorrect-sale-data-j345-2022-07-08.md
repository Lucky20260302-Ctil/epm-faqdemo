---
project: MP
issue_key: MP-539
issue_type: Bug PRD
status: Closed
tags:
- 04_data_sync
- data_sync
- faq
- localiis
- mp
- mpos-api
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/MP-539
created: '2022-07-12'
resolved: '2024-03-06'
fix_version: ''
components: []
has_images: false
category: 04_Data_Sync
category_label: 資料同步
quality: partial
title: 'MP-539: Incorrect sale data: J345 2022-07-08'
---
# MP-539: Incorrect sale data: J345 2022-07-08

## 問題描述

J345-MA005279

2022-07-08

Local IIS 3.14.0




## Jira Comments

> **Joy Li** (2022-07-12):
> \\172.16.183.201\localuser\support\JIRA_DB\MP-539\
 IIS Log and dbSSE dbtran and dbhist copied

> **Sang** (2022-07-20):
> [3.19.0] 1.Adding fields back for miscalculations bug fixes (CY Lau: 20220714 Jira  /Jira  / )  1) Product.cs  2) Memos.cs  3) Shared.cs : ConvertSalesItem2Product, ConvertProduct2SalesItem, ConvertProduct2SalesItem,ConvertMemoData2SalesData 2. Write Disc Analysis for Tax Exempted MM Memo Disc Memo Fixed (KTS 220714 v72.02R18, v750.02 )

## 相關資訊

- **Jira:** [MP-539](https://ctil.atlassian.net/browse/MP-539)
- **解決方式:** Done