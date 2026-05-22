---
project: BE
issue_key: BE-683
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
jira_url: https://ctil.atlassian.net/browse/BE-683
created: '2022-11-09'
resolved: '2023-03-03'
fix_version: ''
components: []
has_images: false
category: 05_Error_Exception
category_label: 報錯與異常
quality: partial
title: 'BE-683: Cannot select export file name in Export POS Master Data'
---
# BE-683: Cannot select export file name in Export POS Master Data

## 問題描述

Env: [https://172.16.138.101/chainstoreplus/](https://172.16.138.101/chainstoreplus/)

Location: Export POS Master Data (DI9008)

Reproduce steps:

1. To Export POS Master Data

2. Click export file name

Existing result:

Field of export file name show as dimmed & **no button** can be clicked to select file name (Ref:image-2022-11-09-11-45-50-465.png, screenshot-1.png)

 

Remark:

Seems missing a Browse button next to Field of export file name



## 相關資訊

- **Jira:** [BE-683](https://ctil.atlassian.net/browse/BE-683)
- **解決方式:** Done