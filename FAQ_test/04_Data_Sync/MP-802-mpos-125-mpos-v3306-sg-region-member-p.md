---
project: MP
title: "MP-802: [MPOS-125] MPOS - v3.30.6 SG Region, member profile and purchase history is not available"
issue_key: MP-802
issue_type: Bug PRD
status: Closed
faq_score: 6.0
faq_category: 04_Data_Sync
faq_category_label: 資料與同步
tags: [faq, mp, data_sync, mpos]
jira_url: "https://ctil.atlassian.net/browse/MP-802"
created: 2025-09-30
resolved: 
resolution: 
has_images: True
---

# MP-802: [MPOS-125] MPOS - v3.30.6 SG Region, member profile and purchase history is not available

## 問題描述

for MPOS V3.30.6, we found that purchase history and profile both not available, kindly check the details from attached video. UI log also uploaded, testing machine IP: 10.34.103.13(OCQ92), connect to apawiqwposweb24.

CS2K POS no such issues, you could use vip phone no 98091701 to have a try.

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/ebba6b0e-b375-4841-8ec9-63e7c01045ec)（需 Jira 登入）



## 附件截圖

1. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/ebba6b0e-b375-4841-8ec9-63e7c01045ec)


## Jira Comments

> **Daniel Leung** (2025-09-30):
>  Cannot see the video, require login

> **Daniel Leung** (2025-09-30):
>     Please check two config in MPOS API web.config  - ThirdPartyModuleInstallPath - CRMType  Please check the location of 3P Module is match ThirdPartyModuleInstallPath. Please check IIS setting : MemberPurchase/Member -> Request Filtering → right click → Edit Request Filtering Settings → set Maximum allowed content length and Maximum query string to 30000000.

> **Tovi Wang** (2025-10-10):
>    Find the RCA,Let me correct the setting,then let Coach QA double testing it.

> **Tovi Wang** (2025-10-10):
>  After added follow config in web.config,Now MPOS pop out new error when checking Purchase History.I checked MPOS UI log & CRMAPI log,But NOT found the 4040 error.Could you help to double check it?Thanks!     <add key="ThirdPartyModuleInstallPath" value=" qacs2000web.coach.com " />     <add key="CRMType" value="acxiom" />

> **Tovi Wang** (2025-10-10):
>    MPOS UI log,MPOS APIlog,CRMAPI log here.Please help to take a look.Thanks!

> **Tovi Wang** (2025-10-16):
>  Many Thanks for your help. After we investigated，We found the BE ‘crm_api_config’ value can’t synced to FE Dbsse dbtrans Tblconfig due to ‘crm_api_config’ value Exceeded the length set for the field. CC      1.BE  dbconfig: 2.The BE config value can’t synced to dbsse tblconfig due to ‘crm_api_config’ value Exceeded the length. ‘crm_api_config’ value:（180 characters） eyJSRUFDVF9BUFBfUkVHSU9OIjoxMiwiUkVBQ1RfQVBQX0NPTVBBTllDT0RFIjoiY29hY2giLCJSRUFDVF9BUFBfVVNFUk5BTUUiOiJjcm0iLCJSRUFDVF9BUFBfUEFTU1dPUkQiOiIyMDI0MTAwMSIsIlJFQUNUX0FQUF9TT1VSQ0UiOiJhY3hpb20ifQ== But FE Dbsse dbtrans Tblconfig value Max characters setting is 125.

> **Tovi Wang** (2025-10-16):
> 

> **Tovi Wang** (2025-10-17):
>   Confirmed with Neil can normal search out purchase history after expanded tblconfig table config_value field length from ‘125' to '400’. CC   

> **Sang** (2025-10-20):
>  Updated program uploaded to  \\ds411\share\POS_FE_Release_64\20251020 Coach v750.04R14E v750.04R14E Add DBVer 007.001.003.074A (MPOS) - Ext dbtrans.MDF tblSysconfig_Bak,tblConfig.config_value to 400 nchar - override 007.001.003.063B (KTS 251020 MP-802 v750.04R14E, v750.05)

> **Joy Li** (2025-10-20):
>   Please arrange testing and provide timeline.

> **Sherman tse** (2025-10-27):
> verified on QA

> **Joy Li** (2025-11-04):
> released to Tapestry by Joy on 2025-11-04

## 相關資訊

- **Jira:** [MP-802](https://ctil.atlassian.net/browse/MP-802)