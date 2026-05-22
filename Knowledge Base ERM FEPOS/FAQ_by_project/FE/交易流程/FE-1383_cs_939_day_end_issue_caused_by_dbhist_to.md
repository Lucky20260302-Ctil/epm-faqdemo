---
tags: [faq, fe, 交易流程]
component: "Day End"
symptom: "After issue sales memo, FE will insert record in jouprint table."
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-1383
resolved: 2024-05-24
fix-version: ""
---

# FE-1383: [CS-939] day end issue caused by dbhist too large

## 問題

After issue sales memo, FE will insert record in jouprint table.
Since the table will not purge, the size of dbhist.sdf is increased. Then cause day end issue.
Program will change:

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2024-05-24
### Jira Comments (7 則)
**Andrew_Au** (2024-05-13):
need to set dbtrans.tblconfig ENABLECACHEPRINTDATA=Y
**Andrew_Au** (2024-05-13):
Before Day End
after Day End
**Andy Ko** (2024-05-13):
sorry not sure why my computer was logged into Andrew’s account. These tests/comments are from me instead
**Joy Li** (2024-05-22):
@@Andy Ko Please prepare me a test report instead of upload image.
I need test report for release.
you may take a look the test report sample from Sherman. Please assign the Jira to me after you upload the test report.
Please upload the test report in excel or word file with below information
1. 
2. 
cc. @@Andrew_Au
**Joy Li** (2024-05-23):
@@Andy Ko Please share the testing report
**Andy Ko** (2024-05-23):
report: \\ds411\share\JIRA_Test_Report\20240523 Andy
**Joy Li** (2024-05-23):
test report checked

## 相關資訊

- Jira: [FE-1383](https://ctil.atlassian.net/browse/FE-1383)
- Fix Version: 未記錄
- 解決日期: 2024-05-24
