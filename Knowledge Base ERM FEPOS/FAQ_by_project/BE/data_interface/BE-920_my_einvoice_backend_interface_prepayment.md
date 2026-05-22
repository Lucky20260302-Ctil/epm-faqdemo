---
tags: [faq, be, data_interface]
component: "Data Interface"
symptom: "when transaction includes gift cert payment, the prepayment field will be incorrectly calculated and"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: BE-920
resolved: 2024-10-17
fix-version: ""
---

# BE-920: MY eInvoice backend interface prepayment amount issue

## 問題

when transaction includes gift cert payment, the prepayment field will be incorrectly calculated and thus the transaction is not successfully sent.

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2024-10-17
### Jira Comments (1 則)
**Anson Cheung** (2024-10-16):
Fix E1193 Incorrect totalPayableAmount error by placing the “prePaymentAmount” to the right place:
{"documentNumber":"OC601-00099447","errors":[{"errorCode":"E1193","errorMessage":"Incorrect totalPayableAmount entered, it should be equal to the value of Formula: ((Total Including Tax - Prepayment Amount) + Rounding Amount)."}]}

## 相關資訊

- Jira: [BE-920](https://ctil.atlassian.net/browse/BE-920)
- Fix Version: 未記錄
- 解決日期: 2024-10-17
