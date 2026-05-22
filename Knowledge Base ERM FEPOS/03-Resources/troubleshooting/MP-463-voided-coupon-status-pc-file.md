---
tags: [bug, qa]
component: MPOS API
symptom: "Redeemed e-coupon does not become available again after sales memo is voided"
root-cause: "PC file processing logic does not handle the void case — voided sales memo records do not trigger e-coupon re-availability update"
solution: "Update PC file logic to update e-coupon records and restore availability when a sales memo is voided"
jira: MP-463
resolved: 2021-07-16
---

# MP-463: Redeemed Coupon Status Not Updated on Void — PC File Logic

## 問題

When a sales memo that used an e-coupon is voided, the redeemed e-coupon should become **available again** for reuse. However, the coupon remains in "redeemed" status and cannot be used again.

## 根因

The PC file (Posting file) logic processes sales memos and coupon redemptions, but does **not handle the void case**. When a voided sales memo is processed:

1. The original coupon redemption records (PCD) are not reversed
2. The e-coupon status in the database remains as "redeemed"
3. The coupon is never returned to "available" status

This is a missing business logic path in the PC file processing — only the creation flow was implemented, not the void reversal flow.

## 解法

Updated the PC file processing logic to:
- Detect when a voided sales memo contains e-coupon redemptions
- Update the e-coupon record status from "redeemed" back to "available"
- Ensure the coupon can be reused by the same member

**Fix Version**: `3.10.2`

## 相關問題

- [[MP-464]] — Related e-coupon fix (re-used voided e-coupon)
- [[FE-1619]] — Related PCD posting fix (FE side)
