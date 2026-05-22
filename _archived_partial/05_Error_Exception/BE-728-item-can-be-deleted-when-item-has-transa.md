---
project: BE
issue_key: BE-728
issue_type: Bug QA
status: Closed
tags:
- 05_error_exception
- backend-(web)
- be
- error_exception
- faq
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/BE-728
created: '2023-03-22'
resolved: '2023-04-06'
fix_version: ''
components: []
has_images: false
category: 05_Error_Exception
category_label: 報錯與異常
quality: partial
title: 'BE-728: Item can be deleted when item has transaction'
---
# BE-728: Item can be deleted when item has transaction

## 問題描述

Item can be deleted in item master when item has transaction.

 

Expected result:

Item cannot be deleted in item master when item has transaction.

 

 

Remark:

.net version has no issue (Ref: image-2023-03-22-15-37-24-813.png)

 

*Transaction from Sales Memo Journal Enquiry (SE7011)

 



## 相關資訊

- **Jira:** [BE-728](https://ctil.atlassian.net/browse/BE-728)
- **解決方式:** Done