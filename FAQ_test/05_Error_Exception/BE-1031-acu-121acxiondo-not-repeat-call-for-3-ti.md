---
project: BE
issue_key: BE-1031
issue_type: Improvement
status: Closed
tags:
- 05_error_exception
- api
- be
- error_exception
- faq
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/BE-1031
created: '2025-03-19'
resolved: '2025-05-02'
fix_version: ''
components: []
has_images: false
category: 05_Error_Exception
category_label: 報錯與異常
quality: partial
title: 'BE-1031: [ACU-121][Acxion]Do not repeat call for 3 times when receive 400 error from CRM'
---
# BE-1031: [ACU-121][Acxion]Do not repeat call for 3 times when receive 400 error from CRM 

## 問題描述

Check whether current program will repeat call for 3 times if there is return error from CRM API:

1. If there is no response from API call, then try for 3 times.

2. If there is error return from API, program should not call API again.

HTTPStatusCode : 400,404, 500 no need to trigger the retry



## 相關資訊

- **Jira:** [BE-1031](https://ctil.atlassian.net/browse/BE-1031)
- **解決方式:** Done