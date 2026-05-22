---
project: FE
issue_key: FE-1482
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
jira_url: https://ctil.atlassian.net/browse/FE-1482
created: '2024-08-15'
resolved: '2024-08-15'
fix_version: ''
components: []
has_images: true
category: 05_Error_Exception
category_label: 報錯與異常
quality: partial
title: 'FE-1482: [Coach][JP][Saleshub] Fail to complete payment by using reinstated MM coupon'
---
# FE-1482: [Coach][JP][Saleshub] Fail to complete payment by using reinstated MM coupon

## 問題描述

[Coach][Saleshub] Fail to complete payment by using reinstated MM coupon

Use: MPOS

Reproduce steps:

1. Issue an order with Member' MM coupon

2. Void the order

3. Issue an order use the reinstated MM coupon

Expected result:

Able to complete payment with reinstated MM coupon

> 📎 **image-20240815-062045.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/7459ea26-48d0-4921-b204-cf7e1e3ad494)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20240815-062045.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/7459ea26-48d0-4921-b204-cf7e1e3ad494)

## 相關資訊

- **Jira:** [FE-1482](https://ctil.atlassian.net/browse/FE-1482)
- **解決方式:** Done