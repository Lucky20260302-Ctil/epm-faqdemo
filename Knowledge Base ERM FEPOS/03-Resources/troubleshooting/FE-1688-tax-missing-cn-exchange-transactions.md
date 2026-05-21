---
tags: [bug, production, hotfix]
component: Front End
symptom: "Tax (VAT/GST) values missing for CN exchange transactions at V75 stores"
root-cause: "Exchange memo transactions at V75 not calculating item-level tax (jouinv_vat_value, jouinv_gst_per) during the exchange process"
solution: "Enhanced exchange transaction flow to properly calculate and include item tax for exchange memos"
jira: FE-1688
resolved: 2025-05-30
---

# FE-1688: [CS-1429] Tax Missing for CN Exchange Transactions

## 問題

Two CN V75 stores reported missing tax values on exchange transactions. Data patch was applied to DB as a temporary fix.

**Affected transactions:**
- `OCF22-10189075` (04-24)
- `OCF85-00092495` (04-22)

**Symptoms in data:**
- `jouinv_vat_value` and `jouinv_gst_per` are empty/missing in DB
- Exchange memo `OCF22-10189075` uses `jouinv_misc_amt = '60'`
- T9 log confirms the memo is **NOT** marked as Tax Free
- NPOS log shows the transaction flow

## 根因

Exchange transactions at V75 were not triggering item-level tax calculation. The exchange memo flow bypasses the normal tax calculation routine, causing `jouinv_vat_value` and `jouinv_gst_per` to be empty.

The source memo (`OCF22-10188837`) contains a `jouinv_misc_amt = '60'` which may indicate the misc amount is being populated instead of proper tax fields.

## 解法

Enhanced the exchange transaction handling to properly calculate item-level tax for exchange memos. The fix ensures that when an exchange transaction occurs, the VAT value and GST percentage are computed and written to the invoice record.

**Fix Version**: `FE-V75.04R13A`

_See Jira ticket for resolution details._

## 相關問題

- [CS-1429](https://hktdc.atlassian.net/browse/CS-1429) — Coach Jira reference
- [[FE-1696-sqlexpress-standalone-mode-heartbeat|FE-1696]] — Related V75 fix in same release
