---
tags: [faq, fe, 交易流程]
component: "Enquiry, Sales"
symptom: "This issue is related to the Give Away and the MM coupon event below."
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-820
resolved: 2022-06-15
fix-version: ""
---

# FE-820: Ticket 2020152 Sales memo net amt not match with payment amount

## 問題

This issue is related to the Give Away and the MM coupon event below.
The mask items were separated when trigger the Giveaway event. Eventually , POS has assigned the wrong coupon discount to the item adjustment(INVTRX_MIXCOUPONREF_NET_AMT) after completed the payment.
DB copied in \\172.16.183.201\localuser\support\20201030\BPSHKG24
Thanks.

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2022-06-15

## 相關資訊

- Jira: [FE-820](https://ctil.atlassian.net/browse/FE-820)
- Fix Version: 未記錄
- 解決日期: 2022-06-15
