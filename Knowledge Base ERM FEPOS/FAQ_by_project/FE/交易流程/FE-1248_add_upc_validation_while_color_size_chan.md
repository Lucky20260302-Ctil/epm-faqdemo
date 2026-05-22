---
tags: [faq, fe, 交易流程]
component: "Front End"
symptom: "OCF95-10025549"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-1248
resolved: 2024-09-23
fix-version: ""
---

# FE-1248: Add UPC validation while color size change

## 問題

OCF95-10025549
Refer to log, we found that user selected CI059 Col='UYP' & size='9   B' by Barcode scan.
Then change the size code to '8.5B' manually. Since CI059 'UYP' '8.5B' is valid item color size but no UPC.
We do NOT have UPC validation while color size change.

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2024-09-23
### Jira Comments (1 則)
**Joy Li** (2023-05-19):
Sang will change in V72.02R3.23 and V7.5

## 相關資訊

- Jira: [FE-1248](https://ctil.atlassian.net/browse/FE-1248)
- Fix Version: 未記錄
- 解決日期: 2024-09-23
