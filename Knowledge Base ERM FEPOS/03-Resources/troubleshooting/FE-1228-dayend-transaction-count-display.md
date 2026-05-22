---
tags: [bug, qa]
component: Front End
symptom: "PC23XXXX displays incorrect transaction count after Day End"
root-cause: "Day End routine may not be counting all transaction types in the PC23 report output; exact root cause pending in original fix"
solution: "Fix applied in version 7.5.0.02; verified for sales, transfer, deposit transaction types"
jira: FE-1228
resolved: 2023-03-27
---

# FE-1228: Display Incorrect Number of Transaction in PC23XXXX After Day End

## 問題

After running Day End, the PC23XXXX report shows an incorrect number of transactions. This affects the Day End reconciliation accuracy.

**Transaction types included in the report:**
sales, transfer, deposit, service, Misc, Gift cert, Petty Cash, Bank In, Open item, Giveway, Redm, Payment, Tfx Rec, Pts Adj

## 根因

The Day End PC23 report generation was not counting all transaction types correctly. The specific root cause is not documented in the ticket.

## 解法

Fix applied in version `7.5.0.02`. Verified working for:
- Sales transactions
- Transfer transactions
- Deposit transactions

Remaining transaction types were scheduled for later verification.

_See Jira ticket for resolution details._

## 相關問題

- [[FE-1225]] — DotNet Day End missing TR Out / PCD 94 transaction count (related Day End counting issue)
