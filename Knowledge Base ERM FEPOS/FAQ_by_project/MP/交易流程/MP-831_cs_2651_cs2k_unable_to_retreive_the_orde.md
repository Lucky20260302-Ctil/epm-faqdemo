---
tags: [faq, mp, 交易流程]
component: "MPOS, MPOS API"
symptom: "we did testing with CS2K version: v75.004.2400.0000 and MPOS 3.30.8, during testing we found that CS"
root-cause: "待提取"
solution: "### Jira Comments (12 則)"
jira: MP-831
resolved: 
fix-version: ""
---

# MP-831: [CS-2651] CS2K Unable to retreive the order upload by MPOS

## 問題

we did testing with CS2K version: v75.004.2400.0000 and MPOS 3.30.8, during testing we found that CS2K unable to retreive the order upload via MPOS first time.
Testing machine IP: 10.34.103.3(KR Region - OCQ96), connecting to web24.
Reproduce steps:
|  |  |
| --- | --- |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
**Then nothing showing in CS2K**, from MPOS we modify the draft and upload again, then able to trigger:
|  |  |
| --- | --- |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (12 則)
**Joy Li** (2026-04-28):
@@Daniel Leung Please check IPA and API log
**Joy Li** (2026-04-28):
|  |
| --- |
Some notes from Coach team
**Sherman tse** (2026-05-04):
\\ds411\share\POS_FE_Release_64\20260430 Coach v750.04R25
FE release from Sang
**Daniel Leung** (2026-05-04):
MPOS-API: \\ds411\share\POS_MPOS_Release\3.30.x\3.30.8-20260504.1
**Automation for Jira** (2026-05-05):
Issue has been created since
Days since: 7
Week since : 1
Issue due date difference
Days since : 
Weeks since:
**Sherman tse** (2026-05-15):
@@Sang  The issue still is existing by below steps:
1. Upload an item to queue busting by MPOS
2. To FE POS to retrive the order to the sales screen
3. Click on Cancel to clear the retrived order  in FE POS
4. To MPOS > select the order from the busket
5. Change the item, then process re-upload to queue bustket
6. To FE POS to retrive the order to the sales screen again
**Tested VM: **172.16.138.180 .\sxd Yan20201104@ Version: 7.5.0.04R25 (Build260430)
Existing result:
Fail to retrive the edited  order from MPOS
Has below error from NLog:
**Sang** (2026-05-18):
@@Sherman tse FE POS VM is 172.16.138.180 or 10.34.103.3 ?
**Sang** (2026-05-18):
@@Daniel Leung @@Cy Lau MPOS save sales data to Queue, if data have member, but has both vipmas(dtovipmas) and  viptype (dtoViptyp) object. The pro
**Sang** (2026-05-18):
@@Sherman tse @@Daniel Leung @@Cy Lau This data has vipmas object but has not viptype object
**Daniel Leung** (2026-05-18):
@@Sherman tse @@Cy Lau @@Joy Li 
new mpos api version uploaded to \\ds411\share\POS_MPOS_Release\3.30.x\3.30.8-20260518.1
**Jeffrey wen** (2026-05-21):
# Test Cases — MPOS ↔ FE POS Queue Busting
---
# Positive Cases
**TC-P01: Cancel → Modify → Re-upload → Retrieve**
|  |  |
| --- | --- |
|  |  |
|  |  |
|  |  |
**TC-P02: Add / Remove Items → Re-upload → Retrieve**
|  |  |
| --- | --- |
|  |  |
|  |  |
|  |  |
**TC-N03: MPOS Edits After FE POS Completes Transaction**
|  |  |
| --- | --- |
|  |  |
|  |  |
|  |  |
---
# Negative Cases
**TC-N01: MPOS Edits While FE POS Holds the Order (No Cancel)**
|  |  |
| --- | --- |
|  |  |
|  |  |
|  |  |
**Joy Li** (2026-05-21):
@@Daniel Leung @@Jason Wu

## 相關資訊

- Jira: [MP-831](https://ctil.atlassian.net/browse/MP-831)
- Fix Version: 未記錄
- 解決日期: 未記錄
