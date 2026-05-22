---
tags: [faq, fe, 交易流程]
component: "Front End"
symptom: "in CSplus v75, the history log will be zipped into retdata6/history and should be purged periodicall"
root-cause: "待提取"
solution: "### Jira Comments (1 則)"
jira: FE-1819
resolved: 
fix-version: ""
---

# FE-1819: incomplete log purging in frontend Retdata6/history

## 問題

in CSplus v75, the history log will be zipped into retdata6/history and should be purged periodically based on configutation DELETEHISTORYPERIOD.
However, it is found that in Coach CN Prod frontend, the zipped NPOS, UploadPCD and WA logs have not been purged even passed the house keeping period.
Hence require modifying the frontend to include those logs into housekeeping cycle.

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (1 則)
**Automation for Jira** (2025-12-29):
Issue has been created since
Days since: 33
Week since : 4
Issue due date difference
Days since : 
Weeks since:

## 相關資訊

- Jira: [FE-1819](https://ctil.atlassian.net/browse/FE-1819)
- Fix Version: 未記錄
- 解決日期: 未記錄
