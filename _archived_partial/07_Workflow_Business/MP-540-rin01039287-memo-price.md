---
project: MP
issue_key: MP-540
issue_type: Bug PRD
status: Closed
tags:
- 07_workflow_business
- faq
- mp
- mpos
- mpos-api
- workflow_business
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/MP-540
created: '2022-08-10'
resolved: '2024-03-06'
fix_version: ''
components: []
has_images: false
category: 07_Workflow_Business
category_label: 業務流程
quality: partial
title: 'MP-540: RIN01039287: Memo price'
---
# MP-540: RIN01039287: Memo price

## 問題描述

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



## 相關資訊

- **Jira:** [MP-540](https://ctil.atlassian.net/browse/MP-540)
- **解決方式:** Done