---
tags: [faq, fe, 交易流程]
component: "Day End"
symptom: "Will jump 2 rows if  type 'Enter' instead of 1 row in CASH Denomination"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-1901
resolved: 2026-03-25
fix-version: ""
---

# FE-1901: [CS-2058] Issue_ANZ_INC3434107_Question about Day END Cash Balancing

## 問題

Will jump 2 rows if  type "Enter" instead of 1 row in CASH Denomination
Troubleshooting:
1. 
2.E.g. Enter quantity of 5 cents for 5, then we tick "Enter", it jump to 20cents instead of next row (10 cents).

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2026-03-25
### Jira Comments (7 則)
**Joy Li** (2026-03-17):
***COACH testing PC 10.34.103.17***
- 
Use Tab >> go to next line >> Result OK
Use Enter >> go down 2 line >> Result Fail
**Joy Li** (2026-03-17):
@@Joy Li
Sanyo QAQC testing PC
- 
Use Tab >> go to next line >> Result OK
Use Enter >> go to next line  >> Result OK
**Automation for Jira** (2026-03-18):
Issue has been created since
Days since: 0
Week since : 0
Issue due date difference
Days since : 
Weeks since:
**Sang** (2026-03-18):
@@Joy Li
1.
**Sherman tse** (2026-03-24):
Tested with different input mathod, found that used with non-ENG method would reproduce the issue with release R22 Build 260324
**Sang** (2026-03-24):
@@Sherman tse @@Cy Lau  @@Joy Li @@Bobby
CASH Denomination Input UI - Change to manual focus next denominationinput control
Program uploaded to \\ds411\share\POS_FE_Release_64\20260324 Coach v750.04R22 - 3
**Sherman tse** (2026-03-24):
Verified ok on QA

## 相關資訊

- Jira: [FE-1901](https://ctil.atlassian.net/browse/FE-1901)
- Fix Version: 未記錄
- 解決日期: 2026-03-25
