---
project: WEB
title: "WEB-230: [eName] eName cannot show the correct store code in web"
issue_key: WEB-230
issue_type: Bug PRD
status: Closed
faq_score: 5.5
faq_category: 05_Error_Exception
faq_category_label: 錯誤與異常
tags: [faq, web, error_exception, ename]
jira_url: "https://ctil.atlassian.net/browse/WEB-230"
created: 2022-06-13
resolved: 2022-06-13
resolution: Done
has_images: False
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