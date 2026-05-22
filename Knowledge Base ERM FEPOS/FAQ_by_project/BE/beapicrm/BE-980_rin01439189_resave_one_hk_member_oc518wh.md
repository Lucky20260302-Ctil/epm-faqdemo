---
tags: [faq, be, beapicrm]
component: "Backend (ChainStorePlus 7.0)"
symptom: "**1.Resave one HK member OC518WH00031506 will pop out error in BE UI.Same region other member can no"
root-cause: "待提取"
solution: "### Jira Comments (19 則)"
jira: BE-980
resolved: 
fix-version: ""
---

# BE-980: [RIN01439189] - Resave one HK member OC518WH00031506 will pop out error in BE UI

## 問題

**1.Resave one HK member OC518WH00031506 will pop out error in BE UI.Same region other member can normal open and resaved.Could you help to check the RCA and workaround?**
2.I checked the member data in DB seems is normal,And NOT found abnormal.

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (19 則)
**Tovi Wang** (2025-01-13):
@@Cy Lau @@Sang Someone can help to check this one case?Please help to take a look.Thanks!
**Cy Lau** (2025-01-13):
@@Jerry Wong  Please follow
**Jerry Wong** (2025-01-13):
@@Tovi Wang   Can I get the log and the member data?
**Tovi Wang** (2025-01-13):
@@Jerry Wong 我们需要什么log呀？这个member OC518WH00031506 在BE UI报错，报错信息如截图所示。需要查下为什么只有这个member 在BE UI报错？
**Tovi Wang** (2025-01-13):
Can you reproduce the error in BE UI or I can reproduce it then share to you.
**Jerry Wong** (2025-01-13):
@@Tovi Wang 
只有這兩張截圖不夠，我要知道這個member所有field value才能reproduce和這個BE UI的log file。
**Tovi Wang** (2025-01-13):
@@Jerry Wong  Could you share me the BE UI log path?
Follow file is the member details data.
**Jerry Wong** (2025-01-14):
@@Tovi Wang
log_path in .config file
**Jerry Wong** (2025-01-14):
@@Tovi Wang
I found that the member is missing [vip_birth_iyy], it should not be null.
**Tovi Wang** (2025-01-14):
@@Jerry Wong vip_birth_iyy 是Null会导致BE UI报错嘛？因为我看到DB里面有很多VIP data  vip_birth_iyy 都是Null
**Jerry Wong** (2025-01-14):
@@Tovi Wang 是的 正常BE UI是輸入不到null的 如果null會變0的 
[vip_birth_iyy] [vip_birth_imm][vip_birth_idd] 這3個field都是
**Tovi Wang** (2025-01-14):
@@Jerry Wong 据我了解，这个会员created by Ename.在Ename上 [vip_birth_iyy] [vip_birth_imm][vip_birth_idd] 这三个字段是可选的，不是必填的。
**Jerry Wong** (2025-01-14):
@@Tovi Wang  
Release
\\ds411\csms60\delivery\coach\update-coach-2025-01-14
**Tovi Wang** (2025-01-15):
“Release
\\ds411\csms60\delivery\coach\update-coach-2025-01-14”
@@Jerry Wong what’s this?Need package release to fixed this issue?
**Jerry Wong** (2025-01-15):
@@Tovi Wang
Yes, please replace the file in program
**Tovi Wang** (2025-01-15):
@@Jerry Wong May I know the RCA?How to we fixed the issue?The error gone now in BE UI?
**Jerry Wong** (2025-01-15):
@@Tovi Wang [vip_birth_iyy] [vip_birth_imm][vip_birth_idd] can’t be display NULL in BE UI. So that, Coverting null to 0 in the UI
**Andrew_Au** (2025-03-21):
@@Tovi Wang @@pierre.shi The issue pending for a long time. Please update the current status
**Tovi Wang** (2025-03-21):
issue resumed now.please closed first.

## 相關資訊

- Jira: [BE-980](https://ctil.atlassian.net/browse/BE-980)
- Fix Version: 未記錄
- 解決日期: 未記錄
