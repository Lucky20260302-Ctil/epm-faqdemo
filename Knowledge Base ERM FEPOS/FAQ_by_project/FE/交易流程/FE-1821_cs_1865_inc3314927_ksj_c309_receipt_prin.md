---
tags: [faq, fe, 交易流程]
component: "Day End"
symptom: "**Scope of Analysis**"
root-cause: "待提取"
solution: "### Jira Comments (3 則)"
jira: FE-1821
resolved: 
fix-version: ""
---

# FE-1821: [CS-1865] INC3314927 KSJ C309 Receipt Print performance issue

## 問題

**Scope of Analysis**
The printing process was reviewed based on transaction save and receipt printing. We identified that transaction save includes two components:
1. 
2. 
During the investigation, we observed that the Member Data Upload step contributes significantly to the overall time.
**Performance Comparison (Logs from 2025-11-24):**
Store C309 shows slightly higher median and average times compared to C318, especially during member data upload.
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
As  @@Sang mentioned that
tblconfig.WebApiUpdateNewMember has been created to suppress call web API to upsert member when create new TX. However, this config was only applied to CS2000, CSPLUS, AXIOM CRM.  
**C360 and Memberson** has not applied this enhancement yet.

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (3 則)
**Sang** (2025-11-28):
v750.04R13E1
1. 
Source code uploaded to
1. 
2. 
3.
**Automation for Jira** (2025-11-28):
Issue has been created since
Days since: 0
Week since : 0
Issue due date difference
Days since : 
Weeks since:
**Andrew_Au** (2026-05-05):
@@Sherman tse  Please update the ticket status

## 相關資訊

- Jira: [FE-1821](https://ctil.atlassian.net/browse/FE-1821)
- Fix Version: 未記錄
- 解決日期: 未記錄
