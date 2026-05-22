---
project: MP
issue_key: MP-644
issue_type: Bug PRD
status: Closed
tags:
- 05_error_exception
- error_exception
- faq
- mp
- mpos
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/MP-644
created: '2023-03-29'
resolved: '2024-07-11'
fix_version: ''
components: []
has_images: false
category: 05_Error_Exception
category_label: 報錯與異常
quality: partial
title: 'MP-644: full-width character Sales staff code AA'
---
# MP-644: full-width character Sales staff code AA

## 問題描述

1. In MPOS, user input Sales staff code AA (full-width character), the MPOS PC file contain full-width character AA will cause posting error.

2. Also the order with full-width character AA will retrieve by FE and cause FE PC file contain full-width character AA

Please help to Block or translate the full-width character AA to half-width character AA



## 相關資訊

- **Jira:** [MP-644](https://ctil.atlassian.net/browse/MP-644)
- **解決方式:** Done