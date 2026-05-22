---
tags: [faq, fe, 交易流程]
component: "Enquiry, Frontend"
symptom: "Till often prompts standalone mode when store processing CashDrawBalance enquiry."
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-1524
resolved: 2025-03-07
fix-version: ""
---

# FE-1524: RIN01389185 - PRC - OCF47  - CS2000 - FE : All Till often prompts standalone mode when store processing CashDrawBalance enquiry 

## 問題

Till often prompts standalone mode when store processing CashDrawBalance enquiry.
Current total 3 stores call out the same issue.
RIN01389185,  OCF47 
RIN01403186,  OCF26
RIN01404389,  OCF8
POS version : 72.0221.0102

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2025-03-07
### Jira Comments (20 則)
**Tovi Wang** (2024-10-16):
@@Sang Could you help to check the root cause and provide long term solution?
@@Jason Wu I provide OCF47 & OCF26 logs to you by zoom.Please send it to sang.Thanks!
**Tovi Wang** (2024-10-16):
@@Sang logs copied in \\172.16.183.201\localuser\support\20241016\Sang,Please check.
**Tovi Wang** (2024-10-17):
@@Sang Email “RIN01389185 - CN OCF47 Store feedback that All Till often pop out standalone mode“ for your reference.
**Tovi Wang** (2024-11-06):
@@Sang Could you help to prepare the tools to test this issue?Because the issue is still ongoing.
CC: @@Joy Li@@Jason Wu @@pierre.shi  FYI.
**Cy Lau** (2024-11-15):
Hi all,
After investigation, the explanation is as below:
With log analysis:
The SQL execution time exceeded 30 sec limitations in DBHist/DBSSE for building transaction summary for other Tills
All the evidence points towards DBSSE, the SQLExpress performance. I would suggest the next action point would be obtain the EventLogs of SQLExpress to see if any clues about the SQL Execution. @@Joy Li  @@Jason Wu 
@@Sang  The Extend Calculate Consolidated Cash Drawer Balance Enquiry Execute Time , have it been applied in 72 ? And seems the 30sec isn’t enough tho……
**Tovi Wang** (2024-12-04):
@@Cy Lau @@Sang  OCF8 Till0 have the time out error in 30/11/2024 21:13:03.And I found the clues about the SQL Execution when time out error happend again.
1.From T9 log,We can see the doRefresh.Error in 30/11/2024 21:13:03.
2.From Npos log,We can see the time out error when excute follow SQL.
3.From trace log,We can see the dbsse is excuting the same sql in 30/11/2024 21:13:03
So from up log,can we confirm the RCA and new advice to coach team?
CC: @@Joy Li @@Jason Wu @@pierre.shi FYI.
**Tovi Wang** (2024-12-04):
Up OCF8 Till0 11-30 log for your reference.
**Cy Lau** (2024-12-05):
@@Tovi Wang  Yes , your Server Profile helps a lot, it is owing to the SQL execution timeout,
In latest v75 has extended the execution timeout.
+ @@pierre.shi
**Tovi Wang** (2024-12-05):
@@Cy Lau Many Thanks for your confirmation.
But I don't think extend the execution timeout is the optimal solution. Because the SQL execution performance issue is not resolved, the store will still call out in future.
For example, when searching for CashDrawBalance, Store need to load for 30s to 1min, which the store still cannot accept. Can we optimize and improve the performance of SQL execution statements to shorten search time？which is the ultimate expected result for the store.
**Cy Lau** (2024-12-05):
For the optimization, I would put it into the backlog or roadmap
TBH, how many stores did call out for this issue out of total deployed store.
**Tovi Wang** (2024-12-05):
So far,
1.For V72 version,More than 3 stores call out this issue.
2.for V75 version,One KMY720 store(FE-1576) also wish to optimize and improve the performance of SQL execution statements to shorten search time.
Jira [🔗](https://ctil.atlassian.net/browse/FE-1576) for your reference
**Tovi Wang** (2024-12-05):
In latest v75 has extended the execution timeout.
→ @@Cy Lau May I know which V75 version has has extended the execution timeout? For All region?
**Sang** (2024-12-10):
1.
**Tovi Wang** (2024-12-13):
Dear @@Cy Lau  For bellow 2 released.May I know the ETA?Thanks!
1.For the time out error:
--->We will Extend Calculate Consolidated Cash Drawer Balance Enquiry Execute Time to 30 Sec.
Target released in v750.04R08+, v750.05
ETA:???
2.For long loading issue:
--->dbHist.[Return Voucher] Add Index RetVon_Redeem_Loc () to improve Cash Balance Enquiry Calc Performance.
Target released in DB Ver 007.001.003.088
ETA:???
**Andrew_Au** (2024-12-24):
@@Tovi Wang  Please update the ticket status
**Sherman tse** (2025-01-24):
Issue is related to [🔗](https://ctil.atlassian.net/browse/FE-1590)
Close case
**Andrew_Au** (2025-02-12):
@@Sherman tse  Please update the ticket status
**Andrew_Au** (2025-03-06):
@@Tovi Wang @@pierre.shi  Should I change the ticket status to close
**Tovi Wang** (2025-03-07):
@@Andrew_Au Please close.
**Andrew_Au** (2025-03-07):
Thanks

## 相關資訊

- Jira: [FE-1524](https://ctil.atlassian.net/browse/FE-1524)
- Fix Version: 未記錄
- 解決日期: 2025-03-07
