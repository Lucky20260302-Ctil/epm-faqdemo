---
tags: [faq, fe, 交易流程]
component: "Frontend"
symptom: "@@Cy Lau"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-1699
resolved: 2025-05-30
fix-version: ""
---

# FE-1699: [CS-1441]KR QA PC - First open CSPLUS will pop out follow error after dayend

## 問題

@@Cy Lau
KR QA PC - First open CSPLUS will pop out follow error after dayend.
I checked FE log but NOT found relates error.Please help to further checking.
Testing QA PC:KR        OCQ96-0        10.33.248.10
CC @@Joy Li

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2025-05-30
### Jira Comments (5 則)
**Cy Lau** (2025-05-26):
250526 : using init everytime to overcome the issue:
\\ds411\share\POS_FE_Release_64\20250526 Coach KR TMU PrintAgent
set or add “IsForceToInitSQLite“ = 'N' to disable autoInit, default always Init
Testing case:
#1 DayEnd of CSPLUS
#2 Reopen CSPLUS whether the error pops out
above unit test has been conducted on the same TP QAQC VM on 20250526
**Tovi Wang** (2025-05-26):
@@Cy Lau  Many Thanks for your update.But Sophia ask how do we fixed  this issue?What’s the RCA?
她问可不可以先把change 给rollback 回去？正式released版本给到他们之后她在测试。
**Cy Lau** (2025-05-26):
RCA : With unknown reason ( which happens only on that environment, cannot be reproduced in SY QAQC vm ) the PrintRequest table required by X32TMUPrintAgent does not exist in the record sqlite.
Fixes : ensure the completeness of the record sqlite, each action of X32TMUPrintAgent will health check and repair the record sqlite.
**Tovi Wang** (2025-05-26):
@@Cy Lau Many Thanks for your details clarify.
**Tovi Wang** (2025-05-27):
@@Cy Lau @@Joy Li As Sophia’s request.Follow 2 Jira issue for KR enhancement.Please help to combine into one package released to Coach QA.Thanks!
CS-1440
CS-1441

## 相關資訊

- Jira: [FE-1699](https://ctil.atlassian.net/browse/FE-1699)
- Fix Version: 未記錄
- 解決日期: 2025-05-30
