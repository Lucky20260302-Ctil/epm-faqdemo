---
tags: [faq, mp, 交易流程]
component: "MPOS API"
symptom: "Owing to the Config calling from Lic DB ,"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: MP-643
resolved: 2024-11-06
fix-version: ""
---

# MP-643: Lic Config Migration

## 問題

Owing to the Config calling from Lic DB ,
The grace period would not be effective if the Lic DB is not available in terms of db failure or connection issue.
According to the record, the configs are seldom adjusted , added or removed. It is suggested that to put a static sqlite file to replace the Lic DB connection with following advantages :
1) Less development efforts
2) Less testing efforts
3) Reduce network IO

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2024-11-06

## 相關資訊

- Jira: [MP-643](https://ctil.atlassian.net/browse/MP-643)
- Fix Version: 未記錄
- 解決日期: 2024-11-06
