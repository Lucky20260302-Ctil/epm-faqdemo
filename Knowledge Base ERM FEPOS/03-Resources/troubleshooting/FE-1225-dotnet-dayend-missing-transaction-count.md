---
tags: [bug, production]
component: Front End
symptom: "DotNet Day End process writes PCD 94 with missing transaction count for transfer and redemption transactions"
root-cause: "Day End PCD 94 write routine does not count Transfer Out, Transfer Received, Gift Redeem, and Extra Bonus Points transactions"
solution: "Fix DotNetDayend Write 94 PCD to include Other Transaction Count for all transaction types: Transfer Out, Transfer Rec, Gift Redeem, Extra Bonus Pts"
jira: FE-1225
resolved: 2023-06-23
---

# FE-1225: DotNet Day End Missing TR Out Transaction Count

## 問題

After running DotNet Day End, the PCD 94 record shows incorrect transaction counts. Specifically, the following transaction types are not being counted:

- Transfer Out
- Transfer Received (TR Rec)
- Gift Redeem
- Extra Bonus Points

This causes the day-end reconciliation to show mismatched totals for these transaction categories.

## 根因

The DotNet Day End `WritePCD94` routine was only counting a subset of transaction types (sales, transfer, deposit) and omitted the "Other Transaction" categories. The PCD 94 data structure was not including Transfer Out, Transfer Received, Gift Redeem, and Extra Bonus Points in the count calculation.

## 解法

Fixed `DotNetDayend Write 94 PCD` to include **Other Transaction Count** covering:
- Transfer Out
- Transfer Rec
- Gift Redeem
- Extra Bonus Pts

**Fix reference**: `KTS 230321 v750.02R01G`

**Fix Versions**: `v750.02R01G`, `v750.03`

## 相關問題

- [[FE-1228-dayend-transaction-count-display|FE-1228]] — Display incorrect number of transaction in PC23XXXX after Day End
