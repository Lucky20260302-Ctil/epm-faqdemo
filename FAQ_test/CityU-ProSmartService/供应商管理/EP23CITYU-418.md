---
tags: [faq, CityU, bug]
component: "Supplier Info"
symptom: "Email check flags supplier own email as duplicate"
root-cause: "Validation compares all emails including supplier own current email"
solution: "Exclude current supplier own email from check"
jira: EP23CITYU-418
resolved: 2024-03-21
fix-version: ""
---

# EP23CITYU-418: Email Duplication Check Flags Own Email as Duplicate

## 問題

Email check flags supplier own email as duplicate

## 根因

Validation compares all emails including supplier own current email

## 解法

Exclude current supplier own email from check

## 相關資訊

- Jira: [EP23CITYU-418](https://ctil.atlassian.net/browse/EP23CITYU-418)
- 解決日期: 2024-03-21
