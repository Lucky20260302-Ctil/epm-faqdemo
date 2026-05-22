---
tags: [faq, be, beapicrm]
component: "API"
symptom: "[Coach][CRM milestone 2] mapping issue of member id"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: BE-924
resolved: 2024-11-01
fix-version: ""
---

# BE-924: [Coach][CRM milestone 2] mapping issue of member id

## 問題

[Coach][CRM milestone 2] mapping issue of member id
- 
- 
{
    "code": "200",
    "message": "SUCCESS",
    "data": {
        "records": [
            {
              <span style="color:#ff5630">**  "id": "8537476690582695936",**</span>
                "customer_code": "1849135675391041536",
                "crm_id": "8537476690582695936",
                "customer_type": "PROSPECT",
                "open_id": null,
                "union_id": null,
                "taobao_nick": null,
                "wechat": null,
                "jd_id": null,
                "mobile": "18676585884",
                "mix_mobile": "09f5423c94f5b388c535efac6d8112e5",
                "jd_mix_mobile": null,
                "vipcom_mix_mobile": null,
                "mobile_valid_flag": false,
                "email": "[testtt@gmail.com](mailto:testtt@gmail.com)",
                "email_valid_flag": null,
                "name": "胡俊轩TT",
                "first_name": "TT",
                "last_name": "胡俊轩",
                "socialMedia": null,
                "status": 1,
                "driving_license": null,
                "birth_year": 1999,
                "birth_month": 10,
                "birth_day": 20,
                "spoken_language": null,
                "written_language": null,
                "gender_code": "M",
                "salutation_code": null,
                "registration_date": "2024-05-06T00:00:00.000+0800",
                "advisor_code": null,
                "counter_code": null,
                "management_advisor_code": null,
                "management_counter_code": null,
                "country_code": "CN",
                "nationality_code": "CN",
                "province_code": null,
                "province": null,
                "city_code": null,
                "city": null,
                "district_code": "",
                "district": null,
                "address1": "",
                "address2": "",
                "address3": "",
                "address4": "",
                "address_detail": "",
                "address_flag": null,
                "zip": "",
                "telephone": "",
                "telephone_valid_flag": null,
                "work_phone": null,
                "work_phone_valid_flag": null,
                "work_phone_areacode": null,
                "fax": null,
                "fax_valid_flag": null,
                "alternate_email": null,
                "alternate_email_valid_flag": null,
                "occupation_code": null,
                "occupation": "",
                "mix_nick": null,
                "contact_mean_id": null,
                "contact_time": null,
                "income_category": null,
                "unsubscription_flag": null,
                "first_channel_code": "POS",
                "delete_flag": false,
                "dedup_customer_id": null,
                "age_group": "",
                "seq_number": null,
                "promo_code": null,
                "request_type": null,
                "alias": "",
                "action": "C",
                "areacode": "",
                "staff_no": "",
                "no_edm": "0",
                "no_dm": "0",
                "no_phone": "0",
                "no_sms": "0",
                "accept_online_shopping": null,
                "no_wechat": null,
                "no_line": null,
                "repository_flag": null,
                "creation_date_time": "2024-10-24T01:07:54.949+0800",
                "modified_date_time": "2024-10-24T09:31:24.644+0800",
                "management_country": null,
                "source": null,
                "lapsed_flag": null,
                "dummy_flag": null,
                "campaign_date": null,
                "address_manually_valid": null,
                "last_date": "2024-10-23",
                "last_time": "17:18:14",
                "external_id": null,
                "total_valid_points": 9900.0,
                "tier_point": 9900.0,
                "first_purchase_date_time": "2024-05-06T17:52:00.000+0800",
                "first_purchase_amount": 9900.0,
                "last_purchase_date_time": "2024-05-06T17:52:00.000+0800",
                "last_purchase_amount": 9900.0,
                "last_year_amount": 9900.0,
                "last_year_unit_cnt": 1,
                "purchase_amount": 9900.0,
                "purchase_number": null,
                "vip_level": "B",
                "expiry_start_date": null,
                "expiry_end_date": "2025-05-31T23:59:59.000+0800",
                "pst_need_to_upgrade": null,
                "pst_need_to_renew": null,
                "next_vip_level": "C",
                "tier_priority": null,
                "privacy_policy": null,
                <span style="color:#bf2600">**"membership": "OC1350C00015337",**</span>
                "member_expiry_date": null,
                "employee": null,
                "comment": null,
                "client_category": null,
                "upgrade_date_time": null,
                "pnt_modified_date_time": null,
                "attribute1": null,
                "attribute2": null,
                "attribute3": null,
                "attribute4": null,
                "attribute5": null,
                "attribute6": null,
                "attribute7": null,
                "attribute8": null,
                "attribute9": null,
                "attribute10": null,
                "ouidMap": null,
                "omid": null,
                "channelCustomerDTOList": null,
                "client_type_desc": null,
                "client_type_code": null,
                "subMemberships": []
            }
        ],
        "pageNum": 0,
        "pageSize": 100,
        "isFirstPage": true,
        "isLastPage": true,
        "hasNextPage": false,
        "total": 1,
        "pages": 1
    }
}

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2024-11-01

## 相關資訊

- Jira: [BE-924](https://ctil.atlassian.net/browse/BE-924)
- Fix Version: 未記錄
- 解決日期: 2024-11-01
