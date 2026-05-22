---
project: FE
issue_key: FE-1189
issue_type: Improvement
status: Closed
tags:
- 03_performance_timeout
- faq
- fe
- front-end
- performance_timeout
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/FE-1189
created: '2022-12-07'
resolved: '2022-12-09'
fix_version: ''
components: []
has_images: false
category: 03_Performance_Timeout
category_label: 效能與超時
quality: partial
title: 'FE-1189: Sporthouse - Select Cash Coupon Performance Improvement'
---
# FE-1189: Sporthouse - Select Cash Coupon Performance Improvement

## 問題描述

Cash Coupon Contains 2.6M records.

Select coupon take 7-10 Sec. 

2022/12/07 09:03:51 GetCashCouponItems:Select * from TblCoupon Where Coupon_Type = 'CC' And Coupon_No like '%10000034%' Order by Coupon_Type, Coupon_No
2022/12/07 09:04:02 GetCashCouponItems - End



## 相關資訊

- **Jira:** [FE-1189](https://ctil.atlassian.net/browse/FE-1189)
- **解決方式:** Done