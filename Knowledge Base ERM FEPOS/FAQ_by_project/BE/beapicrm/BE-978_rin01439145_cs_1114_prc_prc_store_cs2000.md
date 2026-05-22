---
tags: [faq, be, beapicrm]
component: "Backend (ChainStorePlus 7.0)"
symptom: "1. "
root-cause: "待提取"
solution: "### Jira Comments (19 則)"
jira: BE-978
resolved: 
fix-version: ""
---

# BE-978: [RIN01439145] [CS-1114]- PRC - PRC_Store - CS2000 - Posting : Posting Main terminated

## 問題

1. 
2.Stucked by PCD file pcd20250106143014.OCF523__0.The file data seems normal.
3.I just only can find the joupay data for memo OCF523 - 00017460 in DB.Missing jouinv data & joudis data for the memo.
psterr table error info “Cannot insert duplicate key row in object 'dbo.joupay' with unique index 'Ijoupa”

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (19 則)
**Tovi Wang** (2025-01-06):
@@Cy Lau 明天帮忙看下这个issue。polling log我明天copy 发你。谢谢！
CC: @@Joy Li @@pierre.shi @@Jason Wu  FYI.
**Tovi Wang** (2025-01-07):
Coach Jira [CS-1114](https://jira.tapestry.support/browse/CS-1114)
**Tovi Wang** (2025-01-07):
@@pierre.shi  Please also provide the polling log here.Thanks!
**pierre.shi** (2025-01-07):
Hi All, polling logs have been uploaded as attachment in ticket.
**Tovi Wang** (2025-01-07):
@@Cy Lau Please help to check this issue with high priority,Coach Jira CS-1114 for your reference.
CC @@Joy Li  FYI.Please assist.
**Cy Lau** (2025-01-08):
can it be resolved by clear record and repost ?
@@Tovi Wang
**Tovi Wang** (2025-01-08):
@@Cy Lau Yes,you are right.The temp work around is that removed the stuck file firstly,then delete the incorrect joupay data and re-import the PCD file.This issue happend in before and Coach Team urge require us to find the root cause and thoroughly resolve it. Because it can lead to CN posting terminated and dayend issues.
**Tovi Wang** (2025-02-05):
@@Cy Lau@@Jason Wu  Please help to investgate this issue and provide the long term solution.Because issue still happening.
Add 2 same issue on 02 Feb:
1.RIN01448832,OCF18-00054574
2.RIN01448835,OCF1-30538764
CC: @@pierre.shi
**Tovi Wang** (2025-02-05):
I suspect it is the same RCA with jira BE-977.All belong to posting issue.But the issue symptoms are different.Please FYI.
**Tovi Wang** (2025-02-05):
@@Cy Lau @@Joy Li Could you help to double confirm The issue if is already fixed in FE release V75 and BE hot fix?If yes,Let me updated to Coach team and keep monitoring the issue in V75.
**Cy Lau** (2025-02-05):
From our log :
CY 241004
1. 
2. 
3. 
4. 
---
And at 250117, Dev Team received bug reports and release a hotfix:
# "**1.25.01.1700"**
CY 250117 1) bug fixing for pstlog_dbObj shared conn instance causing crash 2) redefine version as ver.yy.mm.dd{build}
2025-01-17 pstlog_dbObj - make new connection 1) Fix issue - BE-976 RIN01434568-COACH JP Posting MQ_A&MQ_01 terminated
**Cy Lau** (2025-02-06):
In fact , if they are using the version since delay with random jitter :
the LHS would be the last few digits of the jouinv_key,   the RHS would be the delay in ms
**Tovi Wang** (2025-02-06):
@@Cy Lau Thanks for your details clarify.Let us keep monitoring in V75 store.
**Andrew_Au** (2025-02-24):
@@Tovi Wang Can I close the ticket ?
**Tovi Wang** (2025-02-24):
@@Andrew_Au Still keep monitoring in CN V75 store if have this issue or NOT.
**Andrew_Au** (2025-02-24):
I close the ticket first.
**Automation for Jira** (2025-12-11):
Issue has been created since
Days since: 338
Week since : 48
Issue due date difference
Days since : 
Weeks since:
**pierre.shi** (2025-12-11):
Hi @@Cy Lau This issue occurred again in PRC region, pos V75.
[INC3342923]
**pierre.shi** (2025-12-11):
logs uploaded

## 相關資訊

- Jira: [BE-978](https://ctil.atlassian.net/browse/BE-978)
- Fix Version: 未記錄
- 解決日期: 未記錄
