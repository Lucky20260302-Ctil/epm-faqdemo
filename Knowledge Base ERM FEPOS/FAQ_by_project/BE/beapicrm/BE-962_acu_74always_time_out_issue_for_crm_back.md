---
tags: [faq, be, beapicrm]
component: "Backend (ChainStorePlus 7.0)"
symptom: "_（Jira 中無 description 內容）_"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: BE-962
resolved: 2024-12-20
fix-version: ""
---

# BE-962: [ACU-74]Always Time out issue for CRM Backend Data Sync program in HK/MO QA

## 問題

_（Jira 中無 description 內容）_

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2024-12-20
### Jira Comments (9 則)
**Tovi Wang** (2024-12-05):
QA CRM log for your reference.@@Cy Lau
**Tovi Wang** (2024-12-05):
@@Cy Lau  Could you help to check the RCA and give some advice?Thanks!
**Cy Lau** (2024-12-05):
@@Anson Cheung  Please help to follow the RCA
**Anson Cheung** (2024-12-05):
Because the scan date range is extensive, need to increase the value of appsettings 'sqlCmdTimeout' to prevent timeout issue
**Cy Lau** (2024-12-09):
@@Anson Cheung 
Do suspect that the select distinct in where clause would trigger the issue, please help to do isolation checking for the sql :
1. 
2. 
3.
**Anson Cheung** (2024-12-09):
select distinct costs 95% of the query operation, while each select clause other than that costs 1%.
after trying to use temp table to separate the where clause and select distinct, the execution time has been reduced in my testing env.
**Anson Cheung** (2024-12-16):
<u>**Program Release V1.1.6**</u>
Release:
- 
Release notes:
- 
- 
-
**Sherman tse** (2024-12-19):
Verified on QA with 1.1.6
test case attached
**Joy Li** (2024-12-20):
Tested by @@Sherman tse  and released by @@Joy Li  on 2024-12-20

## 相關資訊

- Jira: [BE-962](https://ctil.atlassian.net/browse/BE-962)
- Fix Version: 未記錄
- 解決日期: 2024-12-20
