---
tags: [faq, MP, bug, upgrade]
component: "MPOS"
symptom: "After updating MPOS in JP V75 pilot stores, app keeps loading and shows 'Fail to Connect SalesHub'. SalesHub program cannot launch if login account is 'CS2000'."
root-cause: "SalesHub connectivity dependency: the CS2000 account could not properly launch SalesHub program after MPOS update, causing infinite loading loop."
solution: "Fixed SalesHub launch logic for CS2000 account. See also MPOS-86."
jira: MP-761
resolved: 2025-05-21
fix-version: ""
---

# MP-761: JP V75 Pilot: MPOS Shows 'Fail to Connect SalesHub' After Update

## 問題

After updating MPOS in JP V75 pilot stores, app keeps loading and shows 'Fail to Connect SalesHub'. SalesHub program cannot launch if login account is 'CS2000'.

## 根因

SalesHub connectivity dependency: the CS2000 account could not properly launch SalesHub program after MPOS update, causing infinite loading loop.

## 解法

Fixed SalesHub launch logic for CS2000 account. See also MPOS-86.

## 相關資訊

- Jira: [MP-761](https://ctil.atlassian.net/browse/MP-761)
- Fix Version: 未記錄
- 解決日期: 2025-05-21
