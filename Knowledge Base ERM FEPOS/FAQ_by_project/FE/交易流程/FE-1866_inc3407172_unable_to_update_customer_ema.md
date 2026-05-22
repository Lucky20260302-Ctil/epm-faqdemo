---
tags: [faq, fe, 交易流程]
component: "Front End"
symptom: "Symptom:"
root-cause: "待提取"
solution: "### Jira Comments (11 則)"
jira: FE-1866
resolved: 
fix-version: ""
---

# FE-1866: [INC3407172] Unable to update customer email on CS2000 web

## 問題

Symptom:
Unable to update customer email on CS2000 web
sample member code: KSFA2411S000061
[https://ksjcs2000.katespade.com/CS2000V4](https://ksjcs2000.katespade.com/CS2000V4)
ksfa241
A@111000
Troubleshooting:
1. 
2. 
3. 
4.I can find follow error from web02 2026-01-23 apilog，
Error  info:
Procedure or function spwSE9016M_UpdateMemberInfo has too many arguments specified.
Procedure or function spwSE9016M_UpdateMemberInfo has too many arguments specified.
Procedure or function spwSE9016M_UpdateMemberInfo has too many arguments specified.
A possible object cycle was detected which is not supported. This can either be due to a cycle or if the object depth is larger than the maximum allowed depth of 0.
at csplus_api.Library.DbTools.GetDataFromDB[T](CConnectDB cConnectDB) in C:\Users\samuel ma\Desktop\program\Code\Project\csplus\csplus-api\BeAPI\Library\dbTools.cs:line 657
   at csplus_api.Library.DbTools.GetData[T](String query, Dictionary`2 param, Boolean withLog, String[] selectedRegion) in C:\Users\samuel ma\Desktop\program\Code\Project\csplus\csplus-api\BeAPI\Library\dbTools.cs:line 289

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (11 則)
**Tovi Wang** (2026-01-26):
@@Cy Lau @@Joy Li As we talked.Please help to further checking.Thanks!
**Tovi Wang** (2026-01-28):
@@Cy Lau @@Joy Li Add more info for reference:
This is the first time KS AU store use CS2000 web.
Tested in region Coach MY, the email records can be updated by CS2000 web. Sample Member: OC6000M00000975
Login account: oc13/oc13
Tested in KS MY region, KMY7200M0000996 member email can be updated as well.
Login account: kmy709/password
**Cy Lau** (2026-01-28):
@@Jerry Wong Please do the study for the RCA with log
**Cy Lau** (2026-01-28):
@@Joy Li  would mind checkng the differences between 
SP on KS AU Store vs Coach MY BY :
```
SELECT p.name, t.name AS type_name, p.max_length, p.is_output
FROM sys.parameters p
JOIN sys.types t ON p.user_type_id = t.user_type_id
WHERE object_id = OBJECT_ID('dbo.spwSE9016M_UpdateMemberInfo');
```
**Jerry Wong** (2026-01-28):
In csplus_api, this is the store procedure for updating member, could u check if  passing more parameters than the stored procedure actually accepts
EXEC [spwSE9016M_UpdateMemberInfo] @vip_no,@vip_birth_iyy,@vip_birth_imm,@vip_birth_idd,@vip_birth_date,@vip_first_name,@vip_last_name,@vip_title,@vip_name1,@vip_alias,@vip_addr_1,@vip_addr_2,@vip_addr_3,@vip_addr_4,@vip_tel_1,@vip_tel_2,@vip_email,@vip_id_no,@vip_sex,@vip_postal,@vip_dist_layer,@vip_dist_code,@vip_area,@vip_agegrp,@vip_sub_member,@vip_main_no,@vip_status,@vip_no_edm,@vip_no_dm,@vip_no_phone,@vip_no_sms,@vip_phone1_cntry,@vip_phone1_area,@vip_phone2_cntry,@vip_phone2_area,@vip_nation,@vip_country_code,@vip_country,@vip_addr_5,@vip_last_user, @datatable_glconfig
**Tovi Wang** (2026-01-29):
@@Jerry Wong Yes,I double checked the APILOG found that it is passing more parameters than the stored procedure actually accepts.
Details log capture as follow,So could you please advice and how to fix it?
1.Apply SQL:
2.ERROR - getDataFromDB()
**Tovi Wang** (2026-01-29):
@@Jerry Wong Thanks for your assist.
Found the RCA :
Caused by Missing parameters @vip_comp_code in Stored Procedures [dbo].[spwSE9016M_UpdateMemberInfo] table for 40 & 41 gegion.
**Tovi Wang** (2026-01-29):
StoredProcedure [dbo].[spwSE9016M_UpdateMemberInfo]    Script in current DB for KS AU
**Tovi Wang** (2026-01-30):
Add more info:
AWS ANZ region also NOT have this issue.
So we can confirmed just only KS ANZ region have this issue.
**Tovi Wang** (2026-02-02):
Hot fix had released to Coach QA.closed first.
Details as follow:
<u>**Software Release Note**</u>
**Installation Prerequisites**
No Back Office Release must be installed before install this release.
**Release Media**
COACH_L4.0.0_V70R3.142.zip
- 
- 
**Changes in This Release**
DB Change
-
**Automation for Jira** (2026-02-02):
Issue has been created since
Days since: 6
Week since : 0
Issue due date difference
Days since : 
Weeks since:

## 相關資訊

- Jira: [FE-1866](https://ctil.atlassian.net/browse/FE-1866)
- Fix Version: 未記錄
- 解決日期: 未記錄
