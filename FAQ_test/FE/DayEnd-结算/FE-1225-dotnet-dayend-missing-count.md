---
tags: [faq, FE, bug]
component: "Day End"
symptom: "Day End PCD 94 report missing transfer out (Gift Redeem / Transfer Out) transaction counts, causing dayend validation discrepancies"
root-cause: "The DotNet Day End write logic for PCD 94 did not include TR Out transaction types (Transfer and Gift Redeem) in the transaction count summary."
solution: "Added TR Out transaction counting to PCD 94 write logic. Fix in v750.02R01G."
jira: FE-1225
resolved: 2023-11-16
fix-version: "v750.02R01G"
---

# FE-1225: DotNet Day End PCD 94 Missing Transfer Out (TR Out) Transaction Count

## 問題

Day End PCD 94 report missing transfer out (Gift Redeem / Transfer Out) transaction counts, causing dayend validation discrepancies

## 根因

The DotNet Day End write logic for PCD 94 did not include TR Out transaction types (Transfer and Gift Redeem) in the transaction count summary.

## 解法

Added TR Out transaction counting to PCD 94 write logic. Fix in v750.02R01G.

## 相關資訊

- Jira: [FE-1225](https://ctil.atlassian.net/browse/FE-1225)
- Fix Version: v750.02R01G
- 解決日期: 2023-11-16
