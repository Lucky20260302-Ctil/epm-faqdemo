---
tags: [faq, fe, 交易流程]
component: "Front End"
symptom: "Dear @@Sang"
root-cause: "待提取"
solution: "### Jira Comments (10 則)"
jira: FE-1540
resolved: 
fix-version: ""
---

# FE-1540: RIN01408980 - PRC - OCF29 - CS2000 - FE : member show offline on CS2000 FE

## 問題

Dear @@Sang
For sample VIP No : OCF13H00276576
OCF29 PCE Till6 call out “会员升级信息(离线)” when searched out vip data in 2024-10-22 14:56,
But issue resumed in  2024-10-22 15:20,We NOT do any operation.
Could you help to double check the root cause?And how to avoid this issue in later?
Dear @@Jason Wu
I provided the logs to you by zoom.
1.OCF29 PCE till6 “会员升级信息(离线)”，
2.But issue resumed in  2024-10-22 15:20,We NOT do any operation.
3.RIN01407061,HK OCF1 callout the same issue on 17 Oct.

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (10 則)
**Sang** (2024-10-25):
@@Jason Wu please copy log to me. thanks
**Tovi Wang** (2024-10-25):
@@Sang Could you also please help to clarify follow Lein’s question?Thanks!
**Sang** (2024-10-25):
POS retrieve data which show in ‘Member Upgrade Message’ by direct connect to Backend DB.
**Sang** (2024-10-25):
**Sang** (2024-10-25):
OCF HK @ 18-Oct have abnormal condition:
**Sang** (2024-10-25):
17-Oct 12:14-20:35 connect to backend has problem.
**Sang** (2024-10-25):
OCF 1 Till 7 18-Oct fail to connect BE DB
**Tovi Wang** (2024-11-07):
@@Joy Li As talked in before,This is member offline issue.
Issue Backaround:
When first time check member in Cloud member region，FE will get member data from BE and insert this member to temp table,Member will show online since it is connected with BE.
If search this member again, FE will get this member data from temp table and will show offline since it is not connected with BE.
So Please help to double check this issue with @@Sang  and  how we can optimize the logic?
**Andrew_Au** (2025-02-24):
@@Tovi Wang Can I close the ticket ?
**Tovi Wang** (2025-02-24):
@@Andrew_Au Because CN V75 store will catch the member data from CRM,So will NOT have this issue in V75.Please closed this ticket.

## 相關資訊

- Jira: [FE-1540](https://ctil.atlassian.net/browse/FE-1540)
- Fix Version: 未記錄
- 解決日期: 未記錄
