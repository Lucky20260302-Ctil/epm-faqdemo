---
tags: [faq, BE, bug, production]
component: "Polling / PCD"
symptom: "Posting terminated by PCD file with “String or binary data would be truncated“ error; file becomes stuck and cannot be processed"
root-cause: "User input in PCD line 94 (CashVarComment & DayEndComment) contained line break characters, causing data truncation during posting to the database."
solution: "Replace line break characters with whitespace in PCD line 94 before posting. Fix in V750.04R09C, V750.04R10, v750.05."
jira: BE-999
resolved: 2025-04-10
fix-version: "V750.04R09C, V750.04R10, v750.05"
---

# BE-999: KSJ V75: Posting Terminated — Line Break Characters in PCD Cause Data Truncation

## 問題

Posting terminated by PCD file with "String or binary data would be truncated" error; file becomes stuck and cannot be processed

## 根因

User input in PCD line 94 (CashVarComment & DayEndComment) contained line break characters, causing data truncation during posting to the database.

## 解法

Replace line break characters with whitespace in PCD line 94 before posting. Fix in V750.04R09C, V750.04R10, v750.05.

## 相關資訊

- Jira: [BE-999](https://ctil.atlassian.net/browse/BE-999)
- Fix Version: V750.04R09C, V750.04R10, v750.05
- 解決日期: 2025-04-10
