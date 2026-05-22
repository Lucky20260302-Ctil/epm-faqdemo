---
project: BE
issue_key: BE-1182
issue_type: SOW
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
jira_url: https://ctil.atlassian.net/browse/BE-1182
created: '2025-09-22'
resolved: '2025-11-19'
fix_version: ''
components: []
has_images: true
category: 03_Performance_Timeout
category_label: 效能與超時
quality: partial
title: 'BE-1182: Pangdonglai API modification'
---
# BE-1182: Pangdonglai API modification 

## 問題描述

Request from Lein, new store OC334 opened in Pangdonglai landlord.  And landlord is requesting to change their sales data interface endpoint from feishu to new provider. Hence, endpoint and auth. method will be updated to token authentication with MD5 hashing.

> 📎 **image-20250922-070433.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/1cb13cc5-23fd-4dda-8829-0f02adbee5d0)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20250922-070433.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/1cb13cc5-23fd-4dda-8829-0f02adbee5d0)

## 相關資訊

- **Jira:** [BE-1182](https://ctil.atlassian.net/browse/BE-1182)
- **解決方式:** Done
- **標籤:** LL_Sales_Interface