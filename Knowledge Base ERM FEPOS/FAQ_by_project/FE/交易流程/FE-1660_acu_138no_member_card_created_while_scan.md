---
tags: [faq, fe, 交易流程]
component: "Front End"
symptom: "Test BE Release: R3.93"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-1660
resolved: 2025-05-02
fix-version: ""
---

# FE-1660: [ACU-138]No member card created while scanning new registered member' QR code

## 問題

Test BE Release: R3.93
test POS OCQA1-0: 10.33.248.4
test steps:
1.register member in mini program member center with mobile 19921610075
2.go to CN POS member page, scan Register QR code, no member card created for this member, the expected result should be new member card created for this register member.
3.click confirm, there is error message 'Object Reference not set to...'
1.
2.
3.点击确认后出现下面报错。

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2025-05-02
### Jira Comments (12 則)
**Tovi Wang** (2025-03-25):
@@Sang @@Anson Cheung Please help to take a look this issue.Follow FE log for your further checking.
@@Sherman tse  Could you help to take a look this issue if can reproduced in our QA PC?Thanks!
CC @@Bobby @@Cy Lau
**Cy Lau** (2025-03-25):
@@Tovi Wang  , just want to know, they created the member outsife csplus, and csplus using the QR Code passing to CRM API for member, return as 404 or what ?
**Tovi Wang** (2025-03-26):
@@Cy Lau
1.From WA log,csplus using the QR Code passing to CRM API api/v1/fepos/acxiom/member for member,CRM API return bellow info.Let me copy CRMBEAPI for further confirming.
**Cy Lau** (2025-03-26):
@@Tovi Wang  there is no object reference set to object error from your log tho
**Tovi Wang** (2025-03-26):
@@Cy Lau @@Bobby @@Anson Cheung
1.csplus using the QR Code passing to CRM API for member
2.Cll API /api/v1/acxiom/member,API response as follow:
**Tovi Wang** (2025-03-26):
@@Cy Lau @@Anson Cheung
“@@Tovi Wang  there is no object reference set to object error from your log tho“
-->I can see the error in T9 log.But NOT fount the error in WA log & BEAPI log.
**Cy Lau** (2025-03-26):
The error : Object reference not set to an instance of an object.
[20250325 18:30:13 -3798](doInputVip): doInputVip- Start : Avail V.  Memory : 140736147.362
[20250325 18:30:22 -8719]: Search QC Code Member by Phone No 19921610075-start
[20250325 18:30:25 -4423]:  Status NoExist
[20250325 18:30:25 -4733]: Search QC Code Member -Found, Get Details Completed
<span style="color:#36b37e">**[20250325 18:34:43 -3694]: DC.GetMember**</span>
<span style="color:#36b37e">**[20250325 18:34:47 -0193]: Completed**</span>
<span style="color:#36b37e">**[20250325 18:34:47 -0483]: doMsgCenterMsg- Start : Avail V.  Memory : 140701715.89**</span>
<span style="color:#ff5630">**[20250325 18:34:47 -0493]: doInputVip.Error: Object reference not set to an instance of an object.**</span>
2025/03/25 18:30:21.321 Member QR Code : {"Name":"casey","Mobile":"19921610075","DOB(Year)":"2020","DOB(Mon)":"03","DOB(Day)":"25","Gender":"F","DynamicToken":"9bQsE6AEUCChcRg4"}
2025/03/25 18:30:22.872 SearchMembersByExact start
2025/03/25 18:30:25.436 SearchMembersByExact Completed :1
<span style="color:#36b37e">2025/03/25 18:34:43.490 Online add  Member : </span>
2025/03/25 18:30:21.324 [20250325 06:30:21] ValidateQRCodeToken_acxiom.Start
2025/03/25 18:30:21.325 [20250325 06:30:21] {"dynamicToken":"9bQsE6AEUCChcRg4"}
2025/03/25 18:30:21.325 [20250325 06:30:21] API Call: api/v1/fepos/acxiom/dynamicTokenVerify
2025/03/25 18:30:22.826 [20250325 06:30:22] Result:SUCCESS
2025/03/25 18:30:22.827 [20250325 06:30:22] Response:{"successful":true,"data":{"callCRM":true,"dynamicToken":true,"message":""}}
2025/03/25 18:30:22.829 [20250325 06:30:22] ValidateQRCodeToken_acxiom.End
2025/03/25 18:30:22.879 [20250325 06:30:22] GetMemberListAdv.Start
2025/03/25 18:30:22.880 [20250325 06:30:22] {"DefaultNVipName":"","DefaultNVipEmail":"","ShowCancelMember":true,"CompanyCode":"","IsSearchExact":true,"RowsPerPage":100,"Action":0,"MemberNoRef":"","Filter":{"MemberNo":"","Name":"","FirstName":"","LastName":"","ID":"","HomePhone":"","MobilePhone":"19921610075","Email":"","StaffNo":""},"FilterMatchType":0}
2025/03/25 18:30:22.880 [20250325 06:30:22] API Call: api/v1/fepos/acxiom/member
2025/03/25 18:30:25.433 [20250325 06:30:25] Result:SUCCESS
2025/03/25 18:30:25.434 [20250325 06:30:25] Response:{"successful":true,"data":[{"Vipmas_name":"casey","Vipmas_type":"P","Vipmas_status":"1","Vipmas_expiry_date":"2099-12-31T23:59:59+08:00","Vipmas_tel_no_2":"19921610075","Vipmas_sex":"F","Vipmas_nation":"CN","Vipmas_birth_date":"2020-03-25T00:00:00","Vipmas_join_date":"2025-03-25T18:29:09.77+08:00","Vipmas_email":"","jsonData":{"id":"8592821685307269120","customer_code":"1904480670112075776","crm_id":"8592821685307269120","customer_type":"PROSPECT","open_id":"oKCDxjoEGiu3f9ut2Deh5mXnsDII","union_id":"o_GI00QlYj3kbhtXO1KUfZrpkb5I","taobao_nick":null,"wechat":null,"jd_id":null,"mobile":"19921610075","mix_mobile":"7646503e0cf5263199ccba4ca80b257d","jd_mix_mobile":null,"vipcom_mix_mobile":null,"mobile_valid_flag":true,"email":"","email_valid_flag":null,"name":"casey","first_name":null,"last_name":null,"socialMedia":null,"status":1,"driving_license":null,"birth_year":2020,"birth_month":3,"birth_day":25,"spoken_language":null,"written_language":null,"gender_code":"F","salutation_code":null,"registration_date":"2025-03-25T18:29:09.77+08:00","advisor_code":null,"counter_code":null,"management_advisor_code":null,"management_counter_code":null,"country_code":"CN","nationality_code":null,"province_code":null,"province":"","city_code":null,"city":"","district_code":null,"district":"","address1":null,"address2":null,"address3":null,"address4":null,"address_detail":"","address_flag":null,"zip":null,"telephone":null,"telephone_valid_flag":null,"work_phone":null,"work_phone_valid_flag":null,"work_phone_areacode":null,"fax":null,"fax_valid_flag":null,"alternate_email":null,"alternate_email_valid_flag":null,"occupation_code":null,"occupation":null,"mix_nick":null,"contact_mean_id":null,"contact_time":null,"income_category":null,"unsubscription_flag":null,"first_channel_code":"WECHAT","delete_flag":false,"dedup_customer_id":null,"age_group":null,"seq_number":null,"promo_code":null,"request_type":null,"alias":null,"action":null,"areacode":null,"staff_no":null,"no_edm":null,"no_dm":null,"no_phone":null,"no_sms":null,"accept_online_shopping":null,"no_wechat":null,"no_line":null,"repository_flag":null,"creation_date_time":"2025-03-25T18:29:09.77+08:00","modified_date_time":"2025-03-25T18:29:10.267+08:00","management_country":null,"source":null,"lapsed_flag":null,"dummy_flag":null,"campaign_date":null,"address_manually_valid":null,"last_date":null,"last_time":null,"external_id":null,"total_valid_points":0.0,"tier_point":0.0,"first_purchase_date_time":null,"first_purchase_amount":null,"last_purchase_date_time":null,"last_purchase_amount":null,"last_year_amount":null,"last_year_unit_cnt":null,"purchase_amount":null,"purchase_number":null,"vip_level":"P","expiry_start_date":null,"expiry_end_date":"2099-12-31T23:59:59+08:00","pst_need_to_upgrade":0.0,"pst_need_to_renew":0.0,"next_vip_level":"C","tier_priority":"7","privacy_policy":null,"membership":null,"member_expiry_date":null,"employee":null,"comment":null,"client_category":null,"upgrade_date_time":null,"pnt_modified_date_time":null,"attribute1":null,"attribute2":null,"attribute3":null,"attribute4":null,"attribute5":null,"attribute6":null,"attribute7":null,"attribute8":null,"attribute9":null,"attribute10":null,"ouidMap":null,"omid":null,"channelCustomerDTOList":null,"client_type_desc":null,"client_type_code":null,"subMemberships":[]},"vip_create_date":"2025-03-25T18:29:09.77+08:00"}]}
2025/03/25 18:30:25.435 [20250325 06:30:25] GetMemberListAdv.End
<span style="color:#36b37e">**2025/03/25 18:34:43.831 [20250325 06:34:43] GetEcoupons.Start**</span>
<span style="color:#36b37e">**2025/03/25 18:34:43.831 [20250325 06:34:43] {"Vipmas_vip_code":"","vipmas_tel_no_2":"19921610075"}**</span>
<span style="color:#36b37e">**2025/03/25 18:34:43.832 [20250325 06:34:43] API Call: api/v1/fepos/coupon/queryCustomerCoupons**</span>
<span style="color:#36b37e">**2025/03/25 18:34:46.249 [20250325 06:34:46] Result:SUCCESS**</span>
<span style="color:#36b37e">**2025/03/25 18:34:46.249 [20250325 06:34:46] Response:{"successful":true,"data":[]}**</span>
<span style="color:#36b37e">**2025/03/25 18:34:46.252 [20250325 06:34:46] GetEcoupons.End**</span>
@@Tovi Wang  that’s how should be a log tracing log like
**Cy Lau** (2025-03-26):
One thing shall be curious for is
2025/03/25 18:34:43.490 Online add  Member :
no data following
And Also 
[20250325 18:30:25 -4423]:  Status NoExist
**Cy Lau** (2025-03-26):
RCA found,
Owing to the SOW :
With disable upsert (all)
the return result would be :
{            "vip_name1": "casey",
            "vip_birth_date": "2020-03-25T00:00:00",
            "vip_issue_date": "2025-03-25T18:29:09.77+08:00",
            "vip_email": "",
            "vip_sex": "F",
            "vip_nation": "CN",
            "vip_tel_2": "19921610075",
            "vip_type": "P",
            "vip_status": "1",
            "vip_create_date": "2025-03-25T18:29:09.77+08:00",
            "vip_expiry_date": "2099-12-31T23:59:59+08:00"
        }
Correct Result :
{"vip_no": "OCQ91TC00000007",
    "vip_name1": "you 红",
    "vip_birth_date": "1999-03-20T00:00:00",
    "vip_issue_date": "2025-03-20T10:01:52.418+08:00",
    "vip_email": ["yyou@coach.com](mailto:"yyou@coach.com)",
    "vip_sex": "F",
    "vip_nation": "CN",
    "vip_tel_2": "15008476947",
    "vip_no_edm": "N",
    "vip_no_dm": "N",
    "vip_no_phone": "N",
    "vip_no_sms": "N",
    "vip_type": "V",
    "vip_status": "1",
    "vip_create_date": "2025-03-20T10:01:52.418+08:00",
    "vip_expiry_date": "2026-03-31T23:59:59+08:00"
}
So for the disable feature, adding back the Member API Result without membership
The checking is just an example, please verify and enhance it.
@@Anson Cheung
**Anson Cheung** (2025-03-28):
Release:
[\\ds411\public\samuel\beapi\v1.7.12_20250326](file://ds411/public/samuel/beapi/v1.7.12_20250326)
- 
-
**Sherman tse** (2025-04-01):
Verified on QA
**Sherman tse** (2025-05-02):
Issue has closed in Tapestry jira
close case

## 相關資訊

- Jira: [FE-1660](https://ctil.atlassian.net/browse/FE-1660)
- Fix Version: 未記錄
- 解決日期: 2025-05-02
