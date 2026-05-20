---
tags: [bug, production]
component: Front End
symptom: "VAT amounts incorrect on OC134 transactions — Gain No-change amount (LGV Voucher excess) incorrectly included in GST calculation as Misc Amt"
root-cause: "Gain No-change amount (e.g., LGV Voucher $6.8 excess) is recorded as Misc Amt and included in GST calculation when it should be excluded per tax rules"
solution: "Add tblconfig.CALGSTBYMEMONETEXCLMISCAMT='Y' to exclude non-applicable misc amt (Gain No-change) from GST calculation"
jira: FE-1514
resolved: 2025-03-13
---

# FE-1514: VAT Amount Incorrect — Gain No-Change Amt Included in GST

## 問題

VAT amounts were incorrect for transactions on OC134:
- `OC134-00042938` on 8/16 — deposit memo `00000171` on 8/29, Misc amount: 12
- `OC134-00042949` on 8/16

Store paid by LGV voucher with excess amount ($6.8), which was recorded as Misc Amt and incorrectly included in the VAT/GST calculation.

**Required config settings** (preconditions):
- `USEMMCPNAPPAMTONLY = 'Y'` — Write MM Cpn Face Value as List Price, Applied disc Amt as Sell Price

## 根因

When a customer pays with an LGV voucher that exceeds the transaction amount, the **Gain No-change amount** (excess) is recorded as **Misc Amt** in the memo. The GST calculation routine was including this Misc Amt in the taxable amount, when it should be excluded as it is not a charge for goods/services.

**Settings involved:**
- `CALGSTBYMEMONET = 'Y'` — Calculate GST by Memo Net Amt (include ALL Memo Level Discount)
- Missing: `CALGSTBYMEMONETEXCLMISCAMT` was not set to exclude non-applicable misc amounts

## 解法

**Fix in v750.04R10, v750.05:**
- Added `tblconfig.CALGSTBYMEMONETEXCLMISCAMT = 'Y'`
- When `'Y'`: Calculate GST by Memo Net Amt, **excluding** Misc Amt (Gain No-change from vouchers)
- Ignore non-applicable amounts that are not records as Memo Misc Amt

**Required config combination:**
```
CALGSTBYMEMONET='Y'
CALGSTBYMEMONETEXCLMISCAMT='Y'
```

**Patch reference**: `KTS 250123 v750.04R10, v750.05 Jira FE-1514`

## 相關問題

- [[CS-1129]] — Coach Jira reference
- [[FE-1688]] — Related tax calculation issue (exchange transactions)
