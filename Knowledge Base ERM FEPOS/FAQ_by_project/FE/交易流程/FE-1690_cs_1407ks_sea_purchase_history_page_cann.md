---
tags: [faq, fe, 交易流程]
component: "Frontend"
symptom: "**KSG801** 172.24.253.2 ; Member ID: **01402951** FE version: **V75.004.1100.0008**"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-1690
resolved: 2025-08-29
fix-version: ""
---

# FE-1690: [CS-1407]KS SEA - Purchase history page cannot show up after upgrading to v75.004.1100.0008

## 問題

**KSG801** 172.24.253.2 ; Member ID: **01402951** FE version: **V75.004.1100.0008**
**Steps**: Searching member ID, and then click the ‘purchase history’ function,404 error occurred.
but in the old version: **V75.004.0702.0000,** the function is working well.

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2025-08-29
### Jira Comments (11 則)
**Tovi Wang** (2025-05-09):
Hi @@Sherman tse As talked in teams,PLease help to confirm if can reproduce this issue in our QA env.If anything other question,please ping me.Thanks!
CC @@Cy Lau @@Joy Li
**Tovi Wang** (2025-05-15):
@@Sherman tse  May I know anything update for this issue?Could we reproduce this issue in our side?Sophia is asking me.Thanks!
**Sherman tse** (2025-05-16):
@@Tovi Wang
I remote into coach VM:
KSG- KSG801        172.24.253.2
I met the issue and I try to ping the ip:  [qaksjcs2000.katespade.com](http://qaksjcs2000.katespade.com), it returned timeout
The testing VM seems fail to connect the  [qaksjcs2000.katespade.com](http://qaksjcs2000.katespade.com) casuing 404 error in member purchase histroy
**Tovi Wang** (2025-05-16):
@@Sherman tse Many Thanks for your double confirm.
@@Cy Lau @@Anson Cheung Could you help to further checking and advice?Thanks!
CC @@Joy Li
**Tovi Wang** (2025-06-24):
@@Cy Lau  May I know anything update for this one?Or could you give me some advice?Thanks!
CC @@Joy Li @@Sherman tse
**Sherman tse** (2025-07-21):
\\ds411\public\daniel\membersion\purchaseHistory\build_20250721_v0.0.5
**Sherman tse** (2025-07-22):
Issue has been created since
Days since: 74
Week since : 10
Issue due date difference
Days since : 
Weeks since:
**Sherman tse** (2025-07-22):
verified on Tapestry side QA with webview V0.0.5 (memberson)
**Joy Li** (2025-07-24):
@@Sherman tse  Please prepare the test case for this ticket.
i will check with TP for release timeline.
**Sherman tse** (2025-07-24):
@@Joy Li  Test case attached
**Tovi Wang** (2025-08-29):
Coach QA testing passed.Can be closed.

## 相關資訊

- Jira: [FE-1690](https://ctil.atlassian.net/browse/FE-1690)
- Fix Version: 未記錄
- 解決日期: 2025-08-29
