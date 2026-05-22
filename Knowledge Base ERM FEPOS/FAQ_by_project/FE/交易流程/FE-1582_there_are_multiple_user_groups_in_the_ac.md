---
tags: [faq, fe, 交易流程]
component: "Frontend"
symptom: "We tried to log in with Andrew's account, which had multiple user groups, but the login failed"
root-cause: "待提取"
solution: "### Jira Comments (2 則)"
jira: FE-1582
resolved: 
fix-version: ""
---

# FE-1582: There are multiple user groups in the account

## 問題

We tried to log in with Andrew's account, which had multiple user groups, but the login failed

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (2 則)
**Andrew_Au** (2024-12-13):
if domain user assigned more than 1 user group and the user group not a WIM document mentioned format. The API cannot handle.
**Anson Cheung** (2024-12-13):
Release:
- 
csplus_api:
- 
- 
HKJC WIAM:
- 
-

## 相關資訊

- Jira: [FE-1582](https://ctil.atlassian.net/browse/FE-1582)
- Fix Version: 未記錄
- 解決日期: 未記錄
