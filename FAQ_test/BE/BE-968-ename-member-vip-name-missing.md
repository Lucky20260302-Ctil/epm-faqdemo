---
tags: [faq, BE, bug]
component: "eName / CRM Sync"
symptom: "VIP names were missing or wrong for members created by eName from December 12 onward in HK region"
root-cause: "Members were created in region 11 by CRM, then synchronized to region 10 via cross-region sync, instead of being created directly by HK eName in the correct region."
solution: "Executed data patch using update queries derived from the eName SQLite log to fix the missing/corrupt VIP name data."
jira: BE-968
resolved: 2025-03-15
fix-version: ""
---

# BE-968: HK: Member Created by eName Missing VIP Name Data

## 問題

VIP names were missing or wrong for members created by eName from December 12 onward in HK region

## 根因

Members were created in region 11 by CRM, then synchronized to region 10 via cross-region sync, instead of being created directly by HK eName in the correct region.

## 解法

Executed data patch using update queries derived from the eName SQLite log to fix the missing/corrupt VIP name data.

## 相關資訊

- Jira: [BE-968](https://ctil.atlassian.net/browse/BE-968)
- Fix Version: 未記錄
- 解決日期: 2025-03-15
