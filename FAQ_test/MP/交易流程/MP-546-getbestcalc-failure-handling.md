---
tags: [faq, MP, bug]
component: "MPOS API"
symptom: "Pricing and discount calculation failures (getPricing/GetBestCalc) lead to incorrect discount amounts and pricing variances on transactions without any error notification"
root-cause: "No error handling existed for GetBestCalc API failures. When the pricing engine fails or returns invalid data, the system continues the transaction with incorrect prices silently."
solution: "Added error handling: GetBestCalc failure (returning false) now interrupts the transaction with a proper error alert to the user, preventing incorrect pricing from being applied."
jira: MP-546
resolved: 2022-11-21
fix-version: ""
---

# MP-546: GetBestCalc Pricing Failure — Missing Error Handling Leads to Discount Variance

## 問題

Pricing and discount calculation failures (getPricing/GetBestCalc) lead to incorrect discount amounts and pricing variances on transactions without any error notification

## 根因

No error handling existed for GetBestCalc API failures. When the pricing engine fails or returns invalid data, the system continues the transaction with incorrect prices silently.

## 解法

Added error handling: GetBestCalc failure (returning false) now interrupts the transaction with a proper error alert to the user, preventing incorrect pricing from being applied.

## 相關資訊

- Jira: [MP-546](https://ctil.atlassian.net/browse/MP-546)
- Fix Version: 未記錄
- 解決日期: 2022-11-21
