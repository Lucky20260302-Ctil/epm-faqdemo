---
tags: [faq, fe, 交易流程]
component: "Frontend"
symptom: "Member A0004-01"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-971
resolved: 2021-05-13
fix-version: ""
---

# FE-971: Deposit Settlement should apply new CRM option UI (same as issuing Sales Memo)

## 問題

Member A0004-01
v720.01R03A (Build 210329)
When issue sales memo, the Email CRM will show in the Send e-Receipt box, but when issue Deposit Settlement,  the Email CRM will not show in the Send e-Receipt box for the same member
Sale Memo
Deposit Settlement Memo

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2021-05-13
### Jira Comments (2 則)
**Sang** (2021-05-10):
v720.01R03B
1. MM Calc - Cache Datatable [Mix Product] and [ Mix Discount] in order sequence to avoid wrong calculation in sequence (KTS 210408 Jira 944 v710.02R14ZA, v720.01R03B, v720.02R02, v720.02R03, v720.02R6E, 0.02R07H, v750.01R01A)
2. JC Deposit Settlement - Send e_Receipt UI show Member Email address fixed (KTS 210507 v720.01R03B, R04, v750.01R01A Jira [🔗](https://ctil.atlassian.net/browse/FE-971#icft=FE-971))
**howard** (2021-05-13):

## 相關資訊

- Jira: [FE-971](https://ctil.atlassian.net/browse/FE-971)
- Fix Version: 未記錄
- 解決日期: 2021-05-13
