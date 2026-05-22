---
tags: [faq, mp, 交易流程]
component: "Frontend"
symptom: "1.[MPOS-76]  **MPOS 3.29.5 - Unable to select item after deploy COACH_MPOSWebAPI_R3.29.5d**"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: MP-746
resolved: 2025-05-02
fix-version: ""
---

# MP-746: [MPOS-76]  MPOS 3.29.5 - JP region -Unable to select item after deploy COACH_MPOSWebAPI_R3.29.5d

## 問題

1.[MPOS-76]  **MPOS 3.29.5 - Unable to select item after deploy COACH_MPOSWebAPI_R3.29.5d**
after deploy the patch COACH_MPOSWebAPI_R3.29.5d, if Saleshub was enabled, then unable to select item.
Testing info:
CS2K Testing machine ip: 172.24.253.20(J805)
IPA Version: 3.29.5-20250108.2
API: COACH_MPOSWebAPI_R3.29.5d ( connect to apawiqwposweb24)
Log already uploaded

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2025-05-02
### Jira Comments (10 則)
**Tovi Wang** (2025-02-17):
@@Daniel Leung  02-14 all MPOS logs & Issue video for your further checking.Thanks!
CC @@Cy Lau @@Bobby FYI.
**Daniel Leung** (2025-02-17):
@@Tovi Wang  Please check TblConfig - mPosEncryptKey.
**Tovi Wang** (2025-02-17):
@@Daniel Leung For issue 1.Xconfig mPosEncryptKey value is '0'.Please advice next action.
**Daniel Leung** (2025-02-17):
@@Tovi Wang Please try to set f6brWp8kVPs4HYbIsoykeR5TCAdMmOuV
**Daniel Leung** (2025-02-17):
@@Tovi Wang  For the second issue, is it able to get the correct member?
**Tovi Wang** (2025-02-17):
@@Anson Cheung For issue 1, Set the Xconfig mPosEncryptKey value to  ‘f6brWp8kVPs4HYbIsoykeR5TCAdMmOuV’?right?
**Tovi Wang** (2025-02-17):
@@Daniel Leung Let us follow the second issue in internal Jira [🔗](https://ctil.atlassian.net/browse/MP-747)
**Tovi Wang** (2025-02-17):
@@Daniel Leung @@Cy Lau Bellow question from Neil.
“For the MPOSENCRYPT key, we didn't do any change for this before, the MPOS still working, why this time need to change it? kindly help to explain?”
**Ken Wang** (2025-02-25):
@@Tovi Wang Please update the ticket status
**Sherman tse** (2025-05-02):
Issue has been closed in Tapestry JIRA
Please refer to [https://jira.tapestry.support/browse/MPOS-76](https://jira.tapestry.support/browse/MPOS-76) for details
Close case

## 相關資訊

- Jira: [MP-746](https://ctil.atlassian.net/browse/MP-746)
- Fix Version: 未記錄
- 解決日期: 2025-05-02
