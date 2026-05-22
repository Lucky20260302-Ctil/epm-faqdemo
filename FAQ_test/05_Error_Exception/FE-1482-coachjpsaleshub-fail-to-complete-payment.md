---
project: FE
issue_key: FE-1482
issue_type: Bug QA
status: Closed
faq_score: 9.0
faq_category: 05_Error_Exception
faq_category_label: 錯誤與異常
tags: [faq, fe, error_exception, front-end]
jira_url: "https://ctil.atlassian.net/browse/FE-1482"
created: 2024-08-15
resolved: 2024-08-15
resolution: Done
has_images: True
---

# FE-1482: [Coach][JP][Saleshub] Fail to complete payment by using reinstated MM coupon

> **類型:** Bug QA | **狀態:** Closed
> **分類:** 錯誤與異常 | **FAQ 分數:** 9.0
> **解決日期:** 2024-08-15
> **負責人:** Cy Lau
> **組件:** Front End

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