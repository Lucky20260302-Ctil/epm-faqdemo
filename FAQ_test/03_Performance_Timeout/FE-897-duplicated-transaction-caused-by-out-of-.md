---
project: FE
issue_key: FE-897
issue_type: Bug PRD
status: Closed
tags:
- 03_performance_timeout
- faq
- fe
- performance_timeout
- sales
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/FE-897
created: '2021-01-08'
resolved: '2022-08-18'
fix_version: ''
components: []
has_images: false
category: 03_Performance_Timeout
category_label: 效能與超時
quality: partial
title: 'FE-897: Duplicated Transaction caused by out of memory'
---
# FE-897: Duplicated Transaction caused by out of memory 

## 問題描述

Version : 7.1.0.02R14K

After checking the log files, this issue caused by out of memory . Once the POS is not enough memory to complete the transaction then it may happen wrongly load the last running sequence to complete the transaction again. 

please help to check it.

Thanks.



## 相關資訊

- **Jira:** [FE-897](https://ctil.atlassian.net/browse/FE-897)
- **解決方式:** Done