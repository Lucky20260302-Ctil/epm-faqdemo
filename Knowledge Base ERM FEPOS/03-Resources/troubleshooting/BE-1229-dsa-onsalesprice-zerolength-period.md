---
tags: [bug, production, hotfix]
component: Backend
symptom: "CJ DSA OnSalePrice not effective when effective-from and effective-to datetimes are identical with 00:00:00"
root-cause: "Zero-length effective period (startDate = EndDate with 00:00:00.000) causes PriceChecker to return no OnSalePricing because the price is immediately invalidated by the identical toDateTime"
solution: "Temp solution: data patching with .BAT for case startDate = EndDate with 00:00:00.000"
jira: BE-1229
resolved: 2026-02-26
---

# BE-1229: CJ DSA OnSalesPrice Not Effective Owing to ZeroLength Temp

## 問題

CJ DSA OnSalesPrice is not effective when the promotion period has identical start and end dates. The PriceChecker returns no OnSalePricing for items that should be on sale.

**Scenario:**
- Current DateTime: `2026-02-03 16:34`
- `fromDateTime`: `2026-02-03 00:00:00`
- `toDateTime`: `2026-02-03 00:00:00`
- Although `fromDateTime` is valid, the price is immediately invalidated by `toDateTime` being the same

## 根因

The root cause is a **zero-length effective period** in the pricing data structure:

```
itmprx_onsale_fr_date_1 = itmprx_onsale_to_date_1  (both with 00:00:00)
onsale_fr_date_2 = onsale_to_date_2                  (both with 00:00:00)
```

When both datetimes are identical at `00:00:00`, PriceChecker interprets this as the promotion having zero duration. The `fromDateTime` is technically valid, but the `toDateTime` immediately invalidates it because the time range has no length.

**Definitions:**
- `itmprx_onsale_fr_date_1` / `onsale_fr_date_2` — OnSalePrice effective from DateTime
- `itmprx_onsale_to_date_1` / `onsale_to_date_2` — OnSalePrice effective up to DateTime (End)
- Zero-length period: `fr_date = to_date` with `00:00:00` time component

## 解法

**Temp solution**: Data patching using a `.BAT` script for cases where `startDate = EndDate` with `00:00:00.000`.

The patch adjusts the date range to ensure a non-zero effective period so PriceChecker can properly recognize the OnSalePricing.

**Fix Version**: `BE-V70R3.145`

## 相關問題

- [[CS-2030]] — Related Coach Jira reference
- [[CS-2053]] — Related Coach Jira reference
