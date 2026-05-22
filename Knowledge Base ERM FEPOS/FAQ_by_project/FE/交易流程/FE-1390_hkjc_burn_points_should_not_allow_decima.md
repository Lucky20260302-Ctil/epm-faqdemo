---
tags: [faq, fe, 交易流程]
component: "Front End"
symptom: "When inputting amount for burn points, the lowest value should be 1, but currently the system allows"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-1390
resolved: 2024-06-12
fix-version: ""
---

# FE-1390: HKJC burn points should not allow decimals

## 問題

When inputting amount for burn points, the lowest value should be 1, but currently the system allows decimal:

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2024-06-12
### Jira Comments (2 則)
**Andy Ko** (2024-05-21):
@@Sang I tested inputting 1.50 for BP amount , and it rounded to 2. Is this based on the rounding flag in config?
**Sang** (2024-05-23):
1.

## 相關資訊

- Jira: [FE-1390](https://ctil.atlassian.net/browse/FE-1390)
- Fix Version: 未記錄
- 解決日期: 2024-06-12
