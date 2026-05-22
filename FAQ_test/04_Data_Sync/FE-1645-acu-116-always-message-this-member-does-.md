---
project: FE
issue_key: FE-1645
issue_type: Bug PRD
status: Closed
faq_score: 7.5
faq_category: 04_Data_Sync
faq_category_label: 資料與同步
tags: [faq, fe, data_sync, front-end]
jira_url: "https://ctil.atlassian.net/browse/FE-1645"
created: 2025-03-10
resolved: 2025-03-21
resolution: Done
has_images: True
---

# FE-1645: [ACU-116] Always message 'This member does not consent to enquire out of border' while searching CN member which is existing in HK Backend DB

> **類型:** Bug PRD | **狀態:** Closed
> **分類:** 資料與同步 | **FAQ 分數:** 7.5
> **解決日期:** 2025-03-21
> **負責人:** Anson Cheung
> **組件:** Front End

## 問題描述

Test data: CN member OCF53C00011415 (mobile: 18062000678) is existing in HK BE DB.

Test POS FE : 10.33.248.2

1. Go to HK POS member page

2. input 18062000678 to search member, the message 'This member does not consent to enquire out of border' is popped up.

3. Input member number OCF53C00011415 to search member, the message This member does not consent to enquire out of border' is popped up. '

Expected result:

Display the CN member in the HK POS, Member name and phone number from CN will be masked

> 📎 **image-20250310-065245.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/b7a6edce-d47d-4d43-8150-7d110eff168c)（需 Jira 登入）
Member OCF53C00011415 in DB,vip_com_code = '11'

> 📎 **image-20250310-070046.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/c6567bb5-b396-4793-bd11-7d395a9b236f)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20250310-065245.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/b7a6edce-d47d-4d43-8150-7d110eff168c)
2. 📎 **image-20250310-070046.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/c6567bb5-b396-4793-bd11-7d395a9b236f)


## Jira Comments

> **Tovi Wang** (2025-03-10):
>       Could you help to take a look Yoyo’s question and clarify the details logic for this background?Thanks!

> **Tovi Wang** (2025-03-11):
>  The POS version is 75.004.0409,WA log for your further checking,Thanks! CC       

> **Sang** (2025-03-11):
>         result return from BEGW API , please consult Anson

> **Bobby** (2025-03-11):
>  Please get the sqllite log in \www\apabiqwposweb21 & 22 BEAPICRM\systemlog folder for Anson investigation. 

> **Bobby** (2025-03-11):
>  ,   Log file for your investigation. 

> **Anson Cheung** (2025-03-11):
>  CDP customer privacy checking API returns: {"code":"CDP-CUST-404","message":"Customer not found","data":null} 

> **Tovi Wang** (2025-03-12):
> We have replied the details to yoyo.waiting for her double confirm.

> **Andrew_Au** (2025-03-21):
>    Please update the ticket status

> **Bobby** (2025-03-21):
> According to the CBDT design, if HK and MO enquires CN customer record (vip_comp_code = 11), the information will be masked, otherwise, the information will not be masked.  Tapestry has accepted this. This ticket can be closed. 

## 相關資訊

- **Jira:** [FE-1645](https://ctil.atlassian.net/browse/FE-1645)
- **解決方式:** Done