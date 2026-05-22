---
project: BE
title: "BE-962: [ACU-74]Always Time out issue for CRM Backend Data Sync program in HK/MO QA"
issue_key: BE-962
issue_type: Bug PRD
status: Closed
faq_score: 6.5
faq_category: 04_Data_Sync
faq_category_label: 資料與同步
tags: [faq, be, data_sync, backend-(chainstoreplus-7.0)]
jira_url: "https://ctil.atlassian.net/browse/BE-962"
created: 2024-12-05
resolved: 2024-12-20
resolution: Done
has_images: False
---

# BE-962: [ACU-74]Always Time out issue for CRM Backend Data Sync program in HK/MO QA

## 問題描述

None


## Jira Comments

> **Tovi Wang** (2024-12-05):
> QA CRM log for your reference.  

> **Tovi Wang** (2024-12-05):
>   Could you help to check the RCA and give some advice?Thanks!

> **Cy Lau** (2024-12-05):
>   Please help to follow the RCA

> **Anson Cheung** (2024-12-05):
> Because the scan date range is extensive, need to increase the value of appsettings 'sqlCmdTimeout' to prevent timeout issue

> **Cy Lau** (2024-12-09):
>   Do suspect that the select distinct in where clause would trigger the issue, please help to do isolation checking for the sql : Each Select Clause time consumption , (especially select district ) Each Union Clause  Combinations of the each 

> **Anson Cheung** (2024-12-09):
> select distinct costs 95% of the query operation, while each select clause other than that costs 1%. after trying to use temp table to separate the where clause and select distinct, the execution time has been reduced in my testing env.

> **Anson Cheung** (2024-12-16):
> Program Release V1.1.6   Release: \\ds411\public\anson\CRMSanyoPhaseInterface  \CRMSanyoPhaseInterface_v1.1.6.zip   Release notes: group the items in program level instead of using sql distinct to prevent duplicate items  [BE-964] sql enhancement: create temp table to filter jouinv_date and remove select distinct  [BE-962 ] support the end of filtered date range by set the new appsettings config "toDate"

> **Sherman tse** (2024-12-19):
> Verified on QA with 1.1.6 test case attached  

> **Joy Li** (2024-12-20):
> Tested by    and released by    on 2024-12-20

## 相關資訊

- **Jira:** [BE-962](https://ctil.atlassian.net/browse/BE-962)
- **解決方式:** Done