---
tags: [faq, fe, 交易流程]
component: "Front End"
symptom: "[Coach][CRM milestone 2] Search a member by Scan QR code but Button of Purchase history & Profile di"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-1542
resolved: 2024-11-18
fix-version: ""
---

# FE-1542: [Coach][CRM milestone 2] Search a member by Scan QR code but Button of Purchase history & Profile dimmed 

## 問題

[Coach][CRM milestone 2] Search a member by Scan QR code but Button of Purchase history & Profile dimmed
Member in CRM : `OC1350C00015337`
QR code: YVhaQWRYTmxaRFIwWVhCemRISjVQUT09djJFYmppRDdxaE5pczBnK21RdGJHSzlyejB6V3lBK09oc0RsM0hLODdUUVZydFFwUmNFUXpjSDcwYjIwMnUvUXJVMElrcUFhN2xuRUErQWxHTHpkSUpyRzZBWHBkMXR6VGxmbU9EWWF6U1ZoN2ZDSDBkT2JzYXdLNUd6QWRGU2dqeEhkSjRHdENxMFc2dEVsL2JWTTVBPT0=
Front end got result from APi:
Button of Purchase history & Profile dimmed when scan QR code for members from CRM
Expected result:
Button of Purchase history & Profile undimmed & checkable when members have details from CRM side

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2024-11-18
### Jira Comments (2 則)
**Sang** (2024-11-14):
Member info w/o Jsondata data means data retrieved from BE DB rather than return from CRM.
**Sherman tse** (2024-11-18):
Verified on QA
Able to undim botton: purchase history & profile when users scan vaild qr code

## 相關資訊

- Jira: [FE-1542](https://ctil.atlassian.net/browse/FE-1542)
- Fix Version: 未記錄
- 解決日期: 2024-11-18
