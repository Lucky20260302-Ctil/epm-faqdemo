---
tags: [faq, fe, 交易流程]
component: "Frontend"
symptom: "1.) Not Found -->クーポンが見つかりません"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-984
resolved: 2022-08-16
fix-version: ""
---

# FE-984: CJ Loyalty - message translation

## 問題

1.) Not Found -->クーポンが見つかりません
2.) This e-coupon has been used and cannot be redeemed again. --> 利用済みクーポンの為、使用できません
3.) No Coupon Available --> 利用可能クーポンなし

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2022-08-16
### Jira Comments (2 則)
**howard** (2021-06-21):
1.) The message 利用済みクーポンの為、使用できませ cannot show full message
2.) The message of No Coupon Available should be 利用可能クーポンなし
3.) Updated translation for Cannot apply this coupon -> このクーポンを適用できません (TranslationForLoyaltyProgram_0621.xlsx)
**howard** (2021-06-22):
After updated 210622 Coach v720.02R09 Patch:

## 相關資訊

- Jira: [FE-984](https://ctil.atlassian.net/browse/FE-984)
- Fix Version: 未記錄
- 解決日期: 2022-08-16
