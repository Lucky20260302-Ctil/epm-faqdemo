---
project: BE
title: "BE-677: Pop up a blank page after click On sale price enquiry & additional retail price in SE1001 - Item Information / By Item"
issue_key: BE-677
issue_type: Bug QA
status: Closed
faq_score: 5.0
faq_category: 05_Error_Exception
faq_category_label: 錯誤與異常
tags: [faq, be, error_exception, backend-(web)]
jira_url: "https://ctil.atlassian.net/browse/BE-677"
created: 2022-11-07
resolved: 2024-03-06
resolution: Done
has_images: False
---

# BE-677: Pop up a blank page after click On sale price enquiry & additional retail price in SE1001 - Item Information / By Item

## 問題描述

Env: [https://172.16.138.101/csplus/SE1001](https://172.16.138.101/csplus/SE1001)

Location: SE1001 - Item Information / By Item

Reproduce steps:

1. Login an acc that has no right to access On sale price enquiry SE4007 & additional retail price

2. To Item Information / By Item

3. Click on one of the items

4. Select On sale price enquiry & additional retail price

Existing result:

Pop up a No Access notice, then Pop up a blank page (RFE:screenshot-1.png)

Expected result:

Pop up a No Access notice only

 

Remark:

ACC: P01 / P01



## 相關資訊

- **Jira:** [BE-677](https://ctil.atlassian.net/browse/BE-677)
- **解決方式:** Done