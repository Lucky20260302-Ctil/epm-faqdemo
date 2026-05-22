---
project: FE
issue_key: FE-1217
issue_type: Bug QA
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
jira_url: https://ctil.atlassian.net/browse/FE-1217
created: '2023-02-22'
resolved: '2023-02-23'
fix_version: ''
components: []
has_images: false
category: 05_Error_Exception
category_label: 報錯與異常
quality: partial
title: 'FE-1217: Section of reason code display ALL type in Physical In/Out Information (IC6000)'
---
# FE-1217: Section of reason code display ALL type in Physical In/Out Information (IC6000)

## 問題描述

Reproduce steps:

1. To Physical In/Out Batch Information (IC6000)

2. Click on one of the record & Select "Batch maintenance"

3. Click on one of the items in the batch & Select "Modify"

4. Click on "..." in the Reason field

Existing result:

Section of reason code display ALL type

Expected result:

Only display reason code with type null/P in Physical In/Out Information (IC6000)



## 相關資訊

- **Jira:** [FE-1217](https://ctil.atlassian.net/browse/FE-1217)
- **解決方式:** Done