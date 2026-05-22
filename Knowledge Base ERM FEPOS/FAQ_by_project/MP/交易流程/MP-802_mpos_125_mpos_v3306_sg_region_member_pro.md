---
tags: [faq, mp, 交易流程]
component: "MPOS"
symptom: "for MPOS V3.30.6, we found that purchase history and profile both not available, kindly check the de"
root-cause: "待提取"
solution: "### Jira Comments (12 則)"
jira: MP-802
resolved: 
fix-version: ""
---

# MP-802: [MPOS-125] MPOS - v3.30.6 SG Region, member profile and purchase history is not available

## 問題

for MPOS V3.30.6, we found that purchase history and profile both not available, kindly check the details from attached video. UI log also uploaded, testing machine IP: 10.34.103.13(OCQ92), connect to apawiqwposweb24.
CS2K POS no such issues, you could use vip phone no 98091701 to have a try.

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (12 則)
**Daniel Leung** (2025-09-30):
@@Tovi Wang Cannot see the video, require login
**Daniel Leung** (2025-09-30):
@@Tovi Wang @@Joy Li
1. 
2. 
3.
**Tovi Wang** (2025-10-10):
@@Daniel Leung @@Joy Li Find the RCA,Let me correct the setting,then let Coach QA double testing it.
**Tovi Wang** (2025-10-10):
@@Daniel Leung After added follow config in web.config,Now MPOS pop out new error when checking Purchase History.I checked MPOS UI log & CRMAPI log,But NOT found the 4040 error.Could you help to double check it?Thanks!
<add key="ThirdPartyModuleInstallPath" value="[qacs2000web.coach.com](http://qacs2000web.coach.com)" />
    <add key="CRMType" value="acxiom" />
**Tovi Wang** (2025-10-10):
@@Daniel Leung @@Joy Li MPOS UI log,MPOS APIlog,CRMAPI log here.Please help to take a look.Thanks!
**Tovi Wang** (2025-10-16):
@@Daniel Leung Many Thanks for your help.
After we investigated，We found the BE ‘crm_api_config’ value can’t synced to FE Dbsse dbtrans Tblconfig due to ‘crm_api_config’ value Exceeded the length set for the field.
CC @@Joy Li @@Cy Lau
[1.BE](http://1.BE) dbconfig:
2.The BE config value can’t synced to dbsse tblconfig due to ‘crm_api_config’ value Exceeded the length.
‘crm_api_config’ value:（180 characters）
eyJSRUFDVF9BUFBfUkVHSU9OIjoxMiwiUkVBQ1RfQVBQX0NPTVBBTllDT0RFIjoiY29hY2giLCJSRUFDVF9BUFBfVVNFUk5BTUUiOiJjcm0iLCJSRUFDVF9BUFBfUEFTU1dPUkQiOiIyMDI0MTAwMSIsIlJFQUNUX0FQUF9TT1VSQ0UiOiJhY3hpb20ifQ==
But FE Dbsse dbtrans Tblconfig value Max characters setting is 125.
**Tovi Wang** (2025-10-16):
**Tovi Wang** (2025-10-17):
@@Sang  Confirmed with Neil can normal search out purchase history after expanded tblconfig table config_value field length from ‘125' to '400’.
CC @@Joy Li
**Sang** (2025-10-20):
@@Tovi Wang Updated program uploaded to [\\ds411\share\POS_FE_Release_64\20251020 Coach v750.04R14E](file://ds411/share/POS_FE_Release_64/20251020%20Coach%20v750.04R14E)
v750.04R14E
1.
**Joy Li** (2025-10-20):
@@Sherman tse  Please arrange testing and provide timeline.
**Sherman tse** (2025-10-27):
verified on QA
**Joy Li** (2025-11-04):
released to Tapestry by Joy on 2025-11-04

## 相關資訊

- Jira: [MP-802](https://ctil.atlassian.net/browse/MP-802)
- Fix Version: 未記錄
- 解決日期: 未記錄
