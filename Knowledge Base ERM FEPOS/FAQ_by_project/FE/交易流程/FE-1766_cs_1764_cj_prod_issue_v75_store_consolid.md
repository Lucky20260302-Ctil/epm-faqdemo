---
tags: [faq, fe, 交易流程]
component: "Front End"
symptom: "related SOG ticket:"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-1766
resolved: 2025-10-16
fix-version: ""
---

# FE-1766: [CS-1764] CJ Prod issue_V7.5 store consolidated dayend missing sub till data

## 問題

related SOG ticket:
INC3224817 (store: J841, missing date: 9/29-9/30 of Till 2)
INC3224738  (store: J724, missing date: 9/29-9/30 of Till 2)
INC3223640  (store: J721, missing date: 9/29-9/30 of Till 2 & 3)
INC3229180  (store: J853, missing date: 10/2 of Till 2)
Symptom:
Till 2 sales data cannot reflected on consolidation dayend report
Tested by Joy (use 29/9 as example):
1. 
2. 
3.

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2025-10-16
### Jira Comments (8 則)
**Automation for Jira** (2025-10-06):
Issue has been created since
Days since: 2
Week since : 0
Issue due date difference
Days since : 
Weeks since:
**Sang** (2025-10-06):
@@Angela Chan @@Joy Li Code review found out that if process consolidated day end before sub till complete day end, V75 POS fail to alert missing till message. Please compare dayend time of till 0 and missing till to verify is this the root cause.
**Sang** (2025-10-06):
@@Joy Li @@Angela Chan @@Sherman tse
Enhanced program uploaded to \\ds411\share\POS_FE_Release_64\20251006 Coach v750.04R14D
v750.04R14D
1. 
2.
**Sang** (2025-10-08):
@@Cy Lau This function backup dbtrans.sdf before start day end process, the backup file then copy to main till after till day end complete. Main till use this sub till backup file to do consolidate process
**Sang** (2025-10-08):
@@Cy LauWhen main till do consolidated day end process, this function handle main till copy sub till backup [dbtrans.sd](http://dbtrans.sd)f from sub till to main till, and check the sub till db pos date to ensure the backup file is the correct one
**Cy Lau** (2025-10-08):
Suspected also related to the performance of window API of file handling : 
Copy, delete
and, there’s insignificant logging to show the polling from SubTill by MainTill after exist checking and validation.
**Cy Lau** (2025-10-08):
Updates :
Mainly : 
adding exist checking after operation.
for copying : length check and checksum validation applied.
**Joy Li** (2025-10-16):
Released in V75.004.1404.0000 on 2025-10-15

## 相關資訊

- Jira: [FE-1766](https://ctil.atlassian.net/browse/FE-1766)
- Fix Version: 未記錄
- 解決日期: 2025-10-16
