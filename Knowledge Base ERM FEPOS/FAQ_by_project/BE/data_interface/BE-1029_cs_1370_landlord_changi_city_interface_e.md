---
tags: [faq, be, data_interface]
component: "Data Interface"
symptom: "The landlord CHANGI CITY interface exported data from GentingHighlandsSalesUpload.exe is wrong / inc"
root-cause: "待提取"
solution: "### Jira Comments (4 則)"
jira: BE-1029
resolved: 
fix-version: ""
---

# BE-1029: [CS-1370] Landlord CHANGI CITY interface exported data is wrong

## 問題

The landlord CHANGI CITY interface exported data from GentingHighlandsSalesUpload.exe is wrong / inconsistent.
For the attached sample data on 20250228, we found below incorrect points.
Hour 14 - Payment data in column 11-17 looks correct (the same as DB). The sales without tax (column 6) is consistent with the payment data. But the tax (column 7) looks incorrect, which should be 44.26 instead of 72.17.
Hour 17 - The payment data is not matching DB data. The total sales and tax (column 6 and 7) are wrong / inconsistent with both column 11-17 and DB.
Hour 21 - The payment data is missing 1 record. The total sales and tax are correct.
Also attached records exported from DB for comparing.
Quickly checked other exported data, all have similar behavior.

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (4 則)
**Andrew_Au** (2025-10-08):
@@Tovi Wang  Please update the status
**Tovi Wang** (2025-10-09):
@@Andrew_Au Still under checking,Please hold on.
@@Joy Li  Please help to take a look this Jira CS-1370.Thanks!
**Andrew_Au** (2026-05-05):
@@Tovi Wang Please update the ticket status
**Tovi Wang** (2026-05-07):
@@Andrew_Au can be closed.

## 相關資訊

- Jira: [BE-1029](https://ctil.atlassian.net/browse/BE-1029)
- Fix Version: 未記錄
- 解決日期: 未記錄
