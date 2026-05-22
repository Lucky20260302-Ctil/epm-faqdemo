---
tags: [faq, be, polling]
component: "polling"
symptom: "Issue Detail"
root-cause: "待提取"
solution: "### Jira Comments (13 則)"
jira: BE-1146
resolved: 
fix-version: ""
---

# BE-1146: [CS-1479] Issue_PRC_Member update information will send to FE by Zlog file

## 問題

Issue Detail
Conformed in Current CS2000 version C/B/V/A member information update will be send to FE by Zlog

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (13 則)
**Tovi Wang** (2025-07-10):
@@Cy Lau @@Joy Li  Internal Jira here.Please help to further checking.If need other info please ping me.Thanks!
**Joy Li** (2025-07-14):
@@Jerry Wong i checked that current send log program will send member master which member type should eb “NOT downlaod”. May i know if you need the log for checking>?
cc @@Tovi Wang
**Jerry Wong** (2025-07-14):
@@Joy Li I need the log, and also what is the Date modified of the prj_di8004.dll
**Automation for Jira** (2025-07-14):
Issue has been created since
Days since: 4
Week since : 0
Issue due date difference
Days since : 
Weeks since:
**Jerry Wong** (2025-07-14):
@@Joy Li the vip type is “NOT downlaod” = ‘Y' is also not update dbtmnlog_gen to 'X’ when send log in QA?
**Joy Li** (2025-07-14):
i remember that we tested in QA beofre. it should work in QA.
**Jerry Wong** (2025-07-14):
@@Joy Li QA and prod are same version?
**Tovi Wang** (2025-07-21):
@@Jerry Wong @@Joy Li May I know anything update for this case?Which version?FE version or BE version?
**Jerry Wong** (2025-07-21):
@@Tovi Wang Can I have the data of dbtmnlog, vip and viptyp which is supposed not in the Zlog but sent to FE? 
I want to insert to my local db and do the test in my envionment
**Tovi Wang** (2025-07-22):
@@Jerry Wong Follow dbtmnlog data for your further checking.Thanks!
select * from dbtmnlog where dbtmnlog_date >= '2025-07-01' and dbtmnlog_record_key in (select vip_no from vip where vip_type in ('C','V')) and dbtmnlog_gen = 'Y'
**Tovi Wang** (2025-08-26):
@@Jerry Wong May I know if anything new found for this issue?Please help to share the investigate progress.Thanks!
CC @@Joy Li
**Andrew_Au** (2025-10-08):
@@Tovi Wang @@Joy Li Please update the status
**Tovi Wang** (2025-10-09):
Duplicate with [🔗](https://ctil.atlassian.net/browse/FE-1717),Let us follow up this issue in [🔗](https://ctil.atlassian.net/browse/FE-1717),Please closed this one first.

## 相關資訊

- Jira: [BE-1146](https://ctil.atlassian.net/browse/BE-1146)
- Fix Version: 未記錄
- 解決日期: 未記錄
