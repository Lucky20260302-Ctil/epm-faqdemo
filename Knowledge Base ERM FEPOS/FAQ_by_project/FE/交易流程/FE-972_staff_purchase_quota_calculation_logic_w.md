---
tags: [faq, fe, 交易流程]
component: "Front End"
symptom: "Currently the staff has available quota 2935."
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-972
resolved: 2024-05-04
fix-version: ""
---

# FE-972: Staff purchase quota calculation logic with MM coupon

## 問題

Currently the staff has available quota 2935.
The staff will have a 50% member discount, and further 40% discount MM coupon.
If the non - discount amount > quota, the POS will block this transaction, but actually the discount amount < available quota.

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2024-05-04
### Jira Comments (1 則)
**Sang** (2022-06-16):
17. Staff Limit - Count Qty Exclude Cpn Qty, Check Limit after apply MM Coupons (KTS 220616 v750.02 Jira [🔗](https://ctil.atlassian.net/browse/FE-972#icft=FE-972))

## 相關資訊

- Jira: [FE-972](https://ctil.atlassian.net/browse/FE-972)
- Fix Version: 未記錄
- 解決日期: 2024-05-04
