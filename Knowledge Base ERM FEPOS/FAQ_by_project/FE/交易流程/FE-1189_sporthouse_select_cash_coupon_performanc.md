---
tags: [faq, fe, 交易流程]
component: "Front End"
symptom: "Cash Coupon Contains 2.6M records."
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-1189
resolved: 2022-12-09
fix-version: ""
---

# FE-1189: Sporthouse - Select Cash Coupon Performance Improvement

## 問題

Cash Coupon Contains 2.6M records.
Select coupon take 7-10 Sec.
2022/12/07 09:03:51 GetCashCouponItems:Select * from TblCoupon Where Coupon_Type = 'CC' And Coupon_No like '%10000034%' Order by Coupon_Type, Coupon_No
2022/12/07 09:04:02 GetCashCouponItems - End

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2022-12-09

## 相關資訊

- Jira: [FE-1189](https://ctil.atlassian.net/browse/FE-1189)
- Fix Version: 未記錄
- 解決日期: 2022-12-09
