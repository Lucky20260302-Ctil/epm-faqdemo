---
tags: [bug, production, hotfix]
component: Front End
symptom: "AO PCD posting error — Return Voucher or Gift Cert amount not matching, caused by Bonus Points coupon selection data not cleared on cancel"
root-cause: "Cancel Bonus Points Redeem Discount Coupon fails to clear coupon selection data, leaving inconsistent state that produces invalid PCD 24/25 records"
solution: "Add validation when creating sales memo — if no Online BP Cpn Tender (Pay Type 'O') present, bypass creation of BP Cpns PCD 24/25"
jira: FE-1619
resolved: 2025-03-04
---

# FE-1619: AO PCD Posting Error — Bonus Points Coupon Data Inconsistency

## 問題

Backend posting error for AO store (POS v7.2.0.02R07ZN):
- Error: "Return Voucher or gift cert. amount not match"
- PCD lines 24 & 25 (Bonus Points Coupon records) contained invalid data
- Temporary workaround: manually remove PCD lines 24 & 25

**Log path**: `\\172.16.183.201\localuser\support\20250128\AO_log`

## 根因

When a user **cancels a Bonus Points Redeem Discount Coupon** during transaction, the coupon selection data is not properly cleared from the transaction state. This leaves residual coupon data that later gets written into PCD 24/25 records, producing invalid data that the backend posting rejects.

The root issue is that the cancel flow does not clean up the in-memory coupon selection, so when the sales memo is created, it still references the cancelled coupon data.

## 解法

**Fix in v720.02R07ZS:**
- Added validation when creating a Sales Memo:
  - Check if the transaction has **Online BP Cpn Tender** (Pay Type 'O')
  - If no Online BP Cpn Tender is present, **bypass creation of BP Cpns PCD 24/25**
- This prevents the residual coupon data from being written to the PCD file

**Patch reference**: `KTS 250203 Jira FE-1618 720.02R07ZS`

## 相關問題

- [FE-1618](https://ctil.atlassian.net/browse/FE-1618) — Related fix (same patch)
