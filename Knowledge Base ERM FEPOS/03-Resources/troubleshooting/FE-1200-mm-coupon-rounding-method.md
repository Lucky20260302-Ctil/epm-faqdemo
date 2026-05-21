---
tags: [bug, production]
component: Front End
symptom: "MM Coupon discount calculation produces different net amount than Sales Memo calculation due to rounding order discrepancy"
root-cause: "Sales Memo applies rounding on net amount (RND(Gross x (1-Disc%))) while MM Coupon applies rounding on discount amount first (Gross - RND(Gross x Disc%)), producing different results"
solution: "Apply rounding method on the net amount consistently in MM Coupon module to match Sales Memo calculation logic"
jira: FE-1200
resolved: 2023-11-16
---

# FE-1200: MM Coupon Discount Calculation — Rounding Method Discrepancy

## 問題

MM Coupon discount calculation produces a different net amount compared to the standard Sales Memo calculation for the same gross amount and discount percentage. This causes inconsistent pricing.

**Example (15% discount on $29.50):**

| Method | Calculation | Result |
|--------|------------|--------|
| Sales Memo (correct) | `Net = RND(2950 x (1-15%)) = RND(2507.5)` | **2507** |
| MM Coupon (bug) | `Net = 2950 - RND(2950 x 15%) = 2950 - RND(442.5) = 2950 - 442` | **2508** |

## 根因

The two modules apply **rounding at different points** in the calculation:

**Sales Memo** (correct behavior):
```
Net Amt = RND(Gross Amt x (1 - Disc%))
```
Rounding is applied to the **final net amount** after the full discount has been applied.

**MM Coupon Module** (incorrect behavior):
```
Net Amt = Gross Amt - RND(Gross Amt x Disc%)
```
Rounding is applied to the **discount amount** first, then subtracted from Gross Amt.

These produce different results because `Round(442.5) = 442` → `2950 - 442 = 2508`, whereas `Round(2507.5) = 2507`.

## 解法

Modified the MM Coupon discount calculation to apply rounding on the **net amount** consistently with the Sales Memo logic:

```
Net Amt = RND(Gross Amt x (1 - Disc%))
```

**Fix Versions**: `v750.02`, `v750.03`, `v720.02R20A`

## 相關問題

- [[FE-1520-coupon-discount-calculation-netnetamt|FE-1520]] — Related coupon discount calculation fix (base on NetNetAmt)
- [[FE-1214-levy-mm-coupon-sequence-barcode-validation|FE-1214]] — Related MM Coupon input sequence handling
