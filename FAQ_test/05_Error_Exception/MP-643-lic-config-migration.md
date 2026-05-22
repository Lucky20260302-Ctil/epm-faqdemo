---
project: MP
issue_key: MP-643
issue_type: Improvement
status: Closed
tags:
- 05_error_exception
- error_exception
- faq
- mp
- mpos-api
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/MP-643
created: '2023-03-22'
resolved: '2024-11-06'
fix_version: ''
components: []
has_images: false
category: 05_Error_Exception
category_label: 報錯與異常
quality: partial
title: 'MP-643: Lic Config Migration'
---
# MP-643: Lic Config Migration

## 問題描述

Owing to the Config calling from Lic DB ,

The grace period would not be effective if the Lic DB is not available in terms of db failure or connection issue.

According to the record, the configs are seldom adjusted , added or removed. It is suggested that to put a static sqlite file to replace the Lic DB connection with following advantages :

1) Less development efforts

2) Less testing efforts

3) Reduce network IO 



## 相關資訊

- **Jira:** [MP-643](https://ctil.atlassian.net/browse/MP-643)
- **解決方式:** Done