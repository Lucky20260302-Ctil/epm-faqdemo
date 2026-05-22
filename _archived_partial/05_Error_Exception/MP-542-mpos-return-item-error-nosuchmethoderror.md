---
project: MP
issue_key: MP-542
issue_type: Bug PRD
status: Closed
tags:
- 05_error_exception
- error_exception
- faq
- mp
- mpos
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/MP-542
created: '2022-08-24'
resolved: '2022-10-10'
fix_version: ''
components: []
has_images: false
category: 05_Error_Exception
category_label: 報錯與異常
quality: partial
title: 'MP-542: Mpos return item error ''NoSuchMethodError'''
---
# MP-542: Mpos return item error "NoSuchMethodError"

## 問題描述

An "NoSuchMethodError" occurs when user was trying to return an item that was sold using SIS payment. 

The error can be re-created as below:

Pre-condition:

1. The shop used SIS payment method for that return item/ memo

2. The shop is trying to proceed the return using Mpos (FE POS does not create such issue)

Recreation:

1. The user is trying to proceed the return by setting the quantity to -1

2. Select cash/credit card refund 

3. Error message 



## 相關資訊

- **Jira:** [MP-542](https://ctil.atlassian.net/browse/MP-542)
- **解決方式:** Done