---
tags: [faq, fe, 交易流程]
component: "Front End"
symptom: "When user Log-in POS, POS will validate NetWork connection. If POS can connect Web CAP API,  but whe"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-1143
resolved: 2024-03-01
fix-version: ""
---

# FE-1143: JC Login Process Handle MCRM Server Exception

## 問題

When user Log-in POS, POS will validate NetWork connection. If POS can connect Web CAP API,  but when API connect to MCRM server and receive exception, POS have not handle it (trigger 'Unhandled exception,') and popup ' .. ran into a problem' message, then need to exit POS.

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2024-03-01

## 相關資訊

- Jira: [FE-1143](https://ctil.atlassian.net/browse/FE-1143)
- Fix Version: 未記錄
- 解決日期: 2024-03-01
