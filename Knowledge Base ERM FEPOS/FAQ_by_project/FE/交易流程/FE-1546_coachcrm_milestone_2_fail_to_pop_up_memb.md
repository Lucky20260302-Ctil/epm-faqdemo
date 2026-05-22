---
tags: [faq, fe, 交易流程]
component: "Front End"
symptom: "Reproduce steps:"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-1546
resolved: 2024-11-08
fix-version: ""
---

# FE-1546: [Coach][CRM milestone 2] Fail to pop up member creation screen after scan a new wechat QR code

## 問題

Reproduce steps:
1. 
2. 
Existing result:
Fail to pop up member creation screen after scan a new wechat QR code
New QR string:
YVhaQWRYTmxaRFIwWVhCemRISjVQUT09cThjUmFBSEZwa3dpV2EzZmdaWmpkNWNXREpWY1NCMWs3RUp0VVNteDIwRGdXWkFLRFF1d3RHQ3RFWHc2c1dsT3RYbW5UcCtJQjJYdUZFNEJpcWlYWFJZTktXQ0JLUU5Nbm1SK0E3TTNEQXByR2xjekFDUUxlenBjdlJJYlNiTis=
Old QR string:
YVhaQWRYTmxaRFIwWVhCemRISjVQUT09djJFYmppRDdxaE5pczBnK21RdGJHSzlyejB6V3lBK09oc0RsM0hLODdUUVZydFFwUmNFUXpjSDcwYjIwMnUvUXJVMElrcUFhN2xuRUErQWxHTHpkSUpyRzZBWHBkMXR6VGxmbU9EWWF6U1ZoN2ZDSDBkT2JzYXdLNUd6QWRGU2dqeEhkSjRHdENxMFc2dEVsL2JWTTVBPT0=
DBmas & DBtrans:
\\172.16.183.201\localuser\support\20241101\Sang
VM IP:
172.16.138.131
.\sxd
Yan20201104@

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2024-11-08
### Jira Comments (4 則)
**Sang** (2024-11-01):
set tblconfig.MEMBERNOTFOUNDAUTOCREATE='Y'
**Sang** (2024-11-01):
**Sang** (2024-11-01):
Member Panel Show Member Info which  returned from BEGW  (Refer to uploaded screen)
**Sherman tse** (2024-11-08):
Verified on QA
Close case

## 相關資訊

- Jira: [FE-1546](https://ctil.atlassian.net/browse/FE-1546)
- Fix Version: 未記錄
- 解決日期: 2024-11-08
