---
tags: [faq, fe, 交易流程]
component: "Front End"
symptom: "V7.5 After new log update cannot update records to tblNation_Detail table"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-1155
resolved: 2024-05-04
fix-version: ""
---

# FE-1155: cannot update the nationality display sequense records

## 問題

V7.5 After new log update cannot update records to tblNation_Detail table

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2024-05-04
### Jira Comments (2 則)
**Andrew_Au** (2022-10-05):
Did you means the default settint should be assign nationalitysorted="Y", if backend not define the nationality display value, FE will auto sort by nationality input sequense ?
-
**Sang** (2022-10-06):
Configuration Setting : NATIONALITYSORTEDBY
Nationality sort by (C/D/DS)  (Default C)
C - Code  D - Description S - Display Seq.

## 相關資訊

- Jira: [FE-1155](https://ctil.atlassian.net/browse/FE-1155)
- Fix Version: 未記錄
- 解決日期: 2024-05-04
