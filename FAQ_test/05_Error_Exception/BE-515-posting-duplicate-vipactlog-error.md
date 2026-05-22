---
project: BE
issue_key: BE-515
issue_type: Bug PRD
status: Closed
tags:
- 05_error_exception
- backend-(chainstoreplus-7.0)
- be
- error_exception
- faq
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/BE-515
created: '2021-08-18'
resolved: '2021-08-24'
fix_version: ''
components: []
has_images: false
category: 05_Error_Exception
category_label: 報錯與異常
quality: partial
title: 'BE-515: Posting - duplicate vipactlog error'
---
# BE-515: Posting - duplicate vipactlog error

## 問題描述

- Posting program — Error “Cannot insert duplicate key in object vipactlog”

- The issue is caused by the new member records were creating at this same time in different posting nodes.

- Difficult to reproduce in QA.



## 相關資訊

- **Jira:** [BE-515](https://ctil.atlassian.net/browse/BE-515)
- **解決方式:** Done