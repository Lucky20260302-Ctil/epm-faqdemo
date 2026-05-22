---
project: BE
issue_key: BE-854
issue_type: Bug PRD
status: Closed
tags:
- 05_error_exception
- be
- data-interface
- error_exception
- faq
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/BE-854
created: '2024-05-09'
resolved: '2024-05-09'
fix_version: ''
components: []
has_images: false
category: 05_Error_Exception
category_label: 報錯與異常
quality: partial
title: 'BE-854: [CS-808] KS SEA CRM - Member transactions failed to register to Memberson CRM'
---
# BE-854: [CS-808] KS SEA CRM - Member transactions failed to register to Memberson CRM

## 問題描述

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

>> Return Empty

 

Member No:  RC000079832SG

[[https://qa-memberson-api.katespade.com/api/member/RC000079832SG/transactions?ncludeAllTiers=false&receiptNumber=00013028](https://qa-memberson-api.katespade.com/api/member/RC000079832SG/transactions?ncludeAllTiers=false&receiptNumber=00013028)]

>> memberNumber = RC000079832SG and Identifier = ‘308048c0-fe72-ee11-8472-025072d6ad94’

 

Step 3: Use 3.16 Void Transaction

Use result in Step 2: memberNumber = RC000079832SG and Identifier = ‘308048c0-fe72-ee11-8472-025072d6ad94’

[https://qa-memberson-api.katespade.com/api/member/RC000079832SG/transaction/308048c0-fe72-ee11-8472-025072d6ad94/void-purchase](https://qa-memberson-api.katespade.com/api/member/RC000079832SG/transaction/308048c0-fe72-ee11-8472-025072d6ad94/void-purchase)



## 相關資訊

- **Jira:** [BE-854](https://ctil.atlassian.net/browse/BE-854)
- **解決方式:** Done