---
tags: [faq, mp, 交易流程]
component: "MPOS"
symptom: "New member cannot online update BE, API error data format issue"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: MP-563
resolved: 2024-01-22
fix-version: ""
---

# MP-563: New member cannot online update BE

## 問題

New member cannot online update BE, API error data format issue

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2024-01-22
### Jira Comments (6 則)
**Cy Lau** (2022-10-05):
Anson suspected that missing fields
**Andrew_Au** (2022-10-05):
-
**Anson Cheung** (2022-10-06):
Compare with Sang's input,
Missing value: vip_issue_date, vip_type_start_date, vip_create_date ,
Missing key: vip_no_edm, vip_no_dm, vip_no_phone, vip_no_sms, update_timestamp
**Cy Lau** (2022-10-07):
This would also affect issue [🔗](https://ctil.atlassian.net/browse/MP-563#icft=MP-563)
By the original design of sales memo - member section , the data fields couldn't fulfil upsert member nor communication optout.
@@Andrew_Au for the communication optout,
1) would it be only entered when creation?
2) would it be shown / edited ?
It would be estimated additional workload on new enquiry route for the upsert and optout
**Cy Lau** (2022-10-10):
enhancement : Staff indicator ?
@@Terence Tsang
**Andrew_Au** (2022-10-19):
Caused by testing POS region incorrect set in windows registry.

## 相關資訊

- Jira: [MP-563](https://ctil.atlassian.net/browse/MP-563)
- Fix Version: 未記錄
- 解決日期: 2024-01-22
