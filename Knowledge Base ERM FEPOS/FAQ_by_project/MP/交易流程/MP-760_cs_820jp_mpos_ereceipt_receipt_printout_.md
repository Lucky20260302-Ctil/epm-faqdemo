---
tags: [faq, mp, 交易流程]
component: "MPOS"
symptom: "Receipt printout is showing “レシート再印刷” on the popup after sales."
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: MP-760
resolved: 2025-05-02
fix-version: ""
---

# MP-760: [CS-820]JP | MPOS | eReceipt | Receipt printout popup is showing “レシート再印刷” after sales

## 問題

Receipt printout is showing “レシート再印刷” on the popup after sales.
Business would like to have it change to only “レシート” (Receipt) on the pop up.

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2025-05-02
### Jira Comments (8 則)
**Cy Lau** (2025-03-25):
@@Tovi Wang  @@Daniel Leung 
May I know why it will come back ?
fixed since 3.25…..
@@Tovi Wang  Please gather the version affected
**Daniel Leung** (2025-03-25):
@@Tovi Wang  May I know it’s the Local or SalesHub ? Thanks
**Tovi Wang** (2025-03-25):
@@Cy Lau I also want to know…
CC @@Bobby @@Jason Wu  FYI.
**Tovi Wang** (2025-03-25):
v3.29.5 & v3.30.2 both have this issue for JP region.@@Cy Lau @@Daniel Leung
**Daniel Leung** (2025-03-25):
@@Tovi Wang  Please get the MPOS API version, IPA version and dbCoachLocal.db.
**Sherman tse** (2025-03-25):
Printing flow with e-receipt for CJ:
1. 
2. 
3. 
4. 
5. 
6. 
Therefore, no dialog of the レシート再印刷 in the Printing flow with e-receipt
@@Tovi Wang Please help to comfirm above config if match with Coach region 18 side
using config:
ERECEIPTDISABLEPRINT= N
dbCoachLocal.db:
-
**Sherman tse** (2025-03-25):
If use extpected flow of Printing flow with e-receipt
Need to use fixed IPA app 3.30.2-20250325.3 that will be uploaded to coach side later
**Sherman tse** (2025-05-02):
Issue has fixed
Close case

## 相關資訊

- Jira: [MP-760](https://ctil.atlassian.net/browse/MP-760)
- Fix Version: 未記錄
- 解決日期: 2025-05-02
