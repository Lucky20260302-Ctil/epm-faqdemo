---
tags: [faq, mp, 交易流程]
component: "MPOS"
symptom: "we upgrade the API, the locregister table unable to get the device name, and the locreg_msmqserverna"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: MP-743
resolved: 2025-07-28
fix-version: ""
---

# MP-743: [MPOS-73]MPOS_3.29.5 (MPOS API + IPA) Posting Issue

## 問題

we upgrade the API, the locregister table unable to get the device name, and the locreg_msmqservername will show as XXXX, could you please help to check from your side? we've confirmed all the region upgrade to this version will encounter the issue no matter AWS(apawiqwposweb24) or Ali(apabiqwposweb23).

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2025-07-28
### Jira Comments (8 則)
**Cy Lau** (2025-01-16):
for the locreg_msmqservername , it would be the value of ShopConfig : MSMQ_SERVER_PATH
for the locreg_computername , it would be the AliasName from MPOS device ,
@@Tovi Wang  | @@Jason Wu ,
1. 
1. 
log Fetch ETA : 16 Jan
Investigation  ETA: 17Jan
@@Daniel Leung  Please follow
**Jason Wu** (2025-01-16):
MSMQ_SERVER_PATH
**Jason Wu** (2025-01-16):
Web.config has been replaced
**Cy Lau** (2025-01-17):
about the AliasName (locreg_computername),
The MPOS request validation from MPOS API:
The MPOS API response the AliasName with Unknown/
Then the locreg_computername has been updated at
Also /v1/Server/RegisterBE
But in LicDB :
Please get the Web.Config DAL Log , NPOS Log etc at MPOS API server.
@@Tovi Wang  @@Jason Wu
**Cy Lau** (2025-01-17):
Identified as LIcConnection value invalid
**Andrew_Au** (2025-03-07):
@@Tovi Wang @@pierre.shi Should I change the ticket status to close ?
**Automation for Jira** (2025-07-28):
Issue has been created since
Days since: 192
Week since : 27
Issue due date difference
Days since : 
Weeks since:
**Tovi Wang** (2025-07-28):
@@Andrew_Au Issue resolved,Please closed.

## 相關資訊

- Jira: [MP-743](https://ctil.atlassian.net/browse/MP-743)
- Fix Version: 未記錄
- 解決日期: 2025-07-28
