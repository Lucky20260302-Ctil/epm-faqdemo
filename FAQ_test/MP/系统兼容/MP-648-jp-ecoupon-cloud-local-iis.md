---
tags: [faq, MP, bug]
component: "MPOS API"
symptom: "JP MPOS unable to apply e-coupons during transactions in v3.21.1 on both Cloud IIS and Local IIS environments"
root-cause: "CDP (XC) coupon coding was incompatible with EC coupon format in the MPOS API layer. The two coupon systems used different identifier formats."
solution: "Fixed coupon format compatibility in MPOS API layer. Both CDP and EC coupon formats now supported."
jira: MP-648
resolved: 2023-11-16
fix-version: ""
---

# MP-648: JP MPOS Unable to Use E-Coupon — v3.21.1 (Cloud & Local IIS)

## 問題

JP MPOS unable to apply e-coupons during transactions in v3.21.1 on both Cloud IIS and Local IIS environments

## 根因

CDP (XC) coupon coding was incompatible with EC coupon format in the MPOS API layer. The two coupon systems used different identifier formats.

## 解法

Fixed coupon format compatibility in MPOS API layer. Both CDP and EC coupon formats now supported.

## 相關資訊

- Jira: [MP-648](https://ctil.atlassian.net/browse/MP-648)
- Fix Version: 未記錄
- 解決日期: 2023-11-16
