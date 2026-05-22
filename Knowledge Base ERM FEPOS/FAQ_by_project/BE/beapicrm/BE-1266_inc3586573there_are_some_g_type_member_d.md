---
tags: [faq, be, beapicrm]
component: "API"
symptom: "1.We found some G type member in DB"
root-cause: "待提取"
solution: "### Jira Comments (3 則)"
jira: BE-1266
resolved: 
fix-version: ""
---

# BE-1266:  [INC3586573]There are some G type member data in KS NZ & KS AU DB

## 問題

1.We found some G type member in DB
2.POS API will insert one default data to DB first.
3.
KSFN6481S001021
Event ID:72a87d358a0345aba1562c183048f7a3
Update the actual member data to DB,But connect DB occured  timeout error.

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (3 則)
**Tovi Wang** (2026-05-20):
@@Joy Li As talked.Internal Jira here.
@@Jerry Wong Please help to provide the details of the program enhancement.
**Jerry Wong** (2026-05-21):
currently logic of upsert member. if the input vip is not found, it would create member with default config values first, then update the vip with input values.
Enhancement:
if the input vip is not found, then create member with input values instead of creating default value and updating
**Jerry Wong** (2026-05-21):
the following vip table fields would be assigned value by user input in creating vip
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
Please check that

## 相關資訊

- Jira: [BE-1266](https://ctil.atlassian.net/browse/BE-1266)
- Fix Version: 未記錄
- 解決日期: 未記錄
