---
tags: [faq, FE, bug, production]
component: "Front End"
symptom: "MM Coupon discount calculation produces different net amount (off by 1 cent) than Sales Memo for same gross amount and discount percentage"
root-cause: "Sales Memo applies rounding on net amount (RND(Gross x (1-Disc%))) while MM Coupon applies rounding on discount amount first (Gross - RND(Gross x Disc%)), producing different results. Example: 15% on $29.50 gives 2507 vs 2508."
solution: "Apply rounding method on the net amount consistently in MM Coupon module to match Sales Memo calculation logic. Fix in v720.02R20A."
jira: FE-1200
resolved: 2024-01-22
fix-version: "v720.02R20A"
---

# FE-1200: MM Coupon Discount Calculation — Rounding Method Discrepancy (1-cent error)

## 問題

MM Coupon discount calculation produces different net amount (off by 1 cent) than Sales Memo for same gross amount and discount percentage

## 根因

Sales Memo applies rounding on net amount (RND(Gross x (1-Disc%))) while MM Coupon applies rounding on discount amount first (Gross - RND(Gross x Disc%)), producing different results. Example: 15% on $29.50 gives 2507 vs 2508.

## 解法

Apply rounding method on the net amount consistently in MM Coupon module to match Sales Memo calculation logic. Fix in v720.02R20A.

## 相關資訊

- Jira: [FE-1200](https://ctil.atlassian.net/browse/FE-1200)
- Fix Version: v720.02R20A
- 解決日期: 2024-01-22
