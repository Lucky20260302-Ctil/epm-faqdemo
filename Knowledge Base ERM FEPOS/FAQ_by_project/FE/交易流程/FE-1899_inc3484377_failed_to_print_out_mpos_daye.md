---
tags: [faq, fe, 交易流程]
component: "Front End v750.01R01A"
symptom: "failed to print out mpos dayend report. but can print out by redo dayend on the next day."
root-cause: "待提取"
solution: "### Jira Comments (8 則)"
jira: FE-1899
resolved: 
fix-version: ""
---

# FE-1899: [INC3484377] failed to print out mpos dayend report

## 問題

failed to print out mpos dayend report. but can print out by redo dayend on the next day.
check the T9 log, has timeout error:

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (8 則)
**Automation for Jira** (2026-03-12):
Issue has been created since
Days since: 0
Week since : 0
Issue due date difference
Days since : 
Weeks since:
**Sang** (2026-03-12):
@@pierre.shi Please check does table ‘Invtrx file header’ exist in dbtrans SSE (Till 0 OCF50\SQLEXPRESS)
**pierre.shi** (2026-03-13):
Hi@@Sang this table exists in dbtrans sse(OCF50\SQLEXPRESS\)
**Sang** (2026-03-13):
@@pierre.shi 裏面有冇mpos 開的小票。如果沒有，drop 掉sse 的dbtrans database, restart pos 讓pos 重新建立一個新的dbtrans
**pierre.shi** (2026-03-13):
@@Sang 这个issue发生在10.11号两天，也就是说，如果现在正常了，就不需要这样操作了，对吗？
**Sang** (2026-03-13):
@@pierre.shi 對的
**pierre.shi** (2026-04-07):
Hi @@Sang this issue occurred again.
PRC POS V75 while printint mpos dayend report, will show error:
the error is similar with [🔗](https://ctil.atlassian.net/browse/FE-1590)
Ths logs has been uploaded as attachment.
**pierre.shi** (2026-04-10):
Hi @@Sang  any update for this issue

## 相關資訊

- Jira: [FE-1899](https://ctil.atlassian.net/browse/FE-1899)
- Fix Version: 未記錄
- 解決日期: 未記錄
