---
project: BE
issue_key: BE-506
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
jira_url: https://ctil.atlassian.net/browse/BE-506
created: '2021-07-27'
resolved: '2021-07-27'
fix_version: ''
components: []
has_images: false
category: 03_Performance_Timeout
category_label: 效能與超時
quality: partial
title: 'BE-506: member sync program update'
---
# BE-506: member sync program update

## 問題描述

APP Server Program Change

- Update member sync relative program (prj_cr4002.dll)

- Enhance program to avoid record total loss when SQL select timeout

- Unable to reproduce

- Enhance program to handle large amount vip data sync

- The SQL selection will process in piece to avoid JOB Server memory lack.



## 相關資訊

- **Jira:** [BE-506](https://ctil.atlassian.net/browse/BE-506)
- **解決方式:** Done