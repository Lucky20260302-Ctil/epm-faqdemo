---
tags: [faq, FE, bug, production]
component: "Front End"
symptom: "All tills cannot finish selling when purchasing multiple items — NetNetAmt becomes negative due to coupon discount calculation order"
root-cause: "Sales Memo applies rounding on net amount (RND(Gross x (1-Disc%))) while MM Coupon applies rounding on discount amount first (Gross - RND(Gross x Disc%)), producing different results."
solution: "Modified MM Coupon discount to calculate based on NetNetAmt consistently with Sales Memo: Net Amt = RND(Gross x (1 - Disc%)). Fix in V750.04R07A."
jira: FE-1520
resolved: 2024-12-27
fix-version: "V750.04R07A"
---

# FE-1520: MM Coupon Discount Calculation Uses Wrong Rounding Order

## 問題

All tills cannot finish selling when purchasing multiple items — NetNetAmt becomes negative due to coupon discount calculation order

## 根因

Sales Memo applies rounding on net amount (RND(Gross x (1-Disc%))) while MM Coupon applies rounding on discount amount first (Gross - RND(Gross x Disc%)), producing different results.

## 解法

Modified MM Coupon discount to calculate based on NetNetAmt consistently with Sales Memo: Net Amt = RND(Gross x (1 - Disc%)). Fix in V750.04R07A.

## 相關資訊

- Jira: [FE-1520](https://ctil.atlassian.net/browse/FE-1520)
- Fix Version: V750.04R07A
- 解決日期: 2024-12-27
