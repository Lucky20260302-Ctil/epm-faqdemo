---
project: WEB
issue_key: WEB-230
issue_type: Bug PRD
status: Closed
tags:
- 05_error_exception
- ename
- error_exception
- faq
- web
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/WEB-230
created: '2022-06-13'
resolved: '2022-06-13'
fix_version: ''
components: []
has_images: false
category: 05_Error_Exception
category_label: 報錯與異常
quality: partial
title: 'WEB-230: [eName] eName cannot show the correct store code in web'
---
# WEB-230: [eName] eName cannot show the correct store code in web

## 問題描述

ChainStorePlus WEB Server

- eName Program [ 350cb9d / ba2514a]

- [AQ-618] & [ARP-26] eName cannot show the correct store code in web

- Set eName program Cache time = 10 hrs which handle by IP address

- Load Balancer will restrict to same destination server for single client IP request.

- Reproduce Step:

- Two machine from different IP address connect to ename one by one.

- The correct region and location are shown and used.



## 相關資訊

- **Jira:** [WEB-230](https://ctil.atlassian.net/browse/WEB-230)
- **解決方式:** Done