---
tags: [faq, FE, bug, config]
component: "Zfile / Promo"
symptom: "Promo code CLE062A set up in BE does not appear in POS for specific stores (J433, J378) while other stores work correctly"
root-cause: "The promo Zlog file was not successfully imported into Dbmas for those specific stores. The exact import failure reason was undetermined, but the file was missing from those stores' databases."
solution: "Workaround: Re-save the promo code in Backend UI, which triggers Zlog file re-generation and re-import into Dbmas for all stores. Promo then appears in POS."
jira: FE-1611
resolved: 2025-05-21
fix-version: ""
---

# FE-1611: Promo Code Not Reflecting in POS — Zfile Import Failed for Specific Stores

## 問題

Promo code CLE062A set up in BE does not appear in POS for specific stores (J433, J378) while other stores work correctly

## 根因

The promo Zlog file was not successfully imported into Dbmas for those specific stores. The exact import failure reason was undetermined, but the file was missing from those stores' databases.

## 解法

Workaround: Re-save the promo code in Backend UI, which triggers Zlog file re-generation and re-import into Dbmas for all stores. Promo then appears in POS.

## 相關資訊

- Jira: [FE-1611](https://ctil.atlassian.net/browse/FE-1611)
- Fix Version: 未記錄
- 解決日期: 2025-05-21
