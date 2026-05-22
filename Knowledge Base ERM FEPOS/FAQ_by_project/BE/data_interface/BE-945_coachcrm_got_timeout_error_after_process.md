---
tags: [faq, be, data_interface]
component: "Data Interface"
symptom: "[Coach][CRM ] Got timeout error after process Backend data sync"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: BE-945
resolved: 2024-11-18
fix-version: ""
---

# BE-945: [Coach][CRM ] Got timeout error after process Backend data sync

## 問題

[Coach][CRM ] Got timeout error after process Backend data sync
Reproduce steps:
1. 
2. 
3. 
Existing result:
- 
- 
Uploaded data:
vip_create_date = 2024-05-11 11:18:00.000
jouinv_date = 2024-05-11 00:00:00
jouinv_hour = 11
jouinv_mn = 17
Order id: 00033330
Member ID: OC135MIC0000017

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2024-11-18
### Jira Comments (3 則)
**Joy Li** (2024-11-18):
@@Anson Cheung Please advise what you changed
@@Sherman tse  Please start testing
**Anson Cheung** (2024-11-18):
@@Joy Li use EXISTS/NOT EXISTS to filter crmlog instead of LEFT JOIN crmlog table
**Sherman tse** (2024-11-18):
Verified on QA
Able to process backend data sync without timeout

## 相關資訊

- Jira: [BE-945](https://ctil.atlassian.net/browse/BE-945)
- Fix Version: 未記錄
- 解決日期: 2024-11-18
