---
project: BE
issue_key: BE-970
issue_type: Bug QA
status: Closed
faq_score: 8.5
faq_category: 05_Error_Exception
faq_category_label: 錯誤與異常
tags: [faq, be, error_exception, api]
jira_url: "https://ctil.atlassian.net/browse/BE-970"
created: 2024-12-19
resolved: 2024-12-24
resolution: Done
has_images: True
---

# BE-970: [Coach][CRM milestone 2] Fail to change type "P" from acxiom to type 'C' in pos searching flow

> **類型:** Bug QA | **狀態:** Closed
> **分類:** 錯誤與異常 | **FAQ 分數:** 8.5
> **解決日期:** 2024-12-24
> **負責人:** Sherman tse
> **組件:** API

## 問題描述

[Coach][CRM milestone 2] Fail to change type "P" from acxiom to type 'C' in pos searching flow

Reproduce steps:

1. Get new member from acxiom (gen QR code)

2. POS search the QR code

3. POS get the member details & upsert it to Backend Db

Existing result:

- SQL still show the member from acxiom is type P

- Fail to change type "P" from acxiom to type 'C'

> 📎 **image-20241219-074144.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/7fc15b92-e36b-445c-acba-bd775427709d)（需 Jira 登入）
vip_tel_2: 21001089836



## 附件截圖

1. 📎 **image-20241219-074144.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/7fc15b92-e36b-445c-acba-bd775427709d)

## 相關資訊

- **Jira:** [BE-970](https://ctil.atlassian.net/browse/BE-970)
- **解決方式:** Done