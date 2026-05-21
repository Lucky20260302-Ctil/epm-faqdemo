---
tags: [faq, CityU, bug]
component: "Supplier Profile"
symptom: "Profile updated even after reviewer rejected application"
root-cause: "Missing approval status check on save operation"
solution: "Added approval check before allowing updates"
jira: EP23CITYU-499
resolved: 2024-12-05
fix-version: ""
---

# EP23CITYU-499: Supplier Profile Updated After Reviewer Rejection

## 問題

Profile updated even after reviewer rejected application

## 根因

Missing approval status check on save operation

## 解法

Added approval check before allowing updates

## 相關資訊

- Jira: [EP23CITYU-499](https://ctil.atlassian.net/browse/EP23CITYU-499)
- 解決日期: 2024-12-05
