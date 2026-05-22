---
tags: [faq, mp, 交易流程]
component: "MPOS API"
symptom: "dbmas & dbtran: /172.16.183.201/localuser/support/20230411/MPOS/"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: MP-648
resolved: 2023-11-16
fix-version: ""
---

# MP-648: MPOS-23: JP MPOS Unable to use e-coupon - v3.21.1(Clous IIS & Local IIS both)

## 問題

dbmas & dbtran: \\172.16.183.201\localuser\support\20230411\MPOS\
BE e-coupon : 172.16.138.8\SQLEXPRESS,40000 csdata18_70
COACH side testing PC 10.33.278.3

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2023-11-16
### Jira Comments (1 則)
**Cy Lau** (2023-04-12):
The root cause would be the coding on CDP (XC) makes incompatible to (EC) coupon
It is strongly suggested to run testing on the sales flow from Choosing Member -> With ECoupon / With CDP Coupon -> Complete transaction

## 相關資訊

- Jira: [MP-648](https://ctil.atlassian.net/browse/MP-648)
- Fix Version: 未記錄
- 解決日期: 2023-11-16
