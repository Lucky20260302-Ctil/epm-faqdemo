---
project: BE
title: "BE-702: PO_Cannot triggle trader terms"
issue_key: BE-702
issue_type: Bug PRD
status: Closed
faq_score: 6.5
faq_category: 05_Error_Exception
faq_category_label: 錯誤與異常
tags: [faq, be, error_exception, backend-(chainstoreplus-7.0)]
jira_url: "https://ctil.atlassian.net/browse/BE-702"
created: 2022-11-24
resolved: 2023-11-16
resolution: Done
has_images: False
---

# BE-702: PO_Cannot triggle trader terms

## 問題描述

Env: Prorunner UAT **web & local Backend** 

ACC: sx1                        PW: sx1

Location: Process > Purchase Order Maintenance (PO3000)

Precondition: Fill in Payment Term from one supplier in Supplier File Maintenance (MF1000) 

Reproduce steps:

Expected

1. Purchase Order Information (PO3000) 

2. Create 

3.  Fill in PO No.

4. Select a supplier with Payment term

5. Fill in Currency

6. Triggle Trader Terms in **Others & Remarks (as attached)**

 



## 相關資訊

- **Jira:** [BE-702](https://ctil.atlassian.net/browse/BE-702)
- **解決方式:** Done