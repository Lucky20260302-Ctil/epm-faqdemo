---
tags: [faq, fe, 交易流程]
component: "Front End"
symptom: "After voiding a transaction that has PP pay code (burn points), then the void transaction will retur"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-1438
resolved: 2024-07-09
fix-version: ""
---

# FE-1438: [HKJC] REMS void memo will always return error message even though API returned sucess

## 問題

After voiding a transaction that has PP pay code (burn points), then the void transaction will return a failure message, even though the API returned a success. It is blocking our system from completing the void transaction.

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2024-07-09
### Jira Comments (1 則)
**Sang** (2024-06-27):
'v750.01R02G
1.

## 相關資訊

- Jira: [FE-1438](https://ctil.atlassian.net/browse/FE-1438)
- Fix Version: 未記錄
- 解決日期: 2024-07-09
