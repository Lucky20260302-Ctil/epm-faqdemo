---
project: FE
issue_key: FE-785
issue_type: Bug PRD
status: Closed
tags:
- 03_performance_timeout
- faq
- fe
- frontend
- performance_timeout
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/FE-785
created: '2020-09-30'
resolved: '2020-11-23'
fix_version: ''
components: []
has_images: false
category: 03_Performance_Timeout
category_label: 效能與超時
quality: partial
title: 'FE-785: Incomplete transaction due to out of memory'
---
# FE-785: Incomplete transaction due to out of memory 

## 問題描述

IMX Walter has reported that the transaction has been paid by the WeChat pay, but POS can’t finish the transaction due to out of memory issues at that time.

Ver. 7.1.0.02R14I

Logs and dbtrans copied in \\172.16.183.201\localuser\support\20200930\to_sang

 



## 相關資訊

- **Jira:** [FE-785](https://ctil.atlassian.net/browse/FE-785)
- **解決方式:** Done