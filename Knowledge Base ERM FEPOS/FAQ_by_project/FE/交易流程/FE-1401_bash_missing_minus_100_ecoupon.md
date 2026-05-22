---
tags: [faq, fe, 交易流程]
component: "Front End"
symptom: "The net amount should be 16260, after updeating Dbhist_INVTRX_MIXCOUPONREF_NET_AMT the amount will b"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-1401
resolved: 2024-09-05
fix-version: ""
---

# FE-1401: BASH Missing minus $100 ecoupon

## 問題

The net amount should be 16260, after updeating Dbhist_INVTRX_MIXCOUPONREF_NET_AMT the amount will be correct, also pcd miss post Ecoupon joudis line.

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2024-09-05
### Jira Comments (2 則)
**Sang** (2024-06-03):
DB: \\172.16.183.201\localuser\support\20240603\BASH
**Andrew_Au** (2024-09-05):
Tested the version 7.2.0.02R07ZP , the result is positive .

## 相關資訊

- Jira: [FE-1401](https://ctil.atlassian.net/browse/FE-1401)
- Fix Version: 未記錄
- 解決日期: 2024-09-05
