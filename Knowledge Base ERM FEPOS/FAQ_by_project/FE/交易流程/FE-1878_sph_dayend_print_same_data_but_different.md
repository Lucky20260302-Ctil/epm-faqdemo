---
tags: [faq, fe, 交易流程]
component: "Day End"
symptom: "Here is the different printout"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-1878
resolved: 2026-02-11
fix-version: ""
---

# FE-1878: [SPH] Dayend Print - Same Data but different printout in V72 & V75

## 問題

Here is the different printout
v75:
v72
The point is
1. 
And
2.The report of **v75 till all display 0% gift cert**.
Here is the Retdata6 after dayend:
\\172.16.183.201\localuser\sportshouse\Temp\72afterdayend.zip

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2026-02-11
### Jira Comments (4 則)
**Sang** (2026-02-05):
@@Joseph_Hu V75 is 3-Jan report, v72 is 2-Jan report. Please verify
**Sang** (2026-02-05):
@@Joseph_Hu Revised program uploaded to \\ds411\share\POS_FE_Release_64\20260205 v750.05R07 - SPH
**Joseph_Hu** (2026-02-05):
Fixed
After revised V75:
till all display normally
**Automation for Jira** (2026-02-05):
Issue has been created since
Days since: 1
Week since : 0
Issue due date difference
Days since : 
Weeks since:

## 相關資訊

- Jira: [FE-1878](https://ctil.atlassian.net/browse/FE-1878)
- Fix Version: 未記錄
- 解決日期: 2026-02-11
