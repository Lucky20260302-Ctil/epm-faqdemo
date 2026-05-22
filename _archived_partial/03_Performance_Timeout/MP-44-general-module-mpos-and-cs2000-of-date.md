---
project: MP
issue_key: MP-44
issue_type: Change Request
status: Closed
tags:
- 03_performance_timeout
- faq
- mp
- mpos
- performance_timeout
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/MP-44
created: '2020-03-11'
resolved: '2020-04-15'
fix_version: ''
components: []
has_images: false
category: 03_Performance_Timeout
category_label: 效能與超時
quality: partial
title: 'MP-44: General Module - MPOS and CS2000 of date cannot sync.'
---
# MP-44: General Module - MPOS and CS2000 of date cannot sync.

## 問題描述

Already changed when CS2000 dayend, MPOS trigger API action, will prompt error to inform user to restart app.
But we tested after prompt error, the screen still stay in issue sales, we suggest quite to login screen

(2020/03/12) Change the flow when till 0 process dayend, MPOS will prompt the message and directly logout to login screen  



## 相關資訊

- **Jira:** [MP-44](https://ctil.atlassian.net/browse/MP-44)
- **解決方式:** Done