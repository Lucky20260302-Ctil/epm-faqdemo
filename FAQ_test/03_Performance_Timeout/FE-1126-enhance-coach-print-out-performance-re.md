---
project: FE
issue_key: FE-1126
issue_type: Improvement
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
jira_url: https://ctil.atlassian.net/browse/FE-1126
created: '2022-06-27'
resolved: '2024-05-06'
fix_version: ''
components: []
has_images: false
category: 03_Performance_Timeout
category_label: 效能與超時
quality: partial
title: 'FE-1126: Enhance Coach Print Out Performance - Re-Get Member Name'
---
# FE-1126: Enhance Coach Print Out Performance - Re-Get Member Name

## 問題描述

Case Details:

when POS retrieve Member information which is new created in e-Name platform, POS will get a temporary  value '-' assign to Member Last Name and first name.  In order to print the correct member name in receipt, POS will retrieve member name again in printing receipt process.

 

Improvement:

. Change to retrieve member name in confirm create invoice if the member name is start with '-' or is ''

~~ Change to retrieve member name in printing process  if the member name in sales journal is start with '~~' or is ''

 



## 相關資訊

- **Jira:** [FE-1126](https://ctil.atlassian.net/browse/FE-1126)
- **解決方式:** Done