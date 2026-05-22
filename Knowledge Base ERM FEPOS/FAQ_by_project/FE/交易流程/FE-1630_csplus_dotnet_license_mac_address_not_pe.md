---
tags: [faq, fe, 交易流程]
component: "Front End"
symptom: "HKJC 話佢個license 因為wifi / network card 個mac address not perm 所以出現問題，我想了解一下"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-1630
resolved: 2025-04-16
fix-version: ""
---

# FE-1630: CSPLUS DotNet License - mac address not perm

## 問題

HKJC 話佢個license 因為wifi / network card 個mac address not perm 所以出現問題，我想了解一下

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2025-04-16
### Jira Comments (9 則)
**Sang** (2025-02-25):
@@Cy Lau @@Bobby @@Andrew_Au
there are three type of CSPlus FE License Key.
1. 
i.     File – Tkey.dat
ii.     FE DB – dbtrans.TblReg3.Reg_type=’T’
1. 
1. 
2. 
3. 
1. 
i.     File – Pkey.dat
ii.     FE DB – dbrtans.tblReg3.reg_Type=’P’,
iii.     BE DB - BE.locreg.locreg_lickey
`If hardware ID content change (Change of PC), POS will auto extend Rkey Expiry date ( 14 Days) and need to re-gen permanent License ( thru Offline method / online license API)`. if Fail to grant permanent license within extended period, CSPlus will pop-up license expired message and need to re-input a new S/N (Temp License),
Since some hardware may change MAC Address when we reboot,  we could remove MAC Address from License Hardware ID content.  This change will affect all v75 license user.  The impact is  same as change of hardware and need to re-grant Perm license once, but the license is then independence from MAC Address.
Please comment.
**Andrew_Au** (2025-02-25):
[🔗](https://ctil.atlassian.net/browse/FE-1511)
**Ken Wang** (2025-03-03):
@@Sang    In order to come up with a work around for FE-1511, can you share the Pkey validation logic by POS in details?
- 
- 
- 
- 
Thanks
**Andrew_Au** (2025-03-06):
@@Sang @@Bobby @@Ken Wang Sang , we are still waiting for your reply.
**Sang** (2025-03-10):
@@Bobby @@Cy Lau @@Andrew_Au @@Ken Wang '--------------------------------
CSPLus v75 License Work Flow
'--------------------------------
Get License Key (License.Validate3)
1. 
2. 
3. 
'-----------------------------
Source Code Reference
1. 
2. 
3.
**Ken Wang** (2025-03-10):
@@Sang  I have drawn a workflow diagram <span style="color:#4c9aff">**CSPLus v75 License Work Flow.png**</span> to help understanding the case. Please see if it is correct to the current logic.
**Ken Wang** (2025-03-10):
Attached a revised diagram after Sang review
**Sang** (2025-04-07):
@@Ken Wang @@Andrew_Au @@Bobby @@Cy Lau
Please find a testing program with enhancement of  dotnet license to handle MAC Address not permanent issue in \\ds411\share\POS_FE_Release_64\20250407 JC REMS v750.01R02T - Beta
'v750.01R02T
1. 
a. Add Log,
b. first time install - write PC MAC Address to Window Registry
c. Gen HardwareID - use Registry Mac Address if available or else use PC MAC Address to generate HardwareID
d. Input Tkey - add online register RKEY to BE
e. DayEnd / Exit POS - Online Get Perm license if it is available
**Ken Wang** (2025-04-16):
@@Sang @@Andrew_Au  uploaded the specification document of the POS License logic improvement for your reference.

## 相關資訊

- Jira: [FE-1630](https://ctil.atlassian.net/browse/FE-1630)
- Fix Version: 未記錄
- 解決日期: 2025-04-16
