---
tags: [faq, FE, bug]
component: "eName / Member"
symptom: "HK eName: pre-scanning VIP barcode before completing registration causes member query to fail. CBDT API is only called once and does not re-query after registration completes."
root-cause: "The CBDT member query logic was designed to check once at the start of the transaction. After the user completes eName registration, the newly created member is not re-queried, leaving the VIP info unavailable."
solution: "Added re-query logic: after eName registration completion, CBDT is called again to fetch the newly registered member's VIP data. Fix in v720.02R26A, v750.04."
jira: FE-1318
resolved: 2024-05-07
fix-version: "v720.02R26A, v750.04"
---

# FE-1318: HK eName VIP Barcode Pre-scan Fails — CBDT Query Called Only Once

## 問題

HK eName: pre-scanning VIP barcode before completing registration causes member query to fail. CBDT API is only called once and does not re-query after registration completes.

## 根因

The CBDT member query logic was designed to check once at the start of the transaction. After the user completes eName registration, the newly created member is not re-queried, leaving the VIP info unavailable.

## 解法

Added re-query logic: after eName registration completion, CBDT is called again to fetch the newly registered member's VIP data. Fix in v720.02R26A, v750.04.

## 相關資訊

- Jira: [FE-1318](https://ctil.atlassian.net/browse/FE-1318)
- Fix Version: v720.02R26A, v750.04
- 解決日期: 2024-05-07
