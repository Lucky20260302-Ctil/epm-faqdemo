---
project: FE
title: "FE-1689: [Coach][PrintAgent] PrintAgent default waiting Time not enough, x32TMUPrint.exe would occur timeout"
issue_key: FE-1689
issue_type: Bug QA
status: Closed
faq_score: 7.0
faq_category: 03_Performance_Timeout
faq_category_label: 效能與逾時
tags: [faq, fe, performance_timeout, front-end]
jira_url: "https://ctil.atlassian.net/browse/FE-1689"
created: 2025-05-08
resolved: 2025-09-30
resolution: Done
has_images: False
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