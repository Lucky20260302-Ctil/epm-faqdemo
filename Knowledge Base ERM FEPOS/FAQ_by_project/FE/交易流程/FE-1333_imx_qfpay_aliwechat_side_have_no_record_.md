---
tags: [faq, fe, 交易流程]
component: "Front End"
symptom: "Our Finance would not verify a voided Alipay transaction **#10006745**  from 24/12 records ."
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-1333
resolved: 2024-05-04
fix-version: ""
---

# FE-1333: IMX QFPay Ali/Wechat side have no record and we have void record.

## 問題

Our Finance would not verify a voided Alipay transaction **#10006745**  from 24/12 records .
And QFPAY (our AliPay / WeChat vendor) also cannot find this transaction from their system too. (you would check below email for your reference)
From POS system , the sales record was issued as #10006744. It can be voided as #10006745 and print out sales memo successfully.
Please investigate into this problem .
Attached the related log files and sales memos layout for your handling .
Logs Path: \\172.16.183.201\localuser\support\20240110\BPSHKG37

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2024-05-04

## 相關資訊

- Jira: [FE-1333](https://ctil.atlassian.net/browse/FE-1333)
- Fix Version: 未記錄
- 解決日期: 2024-05-04
