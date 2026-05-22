---
tags: [faq, fe, 會員_api]
component: "interface"
symptom: "Below transaction having unknown sales item type code 9999 error in CAR."
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-1600
resolved: 2025-02-12
fix-version: ""
---

# FE-1600: [CS-1309] Issue-MY-INC2772129- CAR Error - MY-A130-Unknown Sales item type code 9999 12/20

## 問題

Below transaction having unknown sales item type code 9999 error in CAR.
Raise this ticket to request for a Program enhance.
**Transaction Nuber:**
MY-OC602-40060402 of 12/20
**Root Cause:**
Normally,CAR interface file separate by ' | '.The issue caused by user input remarks which contain ' | '.
Details in Bellow Email:

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2025-02-12
### Jira Comments (7 則)
**Tovi Wang** (2024-12-31):
We will add a enhance which means that no matter what channel the data enters the CAR file remarks field, Any special character containing 'I' in remarks field will be automatically removed by CAR system.
ETA: Need to double confirm with dev team.
@@Cy Lau @@Joy Li As talked in before,Please help to prepare the new released and provide the ETA.Thanks!
**Cy Lau** (2025-01-02):
Source target to be enhanced:
svn://sanyosvn.ctil.com/svn/cs2000/Trunk/BackEnd.Net(VS2017 FW 4.5.2 NEW)/Coach_CAR
**Cy Lau** (2025-01-02):
@@Jerry Wong  Please do the enhancement: replace(“|“, “ “)
@@Joy Li  Please help to get the set of following DLL for the current development :
**Joy Li** (2025-01-02):
@@Cy Lau  @@Jerry Wong
Different set in CN APP server and AWS APP Server.
Let me copy both and send you.
**Jerry Wong** (2025-01-02):
Release:
\\ds411\csms60\delivery\coach\update_coachCAR-2024-01-02
**Cy Lau** (2025-01-03):
Please remind that the CAR program should deploy the .exe only
**Sherman tse** (2025-01-22):
Verified on QA

## 相關資訊

- Jira: [FE-1600](https://ctil.atlassian.net/browse/FE-1600)
- Fix Version: 未記錄
- 解決日期: 2025-02-12
