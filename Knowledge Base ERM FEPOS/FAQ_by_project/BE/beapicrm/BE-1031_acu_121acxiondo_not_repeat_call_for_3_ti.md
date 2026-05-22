---
tags: [faq, be, beapicrm]
component: "API"
symptom: "Check whether current program will repeat call for 3 times if there is return error from CRM API:"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: BE-1031
resolved: 2025-05-02
fix-version: ""
---

# BE-1031: [ACU-121][Acxion]Do not repeat call for 3 times when receive 400 error from CRM 

## 問題

Check whether current program will repeat call for 3 times if there is return error from CRM API:
1. 
2. 
HTTPStatusCode : 400,404, 500 no need to trigger the retry

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2025-05-02
### Jira Comments (2 則)
**Anson Cheung** (2025-03-21):
Release:
[\\ds411\public\samuel\beapi\v1.7.10_20250319](file://ds411/public/samuel/beapi/v1.7.10_20250319)
- 
- 
-
**Sherman tse** (2025-05-02):
verified on qa
test case attached
Close case

## 相關資訊

- Jira: [BE-1031](https://ctil.atlassian.net/browse/BE-1031)
- Fix Version: 未記錄
- 解決日期: 2025-05-02
