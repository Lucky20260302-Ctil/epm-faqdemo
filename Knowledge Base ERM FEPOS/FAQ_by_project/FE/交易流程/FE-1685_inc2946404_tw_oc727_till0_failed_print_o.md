---
tags: [faq, fe, 交易流程]
component: "Day End"
symptom: "day end report print & re-print fail"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-1685
resolved: 2025-06-05
fix-version: ""
---

# FE-1685: INC2946404 - TW - OC727 Till0 failed print out dayend report

## 問題

day end report print & re-print fail
no issue in memo print

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2025-06-05
### Jira Comments (8 則)
**Joy Li** (2025-05-02):
Please foud  for the error detail. @@Sang
**Sang** (2025-05-07):
@@Joy Li @@Tovi Wang according to the log file, problem occurred in re-print day end, is there any problem when print day end in day end process?  Please get 2/May dbtrans.sdf, RP250502.dat, RP250502.xml and 2/5 others logs.
**Sang** (2025-05-13):
@@Tovi Wang Any update?
**Tovi Wang** (2025-05-13):
@@Sang I don’t know the issue details.Bellow details log for your reference.
@@Joy Li @@pierre.shi Do you have any operation for SOG ticket INC2946404?Could you help to share the details to Sang?Thanks!
**pierre.shi** (2025-05-13):
@@Tovi Wang  @@Joy Li  This issue is caused by that one printer has duplicated names in printer list.
1. 
2. 
Hi @@Sang  could you please help to check why one printer with several different names may cause this issue.
**Sang** (2025-05-13):
@@pierre.shi POS select printer which printer name contains the value defined in tblconfig. If more than one printer name match the selection, POS will use the first matching printer which may not be the one expected.
**Andrew_Au** (2025-06-05):
@@Joy Li @@Tovi Wang @@pierre.shi Please update the ticket status
**pierre.shi** (2025-06-05):
Hi @@Andrew_Au  please help to close this ticket.

## 相關資訊

- Jira: [FE-1685](https://ctil.atlassian.net/browse/FE-1685)
- Fix Version: 未記錄
- 解決日期: 2025-06-05
