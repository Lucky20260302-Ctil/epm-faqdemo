---
project: BE
issue_key: BE-841
issue_type: Improvement
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
jira_url: https://ctil.atlassian.net/browse/BE-841
created: '2024-04-15'
resolved: '2024-05-24'
fix_version: ''
components: []
has_images: false
category: 03_Performance_Timeout
category_label: 效能與超時
quality: partial
title: 'BE-841: Colsiz_seq fully occupied and causes ITMEAN interface hang up'
---
# BE-841: Colsiz_seq fully occupied and causes ITMEAN interface hang up

## 問題描述

Coach reports that the itmean import data interface process hang up. The root cause is the colsiz_seq is fully occupied. The workaround is to delete unused color & size seq. and find space for the new color & size record create. Tapestry requests a long term solution now.



## 相關資訊

- **Jira:** [BE-841](https://ctil.atlassian.net/browse/BE-841)
- **解決方式:** Done
- **標籤:** CS-924