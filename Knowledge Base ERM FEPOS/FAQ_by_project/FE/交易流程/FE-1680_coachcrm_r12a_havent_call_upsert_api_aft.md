---
tags: [faq, fe, 交易流程]
component: "Front End"
symptom: "[Coach][CRM] R12A haven't call upsert api after issue an order with new member created by POS"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-1680
resolved: 2025-04-29
fix-version: ""
---

# FE-1680: [Coach][CRM] R12A haven't call upsert api after issue an order with new member created by POS 

## 問題

[Coach][CRM] R12A haven't call upsert api after issue an order with new member created by POS
Build no.: 7.5.0.04R12A (Build250414)
Reproduces steps:
1. 
2. 
3. 
Existing result:
- 
- 
New member created by POS:
OC1350C00015399
Region: CN

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2025-04-29
### Jira Comments (2 則)
**Sang** (2025-04-28):
please check tblconfig.WEBAPIUPDATENEWMEMBER  value. This config add on v750.04R11A
v750.04R11A
1. 
2.
**Sherman tse** (2025-04-29):
Able to call usert api after change the config as **tblconfig.WEBAPIUPDATENEWMEMBER - Y**
Close case

## 相關資訊

- Jira: [FE-1680](https://ctil.atlassian.net/browse/FE-1680)
- Fix Version: 未記錄
- 解決日期: 2025-04-29
