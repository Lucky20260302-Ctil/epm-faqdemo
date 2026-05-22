---
tags: [faq, mp, 交易流程]
component: "MPOS"
symptom: "KSJ MPOS v75 MPOS search employee vip failed on 2025-02-28. Kindly help to check:"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: MP-751
resolved: 2025-05-02
fix-version: ""
---

# MP-751: [MPOS-80] MPOS 3.29.5 - KSJ search Employee vip failed

## 問題

KSJ MPOS v75 MPOS search employee vip failed on 2025-02-28. Kindly help to check:
Testing info:
IPA: MPOS v3.29.5 20250212.1
API: COACH_MPOSWebAPI_R3.29.5d
Testing machine: 172.24.253.69(C309) - Connect to apawiqwposweb01
Employee no: 205655

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2025-05-02
### Jira Comments (16 則)
**Tovi Wang** (2025-03-03):
@@Daniel Leung @@Cy Lau 2025-02-28 MPOS log for your further checking.Thanks!
**Tovi Wang** (2025-03-04):
@@Daniel Leung @@Cy Lau May I know anything update?Thanks!
**Daniel Leung** (2025-03-04):
@@Tovi Wang I can’t find any log about user requesting member-205655.  Can you double confirm the log is correct? Thank you
**Tovi Wang** (2025-03-05):
@@Daniel Leung Let me double check & confirm the log.
**Tovi Wang** (2025-03-05):
@@Daniel Leung Follow New MPOS logs for your further checking.Double checked the DAL log found the error info “C360 connection error (400) - BadRequest”.employee vip data should be come from ‘Till0 Local DBsse' instead of 'C360’.Please double check and confirm.Thanks!
**Daniel Leung** (2025-03-05):
@@Tovi Wang  Can you help check MposSeachStaffExact in dbConfig? Thank you
**Tovi Wang** (2025-03-05):
@@Daniel Leung
1.MposSeachStaffExact config setting is 'N' in DBsse.
2.NOT found MposSeachStaffExact config in DB dbConfig.
**Daniel Leung** (2025-03-05):
@@Tovi Wang  Please also help check OnlineCRMSystem in TblConfig
**Tovi Wang** (2025-03-06):
@@Daniel Leung OnlineCRMSystem config setting is 'C360' in Dbtrans Tblconfig.Shouldn't this place be set to C360?Please advice.
**Tovi Wang** (2025-03-06):
@@Daniel Leung May I know anything update please?Thanks!
**Daniel Leung** (2025-03-06):
@@Tovi Wang Seems a bug on MPOS API , still checking
**Tovi Wang** (2025-03-07):
@@Daniel Leung Please give me some update for today.Many Thanks!
CC @@Bobby @@Cy Lau
**Daniel Leung** (2025-03-07):
@@Tovi Wang It’s a MPOS API Bug, will be fixed on R30.
**Tovi Wang** (2025-03-07):
@@Daniel Leung Many Thanks for your double confirm.
Could you give me some details?such as IPA version?Which MPOS version?ETA?Then I can update the details to Coach team.
**Daniel Leung** (2025-03-13):
MPOS API - \\ds411\share\POS_MPOS_Release\3.29.X\3.29.5-20250313.1b1
IPA - [🔗](https://ios.ctil.com/mpos/PreCoach/)  - 3.29.5-2025.313.1
**Sherman tse** (2025-03-13):
Verified on QA
test case attached

## 相關資訊

- Jira: [MP-751](https://ctil.atlassian.net/browse/MP-751)
- Fix Version: 未記錄
- 解決日期: 2025-05-02
