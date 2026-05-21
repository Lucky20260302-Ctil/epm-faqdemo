---
tags: [faq, FE, bug, production]
component: "PCD Posting"
symptom: "AO brand PCD posting error: 'Return Voucher or gift cert. amount not match' when bonus points coupon selection is not cleared after transaction cancel"
root-cause: "When a transaction using bonus points coupon is cancelled, the coupon selection state is not cleared. On next transaction, the stale coupon data causes amount mismatch in PCD posting validation."
solution: "Clear coupon selection state on transaction cancel/void. Ensure coupon data is reset before starting new transaction. Fix in v720.02R07ZS."
jira: FE-1619
resolved: 2025-03-04
fix-version: "v720.02R07ZS"
---

# FE-1619: AO PCD Posting Error — Bonus Points / Return Voucher Amount Mismatch

## 問題

AO brand PCD posting error: 'Return Voucher or gift cert. amount not match' when bonus points coupon selection is not cleared after transaction cancel

## 根因

When a transaction using bonus points coupon is cancelled, the coupon selection state is not cleared. On next transaction, the stale coupon data causes amount mismatch in PCD posting validation.

## 解法

Clear coupon selection state on transaction cancel/void. Ensure coupon data is reset before starting new transaction. Fix in v720.02R07ZS.

## 相關資訊

- Jira: [FE-1619](https://ctil.atlassian.net/browse/FE-1619)
- Fix Version: v720.02R07ZS
- 解決日期: 2025-03-04
