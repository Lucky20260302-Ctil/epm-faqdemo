---
tags: [faq, fe, 交易流程]
component: "Front End"
symptom: "Sales Memo - apply rounding method on the net amount ( Gross Amt - Disc Amt) ."
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-1200
resolved: 2023-11-16
fix-version: ""
---

# FE-1200: MM Coupon Discount Calculation - Apply Rounding Method

## 問題

Sales Memo - apply rounding method on the net amount ( Gross Amt - Disc Amt) .
Net amt = RND (Gross amt x (1- DIsc %))
ex:    Net Amt = 2950 x (1-15%) = 2507.5 --> 2507 ( Round down)
However in MM Coupon Module,  POS apply rounding method on MM Coupon discount amount first, then calculate net amt.
Net Amt = Gross Amt - RND ( Gross Amt x Disc %)
ex:  Net Amt  = 2950 - RND(2950 x15%) = 2950 - Rnd(442.5 --> 442) = 2508
Thus getting different Result.
This bug occurred in v720.02R10+ caused by Fixing Multi Disc Perc MM Coupon Not based on Net/Net Amount cause negative value (KTS 210719 v720.01R10 Item 15, v750.01R01A)

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2023-11-16

## 相關資訊

- Jira: [FE-1200](https://ctil.atlassian.net/browse/FE-1200)
- Fix Version: 未記錄
- 解決日期: 2023-11-16
