---
tags: [faq, be, beapicrm]
component: "API"
symptom: "Error popped when user re-send e-receipt. (email send but error message popped)"
root-cause: "待提取"
solution: "### Jira Comments (2 則)"
jira: BE-1263
resolved: 
fix-version: ""
---

# BE-1263: [INC3572034] COACH AU OCFA221 re-send e-receipt error message pop

## 問題

Error popped when user re-send e-receipt. (email send but error message popped)
WA Log:
Send_eReceipt.Error: Arithmetic overflow error converting expression to data type nvarchar.Arithmetic overflow error converting expression to data type nvarchar.The statement has been terminated.The statement has been terminated.
TO -reproduce:
1. 
2.

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (2 則)
**Joy Li** (2026-05-05):
From @@Cy Lau  fixed "Arithmetic overflow error" caused by nvchar
\\ds411\share\POS_BE_Componenet_Release\BEAPI\eReceipRestfulService_260505
**Automation for Jira** (2026-05-06):
Issue has been created since
Days since: 0
Week since : 0
Issue due date difference
Days since : 
Weeks since:

## 相關資訊

- Jira: [BE-1263](https://ctil.atlassian.net/browse/BE-1263)
- Fix Version: 未記錄
- 解決日期: 未記錄
