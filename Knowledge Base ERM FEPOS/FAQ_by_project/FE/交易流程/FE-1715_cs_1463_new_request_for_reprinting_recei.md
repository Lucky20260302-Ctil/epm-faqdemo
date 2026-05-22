---
tags: [faq, fe, 交易流程]
component: "Front End"
symptom: "When we are doing the store visit, we hear about the request from store that they don't want to have"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-1715
resolved: 2025-07-15
fix-version: ""
---

# FE-1715: [CS-1463] New Request for Reprinting receipt

## 問題

When we are doing the store visit, we hear about the request from store that they don't want to have both store and customer receipt for reprinting from outlet.
but for retail, we need to have both store and customer in receipt.
for TMU, we'd like to have 3 options by xconfig as only store receipt, only customer receipt and both store and customer receipt.
The enhancement would be happened for TMU and Re-printing functions only

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2025-07-15
### Jira Comments (9 則)
**Sang** (2025-06-20):
@@Sherman tse Coach/KS all region exclude JP print both Store and Customer Receipt copy; JP have more other copies.  Please clarify this enhancement need to apply to which region and is this for re-printing only or both print /Re-printing.
**Sang** (2025-06-20):
@@Sherman tse Further, Sales / Service / Gift Certificate and Customer Receipt  (tblconfig.EnableCustomerPrintReceipt='Y') Module print both Store and Customer Copy. Is this control logic applies to all these module ?
**Sherman tse** (2025-06-20):
@@Sang This reprint enhancement cover all Coach execpt CoachJP
**Cy Lau** (2025-06-23):
For Coach (Exclude JP)
Current:
1. 
2. 
3. 
The Re-print function also serve as a fallback in case Print function not working.
The following would be the proposed enhancement:
Objective :
1. 
2. 
By ENABLECUSTOMERPRINTRECEIPT='Y'
::plus:: CUSTOMERPRINTRECEIPTTYPE=S/C/ALL
StoreFront could using “Reprint“ for reprint all copies
”Print Customer Receipt” for xconfig controlled output
**Sang** (2025-06-24):
1.
**Cy Lau** (2025-06-27):
@@Sang 
Release
\\ds411\share\POS_FE_Release_64\20250624 Coach v750.04R13D
**Sherman tse** (2025-07-15):
Veifired on QA FE POS
Test case attached
mpos still testing completed on 15 Jul
**Joy Li** (2025-07-15):
Issue has been created since
Days since: 25
Week since : 3
Issue due date difference
Days since : 
Weeks since:
**Joy Li** (2025-07-15):
FE package V75.004.1503.0000 is released on 2025-07-15
-

## 相關資訊

- Jira: [FE-1715](https://ctil.atlassian.net/browse/FE-1715)
- Fix Version: 未記錄
- 解決日期: 2025-07-15
