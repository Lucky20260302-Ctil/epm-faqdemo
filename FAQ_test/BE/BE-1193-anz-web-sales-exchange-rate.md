---
tags: [faq, BE, bug, config]
component: "Data Interface"
symptom: "Importing e-commerce sales files into POS system fails with “Exchange rate not found“ error for files that previously worked"
root-cause: "Incorrect currency code setting in the system configuration caused exchange rate lookup to fail."
solution: "Fixed the currency code setting to the correct value in system configuration."
jira: BE-1193
resolved: 2025-03-25
fix-version: ""
---

# BE-1193: ANZ POS: Web Sales Import Error — Exchange Rate Not Found

## 問題

Importing e-commerce sales files into POS system fails with "Exchange rate not found" error for files that previously worked

## 根因

Incorrect currency code setting in the system configuration caused exchange rate lookup to fail.

## 解法

Fixed the currency code setting to the correct value in system configuration.

## 相關資訊

- Jira: [BE-1193](https://ctil.atlassian.net/browse/BE-1193)
- Fix Version: 未記錄
- 解決日期: 2025-03-25
