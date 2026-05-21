---
tags: [faq, CityU, bug]
component: "Supplier Sync"
symptom: "Rejected records still synced to Oracle"
root-cause: "date_modified updated even when rejected, triggering sync"
solution: "Do not update date_modified when rejected"
jira: EP23CITYU-462
resolved: 2024-09-19
fix-version: ""
---

# EP23CITYU-462: Rejected Supplier Records Still Synced to Oracle EBS

## 問題

Rejected records still synced to Oracle

## 根因

date_modified updated even when rejected, triggering sync

## 解法

Do not update date_modified when rejected

## 相關資訊

- Jira: [EP23CITYU-462](https://ctil.atlassian.net/browse/EP23CITYU-462)
- 解決日期: 2024-09-19
