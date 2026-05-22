---
tags: [faq, fe, 其他]
component: "POS+BE"
symptom: "In accordance with PIPL requirements, any changes to the isConsentToHK indicator will take effect im"
root-cause: "待提取"
solution: "### Jira Comments (5 則)"
jira: FE-1663
resolved: 
fix-version: ""
---

# FE-1663: HKJC BJ RTM - PIPL needs to save the latest IsConsentToHK in Deposit Return and Deposit Settlement.  

## 問題

In accordance with PIPL requirements, any changes to the isConsentToHK indicator will take effect immediately. Therefore, it is essential to save the latest isConsentToHK status in both the deposit return and Deposit Settlement. Additionally, POS postings must update this status in the deposit journal. The issue of transaction synchronization can be disregarded, as Datamart will mask all customer transactions, rendering the data unusable. However, void deposits and void deposit settlements can be exceptions, as these actions occur only on the same day.
We expect the update for the deposit records to be based on the consent status as at the moment of the void/settlement.
Given that there could be a long timeframe between deposit and settlement, it is possible that the consent flag would change during the time.
Therefore, we expect the update of the deposit to be based on the latest consent flag of the members.
1. 
Created deposit 00000174 and 00000175 for consented member, then updated consent flag to **non**-consent.
After non-consent, settle 174 and void 175.
In DM_HOSP Sales, the settled check (00001350) is not sent (expected).
However, in DM_HOSP Deposit, update is still being received , 175 updated status to 41
Similarly for the HK Member case :
Created deposit 178, 179, then change to **non**-consent, settle 178, void 179
No update in sales table (expected), but updated in deposit table.
|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |
Yellow highlight for BJ member , Blue pen for HK member
1. 
|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (5 則)
**Sang** (2025-03-31):
@@Bobby @@Andrew_Au @@Ken Wang
v720.01R05E JC RTM BK - IsConsentToHK unsvailable in DataMart (KTS 250331 FE-1663 v720.01R05F )
1. 
1. 
1.
**Andrew_Au** (2025-08-28):
Could we change the ticket status to close ?
**Automation for Jira** (2025-09-14):
Issue has been created since
Days since: 168
Week since : 24
Issue due date difference
Days since : 166
Weeks since: 23
**Andrew_Au** (2025-09-14):
@bobby Please update the ticket status
**Andrew_Au** (2025-09-30):
@@Bobby  The ticket pending for a long time. Please update the ticket status

## 相關資訊

- Jira: [FE-1663](https://ctil.atlassian.net/browse/FE-1663)
- Fix Version: 未記錄
- 解決日期: 未記錄
