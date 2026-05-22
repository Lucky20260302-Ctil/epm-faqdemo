---
tags: [faq, fe, 交易流程]
component: "Front End v750.01R01A"
symptom: "As B223 reported EWIN223PC1 got print day end issue - print to EPSON TM-L90 Label printer. But the c"
root-cause: "待提取"
solution: "### Jira Comments (3 則)"
jira: FE-1883
resolved: 
fix-version: ""
---

# FE-1883: HKJC REMS B223 Print Day End Issue

## 問題

As B223 reported EWIN223PC1 got print day end issue - print to EPSON TM-L90 Label printer. But the correct print queue should be OCB223MFD01. Tried to reprint day end, it seems only set OCB223MFD01 as default printer, then system able to print it in this print queue.

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (3 則)
**Bobby** (2026-02-10):
@@Sang @@Andrew_Au @@Cy Lau,@@Joy Li ,
Sang will prepare a testing program to trace the issue. Then we will arrange a remote session to store to troubleshoot the problem.
**Automation for Jira** (2026-02-10):
Issue has been created since
Days since: 0
Week since : 0
Issue due date difference
Days since : 2
Weeks since: 0
**Sang** (2026-02-10):
@@Bobby testing program and data uploaded to \\ds411\share\POS_FE_Release_64\20260210 REMS Print Day End Tester

## 相關資訊

- Jira: [FE-1883](https://ctil.atlassian.net/browse/FE-1883)
- Fix Version: 未記錄
- 解決日期: 未記錄
