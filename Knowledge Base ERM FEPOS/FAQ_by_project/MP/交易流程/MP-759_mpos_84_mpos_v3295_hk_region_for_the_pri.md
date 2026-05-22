---
tags: [faq, mp, 交易流程]
component: "MPOS"
symptom: "during testing for HK MPOS, we found that for HK region, it will always pop-up below window after cr"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: MP-759
resolved: 2025-05-02
fix-version: ""
---

# MP-759: [MPOS-84] MPOS V3.29.5 HK Region, for the print function should print directly instead pop-up window

## 問題

during testing for HK MPOS, we found that for HK region, it will always pop-up below window after create transaction, and also for reprint & void function, it will also pop-up window ask to choose 'printer'. kindly help to check.
MPOS IPA: v3.29.5-20250212.1
MPOS API: R3.29.5d
Testing machine IP: 10.33.254.14(OCQ10) connect to apabiqwposweb23

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2025-05-02
### Jira Comments (20 則)
**Tovi Wang** (2025-03-21):
@@Daniel LeungAs talked in teams.I corrected the dbCoachLocal.db config,but issue still.Please help to further checking and advice.
CC @@Cy Lau @@Bobby
**Tovi Wang** (2025-03-21):
@@Daniel Leung MPOS log for your further checking.
**Daniel Leung** (2025-03-21):
In Mpos log , both config did not change to 1. Are you sure you change the correct dbCoachLocal.db in correct MPOS API ? @@Tovi Wang 
Logs show the MPOS API is [https://10.83.29.1/sanyoservice.api.fe_10](https://10.83.29.1/sanyoservice.api.fe_10). Please check the dbCoachLocal.db in this API folder,thanks.
**Tovi Wang** (2025-03-21):
@@Daniel Leung 我刚才又copy dbCoachLocal.db double confirm了下，是都已经改成1了，MPOS API（\\apabiqwposweb23\APABIQWPOSWEB23\SanyoService.API.FE_10） 应该也是对的。下面的log截图有没有可能是我改config之前的log?我让Neil上传最新测试的log给你再double confirm下？
**Tovi Wang** (2025-03-21):
@@Daniel Leung @@Cy Lau  Coach Jira [CS-820](https://jira.tapestry.support/browse/CS-820),这个是之前的issue record.for your reference.
**Daniel Leung** (2025-03-24):
apabiqwposweb23的 IP 是  10.83.29.1 ?@@Tovi Wang
**Tovi Wang** (2025-03-24):
@@Daniel Leung Right.
**Daniel Leung** (2025-03-24):
If you confirm PrintRecieptFlow changed to 1 in  10.83.29.1, please test again and upload the latest MPOS log , thanks. @@Tovi Wang
**Tovi Wang** (2025-03-24):
@@Daniel Leung Newest MPOS log for your further checking.
**Tovi Wang** (2025-03-24):
@@Daniel Leung
As talked in teams.used the newest MPOS IPA to test.But issue still.Please advice next action.Thanks!
**Daniel Leung** (2025-03-24):
@@Sherman tse  new version 3.29.5-20250324.1 uploaded to [🔗](https://ios.ctil.com/mpos/PreCoach/)
**Tovi Wang** (2025-03-24):
@@Sherman tse@@Bobby @@Cy Lau  Please help to testing this issue and advice the ETA to Neil.Thanks!
**Sherman tse** (2025-03-25):
ETA of QA: 25/03
**Cy Lau** (2025-03-25):
Please also includes checking on [🔗](https://ctil.atlassian.net/browse/MP-760) @@Sherman tse
**Daniel Leung** (2025-03-25):
@@Cy Lau  Reprint will always display popup , should I change it ?
**Daniel Leung** (2025-03-25):
3.29.5-20250325.1 uploaded to [🔗](https://ios.ctil.com/mpos/PreCoach/)
**Sherman tse** (2025-03-25):
Verified on QA
test case attached
**Tovi Wang** (2025-03-28):
@@Sherman tse @@Bobby Could you help to double check and confirm this issue again?The issue is fixed in our QA PC?right?But Neil said issue still.Please take a look first.Thanks!
**Tovi Wang** (2025-03-28):
@@Sherman tse   Resource backup HK dbCoachLocal.db for your reference.Please help to testing this config is working or not.Thanks!
**Sherman tse** (2025-05-02):
issue has fixed
close case

## 相關資訊

- Jira: [MP-759](https://ctil.atlassian.net/browse/MP-759)
- Fix Version: 未記錄
- 解決日期: 2025-05-02
