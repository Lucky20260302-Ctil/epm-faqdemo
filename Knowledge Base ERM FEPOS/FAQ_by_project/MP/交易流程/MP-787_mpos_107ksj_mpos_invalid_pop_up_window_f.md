---
tags: [faq, mp, 交易流程]
component: "MPOS"
symptom: "hi [Joy Li](https://jira.tapestry.support/secure/ViewProfile.jspa?name=Joy_Li) [Tovi Wang](https://j"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: MP-787
resolved: 2025-07-29
fix-version: ""
---

# MP-787: [MPOS-107]KSJ MPOS - Invalid pop-up window for '領収書印刷‘ function

## 問題

hi [Joy Li](https://jira.tapestry.support/secure/ViewProfile.jspa?name=Joy_Li) [Tovi Wang](https://jira.tapestry.support/secure/ViewProfile.jspa?name=Tovi_Wang) (CC:[Shie Saito](https://jira.tapestry.support/secure/ViewProfile.jspa?name=ssaito%40tapestry.com) )Could you please help to check below issue for KSJ:
**QA Testing info:**
IPA Version: v3.29.6-20250703.1
API Version: COACH_MPOSWebAPI_R3.29.5f
Testing machine: C309(172.24.253.69) - connect to apawiqwposweb01, UI log already uploaded.

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2025-07-29
### Jira Comments (12 則)
**Tovi Wang** (2025-07-21):
@@Daniel Leung MPOS login page which contain the APP version and Server version information for your further checking.Thanks!
CC @@Joy Li
**Daniel Leung** (2025-07-21):
@@Tovi Wang Since there are two version of 3.29.6 (20250612.1 & 20250703.1 ) on [🔗](https://ios.ctil.com/mpos/Coach/) , please make sure QA is using 20250703.1. 
I have tested both version on my side, 20250612.1 has this problem but 20250703.1 has not.
**Tovi Wang** (2025-07-21):
@@Daniel Leung Thanks for your double confirm.Let me double confirm with Coach QA team.
**Tovi Wang** (2025-07-22):
@@Daniel Leung Could you help to double check and confirm IPA version 20250703.1 fixed this issue or not?Coach QA uninstall the IPA version,then reinstall,But issue still.
**Daniel Leung** (2025-07-22):
@@Tovi Wang Is it come from reprint page? This memo is sales/void/deposit? Please also copy the dbCoachLocal.db from MPOS API. Thank you
**Tovi Wang** (2025-07-22):
@@Daniel Leung Should be come from sales memo,Testing video for your reference.I am copying the dbCoachLocal.db
[ImportedSegment.774496761.103281.mov](https://ourtapestry-my.sharepoint.com/:v:/g/personal/nliu2_tapestry_com/EWRcRWsi-edBlNDrSNQaQ3wB3hYQigJCTAHrEnD7UZ6zkA?e=Ll1pXp&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0%3D)
**Tovi Wang** (2025-07-22):
@@Daniel Leung The dbCoachLocal.db for your further checking.
**Daniel Leung** (2025-07-22):
@@Tovi Wanghot fix version uploaded to [🔗](https://ios.ctil.com/mpos/PreCoach/)  - 3.29.6-20250722.1
**Tovi Wang** (2025-07-22):
@@Joy Li @@Sherman tse
Please help to testing this hot fix and prepare the released.Thanks!
**Automation for Jira** (2025-07-23):
Issue has been created since
Days since: 2
Week since : 0
Issue due date difference
Days since : 
Weeks since:
**Sherman tse** (2025-07-23):
Verified on QA
test case attached
**Joy Li** (2025-07-29):
Released to TP on 2025-07-29

## 相關資訊

- Jira: [MP-787](https://ctil.atlassian.net/browse/MP-787)
- Fix Version: 未記錄
- 解決日期: 2025-07-29
