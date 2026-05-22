---
project: BE
issue_key: BE-516
issue_type: Bug PRD
status: Closed
tags:
- 03_performance_timeout
- backend-(chainstoreplus-7.0)
- be
- faq
- performance_timeout
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/BE-516
created: '2021-08-24'
resolved: '2021-08-24'
fix_version: ''
components: []
has_images: false
category: 03_Performance_Timeout
category_label: 效能與超時
quality: partial
title: 'BE-516: Polling program --- Error “ETX file not found”'
---
# BE-516: Polling program --- Error “ETX file not found”

## 問題描述

- Polling program — Error “ETX file not found”

- From daily support case, we found that there are some sales memo is missing in BE. After checking, we found that those file are missing because polling task is processing before acp file is uploaded. Therefore, polling task will return “ETX file not found”. Program is changed to process the file if STX and ETX is uploaded.

- Difficult to reproduce in QA.



## 相關資訊

- **Jira:** [BE-516](https://ctil.atlassian.net/browse/BE-516)
- **解決方式:** Done