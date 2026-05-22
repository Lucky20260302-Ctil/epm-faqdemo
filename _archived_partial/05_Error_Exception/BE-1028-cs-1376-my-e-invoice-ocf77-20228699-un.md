---
project: BE
issue_key: BE-1028
issue_type: Bug PRD
status: Closed
tags:
- 05_error_exception
- be
- data-interface
- error_exception
- faq
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/BE-1028
created: '2025-03-12'
resolved: ''
fix_version: ''
components: []
has_images: true
category: 05_Error_Exception
category_label: 報錯與異常
quality: partial
title: 'BE-1028: [CS-1376] MY E-invoice - ''OCF77-20228699'' unable send to BDO'
---
# BE-1028: [CS-1376] MY E-invoice - "OCF77-20228699" unable send to BDO

## 問題描述

Recent 2 days we've keep receiving below error message for Coach MY e-invoice. Transaction no is: OCF77-20228699, kindly help to check, log also attached.

[{"documentNumber":"OCF77-20228699","errors":[

{"errorCode":"E1089","errorMessage":"Incorrect Line Item excluding tax amount entered, it should be equal to the value of Subtotal - Discount + Fee / Charge Amount."}

,{"errorCode":"E1240","errorMessage":"Invalid data in Invoice line Items"}]

1.error info in log

> 📎 **image-20250312-022709.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/a61003bb-8cce-4a2f-807a-54e0664ada60)（需 Jira 登入）

2.OCF77-20228699 data in DB.The error if due to item_sell_price(585) > item_list_price(460) or not?Please help to double confirm and clarify.Thanks!

@@Anson Cheung 

> 📎 **image-20250312-023442.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/3cf13fb9-41dc-4df2-9642-9f0c803551d5)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20250312-022709.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/a61003bb-8cce-4a2f-807a-54e0664ada60)
2. 📎 **image-20250312-023442.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/3cf13fb9-41dc-4df2-9642-9f0c803551d5)

## 相關資訊

- **Jira:** [BE-1028](https://ctil.atlassian.net/browse/BE-1028)