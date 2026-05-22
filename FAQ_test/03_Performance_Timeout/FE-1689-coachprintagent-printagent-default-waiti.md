---
project: FE
issue_key: FE-1689
issue_type: Bug QA
status: Closed
tags:
- 03_performance_timeout
- faq
- fe
- front-end
- performance_timeout
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/FE-1689
created: '2025-05-08'
resolved: '2025-09-30'
fix_version: ''
components: []
has_images: false
category: 03_Performance_Timeout
category_label: 效能與超時
quality: partial
title: 'FE-1689: [Coach][PrintAgent] PrintAgent default waiting Time not enough, x32TMUPrint.exe would occur timeout'
---
# FE-1689: [Coach][PrintAgent] PrintAgent default waiting Time not enough, x32TMUPrint.exe would occur timeout 

## 問題描述

[Coach][PrintAgent] PrintAgent default waiting Time not enough, x32TMUPrint.exe would occur timeout 

Currently,POS call PrintAgent waiting Time,
      a. Memo - 10 Sec
      b. Enquiry Report - 30 Sec
      c. DayEnd report - 60 Sec

Suggest to make config configurable, so that we can adjust it to ideal waiting time



## 相關資訊

- **Jira:** [FE-1689](https://ctil.atlassian.net/browse/FE-1689)
- **解決方式:** Done