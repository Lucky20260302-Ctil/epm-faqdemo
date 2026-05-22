---
tags: [faq, fe, 交易流程]
component: "Front End"
symptom: "there' are 2 issues on Prorunner (store: P10) on 27 Nov 2025:"
root-cause: "待提取"
solution: "### Jira Comments (6 則)"
jira: FE-1823
resolved: 
fix-version: ""
---

# FE-1823: No data shown on 員工考勤 report & no option of location selection when doing transfer memo

## 問題

there' are 2 issues on Prorunner (store: P10) on 27 Nov 2025:
1. 
2. 
please have a look, logs and related files provided, thank you.

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (6 則)
**Sang** (2025-11-28):
@@Angela Chan Please get Nov-26 & 27 logs and PC251126.dat , PC251127.dat
**Sang** (2025-11-28):
@@Angela Chan please get Nov-26 & 27 all logs, RP files, PC files and dbtrans.sdf.
**Angela Chan** (2025-11-28):
@@Sang
please find P10 ZIP file, let me know if still need others, thank you
**Sang** (2025-11-28):
@@Angela Chan if we can re-produce 'no option of location selection when doing transfer memo', then copy back dbmas.mdf (SSE)
**Automation for Jira** (2025-11-28):
Issue has been created since
Days since: 0
Week since : 0
Issue due date difference
Days since : 
Weeks since:
**Sang** (2025-11-28):
After Nov-26 Day end process has been completed, POS has not auto terminated. Nov-26 POS instance continuous operate on Nov-27 (ref: T9251126.dat)
this when Staff ‘1033’ signed-in @10:37:39, POS log the sign-in pos date still 2025/11/26, and caused sub-sequence abnormal records.  I can’t find any log records why POS has not terminated after day-end and can’t re-produce this issue.  Let us keep monitoring first

## 相關資訊

- Jira: [FE-1823](https://ctil.atlassian.net/browse/FE-1823)
- Fix Version: 未記錄
- 解決日期: 未記錄
