---
tags: [faq, FE, config, performance]
component: "Member API"
symptom: "Severe performance issue: transaction completion takes very long time due to CRM member API bottleneck in Coach China stores"
root-cause: "The system calls member search/upsert API during CompleteTransaction. The 3rd Party CRM API becomes a bottleneck, causing slow transaction completion. Multiple stores affected."
solution: "Added configuration toggle to disable VIP searching during CompleteTransaction. Set config to bypass CRM API calls, making completion independent of VIP validation. Use when CRM API is slow."
jira: FE-1654
resolved: 2025-09-30
fix-version: "v750.04R11A"
---

# FE-1654: Slow Transaction Completion Due to CRM Member API Bottleneck — Config Workaround

## 問題

Severe performance issue: transaction completion takes very long time due to CRM member API bottleneck in Coach China stores

## 根因

The system calls member search/upsert API during CompleteTransaction. The 3rd Party CRM API becomes a bottleneck, causing slow transaction completion. Multiple stores affected.

## 解法

Added configuration toggle to disable VIP searching during CompleteTransaction. Set config to bypass CRM API calls, making completion independent of VIP validation. Use when CRM API is slow.

## 相關資訊

- Jira: [FE-1654](https://ctil.atlassian.net/browse/FE-1654)
- Fix Version: v750.04R11A
- 解決日期: 2025-09-30
