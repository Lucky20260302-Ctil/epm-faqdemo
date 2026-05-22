---
tags: [faq, fe, 交易流程]
component: "Front End"
symptom: "Day end issue is caused by missing sales . The missing memo is fail to post due to different incorre"
root-cause: "待提取"
solution: "### Jira Comments (12 則)"
jira: FE-1769
resolved: 
fix-version: ""
---

# FE-1769: Posting Error by incorrect Sales code

## 問題

Day end issue is caused by missing sales . The missing memo is fail to post due to different incorrect sales staff code.
The issue is happen after JP upgrade to V75 last week.
|  |  |  |  |
| --- | --- | --- | --- |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (12 則)
**Joy Li** (2025-10-08):
@@Sang@@Cy Lau
Please help for this issue.
**Automation for Jira** (2025-10-09):
Issue has been created since
Days since: 0
Week since : 0
Issue due date difference
Days since : 
Weeks since:
**Sang** (2025-10-09):
@@Joy Li @@Tovi Wang  Please get dbtbk07.sdf, DbHist20251007.zip, all 2025-10-07 logs and PCD from J859 Till 0,
**Joy Li** (2025-10-09):
@@pierre.shi  Please help to get all log files from J859 till 0 on 2025-10-07.
Also please copy dbhist and dbtbk07 to Sang.
|  |  |  |  |
| --- | --- | --- | --- |
**pierre.shi** (2025-10-09):
Hi @@Joy Li  @@SangThe logs have been uploaded.
**pierre.shi** (2025-10-09):
Hi @@Joy Li  @@SangThe logs have been uploaded.
**Joy Li** (2025-10-09):
@@Sang  Log copied
**Sang** (2025-10-09):
From J859 T9 Log file record change sales staff from [539583] To [53958]
**Sang** (2025-10-09):
@@pierre.shi @@Joy LiPlease get dbtbk06.sdf, DbHist20251006.zip, all 2025-10-06 logs and PCD from J805 Till 0,
**pierre.shi** (2025-10-10):
Hi@@Sang logs uploaded.
**Sang** (2025-10-13):
From J805 T9251006.dat, change staff code from [AA] to [523520]
J805 Till 0, 2025-10-06, SA ‘523520’ have ff tx
+ @@pierre.shiPlease help to check J805 Till 0 dbmas.tblsalady table, Is Staff [523520] record available in [tblsalady] table ?
**pierre.shi** (2025-10-20):
@@Sang can’t be found in tblsalady

## 相關資訊

- Jira: [FE-1769](https://ctil.atlassian.net/browse/FE-1769)
- Fix Version: 未記錄
- 解決日期: 未記錄
