---
tags: [faq, fe, 交易流程]
component: "Front End"
symptom: "[ANZ] Missing 4 rows of vip_no_dm in body of  Dayend upsert member from [dbTrans].[dbo].[NEW VIP]"
root-cause: "待提取"
solution: "### Jira Comments (3 則)"
jira: FE-1888
resolved: 
fix-version: ""
---

# FE-1888: [ANZ] Missing 4 rows of vip_no_dm in body of  Dayend upsert member from [dbTrans].[dbo].[NEW VIP]

## 問題

[ANZ] Missing 4 rows of vip_no_dm in body of  Dayend upsert member from [dbTrans].[dbo].[NEW VIP]
body of  Dayend upsert member from [dbTrans].[dbo].[NEW VIP]:
{ "vip_no":"OC602MBS0000001", "vip_last_name":"TSEEES", "vip_first_name":"TESTERRRR", "vip_title":"", "vip_type":"C", "vip_issue_date":"2025/10/24", "vip_issue_loc":"OC602", "vip_expiry_date":"2026/10/23", "vip_birth_iyy":"1999", "vip_birth_imm":"09", "vip_birth_idd":"09", "vip_tel_1":"2728383894", "vip_tel_2":"6850123400", "vip_sex":"M", "vip_addr_1":" ", "vip_addr_2":" ", "vip_addr_3":" ", "vip_addr_4":" ", "vip_postal":" ", "[vip_email":"TESTER123246@GMAIL.COM](mailto:vip_email%22:%22TESTER123246@GMAIL.COM)", "update_timestamp":"2026/02/13 08:00:00", "vip_type_start_date":"2025/10/24", "vip_create_date":"2025/10/24", "vip_kana_first_name":"", "vip_kana_last_name":""}
Please refer to WA for details.

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (3 則)
**Automation for Jira** (2026-02-16):
Issue has been created since
Days since: 2
Week since : 0
Issue due date difference
Days since : 
Weeks since:
**Sang** (2026-02-16):
@@Sherman tse MPOS have not fill in data of Member communication channel, so upsert member  have not such row.
**Andrew_Au** (2026-05-05):
@@Sherman tse Please update the ticket status

## 相關資訊

- Jira: [FE-1888](https://ctil.atlassian.net/browse/FE-1888)
- Fix Version: 未記錄
- 解決日期: 未記錄
