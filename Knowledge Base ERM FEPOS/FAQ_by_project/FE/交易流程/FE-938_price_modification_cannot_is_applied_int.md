---
tags: [faq, fe, 交易流程]
component: "Front End"
symptom: "AH1S-TILL0"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-938
resolved: 2022-08-18
fix-version: ""
---

# FE-938: Price Modification cannot is applied into item with negative quantity (sales return)

## 問題

AH1S-TILL0
172.16.199.243,40000
When get return item price without memo no., sales memo will not found or cannot found any valid price from history, current price will be use.
If Shift +F1 to change price, it will display following message.

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2022-08-18
### Jira Comments (1 則)
**Sang** (2021-03-22):
3. Shift-F1 Price Modification - Price Correction Mode bypass Validate Corrected list Price lower than max discount price (KTS 210322 v720.01R03A)

## 相關資訊

- Jira: [FE-938](https://ctil.atlassian.net/browse/FE-938)
- Fix Version: 未記錄
- 解決日期: 2022-08-18
