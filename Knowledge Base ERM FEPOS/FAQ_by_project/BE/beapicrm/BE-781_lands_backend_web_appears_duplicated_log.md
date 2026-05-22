---
tags: [faq, be, beapicrm]
component: "Backend (Web)"
symptom: "VM: 172.16.138.65"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: BE-781
resolved: 2023-08-01
fix-version: ""
---

# BE-781: [Lands] BackEnd Web appears duplicated log in Interface Update Log Enquiry (SE8008)

## 問題

VM: 172.16.138.65
[https://172.16.138.65/EnterpriseSystemAPI/swagger/index.html](https://172.16.138.65/EnterpriseSystemAPI/swagger/index.html)
Reproduce steps:
Execute import log API: /api/v1/ImportLog for **1 time** with 1753 yr
{
"data": [
{
"importEndDateTime": "1753-07-18T08:14:38.674Z",
"errMessage": "test1753",
"successfulCount": 0,
"failCount": 0,
"totalCount": 0,
"lineErrs": [
{
"lineNo": 0,
"errMessage": "test1753"
}
],
"filename": "test1753",
"importStartDateTime": "1753-07-18T08:14:38.674Z",
"fileDateTime": "1753-07-18T08:14:38.674Z"
}
]
}
Existing result:
BackEnd Web appears duplicated log in Interface Update Log Enquiry (SE8008)
Remark:
Issue seems occurs in inputing 1753 yr only

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2023-08-01
### Jira Comments (1 則)
**Sherman tse** (2023-08-01):
Verified on LANDS uat, close case

## 相關資訊

- Jira: [BE-781](https://ctil.atlassian.net/browse/BE-781)
- Fix Version: 未記錄
- 解決日期: 2023-08-01
