---
tags: [faq, fe, 交易流程]
component: "Frontend"
symptom: "The Expiry Date after account creation is logged in is 1"
root-cause: "待提取"
solution: "### Jira Comments (2 則)"
jira: FE-1581
resolved: 
fix-version: ""
---

# FE-1581: WIAM, Once the account is logged in, check that the Expiry Date is different from what is described in the file

## 問題

The Expiry Date after account creation is logged in is 1
The document is set to 99

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (2 則)
**Andrew_Au** (2024-12-13):
The API create the new user set the password expiry “1” , according to the document should be set the value to “99”
**Bobby** (2024-12-13):
SRS updated. Use Tracking to check the changes. If you have any question, please let us know.

## 相關資訊

- Jira: [FE-1581](https://ctil.atlassian.net/browse/FE-1581)
- Fix Version: 未記錄
- 解決日期: 未記錄
