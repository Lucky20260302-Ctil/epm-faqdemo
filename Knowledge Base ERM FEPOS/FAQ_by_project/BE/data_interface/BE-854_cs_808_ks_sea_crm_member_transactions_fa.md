---
tags: [faq, be, data_interface]
component: "Data Interface"
symptom: "Refer to [TAPSG POS API Specification v1_9_10.pdf](https://jira.tapestry.support/secure/attachment/8"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: BE-854
resolved: 2024-05-09
fix-version: ""
---

# BE-854: [CS-808] KS SEA CRM - Member transactions failed to register to Memberson CRM

## 問題

Refer to [TAPSG POS API Specification v1_9_10.pdf](https://jira.tapestry.support/secure/attachment/800199/800199_TAPSG+POS+API+Specification+v1_9_10.pdf)
<u>Register Transaction</u>
Current Logic: Registrar transaction with Member >> Registrar transaction with Member exclude member Type = E
Step 1 : Use 3.6 Get Membership Information [[https://qa-memberson-api.katespade.com/api/profile/00957423/memberships?memberType](https://qa-memberson-api.katespade.com/api/profile/00957423/memberships?memberType)=] to get active memberNumber
Member id: 00957423 >> Member No: RC000079832SG
Step 2: Use 3.15 Register Transactions with active memberNumber
Following existing Register flow with active memberNumber
<u>Void Transaction:</u>
Current Logic: Registrar transaction with Member >> Registrar transaction with Member exclude member Type = E
Step 1: Use 3.6 Get Membership Information [[https://qa-memberson-api.katespade.com/api/profile/00957423/memberships?memberType](https://qa-memberson-api.katespade.com/api/profile/00957423/memberships?memberType)=]
Member id: 00957423 >> Member No: VP000179997SG , RC000079832SG
Step 2: Use 3.17 Get Transactions
Loop below API with all member tier to get the memberNumber and Identifier.
[[https://qa-memberson-api.katespade.com/api/member/](https://qa-memberson-api.katespade.com/api/member/)**{memberNumber}**/transactions?ncludeAllTiers=false&receiptNumber=**{receiptNumber}**]
Sample:
Member No: VP000179997SG
[[https://qa-memberson-api.katespade.com/api/member/](https://qa-memberson-api.katespade.com/api/member/) VP000179997SG /transactions?ncludeAllTiers=false&receiptNumber=00013028]
Member No:  RC000079832SG
[[https://qa-memberson-api.katespade.com/api/member/RC000079832SG/transactions?ncludeAllTiers=false&receiptNumber=00013028](https://qa-memberson-api.katespade.com/api/member/RC000079832SG/transactions?ncludeAllTiers=false&receiptNumber=00013028)]
Step 3: Use 3.16 Void Transaction
Use result in Step 2: memberNumber = RC000079832SG and Identifier = ‘308048c0-fe72-ee11-8472-025072d6ad94’
[https://qa-memberson-api.katespade.com/api/member/RC000079832SG/transaction/308048c0-fe72-ee11-8472-025072d6ad94/void-purchase](https://qa-memberson-api.katespade.com/api/member/RC000079832SG/transaction/308048c0-fe72-ee11-8472-025072d6ad94/void-purchase)

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2024-05-09
### Jira Comments (1 則)
**Joy Li** (2024-05-09):
Program is released in V70R3.57 on 2024-05-06
QA Tester: @@Andrew_Au

## 相關資訊

- Jira: [BE-854](https://ctil.atlassian.net/browse/BE-854)
- Fix Version: 未記錄
- 解決日期: 2024-05-09
