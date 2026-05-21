---
tags: [bug, production]
component: Front End
symptom: "All tills cannot complete selling when purchasing 3 pieces with one item after coupon discount application"
root-cause: "Coupon discount amount calculation incorrectly bases on original price instead of NetNetAmt (net amount after other discounts)"
solution: "Fix rounding calculation of coupon discount amount to base on NetNetAmt instead of original price"
jira: FE-1520
resolved: 2024-12-27
---

# FE-1520: All Till Cannot Finish Selling — Coupon Discount Calculation

## 問題

Multiple stores (OCF7 - CS2000, CN-OCF3) reported that all tills cannot click "完成" (complete) when purchasing 3 pieces with one item. The issue was reproducible in production but could not be reproduced in QA environment.

Affected stores:
- RIN01399092 — OCF7 (CS2000)
- RIN01402692 — CN-OCF3

Reported via logs sent through Teams and Zoom.

## 根因

The coupon discount amount calculation uses the **original price** as the base instead of **NetNetAmt** (the net amount after applying other discounts). This causes a rounding discrepancy that prevents the transaction from completing when the calculation overflows or produces an inconsistent state.

The fix corrects the rounding calculation to use `NetNetAmt` as the base for coupon discount amount.

**Fix reference**: `Fix Round Calc Cpn Disc Amt base on NetNetAmt (KTS 241009)`

## 解法

Modified the coupon discount rounding calculation to base the discount amount on `NetNetAmt` instead of the original price. This ensures the discount arithmetic is consistent with the net pricing used throughout the rest of the transaction.

**Fix Versions**: `V750.04R07+`, `v750.05`

_See Jira ticket for resolution details._

## 相關問題

- [CS-1171](https://hktdc.atlassian.net/browse/CS-1171) — Coach Jira reference
