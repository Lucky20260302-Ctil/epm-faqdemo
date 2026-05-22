---
tags: [faq, fe, 交易流程]
component: "Front End"
symptom: "ImagineX side have upgraded the FE version to 7.1.0.02R14ZP, but seems like the same issue."
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-1312
resolved: 2024-03-05
fix-version: ""
---

# FE-1312: IMX V71 posting error "Return Voucher or gift cert amount not matched"

## 問題

ImagineX side have upgraded the FE version to 7.1.0.02R14ZP, but seems like the same issue.
I have copied the logs to below path, please have a look.
\\172.16.183.201\localuser\support\20231108\cmstpe430

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2024-03-05
### Jira Comments (2 則)
**Sang** (2023-11-14):
Problem due to fail to change PCD Delimiter settng (tblconfig.ZlogFileType) from 'F' (Fixed Length) to 'D' (Tab Delimiter)
**Sang** (2023-11-14):
Solution:
1. 
2.

## 相關資訊

- Jira: [FE-1312](https://ctil.atlassian.net/browse/FE-1312)
- Fix Version: 未記錄
- 解決日期: 2024-03-05
