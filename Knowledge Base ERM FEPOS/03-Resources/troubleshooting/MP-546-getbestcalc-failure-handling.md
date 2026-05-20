---
tags: [bug, production]
component: MPOS
symptom: "GetBestCalc pricing API failure leads to discount variances and pricing variances in MPOS transactions"
root-cause: "getBestCalc API failure (returns false) is not handled — transaction continues with wrong pricing data"
solution: "API catches error and returns false status; MPOS shows alert message and interrupts the transaction when pricing fails"
jira: MP-546
resolved: 2022-11-21
---

# MP-546: GetBestCalc Failure Handling — Pricing Variance

## 問題

When the MPOS pricing API (`getBestCalc`) fails, the transaction continues with incorrect pricing data, leading to:
- Discount variances
- Pricing variances between POS and expected amounts

## 根因

The `getBestCalc` API can fail (return `false`) when it is unable to retrieve the best price calculation from the server. When this happens:

- **API side**: The failure is not properly caught and communicated back to MPOS
- **MPOS side**: The transaction continues without alerting the user, using stale/incorrect pricing data

This results in the transaction being completed with wrong prices, which later shows up as discount/pricing variances in reports.

## 解法

**Two-sided fix:**

1. **API side**: Catch the getBestCalc error and return `false` status to MPOS
2. **MPOS side**: Show a message box / alert to the user when pricing failure is detected, and **interrupt the transaction** to prevent incorrect pricing

This ensures that when the pricing service is unavailable, the transaction is halted rather than completed with wrong data.

## 相關問題

- [[FE-1520]] — Related discount/pricing calculation fix (coupon discount)
- [[FE-1200]] — MM Coupon rounding method
