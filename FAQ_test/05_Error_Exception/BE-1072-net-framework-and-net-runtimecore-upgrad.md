---
project: BE
issue_key: BE-1072
issue_type: Task
status: Closed
faq_score: 7.5
faq_category: 05_Error_Exception
faq_category_label: 錯誤與異常
tags: [faq, be, error_exception, backend-(chainstoreplus-7.0)]
jira_url: "https://ctil.atlassian.net/browse/BE-1072"
created: 2025-06-12
resolved: 
resolution: 
has_images: False
---

# BE-1072: .NET framework and .NET runtime(core) upgrade

> **類型:** Task | **狀態:** Closed
> **分類:** 錯誤與異常 | **FAQ 分數:** 7.5
> **負責人:** Sherman tse
> **組件:** Backend (ChainStorePlus 7.0)

## 問題描述

- ALI
-BEAPI 96e173f4-acxiom (CN)
- BEGW 157c47fb-acxiom (CN)
-CSPlus (Enquiry) - DONE
-Coach_Pangdonglai-jett (core) need test
-CRMSanyoPhaseInterface---DONE
-My_eInvoice----RED BLUE-- Cannot test in our lab
-PApmoAPI----Cannot test in our lab as cannot open email
-checkhealth-----deployed to 172.16.138.13 (logined by judy)skip: CheckHealth.dll.config--- DONE
-POSRedInvoicing -- Cannot test in our lab
-TripleDES_decrypt (CRM_DECRYPT)---deployed to 172.16.138.13----?

MPOS- Print Agent, Printhub, Saleshub (ALI)
MPOS regression test for test BEAPI & BEGW (ali & aws & ?)

- **.Net 8**

| BEAPI 641ef496(aws) | [\\ds411\public\samuel\beapi\v2.2.4_641ef496_net8_20250612](file://ds411/public/samuel/beapi/v2.2.4_641ef496_net8_20250612) | 
| BEAPI 96e173f4-acxiom (CN) | [\\ds411\public\samuel\beapi\v1.8.0_96e173f4_net8_20250623](file://ds411/public/samuel/beapi/v1.8.0_96e173f4_net8_20250623) | 
| BEAPI 0d407e57--TBC Ignore | [\\ds411\public\samuel\beapi\v1.5.5_0d407e57_net8_20250612](file://ds411/public/samuel/beapi/v1.5.5_0d407e57_net8_20250612) | 
| BEGW 9c92a274 (aws) | [\\ds411\public\samuel\beapi\v2.2.3_9c92a274_net8_20250611](file://ds411/public/samuel/beapi/v2.2.3_9c92a274_net8_20250611) | 
| BEGW 157c47fb-acxiom (CN) | [\\ds411\public\samuel\beapi\v1.6.8_157c47fb_net8_20250611](file://ds411/public/samuel/beapi/v1.6.8_157c47fb_net8_20250611) | 
| CSPlus (Enquiry) - DONE (ALI) | [\\ds411\public\samuel\csplus\v2.13.9_20250609](file://ds411/public/samuel/csplus/v2.13.9_20250609) | 
| Coach_Pangdonglai-jett (core) | [\\ds411\public\anson\Coach_Pangdonglai\ Coach_Pangdonglai_v0.0.2_20250609.zip](file://ds411/public/anson/Coach_Pangdonglai) | 
| CRMSanyoPhaseInterface-----deployed to 172.16.138.13 (logined by judy)---DONEskip: appsetting.json | [\\ds411\public\anson\CRMSanyoPhaseInterface \CRMSanyoPhaseInterface_v1.2.4.zip](file://ds411/public/anson/CRMSanyoPhaseInterface) | 
| My_eInvoice----RED BLUE-- Cannot test in our lab | [\\ds411\public\anson\MY_eInvoice\MY_eInvoice_v1.0.1_20250610.zip](file://ds411/public/anson/MY_eInvoice) | 
| PApmoAPI----Cannot test in our lab as cannot open email | [\\ds411\public\anson\PApmoAPI\v1.0.2_20250611](file://ds411/public/anson/PApmoAPI/v1.0.2_20250611) | 
| checkhealth-----deployed to 172.16.138.13 (logined by judy)skip: CheckHealth.dll.config--- DONE | [\\ds411\public\anson\PApmoAPI\checkhealth \20250611 checkhealth_build_c9fc081d.zip](file://ds411/public/anson/PApmoAPI/checkhealth) | 
| POS_API (AWS) | [\\ds411\public\samuel\POS_API\POS_API\v2.09.04_20250611](file://ds411/public/samuel/POS_API/POS_API/v2.09.04_20250611) | 
| POSRedInvoicing -- Cannot test in our lab | [\\ds411\public\anson\eInvoice\v1.1.5_20250611](file://ds411/public/anson/eInvoice/v1.1.5_20250611) | 
| TrxToAGREX----non core, has log OK JP | [\\ds411\public\anson\TrxToAGREX\v1.3.4_20250611](file://ds411/public/anson/TrxToAGREX/v1.3.4_20250611) | 
| MembersonAPI & MembersonGW----KSJ-- cannot test in our lab | \\ds411\public\anson\Memberson\v1.1.1_20250618 | 
| TripleDES_decrypt (CRM_DECRYPT)---deployed to 172.16.138.13----? | \\ds411\public\anson\TripleDES_decrypt\v1.0.2_20250625 | 

 

- **.NET Framework 4.8--- has normal log--- ****DONE**
Please update the <supportedRuntime> / <targetFramework> = "4.8" in Web.config and exe.config

| CoachChinaDisneySalesInterface | [\\ds411\public\anson\COACH_Disney\ Coach_Disney_v0.0.5_20250610.zip](file://ds411/public/anson/COACH_Disney) | 
| EnameWebApi | [\\ds411\public\samuel\ename\v1.06.23_20250610](file://ds411/public/samuel/ename/v1.06.23_20250610) | 
| SalesMemoSoftCopyScheduler | [\\ds411\public\samuel\mPOS SalesMemoSoftCopyScheduler\V5.7_20250610](file://ds411/public/samuel/mPOS%20SalesMemoSoftCopyScheduler/V4.4_20230607) | 
| pmoPortalTaskScheduler | [\\ds411\public\samuel\MM MailApprove\20250611](file://ds411/public/samuel/MM%20MailApprove/20220902) | 
| pmoPortal | [\\ds411\public\samuel\mmportal\v1.06.08_20250611](file://ds411/public/samuel/mmportal/v1.06.08_20250611) | 
| ActiveDirectoryCacheProgram | [\\ds411\public\samuel\mmportal\v1.06.08_20250611](file://ds411/public/samuel/mmportal/v1.06.08_20250611) | 

# Release:

**.Net Framework 4.8**

- Coach Program

- [\\DS411\csms60\.net_update FW 4.8\Coach](file://ds411/csms60/.net_update%20FW%204.8/Coach)

- [ ] Coach_APTOS.exe
- [x] Coach_BP.exe
- [x] Coach_CAR.exe
- [x] Coach_CRM.exe
- [x] Coach_DCLEAN.exe
- [x] Coach_ECOMM.exe
- [x] Coach_ECOMM_Rakuten.exe
- [x] Coach_HHT.exe
- [ ] Coach_IPP.exe
- [x] Coach_ONSALE.exe
- [x] Coach_SAP.exe
- [x] Coach_TRAFFIC.exe
- [x] Coach_WEB.exe
- [x] Coach_WMS.exe
- [ ] KS_CDP.exe
- [x] KS_GEO.exe
- [x] KSJ_CRM.exe

- Coach [Backend.Net](http://backend.net/)----- BACKEND Application

- [\\DS411\csms60\.net_update FW 4.8\Coach\Backend.Net](file://ds411/csms60/.net_update%20FW%204.8/Coach/Backend.Net)

- [ ] [Backend.Net](http://Backend.Net)



## 相關資訊

- **Jira:** [BE-1072](https://ctil.atlassian.net/browse/BE-1072)