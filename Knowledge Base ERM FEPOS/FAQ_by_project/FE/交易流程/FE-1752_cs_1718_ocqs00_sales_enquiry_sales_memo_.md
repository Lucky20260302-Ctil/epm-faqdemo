---
tags: [faq, fe, 交易流程]
component: "Enquiry"
symptom: "Issue description:"
root-cause: "待提取"
solution: "### Jira Comments (8 則)"
jira: FE-1752
resolved: 
fix-version: ""
---

# FE-1752: [CS-1718] OCQS00 - Sales Enquiry - Sales Memo - Consolidation Issue

## 問題

Issue description:
Unable to proceed with Consolidation of Sales memo - Sales Inquiry for OCQS00 - Hong Kong Golden Image regression
Steps :
1. 
2. 
3. 
Expected:
Able to perform consolidation of available tills
Missing jouinvh in dbhist

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (8 則)
**Joy Li** (2025-09-18):
DAL log and build version is attached.
**Sang** (2025-09-18):
@@Joy Li Can’t find Create SSE dbhist.MDF record in DAL logs. It may created by other till which installed before this till.  Please copy DAL log from other tills also
**Automation for Jira** (2025-09-18):
Issue has been created since
Days since: 0
Week since : 0
Issue due date difference
Days since : 
Weeks since:
**Andrew_Au** (2025-09-18):
@@Sang The `jouinvh` table is rarely missing from `dbhist`, and this isn't a new problem. We still don't know why it fails to generate. iMX, ProRunner, HKJC, and Bash have all reported this in the past.
**Joy Li** (2025-09-19):
@@Sang  @@Andrew_Au
Only jouinh is missing. @@Andrew_Au  May i know if we can reproduce in our lab?
Once i delete the dbhist and Program re-create, the issue is resolved.
Sophia is asking RCA.
**Joy Li** (2025-09-19):
@@Sang
1. 
2.
**Andrew_Au** (2025-09-19):
@@Sang  We are still cannot reproduce the issue in the past. As I know sometimes missing create table missing this table when create the database table.
**Sang** (2025-09-22):
@@Joy Li This message is POS want to update jouinvh table schema but can’t found table in DB. I can’t find Create SSE dbhist.MDF record in DAL logs and the records in BuildVersion Table seems dbhist(SSE) was not created by POS v75 program.  It may created by other tills which installed before this till.  Please copy DAL log from all other tills also.

## 相關資訊

- Jira: [FE-1752](https://ctil.atlassian.net/browse/FE-1752)
- Fix Version: 未記錄
- 解決日期: 未記錄
