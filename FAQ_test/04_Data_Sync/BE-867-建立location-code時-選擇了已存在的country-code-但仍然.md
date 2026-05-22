---
project: BE
issue_key: BE-867
issue_type: Bug QA
status: Closed
tags:
- 04_data_sync
- backend-(web)
- be
- data_sync
- faq
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/BE-867
created: '2024-07-02'
resolved: '2024-08-30'
fix_version: ''
components: []
has_images: true
category: 04_Data_Sync
category_label: 資料同步
quality: partial
---
# BE-867: 建立Location code時, 選擇了已存在的country code, 但仍然彈出了currency Code无效提示

> **類型:** Bug QA | **狀態:** Closed
> **分類:** 資料與同步 | **FAQ 分數:** 5.5
> **解決日期:** 2024-08-30
> **負責人:** ryan
> **組件:** Backend (Web)

## 問題描述

Reproduce steps:

1. 新建一個 Primary-Location

2. 填入必要輸入的資料

3. 在Other Properties table的Country选择“HK”

4. General Info table中的currency自动赋值为“HKD”

5. 点击save

Incorrect result:

- 提示currency Code无效

> 📎 **image-20240702-060056.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/33e681b2-3f3d-41d9-bc99-0942d0e09878)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20240702-060056.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/33e681b2-3f3d-41d9-bc99-0942d0e09878)


## Jira Comments

> **Andrew_Au** (2024-07-05):
> Fixed the api isseu. Please try again.

> **Andrew_Au** (2024-07-05):
> Please use this link  https://172.16.138.95/ChainStorePlus_LandsD_QA/  test again. we fixed api issue.

> **ryan** (2024-07-08):
> 问题依旧存在 {"data":{"ds":{"loctab":[{"loctab_code":"LC","loctab_name":"1","loctab_addr_1":"2","loctab_addr_2":"3","loctab_addr_3":"4","loctab_city":"shanghai","loctab_email":"","loctab_person":"tr","loctab_phone":"88888888","loctab_phone_int":"","loctab_fax":"","loctab_postal":"","loctab_curr":"HKD","loctab_class":"LC","loctab_type":"O","loctab_franchise":"Y","loctab_open_date":"2024-06-30T16:00:00.000Z","loctab_close_date":null,"loctab_country":"HK","loctab_group":"PG","loctab_cust":"CC1","loctab_dist_code":"D1","loctab_link_wh":"","loctab_as400":"","loctab_channel":"1","loctab_int_reason":null,"loctab_int_reason2":null,"loctab_tax_code":"1","loctab_repl_layer":"","loctab_depart_store":"N","loctab_project":"N","loctab_not_download":"","loctab_not_tfx_from":"N","loctab_not_tfx_to":"N","loctab_

> **Andrew_Au** (2024-07-08):
> I created the new location without error. please try again  https://172.16.138.95/ChainStorePlus_LandsD_QA

> **Andrew_Au** (2024-08-29):
> Are you still face the isse in this QA site : https://172.16.138.95/ChainStorePlus_LandsD_QA

## 相關資訊

- **Jira:** [BE-867](https://ctil.atlassian.net/browse/BE-867)
- **解決方式:** Done