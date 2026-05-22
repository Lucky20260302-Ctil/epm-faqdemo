---
tags: [faq, mp, 交易流程]
component: "MPOS"
symptom: "Hi [Joy Li](https://jira.tapestry.support/secure/ViewProfile.jspa?name=Joy_Li) [Tovi Wang](https://j"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: MP-780
resolved: 2025-07-04
fix-version: ""
---

# MP-780: [MPOS-101]KSJ MPOS - v3.29.5f invalid member type issue

## 問題

Hi [Joy Li](https://jira.tapestry.support/secure/ViewProfile.jspa?name=Joy_Li) [Tovi Wang](https://jira.tapestry.support/secure/ViewProfile.jspa?name=Tovi_Wang) (CC:[Shie Saito](https://jira.tapestry.support/secure/ViewProfile.jspa?name=ssaito%40tapestry.com) ), kindly help to confirm with Sherman, since during testing we found same issue as ~~[CS-1424](https://jira.tapestry.support/browse/CS-1424)~~ for KSJ v75 MPOS. Member able to select but when go to payment page, it will show below error.
Testing info:
Testing machine IP: 172.24.253.69(C309) - connect to apawiqwposweb01, UI log uploaded.
IPA Version: v3.29.5-20250325.4
API Version: COACH_MPOSWebAPI_R3.29.5f
Testing vip no: 1173942824[202506111801210000.mp4](https://jira.tapestry.support/secure/attachment/957195/957195_202506111801210000.mp4)

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2025-07-04
### Jira Comments (9 則)
**Tovi Wang** (2025-06-12):
@@Daniel Leung @@Cy Lau As talked in teams,Please help to update the issue details here.Thanks!
CC @@Joy Li
**Tovi Wang** (2025-06-12):
@@Daniel Leung All logs in internal Jira [🔗](https://ctil.atlassian.net/browse/MP-770).
**Daniel Leung** (2025-06-12):
hot fix version uploaded to [🔗](https://ios.ctil.com/mpos/PreCoach/)  - 3.29.6-20250612
**Tovi Wang** (2025-06-12):
@@Cy Lau @@Joy Li @@Sherman tse Please help to arrange testing and provide the ETA.Thanks!
**Joy Li** (2025-06-12):
@@Daniel Leung APi or IPA? Please advise. Thanks.
**Daniel Leung** (2025-06-12):
@@Joy Li ipa
**Tovi Wang** (2025-06-17):
@@Joy Li @@Sherman tse As talked in teams meeting.Dev team has provided the hot fix.Please help to arrange the ETA.
The issue reproduce steps video as follow.Please FYI.If anything other question please ping me.Thanks!
**Sherman tse** (2025-06-23):
Excuted regression test only, as our testing lab is out of white list, we cannot test with C360 member searching.
Regession test case attached
**Joy Li** (2025-07-04):
IPA released on 2025-06-23 by Joy

## 相關資訊

- Jira: [MP-780](https://ctil.atlassian.net/browse/MP-780)
- Fix Version: 未記錄
- 解決日期: 2025-07-04
