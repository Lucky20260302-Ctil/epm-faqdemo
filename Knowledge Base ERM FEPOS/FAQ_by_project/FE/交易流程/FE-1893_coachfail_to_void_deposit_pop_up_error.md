---
tags: [faq, fe, 交易流程]
component: "Front End"
symptom: "[Coach]Fail to void Deposit & pop up error"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-1893
resolved: 2026-02-26
fix-version: ""
---

# FE-1893: [Coach]Fail to void Deposit & pop up error

## 問題

[Coach]Fail to void Deposit & pop up error
vm:
172.16.138.131
.\sxd
Yan20201104@
Version: 7.5.0.4R21 (Build 260210)
Sales lady: 405342  Yy000000

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2026-02-26
### Jira Comments (4 則)
**Automation for Jira** (2026-02-26):
Issue has been created since
Days since: 0
Week since : 0
Issue due date difference
Days since : 
Weeks since:
**Sang** (2026-02-26):
@@Sherman tse In the testing db. Last Deposit Memo No. is 00001137, but in dbtrans.sdf, the last till 0 deposit no. is 00001138.  Please change last deposit no. seq. syscon_dep_no setting to continuous testing.
**Sang** (2026-02-26):
@@Sherman tse Updated program uploaded to \\ds411\share\POS_FE_Release_64\20260226  Coach v750.04R21 - ANZ
1.
**Sherman tse** (2026-02-26):
Verified OK on QA

## 相關資訊

- Jira: [FE-1893](https://ctil.atlassian.net/browse/FE-1893)
- Fix Version: 未記錄
- 解決日期: 2026-02-26
