---
tags: [faq, be, beapicrm]
component: "API"
symptom: "- "
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: BE-1039
resolved: 2025-10-06
fix-version: ""
---

# BE-1039: [ACU-127]Offloading the Upsert Process to a Separate Async Service

## 問題

- 
- 
- 
- 
- 
Offloading the member upsert would be considered as Sync-Member-Upsert and Async-Member-Upsert as diagram:

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2025-10-06
### Jira Comments (5 則)
**Cy Lau** (2025-03-28):
@@Anson Cheung  Please help to do the testing , then merge and build to @sherman  for testing
[http://172.16.138.42:3000/ERM/BEAPI.git](http://172.16.138.42:3000/ERM/BEAPI.git)
Current Branch : 
acxiom_crm_async_service
ETA for QAQC: 31 Mar-1Apr
**Anson Cheung** (2025-03-28):
Release
[\\ds411\public\samuel\beapi\v1.7.14_20250328](file://ds411/public/samuel/beapi/v1.7.14_20250328)
- 
- 
@@Sherman tse Please prepare for testing
**Sherman tse** (2025-04-01):
Verified on QA
attached test case
**Cy Lau** (2025-04-08):
\\ds411\public\samuel\beapi\v1.7.16_20250408
**Andrew_Au** (2025-10-06):
@@Sherman tse  Please update the status

## 相關資訊

- Jira: [BE-1039](https://ctil.atlassian.net/browse/BE-1039)
- Fix Version: 未記錄
- 解決日期: 2025-10-06
