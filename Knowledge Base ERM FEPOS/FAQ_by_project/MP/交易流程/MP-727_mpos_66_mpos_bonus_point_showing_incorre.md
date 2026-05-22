---
tags: [faq, mp, 交易流程]
component: "MPOS"
symptom: "as per we talked today, kindly help to check how to enhance bonus point display on both CS2K & MPOS."
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: MP-727
resolved: 2025-03-20
fix-version: ""
---

# MP-727: [MPOS-66] MPOS - Bonus point showing incorrect of MPOS member display page   

## 問題

as per we talked today, kindly help to check how to enhance bonus point display on both CS2K & MPOS.
1. 
2.

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2025-03-20
### Jira Comments (11 則)
**Joy Li** (2024-11-21):
Tapestry want to show 10224 one.
Or other method to display?
**Cy Lau** (2024-11-27):
Dev team has reviewed on that, additional API and Page is needed
Est. would be given out later.
**Cy Lau** (2024-11-27):
@@Joy Li  @@Bobby 
Please review the following mock-up BP:
**Joy Li** (2024-11-28):
Confirmed with Bobby. We will use display B
**Cy Lau** (2024-11-28):
MPOs API will provide the Bonus Points info via BPData field in Member object
.Affected API: GetMembers
**Cy Lau** (2024-12-01):
\\ds411\share\POS_MPOS_Release\3.29.X\3.29.5-20241201.1b1
Release notes:
1. 
2. 
|  |  |  |
| --- | --- | --- |
|  |  |  |
|  |  |  |
**Cy Lau** (2024-12-01):
@@Daniel Leung Please estimate the delivery schedule of this
**Joy Li** (2024-12-04):
@@Daniel Leung Data is prepared below.
**Cy Lau** (2024-12-09):
@@Daniel Leung  
MPOS enhancement :
 add redmGrpAlertMsg for the description
**Cy Lau** (2024-12-10):
Enable condition for the BonusPointsData Enquiry:
MemberOnLineRedeem = Y / D
OR
MMC_BP = Y
OR
MMC_BP_ALERT = Y
**Andrew_Au** (2025-02-24):
@@Bobby I close the ticket ?

## 相關資訊

- Jira: [MP-727](https://ctil.atlassian.net/browse/MP-727)
- Fix Version: 未記錄
- 解決日期: 2025-03-20
