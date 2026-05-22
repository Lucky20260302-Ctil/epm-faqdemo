---
tags: [faq, fe, 交易流程]
component: "Front End v750.01R01A"
symptom: "_（Jira 中無 description 內容）_"
root-cause: "待提取"
solution: "### Jira Comments (10 則)"
jira: FE-1884
resolved: 
fix-version: ""
---

# FE-1884: HKJC REMS TOCB421-0 license key expired

## 問題

_（Jira 中無 description 內容）_

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (10 則)
**Bobby** (2026-02-10):
According to the locregister data, this POS was last online on 20/02/2025 at 11:40:50. This indicates that the POS has been offline for approximately one year. We suspect that the POS version may not be up-to-date. Our released version is v750.01R02T, which includes enhancements to license registration. Older versions may experience license resets due to changes in the network MAC address or other factors. Therefore, when the user recently accessed the POS, it may have triggered a license reset, prompting them to re-enter the serial number.
**Bobby** (2026-02-10):
To prevent unexpected expiration of registered POS systems and ensure timely notification, we propose the following enhancements to the POS license checking process:
1. The POS sends the temporary key and permanent key via a PCD record and posts them to the backend database. @@Sang , please provide the record type and details so that the support team can easily and reliably verify which POS has completed the registration from the frontend.
2. Add a ‘Online Registration’ button in POS Configuration menu for the support to do the registration or verification immediately instead of waiting for the system update the registration from backend automatically. Hide the button after updated the permanent key in local. 
3. Please verify the locreg_installedversion, locreg_installeddate column will be updated correctly. Currently they are not updated.
**Automation for Jira** (2026-02-12):
Issue has been created since
Days since: 2
Week since : 0
Issue due date difference
Days since : 14
Weeks since: 2
**Sang** (2026-02-20):
**Sang** (2026-02-20):
pcd ‘93’ Have Permanent Key = 1, Have not =0
**Sang** (2026-02-20):
Updated program uploaded to \ds411\share\POS_FE_Release_64\20260220 REMS v750.01R02U
1. 
2. 
3. 
4.
**Sherman tse** (2026-02-23):
@@Sang For details, please refer to above email.
**Andrew_Au** (2026-02-24):
- [x] Successfully updated the POS lisense status to activated and the pcdbak record: <span style="color:#36b37e">**Test Passed **</span>
**Sang** (2026-02-25):
Applied to JC RTM+REMS version v750.01R04
**Sang** (2026-02-25):
Re-applied to latest V75.05R09.

## 相關資訊

- Jira: [FE-1884](https://ctil.atlassian.net/browse/FE-1884)
- Fix Version: 未記錄
- 解決日期: 未記錄
