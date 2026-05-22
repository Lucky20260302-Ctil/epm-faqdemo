---
tags: [faq, fe, 交易流程]
component: "Front End"
symptom: "Case 1: RIN01019507"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-1129
resolved: 2024-03-06
fix-version: ""
---

# FE-1129: POS Freeze (update new log)

## 問題

Case 1: RIN01019507
J481  2022/07/07 12:35(HKT)
Incident description:
1) froze occurred Time : 2022/07/07 12:35(HKT)
2) froze when launching 100% (house keeping system task)
3) restart cs2k and fixed
Data/Log: \\172.16.183.201\localuser\support\JIRA_DB\FE-1129\Case1_J841_20220707\
Case 2: RIN01019328
C333 2022/07/07 09:22:35(HKT)
Incident description:
1) froze occurred Time : 2022/07/07 09:22:35(HKT)
2) froze when launching 100% (house keeping system task)
3) restart cs2k and fixed
\\172.16.183.201\localuser\support\JIRA_DB\FE-1129\Case2_C333_20220707\
Case 3: RIN01021730
J826 called out about Till4 POS freeze issue yesterday in RIN01021730, and we collected info as below per your request:
Issue happened on 2022-07-11 10:45 HKT
User opened cs2000 and freeze on update to 100% so can not boot cs2000.
Please refer to the attachment for the log files ( - RCyymmdd file is from Till0)
Please check. Thanks.

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2024-03-06
### Jira Comments (9 則)
**Joy Li** (2022-07-07):
Case 1 data / log uploaded
**Joy Li** (2022-07-07):
Case 2 data / log uploaded
**Sang** (2022-07-07):
Case 1: RIN01019507
J481  2022/07/07 12:35(HKT) -> 13:35 (JP)
[07/07/2022 13:34:26 -2413]: doBootstrap.Start
..
[07/07/2022 13:34:26 -8373]: Data House Keeping
..
[07/07/2022 13:34:27 -0126]: データベースを更新する
[07/07/2022 13:34:29 -7370]: DataCenter.DBMaintance.SchemaUpdate:00:00:02
..
07/07/2022 13:34:30 -5187]: Created_DBTemp
[07/07/2022 13:34:30 -5888]: Creating Schema For DBTarget
[07/07/2022 13:34:30 -8163]: Created_DBReport
[07/07/2022 13:34:30 -8213]: CreateDBReportSchema
[07/07/2022 13:34:30 -8459]: Creating Schema From DBTrans
[07/07/2022 13:34:31 -3648]: Creating Schema From DBHist
[07/07/2022 13:34:31 -5083]: Creating Schema From Master Server
[07/07/2022 13:34:31 -8168]: Creating Index For DbReport
[07/07/2022 13:34:32 -0150]: Created_DBMix
[07/07/2022 13:34:32 -0652]: Creating Schema For DBTarget
..
[07/07/2022 13:34:34 -2150]: Data House Keeping
..
[07/07/2022 13:34:36 -9552]: Run_HouseKeeping'S' - Start
..
07/07/2022 13:34:38(-1202668483)-frmOpenScr.Prepare Mix_And_Match
07/07/2022 13:34:38(-1202668467)-frmOpenScr.Extract_Mix_And_Match - Not Rebuild All
07/07/2022 13:34:38(-1202668421)-AdoService.clsMMExtract - Start
07/07/2022 13:34:38(-1202668421)-AdoService.clsMMExtract - ExtractMixEffect
07/07/2022 13:34:38(-1202668311)-AdoService.clsMMExtract - ExtractMixTotal
07/07/2022 13:34:39(-1202668264)-AdoService.clsMMExtract - Flag MixProdt
07/07/2022 13:34:44(-1202662436)-AdoService.clsMMExtract - ExtractEventTables_ByEvent False
07/07/2022 13:34:44(-1202662421)-Get MMEffect Union MixTotal Recordset
07/07/2022 13:34:45(-1202661749)-AdoService.clsMMExtract - End
..
[07/07/2022 13:34:45 -7969]: doLogIn.Start
From Start up to Login : 19 sec
From Housekeeping to Login : 9 sec
**Sang** (2022-07-07):
Case 2: RIN01019328
C333 2022/07/07 09:22:35(HKT)
[07/07/2022 10:22:22 -6446]: doBootstrap.Start
..
[07/07/2022 10:22:23 -4342]: Data House Keeping
..
[07/07/2022 10:22:23 -4941]: データベースを更新する
[07/07/2022 10:22:25 -0433]: DataCenter.DBMaintance.SchemaUpdate:00:00:01
..
[07/07/2022 10:22:28 -9113]: Run_HouseKeeping'S' - Start
..
7/07/2022 10:22:31(931939703)-frmOpenScr.Run_HouseKeeping 'S' - End 
07/07/2022 10:22:32(931939718)-frmOpenScr.create SecInf.SecureControl
07/07/2022 10:22:32(931939781)-frmOpenScr.UpdatePosAccProgList
07/07/2022 10:22:32(931939828)-frmOpenScr.Prepare Mix_And_Match
07/07/2022 10:22:32(931939859)-frmOpenScr.Extract_Mix_And_Match - Not Rebuild All
07/07/2022 10:22:32(931939921)-AdoService.clsMMExtract - Start
07/07/2022 10:22:32(931939937)-AdoService.clsMMExtract - ExtractMixEffect
07/07/2022 10:22:32(931939984)-AdoService.clsMMExtract - ExtractMixTotal
07/07/2022 10:22:32(931940015)-AdoService.clsMMExtract - Flag MixProdt
07/07/2022 10:22:32(931940062)-AdoService.clsMMExtract - ExtractEventTables_ByEvent False
07/07/2022 10:22:32(931940062)-Get MMEffect Union MixTotal Recordset
07/07/2022 10:22:32(931940078)-AdoService.clsMMExtract - End
..
[07/07/2022 10:22:33 -2940]: doLogIn.Start
From Start up to Login : 11 sec
From Housekeeping to Login : 5 sec
**Joy Li** (2022-07-12):
Case 1 reply in ticket for record:
issue reported on J481 
2022/07/07 12:35(HKT) -> 13:35 (JP)
Refer to T9220707.dat, POS system only call to start twice.
1. 09:34 JPT
2. 13:34 JPT
As user mentioned, they start POS at 12:34 HKT and report freeze issue. The issue was resolved by restart POS.
But Refer to log, we cannot see the POS restart at 13:34JPT.
Also the time for POS start (include zlog update) until login box shown, the process use 19 sec. 
I think this is still acceptable.
===========================================================================================
[07/07/2022 13:34:26 -2413]: doBootstrap.Start
..
[07/07/2022 13:34:26 -8373]: Data House Keeping
..
[07/07/2022 13:34:27 -0126]: データベースを更新する
[07/07/2022 13:34:29 -7370]: DataCenter.DBMaintance.SchemaUpdate:00:00:02
..
07/07/2022 13:34:30 -5187]: Created_DBTemp
[07/07/2022 13:34:30 -5888]: Creating Schema For DBTarget
[07/07/2022 13:34:30 -8163]: Created_DBReport
[07/07/2022 13:34:30 -8213]: CreateDBReportSchema
[07/07/2022 13:34:30 -8459]: Creating Schema From DBTrans
[07/07/2022 13:34:31 -3648]: Creating Schema From DBHist
[07/07/2022 13:34:31 -5083]: Creating Schema From Master Server
[07/07/2022 13:34:31 -8168]: Creating Index For DbReport
[07/07/2022 13:34:32 -0150]: Created_DBMix
[07/07/2022 13:34:32 -0652]: Creating Schema For DBTarget
..
[07/07/2022 13:34:34 -2150]: Data House Keeping
..
[07/07/2022 13:34:36 -9552]: Run_HouseKeeping'S' - Start
..
07/07/2022 13:34:38(-1202668483)-frmOpenScr.Prepare Mix_And_Match
07/07/2022 13:34:38(-1202668467)-frmOpenScr.Extract_Mix_And_Match - Not Rebuild All
07/07/2022 13:34:38(-1202668421)-AdoService.clsMMExtract - Start
07/07/2022 13:34:38(-1202668421)-AdoService.clsMMExtract - ExtractMixEffect
07/07/2022 13:34:38(-1202668311)-AdoService.clsMMExtract - ExtractMixTotal
07/07/2022 13:34:39(-1202668264)-AdoService.clsMMExtract - Flag MixProdt
07/07/2022 13:34:44(-1202662436)-AdoService.clsMMExtract - ExtractEventTables_ByEvent False
07/07/2022 13:34:44(-1202662421)-Get MMEffect Union MixTotal Recordset
07/07/2022 13:34:45(-1202661749)-AdoService.clsMMExtract - End
..
[07/07/2022 13:34:45 -7969]: doLogIn.Start
**Joy Li** (2022-07-12):
reply COACH ref: case 2
issue reported on C333
2022/07/07 09:22(HKT) -> 10:22 (JP)
Refer to T9220707.dat, POS system only call to start twice.
1. 09:06 JPT
2. 10:22 JPT
As user mentioned, they start POS at 10:22 HKT and report freeze issue. The issue was resolved by restart POS.
But Refer to log, we cannot see the POS restart after 10:22JPT.
Also the time for POS start (include zlog update) until login box shown, the process use 11 sec.
I think this is still acceptable.
From Start up to Login : 11 sec
From Housekeeping to Login : 5 sec
===============================================================================
**Joy Li** (2022-07-13):
Case 3 data uploaded \\172.16.183.201\localuser\support\JIRA_DB\FE-1129\Case3_J826_20220711
**Sang** (2022-07-13):
Case 1 J841
**Sang** (2022-07-13):
Case 3 J826 Till  4

## 相關資訊

- Jira: [FE-1129](https://ctil.atlassian.net/browse/FE-1129)
- Fix Version: 未記錄
- 解決日期: 2024-03-06
