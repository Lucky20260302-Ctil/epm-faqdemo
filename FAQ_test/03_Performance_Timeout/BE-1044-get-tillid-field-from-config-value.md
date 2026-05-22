---
project: BE
issue_key: BE-1044
issue_type: Task
status: Closed
tags:
- 03_performance_timeout
- be
- data-interface
- faq
- performance_timeout
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/BE-1044
created: '2025-04-08'
resolved: '2025-06-05'
fix_version: ''
components: []
has_images: false
category: 03_Performance_Timeout
category_label: 效能與超時
quality: partial
title: 'BE-1044: Get tillId field from config value'
---
# BE-1044: Get tillId field from config value

## 問題描述

As Disney LL does not accept tillid with English char, we cannot export the tillid such as 'MA', 'MB' to them if they have mPOS. Therefore, please help to update to interface program as below:

 

As-Is: Get tillid value from jouinv_no

 

To-Be: 

- change program to get tillid from config file 

- add a new config for determine tillid value



## 相關資訊

- **Jira:** [BE-1044](https://ctil.atlassian.net/browse/BE-1044)
- **解決方式:** Done