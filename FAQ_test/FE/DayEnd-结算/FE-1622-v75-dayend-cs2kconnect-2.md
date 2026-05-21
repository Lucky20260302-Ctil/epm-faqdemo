---
tags: [faq, FE, bug]
component: "Day End"
symptom: "Store OC126 frequently has dayend issues after V75 upgrade. No dayendinfo in cs2000connect.log until next-day PC restart."
root-cause: "Same as FE-1646: forced cs2kconnect execution during dayend (V72) was removed in V75."
solution: "Keep PCs running after dayend for cs2kconnect to complete. Data auto-posts on next startup if missed. See also FE-1646."
jira: FE-1622
resolved: 2025-02-24
fix-version: "v750.01R01A"
---

# FE-1622: V75 Day End Issue on OC126: Dayend Info Not Posted Until Next Day

## 問題

Store OC126 frequently has dayend issues after V75 upgrade. No dayendinfo in cs2000connect.log until next-day PC restart.

## 根因

Same as FE-1646: forced cs2kconnect execution during dayend (V72) was removed in V75.

## 解法

Keep PCs running after dayend for cs2kconnect to complete. Data auto-posts on next startup if missed. See also FE-1646.

## 相關資訊

- Jira: [FE-1622](https://ctil.atlassian.net/browse/FE-1622)
- Fix Version: v750.01R01A
- 解決日期: 2025-02-24
