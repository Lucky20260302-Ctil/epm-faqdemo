---
tags: [faq, be, beapicrm]
component: "Backend (Web)"
symptom: "Reproduce steps:"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: BE-867
resolved: 2024-08-30
fix-version: ""
---

# BE-867: 建立Location code時, 選擇了已存在的country code, 但仍然彈出了currency Code无效提示

## 問題

Reproduce steps:
1. 
2. 
3. 
4. 
5. 
Incorrect result:
-

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2024-08-30
### Jira Comments (5 則)
**Andrew_Au** (2024-07-05):
Fixed the api isseu. Please try again.
**Andrew_Au** (2024-07-05):
Please use this link [https://172.16.138.95/ChainStorePlus_LandsD_QA/](https://172.16.138.95/ChainStorePlus_LandsD_QA/) test again. we fixed api issue.
**ryan** (2024-07-08):
问题依旧存在
`{"data":{"ds":{"loctab":[{"loctab_code":"LC","loctab_name":"1","loctab_addr_1":"2","loctab_addr_2":"3","loctab_addr_3":"4","loctab_city":"shanghai","loctab_email":"","loctab_person":"tr","loctab_phone":"88888888","loctab_phone_int":"","loctab_fax":"","loctab_postal":"","loctab_curr":"HKD","loctab_class":"LC","loctab_type":"O","loctab_franchise":"Y","loctab_open_date":"2024-06-30T16:00:00.000Z","loctab_close_date":null,"loctab_country":"HK","loctab_group":"PG","loctab_cust":"CC1","loctab_dist_code":"D1","loctab_link_wh":"","loctab_as400":"","loctab_channel":"1","loctab_int_reason":null,"loctab_int_reason2":null,"loctab_tax_code":"1","loctab_repl_layer":"","loctab_depart_store":"N","loctab_project":"N","loctab_not_download":"","loctab_not_tfx_from":"N","loctab_not_tfx_to":"N","loctab_tax_exempt":"N","loctab_exclude_oh":"N","loctab_ecomm_int":"N","loctab_ecomm_wh":"","loctab_ecomm_ret_wh":"","loctab_sts_layer":null,"loctab_stw_layer":null,"loctab_grp_layer_1":null,"loctab_grp_code_1":null,"loctab_grp_layer_2":null,"loctab_grp_code_2":null,"loctab_grp_layer_3":null,"loctab_grp_code_3":null,"loctab_grp_layer_4":null,"loctab_grp_code_4":null,"loctab_grp_layer_5":null,"loctab_grp_code_5":null,"loctab_grp_layer_6":null,"loctab_grp_code_6":null,"loctab_grp_layer_7":null,"loctab_grp_code_7":null,"loctab_grp_layer_8":null,"loctab_grp_code_8":null,"loctab_grp_layer_9":null,"loctab_grp_code_9":null,"loctab_grp_layer_10":null,"loctab_grp_code_10":null}]}}}`
**Andrew_Au** (2024-07-08):
I created the new location without error. please try again [https://172.16.138.95/ChainStorePlus_LandsD_QA](https://172.16.138.95/ChainStorePlus_LandsD_QA)
**Andrew_Au** (2024-08-29):
Are you still face the isse in this QA site :[https://172.16.138.95/ChainStorePlus_LandsD_QA](https://172.16.138.95/ChainStorePlus_LandsD_QA)

## 相關資訊

- Jira: [BE-867](https://ctil.atlassian.net/browse/BE-867)
- Fix Version: 未記錄
- 解決日期: 2024-08-30
