---
tags: [faq, fe, 交易流程]
component: "Front End"
symptom: "Case Details:"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-1126
resolved: 2024-05-06
fix-version: ""
---

# FE-1126: Enhance Coach Print Out Performance - Re-Get Member Name

## 問題

Case Details:
when POS retrieve Member information which is new created in e-Name platform, POS will get a temporary  value '-' assign to Member Last Name and first name.  In order to print the correct member name in receipt, POS will retrieve member name again in printing receipt process.
Improvement:
. Change to retrieve member name in confirm create invoice if the member name is start with '-' or is ''
~~ Change to retrieve member name in printing process  if the member name in sales journal is start with '~~' or is ''

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2024-05-06

## 相關資訊

- Jira: [FE-1126](https://ctil.atlassian.net/browse/FE-1126)
- Fix Version: 未記錄
- 解決日期: 2024-05-06
