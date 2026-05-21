---
tags: [faq, FE, bug]
component: "Day End"
symptom: "PC23XXXX report shows incorrect number of transactions after day end consolidation"
root-cause: "The transaction count aggregation in the PC23 report logic was not correctly summing sub-till data during consolidation."
solution: "Fixed PC23 transaction count aggregation to correctly sum all sub-till transactions. Fix in v7.5.0.02."
jira: FE-1228
resolved: 2021-12-03
fix-version: "v7.5.0.02"
---

# FE-1228: Incorrect Transaction Count Displayed in PC23XXXX After Day End

## 問題

PC23XXXX report shows incorrect number of transactions after day end consolidation

## 根因

The transaction count aggregation in the PC23 report logic was not correctly summing sub-till data during consolidation.

## 解法

Fixed PC23 transaction count aggregation to correctly sum all sub-till transactions. Fix in v7.5.0.02.

## 相關資訊

- Jira: [FE-1228](https://ctil.atlassian.net/browse/FE-1228)
- Fix Version: v7.5.0.02
- 解決日期: 2021-12-03
