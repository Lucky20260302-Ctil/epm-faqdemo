---
tags: [faq, be, beapicrm]
component: "API"
symptom: "Refer to API Interface Spec, Member Sync API (v2/cdp/member/pos/sync) should return Y or N in below "
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: BE-986
resolved: 2025-03-06
fix-version: ""
---

# BE-986: [ACU-109] Incorrect Member data in Member Sync API

## 問題

Refer to API Interface Spec, Member Sync API (v2/cdp/member/pos/sync) should return Y or N in below column.
But we found there are some member which return 0 & 1 instead Y/N which caused data update problem in our end. Could you please take a look?
API sample on 2025-01-01: (Some privacy data are replace by ***)
"body": "{"pageSize":"100","pageNum":0,"queryCondition":{"operationType":"AND","subQueryConditions":[
{"key":"mobile","value":"18939765208","valueType":"STRING","operationType":"EQUALS"}
]}}"}
{
"OK": "{"code":"200","message":"SUCCESS","data":{"records":[
{"id":"8621921","customer_code":"8621921","crm_id":null,"customer_type":"C","open_id":"oKCDxjjjJDhNtzZ_-wTpUeDV3WOE","union_id":"o_GI00aowlxLs2eyjPCPQGGsANpg","taobao_nick":null,"wechat":null,"jd_id":null,"mobile":"18939765208","mix_mobile":"6134b9bc69c847e942c20f548cb0b189","jd_mix_mobile":null,"vipcom_mix_mobile":null,"mobile_valid_flag":true,"email":"*********@qq.com","email_valid_flag":true,"name":"***","first_name":"女士","last_name":"蒋","socialMedia":null,"status":1,"driving_license":null,"birth_year":,"birth_month":,"birth_day":,"spoken_language":null,"written_language":null,"gender_code":"","salutation_code":"CN_MS","registration_date":"2015-03-08T00:00:00+08:00","advisor_code":null,"counter_code":"OCF3","management_advisor_code":"*******","management_counter_code":"OC53","country_code":"CN","nationality_code":"11","province_code":"SH","province":"上海","city_code":"SSG","city":"上海","district_code":null,"district":null,"address1":null,"address2":"上海市 ***","address3":null,"address4":null,"address_detail":"上海市 ***","address_flag":"0","zip":null,"telephone":null,"telephone_valid_flag":false,"work_phone":null,"work_phone_valid_flag":false,"work_phone_areacode":null,"fax":null,"fax_valid_flag":false,"alternate_email":null,"alternate_email_valid_flag":false,"occupation_code":null,"occupation":null,"mix_nick":null,"contact_mean_id":null,"contact_time":null,"income_category":null,"unsubscription_flag":false,"first_channel_code":"POS_outlet","delete_flag":false,"dedup_customer_id":null,"age_group":"** - **","seq_number":null,"promo_code":null,"request_type":null,"alias":null,"action":"M","areacode":null,"staff_no":null,"no_edm":"0","no_dm":"0","no_phone":"0","no_sms":"1","accept_online_shopping":null,"no_wechat":null,"no_line":null,"repository_flag":false,"creation_date_time":"2015-03-08T19:34:34.537+08:00","modified_date_time":"2025-01-01T16:27:34.199+08:00","management_country":null,"source":"1","lapsed_flag":false,"dummy_flag":false,"campaign_date":null,"address_manually_valid":"0","last_date":"2022-09-22","last_time":"22:27:04","external_id":null,"total_valid_points":0.0,"tier_point":4400.0,"first_purchase_date_time":"2015-03-08T00:00:00+08:00","first_purchase_amount":2080.0,"last_purchase_date_time":"2022-09-18T00:00:00+08:00","last_purchase_amount":4400.0,"last_year_amount":0.0,"last_year_unit_cnt":0,"purchase_amount":20784.0,"purchase_number":7,"vip_level":"C","expiry_start_date":null,"expiry_end_date":"2023-09-30T23:59:59+08:00","pst_need_to_upgrade":5000.0,"pst_need_to_renew":0.0,"pts_need_to_upgrade":5000.0,"pts_need_to_renew":0.0,"next_vip_level":"B","tier_priority":"5","privacy_policy":null,"membership":"OCF32C00094737","member_expiry_date":null,"employee":null,"comment":null,"client_category":null,"upgrade_date_time":"2022-09-20T00:29:41.314+08:00","pnt_modified_date_time":"2023-10-01T23:17:49.886+08:00","attribute1":null,"attribute2":null,"attribute3":"6134b9bc69c847e942c20f548cb0b189","attribute4":"OCF3","attribute5":null,"attribute6":"2015-03-08 00:00:00.000","attribute7":"2019-07-24 00:00:00.000","attribute8":null,"attribute9":null,"attribute10":null,"ouidMap":null,"omid":null,"channelCustomerDTOList":null,"client_type_desc":null,"client_type_code":null,"subMemberships":["OCF32C00094737"]}
![](https://jira.tapestry.support/images/icons/mail_small.gif)
],"pageNum":0,"pageSize":100,"isFirstPage":true,"isLastPage":true,"hasNextPage":false,"total":1,"pages":1}}"

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2025-03-06
### Jira Comments (6 則)
**Bobby** (2025-01-15):
The POS system calls the BEAPI to update the VIP record in the backend. When CRM returns an expiry date that does not match our record's expiry date, the current logic rejects the update to prevent accidentally overriding the expiry date through the API. CRM serves as the master member database and updating CRM member profile data in our backend is necessary. Therefore, I suggest adding a configuration setting for ACXIOM CRM to bypass the expiry date check and override the profile in our VIP record.
**Andrew_Au** (2025-02-25):
@bobby Did you kown the ticket status ?
**Sherman tse** (2025-02-25):
@@Andrew_Au I am working on it
**Anson Cheung** (2025-03-03):
Release V1.6.20
\\ds411\public\samuel\beapi\v1.6.20_20250115
**Bobby** (2025-03-03):
@@Sherman tse , Please help me to include this ticket in your QC testing.
**Sherman tse** (2025-03-04):
Verified on QA with 1.06.20
test case attached

## 相關資訊

- Jira: [BE-986](https://ctil.atlassian.net/browse/BE-986)
- Fix Version: 未記錄
- 解決日期: 2025-03-06
