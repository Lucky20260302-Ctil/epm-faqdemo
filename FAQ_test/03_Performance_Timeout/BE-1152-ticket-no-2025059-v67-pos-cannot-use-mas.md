---
project: BE
issue_key: BE-1152
issue_type: Bug PRD
status: Open
tags:
- 03_performance_timeout
- backend-(chainstoreplus-7.0)
- be
- faq
- performance_timeout
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/BE-1152
created: '2025-07-29'
resolved: ''
fix_version: ''
components: []
has_images: false
category: 03_Performance_Timeout
category_label: 效能與超時
quality: partial
title: 'BE-1152: Ticket no. 2025059 v67 pos cannot use mastconv files to update pos data'
---
# BE-1152: Ticket no. 2025059 v67 pos cannot use mastconv files to update pos data

## 問題描述

V67 and V7 both can be worked this format like mastconv.dat.01 , mastconv,dat.02 , mastconv.dat.03….and so on  as those data are exported from cs2000 backend .

But after migration ,  using CSP , the file format is changed like mastconv.dat.1 , mastconv.2 , mastconv.3 ….. mastconv.dat.100 , mastconv.dat.101 ….. ,

**>> Please check and confirm if we can generate the mastconv with mastconv.dat.01 , mastconv,dat.02 , mastconv.dat.03**



## 相關資訊

- **Jira:** [BE-1152](https://ctil.atlassian.net/browse/BE-1152)