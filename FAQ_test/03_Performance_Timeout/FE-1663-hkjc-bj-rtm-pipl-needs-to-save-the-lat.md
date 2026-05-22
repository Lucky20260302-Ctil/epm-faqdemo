---
project: FE
issue_key: FE-1663
issue_type: Bug QA
status: Test in Progress
faq_score: 10.0
faq_category: 03_Performance_Timeout
faq_category_label: 效能與逾時
tags: [faq, fe, performance_timeout, pos+be]
jira_url: "https://ctil.atlassian.net/browse/FE-1663"
created: 2025-03-30
resolved: 
resolution: 
has_images: False
---

# FE-1663: HKJC BJ RTM - PIPL needs to save the latest IsConsentToHK in Deposit Return and Deposit Settlement.  

> **類型:** Bug QA | **狀態:** Test in Progress
> **分類:** 效能與逾時 | **FAQ 分數:** 10.0
> **負責人:** Bobby
> **組件:** POS+BE

## 問題描述

In accordance with PIPL requirements, any changes to the isConsentToHK indicator will take effect immediately. Therefore, it is essential to save the latest isConsentToHK status in both the deposit return and Deposit Settlement. Additionally, POS postings must update this status in the deposit journal. The issue of transaction synchronization can be disregarded, as Datamart will mask all customer transactions, rendering the data unusable. However, void deposits and void deposit settlements can be exceptions, as these actions occur only on the same day.

We expect the update for the deposit records to be based on the consent status as at the moment of the void/settlement.

Given that there could be a long timeframe between deposit and settlement, it is possible that the consent flag would change during the time.

Therefore, we expect the update of the deposit to be based on the latest consent flag of the members.

 

1. Records in deposit table for members with consent updated to “no” still being updated - seems unexpected?

 

Created deposit 00000174 and 00000175 for consented member, then updated consent flag to **non**-consent.

After non-consent, settle 174 and void 175.

In DM_HOSP Sales, the settled check (00001350) is not sent (expected).

However, in DM_HOSP Deposit, update is still being received , 175 updated status to 41

 

Similarly for the HK Member case :

 

Created deposit 178, 179, then change to **non**-consent, settle 178, void 179

No update in sales table (expected), but updated in deposit table.

 

| **Test Case ID** | **Testing  Objectives** | **Step** | **Test Scenario** | **MembershipNo to use** | **Inputed case details** | **Test Case ID** | **MembershipNo to use** | **Inputed case details** | 
| RTM_5 | Consent change in CN transactions by **BJ** members, synced to Datamart | 1 | Create **2** **deposit** transaction in RTM **with Discount applied **for BJ members with the following consent details in MCRM:Consent Transfer Data to HK is "Yes"

Consent To Process Sensitive Info is "Yes"

Consent To Third Party is  "Yes"

 | BJ0486-01 | MembershipNo: BJ0486-01
Date: 3/25
RTM system Date: 3/18
Time:16:36 /16:37
Deposit memo number 1: 00000174
Deposit memo number 2: 
00000175 | RTM_13 | CC2040-01 | MembershipNo: CC2040-01
Date: 3/25
RTM system Date: 3/18
Time:16:40/16:42
Deposit memo number 1: 00000178
Deposit memo number 2: 00000179 | 
| RTM_6 |   | 2 | Update to consent status in MCRM toConsent Transfer Data to HK is "No"

Consent To Process Sensitive Info is "No"

Consent To Third Party is  "No"

 |   | (Contact MI for verification before executing Step 3 and 4) | RTM_14 |   | (Contact MI for verification before executing Step 3 and 4) | 
| RTM_7 |   | 3 | Settle the **first** deposit. |   | **MembershipNo: BJ0486-01**
**Date:3/27**
**RTM system Date: 3/18**
**Time: 12:27**
**Settled memo number 1: **
**00000174**
**Sales memo: 00001350** | RTM_15 |   | **MembershipNo: CC2040-01**
**Date:3/27**
**RTM system Date: 3/18**
**Time: 12:35**
**Settled memo number 1: **
** 00000178**
**Sales memo: 00001352** | 
| RTM_8 |   | 4 | Void the **second** deposit. |   | **MembershipNo: BJ0486-01**
**Date: 3/27**
**RTM system Date: 3/18**
**Time:12:28**
**Voided memo number 2: **
** **
**Sales memo: **
**Sales void memo: **
**Void Deposit :00000175** | RTM_16 |   | **MembershipNo: CC2040-01**
**Date: 3/27**
**RTM system Date: 3/18**
**Time:12:33**
**Voided memo number 2: **
** **
**Sales memo: **
**Sales void memo: **
**Void Deposit :**
**00000179** | 

 

Yellow highlight for BJ member , Blue pen for HK member

 

 

 

2. For consent change from non-consent to yes-consent, the settled check showed up in sales, but no update in deposit, please advise if this is expected.

 

| RTM_9 | Consent change in CN transactions by **BJ** members, synced to Datamart | 1 | Create **2** **deposit** transaction in RTM **with Discount applied **for BJ members with the following consent details in MCRM:Consent Transfer Data to HK is "No"

Consent To Process Sensitive Info is "No"

Consent To Third Party is  "No"

 | BJ0485-01 | MembershipNo: BJ0485-01
Date: 3/25
RTM system Date: 3/18
Time:16:38 / 16:39
Deposit memo number 1: 00000176
Deposit memo number 2: 00000177 | RTM_17 | CC2039-01 | MembershipNo: CC2039-01
Date: 3/25
RTM system Date: 3/18
Time:16:42 / 16:43
Deposit memo number 1: 00000180
Deposit memo number 2: 00000181 | 
| RTM_10 |   | 2 | Update to consent status in MCRM toConsent Transfer Data to HK is "Yes"

Consent To Process Sensitive Info is "Yes"

Consent To Third Party is  "Yes"

 |   | (Contact MI for verification before executing Step 3 and 4) | RTM_18 |   | (Contact MI for verification before executing Step 3 and 4) | 
| RTM_11 |   | 3 | Settle the **first** deposit. |   | **MembershipNo: BJ0485-01**
**Date: 3/27**
**RTM system Date: 3/18**
**Time: 12:31**
**Settled memo number 1: **
**00000176**
**Sales memo: 00001351** | RTM_19 |   | **MembershipNo: CC2039-01**
**Date: 3/27**
**RTM system D

## 相關資訊

- **Jira:** [FE-1663](https://ctil.atlassian.net/browse/FE-1663)
- **標籤:** PIPL