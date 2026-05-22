---
project: FE
issue_key: FE-1265
issue_type: Bug QA
status: Closed
tags:
- 05_error_exception
- error_exception
- faq
- fe
- front-end-v760.02
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/FE-1265
created: '2023-06-09'
resolved: '2023-11-16'
fix_version: ''
components: []
has_images: false
category: 05_Error_Exception
category_label: 報錯與異常
quality: partial
title: 'FE-1265: [Lands] Suspend transaction in Resume Order cannot be deleted after day end'
---
# FE-1265: [Lands] Suspend transaction in Resume Order cannot be deleted after day end

## 問題描述

Reproduce steps:

1. Save some orders into Resume Order as suspended  transaction

2. Make a day end

3. Go back to Resume Order 

Existng result:

Resume Order still save suspended  orders 



## 相關資訊

- **Jira:** [FE-1265](https://ctil.atlassian.net/browse/FE-1265)
- **解決方式:** Done