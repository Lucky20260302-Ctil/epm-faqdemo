---
tags: [faq, mp, 交易流程]
component: "MPOS, MPOS API"
symptom: "_（Jira 中無 description 內容）_"
root-cause: "待提取"
solution: "### Jira Comments (13 則)"
jira: MP-744
resolved: 
fix-version: ""
---

# MP-744: [CS-1339]Took approx 3mins to search for VIP on mPOS

## 問題

_（Jira 中無 description 內容）_

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (13 則)
**Cy Lau** (2025-02-01):
Let me add some more explanation, the customer was found right away after input the cell phone number but the scren stuck in "Loading" (Pls refer below screenshot)
It took approx 3mins to get to below screen to attach the customer to the transaction. We did not see such an issue in QA
**Cy Lau** (2025-02-03):
@@Tovi Wang @@pierre.shi  @@Jason Wu
as mentioned in CS-1339 , please gather the logs for investigation
**Cy Lau** (2025-02-03):
The log showing there would be a error occurs during the time:
(dont mind the GetToken_C360....it is just the last event, It should be calling API for getting memberDetails)
This error Err: A task was canceled. is suspected as timeout .
After the first GetToken_C360.End, it shall calling the API for getting MemberDetails, after more than 1mins 40sec , the task was reported as cancelled.
---
The next step would be futher tracing if the timeout occurs :
1. 
1. 
---
Seems the POS_API not in the same timezone with the MPOS_API log,
Please also get the 27-01 POS_API log
@@Jason Wu  @@Tovi Wang  @@pierre.shi
**Jason Wu** (2025-02-04):
@@Cy Lau Logs copied & sent by teams.
**Cy Lau** (2025-02-26):
For record:
26-Feb 0102
**Cy Lau** (2025-02-28):
for record 28-Feb:
**Cy Lau** (2025-03-04):
FOR RECORD :
**Cy Lau** (2025-03-04):
For cipher issue / investigation
**Tovi Wang** (2025-03-06):
@@Cy Lau WA log waiting SOG team upload.other log pass to you first.
**Tovi Wang** (2025-03-06):
@@Cy Lau 没有03-05的WA log,只有03-06的WA log.Please check.
**Andrew_Au** (2025-10-06):
@@Tovi Wang Please update the status
**Andrew_Au** (2025-10-08):
@@Tovi Wang  Please update status
**Tovi Wang** (2025-10-09):
Fixed,Please closed.

## 相關資訊

- Jira: [MP-744](https://ctil.atlassian.net/browse/MP-744)
- Fix Version: 未記錄
- 解決日期: 未記錄
