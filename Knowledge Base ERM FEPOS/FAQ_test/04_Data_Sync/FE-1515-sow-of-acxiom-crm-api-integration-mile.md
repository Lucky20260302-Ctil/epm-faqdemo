---
project: FE
issue_key: FE-1515
issue_type: SOW
status: Closed
faq_score: 4.0
faq_category: 04_Data_Sync
faq_category_label: 資料與同步
tags: [faq, fe, data_sync, front-end-v750.01r01a]
jira_url: "https://ctil.atlassian.net/browse/FE-1515"
created: 2024-09-30
resolved: 2024-11-08
resolution: Done
has_images: False
---

# FE-1515: SOW of ACXIOM CRM API Integration - Milestone 2 - FE Part

> **類型:** SOW | **狀態:** Closed
> **分類:** 資料與同步 | **FAQ 分數:** 4.0
> **解決日期:** 2024-11-08
> **組件:** Front End v750.01R01A

## 問題描述

None


## Jira Comments

> **Sang** (2024-10-14):
> Coach ACXIOM CRM Integration (KTS 241014 Jira FE-1515 v750.04R07, v750.05)        Data: D:\RetData6.Coach.Acxiom   a. Set tblconfig.OnlineCRMSystem = ‘ACXIOM’ (NEW, use BEGW API) Member REtreive from Acxion CRM (W/O Staff data) Acxiom CRM Fail, Retrieve from BE DB b. Search by Staff NO. = thru BWGW api - from BE DB set tblconfig.DisableSearchbyStaffCode='N', c. Exact Search - Member No., Email, Phone No.. Staff No. - Exact only, Disable Adv Search/Wildcard Search set tblconfig.SearchMemberByExactOnly='Y' d. Support WeChat QR Code, Auto create if Member No found ENABLEMEMBERQRCODE='Y WEBAPIUPDATENEWMEMBER='Y'   e. Disable Profile if No JsonData (No from API), show customized Member Profile (WpfWeb.dll need update)             f. Show Member 3rdPartyHistory if Has JsonData (from API) - how c

> **Sang** (2024-10-14):
> 

> **Sang** (2024-10-14):
> 

> **Sang** (2024-10-14):
> BEGW Acxiom Endpoint - API Call: AcxiomGW/api/v1/member

> **Sang** (2024-10-22):
> " file:////Member/acxiom/index.html?data={"  & vbCrLf & "  ""id"": ""8070928028290711552""," & vbCrLf & "  ""customer_code"": null," & vbCrLf & "  ""crm_id"": ""8070928028290711552""," & vbCrLf & "  ""customer_type"": ""PROSPECT""," & vbCrLf & "  ""open_id"": null," & vbCrLf & "  ""union_id"": null," & vbCrLf & "  ""taobao_nick"": ""Litest_18210415004""," & vbCrLf & "  ""wechat"": null," & vbCrLf & "  ""jd_id"": null," & vbCrLf & "  ""mobile"": ""18210415004""," & vbCrLf & "  ""mix_mobile"": ""5d6a9dfd7122c70112ab962540f9f72c""," & vbCrLf & "  ""jd_mix_mobile"": null," & vbCrLf & "  ""vipcom_mix_mobile"": null," & vbCrLf & "  ""mobile_valid_flag"": null," & vbCrLf & "  ""email"": null," & vbCrLf & "  ""email_valid_flag"": null," & vbCrLf & "  ""name"": """"," & vbCrLf & "  ""first_name"": 

> **Sang** (2024-10-22):
> " file:////MemberPurchase/acxiom/index.html?data={""apiUrl"":"" https://erm-coach-be7.sanyoextended.com/BEGWCRM_CN"",""region"":""11"",""storeCode"":""OC135"",""memberNumber"":""""}" Sample URL pass to ACXIOM Member Purchase History WPF webview

> **Sang** (2024-10-22):
> 

> **Sang** (2024-10-22):
> 

> **Sang** (2024-10-23):
> I. Acxiom Member Create Memo - Write PCD '34' Member and upsert Member (KTS 241023 v750.04R08, v750.05)

> **Sang** (2024-10-23):
> 

> **Joy Li** (2024-11-04):
> Released by    on 2024-10-31  Tested by    FE release : V75.004.0800.0000 release email:   

> **Joy Li** (2024-11-04):
> Re-open by one issue in FE   will create Jira for case,.

> **Joy Li** (2024-11-06):
>   release R09 for M2 member fix and dynamic QR  is testing now

> **Joy Li** (2024-11-08):
> Release Summary FE release : V75.004.0800.0000  on 2024-10-31 release email:  FE release: V75.0004.0900.0000 on 2024-11-08 release email:   

## 相關資訊

- **Jira:** [FE-1515](https://ctil.atlassian.net/browse/FE-1515)
- **解決方式:** Done