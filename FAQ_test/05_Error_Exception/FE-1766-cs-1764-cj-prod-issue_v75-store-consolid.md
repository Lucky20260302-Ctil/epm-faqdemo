---
project: FE
issue_key: FE-1766
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
jira_url: https://ctil.atlassian.net/browse/FE-1766
created: '2025-10-03'
resolved: '2025-10-16'
fix_version: ''
components: []
has_images: false
category: 05_Error_Exception
category_label: 報錯與異常
quality: partial
title: 'FE-1766: [CS-1764] CJ Prod issue_V7.5 store consolidated dayend missing sub till data'
---
# FE-1766: [CS-1764] CJ Prod issue_V7.5 store consolidated dayend missing sub till data

## 問題描述

related SOG ticket:

INC3224817 (store: J841, missing date: 9/29-9/30 of Till 2)

INC3224738  (store: J724, missing date: 9/29-9/30 of Till 2)

INC3223640  (store: J721, missing date: 9/29-9/30 of Till 2 & 3)

INC3229180  (store: J853, missing date: 10/2 of Till 2)

Symptom:

Till 2 sales data cannot reflected on consolidation dayend report

Tested by Joy (use 29/9 as example):

1. re-do dayend consolidation → still missing Till 2 sales data on the report

2. rename dbtbk29. sdf and re-do dayend consolidation → still missing Till 2 sales data on the report

3. copy dbtbk29.sdf manually from Till 2 to Till 0 and re-do dayend consolidation → Till 2 sales data can be reflected on consolidation dayend report, also worked for 30/9



## 相關資訊

- **Jira:** [FE-1766](https://ctil.atlassian.net/browse/FE-1766)
- **解決方式:** Done