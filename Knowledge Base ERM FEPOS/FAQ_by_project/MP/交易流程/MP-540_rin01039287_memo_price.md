---
tags: [faq, mp, 交易流程]
component: "MPOS, MPOS API"
symptom: "Incident description:"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: MP-540
resolved: 2024-03-06
fix-version: ""
---

# MP-540: RIN01039287: Memo price

## 問題

Incident description:
A transaction used LPV101B 10%off coupon but didn't calculated
sale memo# : J450-MA001021
HD has troubleshooting:
1) customer purchased 2 items and use LPV101B 10%off coupon. At FE, it indeed show minus 5280. But in TOTAL, it didn't calculated.
2) checked BE, this coupon didn't calculated.
3)On RC file, Total-flash sales（フラッシュセールス）=5280, equal to the coupon amount.
Could you please help to confirm why the coupon didn't calculated? And why have discrepancy between Total and flash sales exactly equal to the coupon amount?
Thank you.
=========================
顾客使用了LPV101B 10%OFF优惠券购买两件商品。
1)在FE上，显示此LPV101B优惠券的确优惠了10%，但是总额处却没有减去其金额(5280￥)。
2)在BE上，显示此优惠券金额为0，没有造成加减计算。
3)在日结报告上，不含税总额减去フラッシュセールス的不含税总额（619830-614550=5280），恰好等于优惠券应减金额；
含税总额减去フラッシュセールス的含税总额（681285-676005=5280），亦恰好等于优惠券应减金额。
用户想知道为何此优惠券没有实际减到金额，并造成合計与フラッシュセールス的差异恰好等于应减金额？

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2024-03-06
### Jira Comments (3 則)
**Joy Li** (2022-08-10):
Data: \\172.16.183.201\localuser\support\JIRA_DB\MP-540\J450-Aug06.zip
**Joy Li** (2022-08-10):
@@Sang @@Cy Lau
Please help to check
**Sang** (2022-08-11):
MM Coupon Calculation log and PCD Log showed EC with 5280 Discount has been applied properly,  Header + Details + Payment data not match may due to IPA handling calculation result problem. It should be fixed in web API v3.19

## 相關資訊

- Jira: [MP-540](https://ctil.atlassian.net/browse/MP-540)
- Fix Version: 未記錄
- 解決日期: 2024-03-06
