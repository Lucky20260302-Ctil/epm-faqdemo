---
tags: [faq, fe, 交易流程]
component: "Front End"
symptom: "as per the attached email, error messages are not correctly displayed"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-1526
resolved: 2025-02-24
fix-version: ""
---

# FE-1526: HKJC MDEER X3 annot show Jwt token is not valid error message after scan an invalid QR code

## 問題

as per the attached email, error messages are not correctly displayed

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2025-02-24
### Jira Comments (4 則)
**Sang** (2024-10-22):
JWT Token Error - cause infinite loop
**Sang** (2024-10-23):
**Sang** (2024-10-28):
1. 
'Response:{"ErrorCode":401,"ErrorDesc":"Jwt Token is not valid"} or 'Response:{"ErrorCode":401,"ErrorDesc":"QR Code is not valid"}
'Response:{"ErrorCode":402,"ErrorDesc":"Jwt Token is expired"} or 'Response:{"ErrorCode":402,"ErrorDesc":"QR Code is not expired"}
** **
**Sang** (2024-10-31):
Handle aws error response

## 相關資訊

- Jira: [FE-1526](https://ctil.atlassian.net/browse/FE-1526)
- Fix Version: 未記錄
- 解決日期: 2025-02-24
