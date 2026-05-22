---
tags: [faq, fe, 交易流程]
component: "Front End"
symptom: "Before this V75 upgrade, MC cs2000 version was V75.004.0702.0000"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-1713
resolved: 2025-07-11
fix-version: ""
---

# FE-1713: [CS-1454] Cash drawer can not be opened after upgrade to V75 - MC region

## 問題

Before this V75 upgrade, MC cs2000 version was V75.004.0702.0000
After upgraded to V75(v75.004.1100.0010), all cash drawers can not be opened due to cah.ini file COM port setting auto changed.   After changed back it works.  Please have a check.
Troubleshooting:
@@Cy Lau @@Sang After [confirmed.MC](http://confirmed.MC) store OC09 till0 after upgraded,cah.ini com port setting value was changed from '1'  to '7'.Seems the cah.ini file was overwrite,Why the cah.ini setting was changed after upgrade?Please help to further checking?.Thanks!
1.Before upgrade:
2.After upgraded:
3.cah.ini.bak file exist in inibak folder.And cah.ini.bak comport setting is 1.

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2025-07-11
### Jira Comments (10 則)
**Tovi Wang** (2025-06-11):
@@Cy Lau @@Sang For MC&HK pilot store, Could you help to double check why cah.ini comport setting was changed after POS upgraded?Thanks!
**Cy Lau** (2025-06-12):
one quick question, all affected tills has been changed to port 7 after upgrade?
**Tovi Wang** (2025-06-12):
@@Cy Lau Let me confirm this point with SOG team.Because SOG team correct the cah.ini comport setting.
**Cy Lau** (2025-06-12):
CY inspectations : which modules would possible to touch the cah.ini
1. 
2. 
3. 
4. 
@@Joy Li
**Tovi Wang** (2025-06-12):
@@Cy Lau 和SOG 确认了，升级后cah.ini comport全部都自动变成7
**Cy Lau** (2025-06-12):
Updates at 1758:
Now the cah.ini would have 2 sources to overwrite in CSPLUS folder:
1. 
2. 
with this enhancement, the current cah.ini in CSPLUS folder would be copied if backup folder doesn’t have the ini
and if ini exists in backup folder, it will overwrite the CSPLUS folder in order to retrieve the config
If user needs to change the com port, changing either
1. 
2. 
cc @@Joy Li  please help arrange the testing case for @@Sherman tse
**Joy Li** (2025-06-12):
@@Sherman tse  could you please refer to below for reference.
case 1: first installation
Case 2: update from V72 to current version
pre-request: v72 installed with cah.ini = 5 + adminupdate
Case 3: update from V75.XXXX.XXXX to current version
pre-request: v75 installed with cah.ini = 5
**Cy Lau** (2025-06-13):
updates on 13/06 :
QAQC reported that backup folder may not exist in the machine
adding create backup folder if not exist
**Cy Lau** (2025-06-13):
update on 13/06 14:29
@@Sherman tse
**Joy Li** (2025-07-11):
Released in setup_75.004.1301.0002.zip on 2025-06-16

## 相關資訊

- Jira: [FE-1713](https://ctil.atlassian.net/browse/FE-1713)
- Fix Version: 未記錄
- 解決日期: 2025-07-11
