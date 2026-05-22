---
tags: [faq, fe, 交易流程]
component: "Front End"
symptom: "[Coach] FE receive a zfile but fail to update tblcoupon table"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-1489
resolved: 2024-09-05
fix-version: ""
---

# FE-1489: [Coach] FE receive a zfile but fail to update tblcoupon table

## 問題

[Coach] FE receive a zfile but fail to update tblcoupon table
Here are 2 zupdate that received by POS but no new record added to tblcoupon table
Only [dbMas].[dbo].[Mix Table] has new record of the coupon:
But log can be found in the UD file
VM:
172.16.138.60
.\sxd
Yan20201104@

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2024-09-05
### Jira Comments (1 則)
**Sherman tse** (2024-09-05):
Found the coupon details from Retdata6 > dbtrans > tblcoupon
Close case

## 相關資訊

- Jira: [FE-1489](https://ctil.atlassian.net/browse/FE-1489)
- Fix Version: 未記錄
- 解決日期: 2024-09-05
