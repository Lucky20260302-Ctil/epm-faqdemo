---
project: BE
issue_key: BE-646
issue_type: Bug QA
status: Closed
tags:
- 05_error_exception
- backend-(web)
- be
- error_exception
- faq
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/BE-646
created: '2022-09-15'
resolved: '2024-04-27'
fix_version: ''
components: []
has_images: false
category: 05_Error_Exception
category_label: 報錯與異常
quality: partial
title: 'BE-646: Cannot back to correct place in menu when users enter from specific tabs'
---
# BE-646: Cannot back to correct place in menu when users enter from specific tabs

## 問題描述

Env: CSplus (website)

ISSUE

Cannot back to correct place in main page when users enter from specific tabs

Reproduce steps:

1. select one of column (e.g.: Process > Stock control)

2. select one of tabs under the column (e.g.: Open Item Recovery)

3. tab Back

 

Existing result:

Back to incorrect place: Table Maintance in main page (Ref: image-2022-09-15-17-00-15-201.png)

 

Expected result:

Back to related place that users enter from : Process > Stock control



## 相關資訊

- **Jira:** [BE-646](https://ctil.atlassian.net/browse/BE-646)
- **解決方式:** Done
- **標籤:** csplus