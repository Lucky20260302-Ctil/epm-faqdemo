---
tags: [faq, CityU, bug]
component: "Supplier Mgmt"
symptom: "False duplicate email when changing company name"
root-cause: "Validation checked against purged supplier data"
solution: "Exclude purged suppliers from duplicate check"
jira: EP23CITYU-493
resolved: 2024-10-15
fix-version: ""
---

# EP23CITYU-493: False Duplicate Email Error (Purged Supplier Data)

## 問題

False duplicate email when changing company name

## 根因

Validation checked against purged supplier data

## 解法

Exclude purged suppliers from duplicate check

## 相關資訊

- Jira: [EP23CITYU-493](https://ctil.atlassian.net/browse/EP23CITYU-493)
- 解決日期: 2024-10-15
