---
project: FE
issue_key: FE-1333
issue_type: Bug PRD
status: Closed
tags:
- 07_workflow_business
- faq
- fe
- front-end
- workflow_business
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/FE-1333
created: '2024-01-11'
resolved: '2024-05-04'
fix_version: ''
components: []
has_images: false
category: 07_Workflow_Business
category_label: 業務流程
quality: partial
title: 'FE-1333: IMX QFPay Ali/Wechat side have no record and we have void record.'
---
# FE-1333: IMX QFPay Ali/Wechat side have no record and we have void record.

## 問題描述

Our Finance would not verify a voided Alipay transaction **#10006745**  from 24/12 records .

And QFPAY (our AliPay / WeChat vendor) also cannot find this transaction from their system too. (you would check below email for your reference)

 

From POS system , the sales record was issued as #10006744. It can be voided as #10006745 and print out sales memo successfully.

Please investigate into this problem .

 

Attached the related log files and sales memos layout for your handling .
Logs Path: \\172.16.183.201\localuser\support\20240110\BPSHKG37

 



## 相關資訊

- **Jira:** [FE-1333](https://ctil.atlassian.net/browse/FE-1333)
- **解決方式:** Done