---
tags: [faq, FE, bug]
component: "Front End"
symptom: "Pressing F7 'Retrieve Order' in POS pops up an error when Open Item Recovery function is not enabled for the store"
root-cause: "The Retrieve Order function depends on Open Item Recovery being enabled. When disabled, the function call fails because the underlying data retrieval path is not initialized."
solution: "Add check for Open Item Recovery status before allowing F7 Retrieve Order; show clear message if feature not enabled. Fix in 2025-02-24."
jira: FE-1605
resolved: 2025-02-24
fix-version: "v750.01R01A"
---

# FE-1605: F7 Retrieve Order Shows Error When Open Item Recovery Is Disabled

## 問題

Pressing F7 'Retrieve Order' in POS pops up an error when Open Item Recovery function is not enabled for the store

## 根因

The Retrieve Order function depends on Open Item Recovery being enabled. When disabled, the function call fails because the underlying data retrieval path is not initialized.

## 解法

Add check for Open Item Recovery status before allowing F7 Retrieve Order; show clear message if feature not enabled. Fix in 2025-02-24.

## 相關資訊

- Jira: [FE-1605](https://ctil.atlassian.net/browse/FE-1605)
- Fix Version: v750.01R01A
- 解決日期: 2025-02-24
