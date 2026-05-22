---
tags: [faq, mp, 交易流程]
component: "MPOS API"
symptom: "Test data: COACH JP"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: MP-649
resolved: 2024-08-30
fix-version: ""
---

# MP-649: L1010B Coupon Discount Variance

## 問題

Test data: COACH JP
FE 172.16.138.37
IIS 172.16.138.37 (region=18, J999) [http://172.16.138.37/sanyoservice.api.fe](https://172.16.138.247/sanyoservice.api.fe)
BE: 172.16.138.8
Item: 
W014 MAH ^WMN
W031 ACN ^WMN
Member : 
J101WJ00000163 
J101WJ00051712 
J999WJ00000120
Ecoupon: L1010B
EC L1010BC0001-L1010BC0060
Case 1: 1item 1 coupon

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2024-08-30
### Jira Comments (2 則)
**Cy Lau** (2024-08-23):
\\ds411\share\POS_MPOS_Release\3.29.X\3.29.1-20240821.1
The invoicing would be aborted by:
1. 
2. 
3. 
This would try to prevent the invoicing with unmatched payment/discount/item lines
**Cy Lau** (2024-08-23):
\\ds411\share\POS_MPOS_Release\3.29.X\3.29.1-20240821.2

## 相關資訊

- Jira: [MP-649](https://ctil.atlassian.net/browse/MP-649)
- Fix Version: 未記錄
- 解決日期: 2024-08-30
