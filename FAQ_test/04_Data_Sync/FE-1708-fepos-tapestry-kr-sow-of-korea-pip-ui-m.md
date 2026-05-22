---
project: FE
title: "FE-1708: FEPOS-Tapestry KR- SOW of Korea PIP UI Masking Enhancements"
issue_key: FE-1708
issue_type: SOW
status: Closed
faq_score: 8.0
faq_category: 04_Data_Sync
faq_category_label: 資料與同步
tags: [faq, fe, data_sync, front-end]
jira_url: "https://ctil.atlassian.net/browse/FE-1708"
created: 2025-06-02
resolved: 2026-05-07
resolution: Done
has_images: True
---

# FE-1708: FEPOS-Tapestry KR- SOW of Korea PIP UI Masking Enhancements

## 問題描述

Configurations in below list will be added into xconfig file for applying into frontend environments.

### vip_mask_enable

On/Off mode Control of masking VIP Personal Information to all Back-end components.Default value is N.

 Y means masking is enabled,

N means masking is disabled.

For **DOB** (Date of Birth), if the configuration value is set as Y, the day field will be masked with Asterisk ‘*’.

### vip_mask_rule

Controlling the masking logic for the VIP personal information field. 

Allow to input numeric characters to indicate the number of characters to be unmasked. 

Negative numbers can also be used for indicating to start unmasking from the last character of value.

Default value is 0 which means masking feature is OFF.

Masking is typically applied to the "customer list" view, which displays multiple customer information on the page. Masking is not necessary on the customer detail page.

In Asian names, it is common for names to be 2 to 4 characters long. If the data length is shorter than the specified value, only one character will be displayed. If both the first name and last name are only one character each, the system will display the first name only while masking the last name.

For Email Address field, only Local Part of the email address will be processed, Domain Part (after @) will not be considered during masking.

**Member Enquiry > Advanced Search**

- Information of **Member Name, Home No., Mobile No. **and **Email address **fields on the member enquiry list will be masked based on the corresponding configuration settings.

- The customer detail page is not required to apply masking after selecting the specific customer.

> 📎 **image-20250602-092348.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/75369676-1ee6-47ed-b026-dc90ec495646)（需 Jira 登入）

> 📎 **image-20250602-092408.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/afbc36aa-5172-4d4b-a280-33dae02a98c7)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20250602-092348.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/75369676-1ee6-47ed-b026-dc90ec495646)
2. 📎 **image-20250602-092408.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/afbc36aa-5172-4d4b-a280-33dae02a98c7)


## Jira Comments

> **Cy Lau** (2025-06-02):
>   I have one concern about  what if the FEPOS offline (cannot access to POSAPI for member) will it get from local db ? If all the members are from API or nothing as offline, then we could consider to make the changes on POS_API only

> **Sang** (2025-06-02):
> We have three way to retrieve member info, 1-0nline thru api, 2-0nline by direct access backend database; 3 -offline by retrieve from local db Get Outlook for iOS< https://aka.ms/o0ukef >

> **Cy Lau** (2025-06-02):
> how about for KR this region ? or shall we ask support about if they are using CRM already ? 

> **Sang** (2025-06-02):
> Best to know. I remember that SOW cover all region. We need to know Coach testing case cover how many CRM method? Get Outlook for iOS< https://aka.ms/o0ukef >

> **Cy Lau** (2025-06-03):
> After checking from the Production env , currently the KR region using CS2000 as online enquiry member type CS2000 accesses directly access BEDB for enquiry. In order to fade out direct DB access , would like to advice TP to switch from CS2000 to CSPLUS ( data source from db)  Those masking would be conducted in API side inside of front end

> **Sang** (2025-06-26):
> v750.04R14 Beta (\\ds411\share\POS_FE_Release_64\20250626 Coach v750.04R14 - Beta) SOW of Tapestry KR PIP UI Masking Enhancements (Ref: Q2025-010-ERM-R) (Jira FE-1701/BE-1068 v750.04R14, v750.05)  a. add tblconfig.vip_mask_enable (Y- Enable, must define vip_mask_rule, N Disable (Default N))  b. add tblconfig.vip_mask_rule (Default 0 - Disable, value should be integer)  	ex. 12345678 ; Mask 6 --> 123456***, Mask -4 *****6789  c. Mask data in Member Enquiry w/c show in List form, show raw data in detail (adv search, SEARCHMEMBERBYEXACTONLY='N')  e. Support Mask Member Data by FE POS  	1. Member retrieve from local DB ENABLEONLINEMEMBER ='N  	2. Member online retrieve from BE DB by FE POS (ENABLEONLINEMEMBER ='Y', tblconfig.ONLINECRMSYSTEM=CS2000  	3. Member online retrieve from Web API (API 

> **Cy Lau** (2025-08-05):
> additional Payload to [BEGW]->BEAPI :  either post or get {  “source“ : “POS/MPOS“, ”mode” : “list/details“, ”salady” : “YWONG“, “module“ : “Sales“ } additional Payload BEAPI->[BEGW]->FEPOS / MPOS { “masked“ : true {vip object with masking handle} }

> **Sang** (2025-08-14):
>     WEB API Client code uploaded to svn://sanyosvn.ctil.com/svn/SvnPepository/branches/PosNetFE/7.5.0.04 Enhancement Summary as follows: Public Class clsDataCenterBEWebClient a. Get Member Details: ( New, with additional Paramter clsMemberEnquiryFilter)   Public Function GetMember(ByVal pMemberNo As String, ByVal pPara As clsMemberEnquiryFilter) As dtoVipMas  b. Get Member List:   Public Function GetMemberListAdv(ByVal pPara As clsMemberEnquiryPara) As List(Of dtoVipMas)  Common.clsMemberEnquiryPara (add - Member Enquiry PIPL Log)     Public Property RequestedBy As String = ""     Public Property RequestedFor As RequestedForTypes = RequestedForTypes.Enquiry             Public Property RequestClientMode As String = "POS"  'POS|MPOS     Public Property RequestModule As String = "Sales"    'S

> **Sang** (2025-08-14):
>    Program updated 

> **Sang** (2025-08-19):
>       R14 uploaded to \\ds411\share\POS_FE_Release_64\20250819 Coach v750.04R14 SOW of Tapestry KR PIP UI Masking Enhancements (Ref: Q2025-010-ERM-R) (Jira FE-1708/BE-1068 v750.04R14, v750.05)  a. add tblconfig.vip_mask_enable (Y- Enable Masked by FE POS, must define vip_mask_rule, N Disable (Default N))  b. add tblconfig.vip_mask_rule (Default 0 - Disable, value should be integer)  	ex. 12345678 ; Mask 6 --> 123456***, Mask -4 *****6789  c. Mask data in Member Enquiry w/c show in List form, show raw data in detail (adv search, SEARCHMEMBERBYEXACTONLY='N')  e. Support Mask Member Data by FE POS  	1. Member retrieve from local DB ENABLEONLINEMEMBER ='N  	2. Member online retrieve from BE DB by FE POS (ENABLEONLINEMEMBER ='Y', tblconfig.ONLINECRMSYSTEM=CS2000  	3. Member online retrieve from

> **Sherman tse** (2025-08-21):
> Communicate with   , found that ID number without masking handling in the JP member listing, enahancement focus on KR region this time, so if TRP side want to mask ID number and katakane, we handle it later (Related captues as below:)

> **Sang** (2025-08-21):
> Mask JP Kana Name

> **Sherman tse** (2025-08-22):
>  we would base on masking principle: 1.  when character of email (before domain part) less than value of vip masking rule, only 1 character can be disclosed 2. According to SOW, If both the first name and last name are only one character each, the system will display the first name only while masking the last name You may follow below results from ename as reference: vip_mask_rule=6

> **Sang** (2025-08-25):
>       h. Email Mask : 1 last word after masking if length => masklen, mask all if length=1 (KTS 250825  v750.04R14, V750.05) 	i. POSSupp add -execute testVipMask MemberDataJsonFileNme MaskRule (ex: -execute testVipMask c:\RetData6\vipmas.txt -4) (KTS 250825  v750.04R14, V750.05)

> **Sang** (2025-08-25):
>   Sample testing member json data file     

> **Sherman tse** (2025-08-26):
>   I set testing data for first name & last name with 6 characters. And, VIP_MASK_RULE=6 Existing reuslt: VM: 172.16.138.148 .\sxd Yan20201104@

> **Sherman tse** (2025-08-26):
>  When tblconfig in POS VIP_MASK_ENABLE=N, and BEGW is enable masking fucntion Use FE search member with mobile no. 13107942 in memebr section (Not advance search), POS still cannot display masked result as below: WA log:

> **Sang** (2025-08-26):
>  these two records is taken from local DB, since POS disable mask vip, so these records display w/o masking

> **Sang** (2025-08-26):
>  

> **Automation for Jira** (2025-09-14):
> Issue has been created since Days since: 103 Week since : 14 Issue due date difference Days since :  Weeks since: 

> **Sherman tse** (2026-01-08):
> released

## 相關資訊

- **Jira:** [FE-1708](https://ctil.atlassian.net/browse/FE-1708)
- **解決方式:** Done