---
project: FE
issue_key: FE-1047
issue_type: Bug PRD
status: Closed
tags:
- 05_error_exception
- error_exception
- faq
- fe
- msmq
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/FE-1047
created: '2021-12-29'
resolved: '2022-08-18'
fix_version: ''
components: []
has_images: false
category: 05_Error_Exception
category_label: 報錯與異常
quality: partial
title: 'FE-1047: MSMQ recovery steps for DB and APP server connection fail'
---
# FE-1047: MSMQ recovery steps for DB and APP server connection fail

## 問題描述

when DB sever and APP server connection fail, the pcd files will be write in MSMQ program folder. 

>> Need to handle auto re-post 

>> Log for such case.



## 相關資訊

- **Jira:** [FE-1047](https://ctil.atlassian.net/browse/FE-1047)
- **解決方式:** Done