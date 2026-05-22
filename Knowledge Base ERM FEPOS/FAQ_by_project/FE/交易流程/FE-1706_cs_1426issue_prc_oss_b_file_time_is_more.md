---
tags: [faq, fe, 交易流程]
component: "Front End"
symptom: "Issue Detail:"
root-cause: "待提取"
solution: "### Jira Comments (5 則)"
jira: FE-1706
resolved: 
fix-version: ""
---

# FE-1706: [CS-1426]Issue_PRC OSS_B file time is more than 30 minutes

## 問題

Issue Detail:
we have found OSS_B was delay over 30 minutes on 20250422 22:00
please kindly find root cause.
1.double confirm 2025-05-2 OSS_B posting 也有这个情况,看来应该是每天都有。好像只是晚上10点以后有这个奇怪的现象，没有任何error 和 terminated.（初步怀疑是晚上10点以后 CN店铺集中开始做dayend,然后 posting file比较多）
2.sample: acp20250528212521.OC105___1
进posting时就已经delay了40多分钟,
ACP file里是dayend info.
use csdata11_70select * from pstlog with (nolock) where pstlog_date = '2025-05-28' and pstlog_node = 'OSS_B'order by pstlog_date desc, pstlog_time ASC
select * from sqlpcdossb---update sqlpcda set sqlpcd_post = 'E'  where sqlpcd_post_ref like 'acp20250528212521.OC105___1'
3.到polling 已经delay 30多分钟了

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (5 則)
**Tovi Wang** (2025-05-30):
@@Joy Li  As talked in yesterday.The issue still happend in everyday.Bellow polling & posting log for your further checking.
.
**Andrew_Au** (2025-06-05):
@@Tovi Wang @@pierre.shi @@Joy Li Please update the ticket status
**Tovi Wang** (2025-08-29):
Need to double check and confirm.Please hold on.
**Tovi Wang** (2025-09-10):
Program released on 2025-07-03
RCA: OSS token expiry and caused polling fail + too many dummy stx file
Program Enhance:
- 
- 
- 
It was already deployed to PR.Not delay now.Can be closed now.
**Automation for Jira** (2025-09-10):
Issue has been created since
Days since: 102
Week since : 14
Issue due date difference
Days since : 
Weeks since:

## 相關資訊

- Jira: [FE-1706](https://ctil.atlassian.net/browse/FE-1706)
- Fix Version: 未記錄
- 解決日期: 未記錄
