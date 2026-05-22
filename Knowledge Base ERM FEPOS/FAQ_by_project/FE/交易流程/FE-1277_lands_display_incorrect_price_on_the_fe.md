---
tags: [faq, fe, 交易流程]
component: "Frontend"
symptom: "Item: 233575 (Hong Kong Guide)"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-1277
resolved: 2023-10-09
fix-version: ""
---

# FE-1277: [Lands] Display incorrect price on the FE

## 問題

Item: 233575 (Hong Kong Guide)
Front end display this item as $128
But SQL display this item in column 1) jouinv_item_amt 2) jouinv_item_amt 3) jouinv_item_amt_fx display $0
Got dbmas & retdata6 for your reference:
\\172.16.183.201\localuser\support\20230727\LandsD\Retdata6+dbmas

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2023-10-09
### Jira Comments (2 則)
**Sang** (2023-08-01):
5. Lands Production Type 'S' (Stock On Hand) Match to CSPLUS Stock Indicator 'B' (KTS 230803 V760.01R03E Jira [🔗](https://ctil.atlassian.net/browse/FE-127#icft=FE-127))
**Sherman tse** (2023-10-09):
Verified on UAT env Lands

## 相關資訊

- Jira: [FE-1277](https://ctil.atlassian.net/browse/FE-1277)
- Fix Version: 未記錄
- 解決日期: 2023-10-09
