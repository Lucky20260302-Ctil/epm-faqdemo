---
project: MP
issue_key: MP-307
issue_type: Bug QA
status: Closed
tags:
- 03_performance_timeout
- faq
- mp
- mpos-api
- performance_timeout
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/MP-307
created: '2020-11-10'
resolved: '2021-07-20'
fix_version: ''
components: []
has_images: false
category: 03_Performance_Timeout
category_label: 效能與超時
quality: partial
title: 'MP-307: Log Enhancement'
---
# MP-307: Log Enhancement

## 問題描述

Using IO Async to improve logging performance.

Some machine contain IO issue such as some low end machine and poor resource VM.

Use IO Async to improve this poor logging performance.

Known Issue:

Some time log is not in ascending order but we have time stamp for each log record.

 



## 相關資訊

- **Jira:** [MP-307](https://ctil.atlassian.net/browse/MP-307)
- **解決方式:** Done