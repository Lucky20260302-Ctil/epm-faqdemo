---
project: FE
issue_key: FE-1033
issue_type: Bug PRD
status: Closed
tags:
- 05_error_exception
- error_exception
- faq
- fe
- front-end
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/FE-1033
created: '2021-11-26'
resolved: '2021-12-03'
fix_version: ''
components: []
has_images: false
category: 05_Error_Exception
category_label: 報錯與異常
quality: partial
title: 'FE-1033: [RIN00888608][Coach CJ] FE checking for Invalid salesperson format ''AA'''
---
# FE-1033: [RIN00888608][Coach CJ] FE checking for Invalid salesperson format 'AA'

## 問題描述

Coach CJ reported invalid salesperson ‘AA’ / ‘aa’ with different format. It is failed to post sales memo due to this reason.

Normally, Coach CJ user will input salesperson code during sales memo creation. They may use another typing method.

 

Per discussion, please try reproduce scenario and apply checking on value of salesperson code. Thank you.

 



## 相關資訊

- **Jira:** [FE-1033](https://ctil.atlassian.net/browse/FE-1033)
- **解決方式:** Done