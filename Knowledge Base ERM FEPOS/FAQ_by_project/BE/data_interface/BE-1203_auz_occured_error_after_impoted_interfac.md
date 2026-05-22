---
tags: [faq, be, data_interface]
component: "Data Interface"
symptom: "[AUZ] Occured error after impoted interface file by Standard Data Interface script"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: BE-1203
resolved: 2026-05-05
fix-version: ""
---

# BE-1203: [AUZ] Occured error after impoted interface file by Standard Data Interface script

## 問題

[AUZ] Occured error after impoted interface file by Standard Data Interface script
Error occured in item master interface
Attached log file:

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2026-05-05
### Jira Comments (5 則)
**Bobby** (2025-11-05):
It is the import file incorrect format. The price field is missing the double quote and causes the error. The problem has been solved after added the double quote.
**Bobby** (2025-11-05):
I renamed the import file name to MASTERITEM_20201023131720.DAT and imported success.
**Automation for Jira** (2026-05-05):
Issue has been created since
Days since: 181
Week since : 25
Issue due date difference
Days since : 
Weeks since:
**Andrew_Au** (2026-05-05):
@@Bobby  Please update the ticket status
**Sherman tse** (2026-05-05):
issue handled by correct formart

## 相關資訊

- Jira: [BE-1203](https://ctil.atlassian.net/browse/BE-1203)
- Fix Version: 未記錄
- 解決日期: 2026-05-05
