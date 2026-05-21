---
tags: [bug, production]
component: Front End
symptom: "Zero levy quantity closed with 'X' returns qty=1 instead of 0; Levy Charge and MM Coupon input sequence handling incorrect; barcode validation fails for short barcodes"
root-cause: "Input sequence handling for Levy Charge and Multi-Member Coupon not properly coordinated; zero-qty close handler defaults to qty=1; barcode length validation not bypassed for codes under 12 digits"
solution: "Enhanced Levy/MM Coupon input sequence handling; fixed close-zero-levy to return qty=0; added 7+5 barcode validation bypass for codes shorter than 12 digits"
jira: FE-1214
resolved: 2023-02-09
---

# FE-1214/FE-1213: Levy & MM Coupon Input Sequence — Zero Qty Close Bug & Barcode Validation

## 問題

Three distinct bugs identified in POS transaction flow:

1. **Levy Charge & MM Coupon input sequence** — When both Levy Charge and Multi-Member Coupon are applied, the input sequence handling causes incorrect behavior in the transaction flow
2. **Zero levy qty close with 'X'** — Pressing 'X' to close a zero-quantity levy line returns `qty=1` instead of `qty=0`, resulting in an extra bag item being added
3. **Barcode validation** — The 7+5 barcode validation fails for barcodes shorter than 12 digits, blocking valid items

## 根因

1. **Input sequence**: The Levy Charge and MM Coupon input routines are not properly sequenced — the system does not handle the interaction between these two discount types correctly
2. **Zero qty close**: The default return value when closing a levy quantity input with 'X' is incorrectly set to `1` instead of `0`
3. **Barcode validation**: The 7+5 barcode format check is applied to all barcodes, but some valid items (particularly shorter codes or non-standard formats) have barcodes under 12 digits that should be bypassed

## 解法

**All fixes included in `v710.02R14ZL`:**

1. **Levy Charge & MM Coupon Input Sequence Enhancement** — Reordered and synchronized the input handling for Levy Charge and Multi-Member Coupon to prevent interaction conflicts
2. **Zero Levy Qty Close Fix** — Using 'X' to close zero levy quantity now correctly returns `qty=0`
3. **Barcode 7+5 Validation Bypass** — Bypass the 7+5 barcode length check when barcode length is less than 12 digits

## 相關問題

- [FE-1213](https://ctil.atlassian.net/browse/FE-1213) — Same fix set (Using 'X' to close zero levy Qty)
