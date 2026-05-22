---
tags: [faq, mp, 系統兼容]
component: "Backend"
symptom: "1.ACP2025062910224698.J450_M file里的 J450-MB002294 data 导致了posting terminate."
root-cause: "待提取"
solution: "### Jira Comments (1 則)"
jira: MP-784
resolved: 
fix-version: ""
---

# MP-784: [CS-1336]Coach JP MQ_A terminate issue

## 問題

1.ACP2025062910224698.J450_M file里的 J450-MB002294 data 导致了posting terminate.
Posting error:
ACP2025062910224698.J450_M Start Processing
[TERMINATE(3)]/ExecuteReader requires the command to have a transaction when the connection assigned to the command is in a pending local transaction.  The Transaction property of the command has not
What’s mean this error?
2.查询PCD file里面此memo的data，发现有一个24 code这行数据。其它没有发现明显异常。

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (1 則)
**Tovi Wang** (2025-07-01):
this is know issue and fixed in Coach Jira CS-1336.Closed internal Jira.
CC @@Joy Li @@pierre.shi

## 相關資訊

- Jira: [MP-784](https://ctil.atlassian.net/browse/MP-784)
- Fix Version: 未記錄
- 解決日期: 未記錄
