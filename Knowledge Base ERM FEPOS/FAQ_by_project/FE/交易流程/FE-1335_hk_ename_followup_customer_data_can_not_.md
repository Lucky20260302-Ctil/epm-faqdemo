---
tags: [faq, fe, 交易流程]
component: "Front End"
symptom: "COACH JIRA: [CS-832](https://jira.tapestry.support/browse/CS-832)"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-1335
resolved: 2024-09-23
fix-version: ""
---

# FE-1335: HK eName FollowUp - customer data can not be queried

## 問題

COACH JIRA: [CS-832](https://jira.tapestry.support/browse/CS-832)
user search member in member panel. Always call API to search.
Do not use cache if user search in UI

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2024-09-23
### Jira Comments (1 則)
**Sang** (2024-01-29):
eName - Member Panel Search Member Online (Jira [🔗](https://ctil.atlassian.net/browse/FE-1335#icft=FE-1335) v720.02R28, v750.04R02)
a. Add tblconfig.OnlineMemberUseLocalCache (Default 'N') - 'Y' use OnlineMemberEnquiry data which cached on local DB, remove at dayend
b. tblconfig.OnlineMemberEnquity ='Y'
b1. online search first
b2. if (b1) not found, then search local DB if    tblconfig.ENNEWVIP ='Y' - New Member created in FE  or tblconfig.OnlineMemberUseLocalCache='Y' - use data cache before
c. tblconfig.OnlineMemberEnquiry ='N'  - Search Local DB first
- 
-

## 相關資訊

- Jira: [FE-1335](https://ctil.atlassian.net/browse/FE-1335)
- Fix Version: 未記錄
- 解決日期: 2024-09-23
