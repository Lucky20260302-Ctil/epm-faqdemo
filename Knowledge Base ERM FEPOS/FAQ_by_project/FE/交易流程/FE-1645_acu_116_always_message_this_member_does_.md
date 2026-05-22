---
tags: [faq, fe, 交易流程]
component: "Front End"
symptom: "Test data: CN member OCF53C00011415 (mobile: 18062000678) is existing in HK BE DB."
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-1645
resolved: 2025-03-21
fix-version: ""
---

# FE-1645: [ACU-116] Always message 'This member does not consent to enquire out of border' while searching CN member which is existing in HK Backend DB

## 問題

Test data: CN member OCF53C00011415 (mobile: 18062000678) is existing in HK BE DB.
Test POS FE : 10.33.248.2
1. 
1. 
1. 
Expected result:
Display the CN member in the HK POS, Member name and phone number from CN will be masked
Member OCF53C00011415 in DB,vip_com_code = '11'

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2025-03-21
### Jira Comments (9 則)
**Tovi Wang** (2025-03-10):
@@Bobby @@Sang @@Anson Cheung  Could you help to take a look Yoyo’s question and clarify the details logic for this background?Thanks!
**Tovi Wang** (2025-03-11):
@@Sang The POS version is 75.004.0409,WA log for your further checking,Thanks!
CC @@Bobby @@Cy Lau @@Anson Cheung
**Sang** (2025-03-11):
@@Tovi Wang @@Bobby @@Cy Lau @@Anson Cheung
result return from BEGW API , please consult Anson
**Bobby** (2025-03-11):
@@Tovi Wang Please get the sqllite log in \www\apabiqwposweb21 & 22 BEAPICRM\systemlog folder for Anson investigation.
**Bobby** (2025-03-11):
@@Anson Cheung ,  Log file for your investigation.
**Anson Cheung** (2025-03-11):
@@Bobby CDP customer privacy checking API returns: {"code":"CDP-CUST-404","message":"Customer not found","data":null}
**Tovi Wang** (2025-03-12):
We have replied the details to yoyo.waiting for her double confirm.
**Andrew_Au** (2025-03-21):
@@Tovi Wang @@pierre.shi Please update the ticket status
**Bobby** (2025-03-21):
According to the CBDT design, if HK and MO enquires CN customer record (vip_comp_code = 11), the information will be masked, otherwise, the information will not be masked.  Tapestry has accepted this. This ticket can be closed.

## 相關資訊

- Jira: [FE-1645](https://ctil.atlassian.net/browse/FE-1645)
- Fix Version: 未記錄
- 解決日期: 2025-03-21
