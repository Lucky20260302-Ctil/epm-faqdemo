---
tags: [faq, fe, 交易流程]
component: "Front End"
symptom: "issue Detail:"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-1371
resolved: 2024-05-24
fix-version: ""
---

# FE-1371: [CS-1001] Issue_Contry Select setting is not working in Coupon setting RIN01324246

## 問題

issue Detail:
Coupon already setting as Courry Code is 30, but not able to use.
Workaround is changing setting to select country from 30 to 30.

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2024-05-24
### Jira Comments (6 則)
**Joy Li** (2024-04-29):
Copy from Tovi email,
KR store call out that The Promotion group of 'Contry Select' setting is not working in POS.Re-save the promotion group with 'Country' instead of 'Country Select' can fixed this issue.
So why The promotion group of 'Contry Select' setting is not working in POS?Could you help to double check?
We can reproduce this issue in QA.The reproduce step and screenshot as attachment word.
And The promotion Zlog for your reference.
**Andy Ko** (2024-05-14):
@@Joy Li seems like all show up now
tested on: 172.16.138.99 / 172.16.138.7
**Joy Li** (2024-05-23):
@@Andy Ko Please prepare me a test report instead of upload image.
I need test report for release.
you may take a look the test report sample from Sherman. Please assign the Jira to me after you upload the test report.
Please upload the test report in excel or word file with below information
1. 
2.
**Joy Li** (2024-05-23):
@@Andy Ko Please share the testing report
**Andy Ko** (2024-05-23):
report: 
\\ds411\share\JIRA_Test_Report\20240523 Andy
**Jason Wu** (2024-05-23):
checked is ok

## 相關資訊

- Jira: [FE-1371](https://ctil.atlassian.net/browse/FE-1371)
- Fix Version: 未記錄
- 解決日期: 2024-05-24
